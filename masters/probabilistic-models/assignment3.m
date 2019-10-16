% ANTONIO VIVACE
% 793509
% 11/05/2019

% nodes of the network
N = 4;
% zeros NxN
dag = zeros(N, N);
% topological order
W = 1; A = 2; H = 3; J = 4;

% adjacency matrix
dag(W, [A J]) = 1;
dag(A, J) = 1;
dag(H, J) = 1;

node_sizes = 2*ones(1, N);
% 2 possible values
discrete_nodes = 1:N;

bnet = mk_bnet(dag, node_sizes, 'names', {'BAD_WEATHER','ACCIDENT','RUSH_HOUR','TRAFFIC_JAM'}, 'discrete', 1:4);

% CPT per node
bnet.CPD{W} = tabular_CPD(bnet, W, [0.95 0.05]);
bnet.CPD{A} = tabular_CPD(bnet, A, [0.7 0.9 0.3 0.1]);
bnet.CPD{H} = tabular_CPD(bnet, H, [0.8 0.2]);
bnet.CPD{J} = tabular_CPD(bnet, J, [0.9 0.05 0.4 0.05 0.7 0.05 0.5 0.05 0.1 0.95 0.6 0.95 0.3 0.95 0.5 0.95]);

% Names
strArray = java_array('java.lang.String', N);
strArray(1) = java.lang.String('BAD_WEATHER');
strArray(2) = java.lang.String('ACCIDENT');
strArray(3) = java.lang.String('RUSH_HOUR');
strArray(4) = java.lang.String('TRAFFIC_JAM');

% graphical representation
names = cell(strArray);
gObj = biograph(dag,names);
gObj = view(gObj);
set(gObj.nodes, 'Color',[1 1 1],'Shape','circle', 'size', [40 25], 'LineColor', [0 0 0]);

engine = likelihood_weighting_inf_engine (bnet);

% evidences P(J=True | A=True)
evidence = cell(1,N);
evidence{A} = 1; % A = TRUE
evidence{J} = 1; % J = TRUE
[engine, loglik] = enter_evidence(engine, evidence);

% samples
numSample = 1000

% generate samples
sampleMatrix = sampling(numSample, N, evidence);
sampleMatrix

% sample weights
weight = weightCalc(bnet, sampleMatrix, evidence);
weight

% likelihoodWeighting on H=True
prob = likelihoodWeighting(sampleMatrix, weight, H, 1);
prob

function [sampleMatrix] = sampling(numSample, N, evidence)
sampleMatrix = zeros(numSample, N);
for i=1:numSample
    for j=1:N
        if(~isempty(evidence{j}))
            value = cellfun(@(m)m(1,1),evidence(j));
        else
            U=rand;
            if U<=0.50
                value = 1;
            else
                value = 2;
            end
        end
        sampleMatrix(i,j) = value;
    end
end
end

function [condvects] = getcondvects(i)
    % every possibly binary condition (correct position on the CPT for the LW)
    g = 2;
    i2 = 2^i;
    condvects = false(i2,i);
    for m = 1 : 1 : i
        m2 = 2^m;
        m3 = (m2/2)-1;
        i3 = i-m+1;
        for g = g : m2 : i2
            for k = 0 : 1 : m3
                condvects(g+k,i3) = true;
            end
        end
        g = m2+1;
    end
end

function [sampleWeight] = weightCalc(bnet, sampleMatrix, evidence)

sampleWeight = ones(size(sampleMatrix, 1), 1); % Creo matrice di zeri

for i=1:size(sampleMatrix, 1)
    for j=1:size(evidence, 2)
        if(~isempty(evidence{j}))
            parents = bnet.parents{j};
            numParents = size(parents, 2);
            parentsValueInSample = zeros(1, numParents + 1);
    
            for k=2:(numParents + 1)
                if(sampleMatrix(i, parents(k - 1)) == 2)
                    parentsValueInSample(1, k) = 0;
                else
                    parentsValueInSample(1, k) = 1;
                end
            en
d
            if(sampleMatrix(i, j) == 2)
                parentsValueInSample(1, 1) = 0;
            else
                parentsValueInSample(1, 1) = 1;
            end
            
            truthTable = getcondvects(numParents + 1);
         
            for k=1:size(truthTable, 1)
                if(isequal(truthTable(k, :), parentsValueInSample(1, :)))
                    rowCPT = k;
                    break;
                end
            end
            sampleWeight(i, 1) = sampleWeight(i, 1) * struct(bnet.CPD{j}).CPT(rowCPT);
        end 
    end
end
end

function [prob] = likelihoodWeighting(sampleMatrix, sampleWeight, node, valueOfNode)
totalWeightNode = 0;
% sum of the weights with node=valueOfNode
totalWeightSample = 0;
% sum of the weigths associated to each sample

for i=1:size(sampleMatrix, 1)
    if(sampleMatrix(i, node) == valueOfNode)
        totalWeightNode = totalWeightNode + sampleWeight(i, 1);
    end
    totalWeightSample = totalWeightSample + sampleWeight(i, 1);
end
prob = totalWeightNode / totalWeightSample; % LW
end
