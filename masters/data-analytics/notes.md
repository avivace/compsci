# Data Analytics

1) Structural equivalence (social networks)

Structural equivalence refers to the extend to hich two nodes **are connected to the same others** - i.e., have the same social environments.
It is often hypothesized that structurally equivalent nodes will be similar in other ways as well, such as attitudes, behaviors or performance.

This definition is strict, but we usually refer to a similarity metric of it.

2) Similarity metrics (social networks)

##### Jaccard

TODO

##### Cosine

TODO

3) Diameter of a network

The longest shortes path in a network.

4) Irony

Hard to sistematically detect. Ensemble methods: more supervised models that evaluate an ensemble composition (Bayesian Model Average). DMC: gain/loss per model

5) Sarcasm

Bayesian Model Average

6) Implicit and explicit sentiment

Explicit: *I like apples*

Implicit: *A good guide for starters*

7) How to evaluate a model robustness?

- Accuracy
- Precision
- Recall
- Minimize FP+FN
- ROCs

TODO: formulas

8) Closeness VS Beetweenes

**Closeness**: Inverse of the sum of the distances (shortest paths) to every other node.

**Betweenees**: Quantity of shortest paths passing by a node

9) ?

10) Named Entity Recognition

TODO

11) Overfitting VS Underfitting

**Overfitting** the model is too much biased/focused on the training set. Low error on the training but growing on the test

**Underfitting** the learning has not finished

TODO: Add plots (curves)

12) Community Detection approaches

##### Node-centric

Each node in a group must satisfy certain properties, such as:

- Complete Mutality (TODO)
- Reachability of members
- Nodal degress
- ...

##### Group-centric

Each group, as a whole, satisfies some metrics. E.g. group density must be over a set threshold.


##### Network-centric

Partition the network in disjoin subsets.

- K-Means
- Similarity-based clustering
	+ Structural equivalence
	+ Vertex similarities (Jaccard, Cosine)
- Minimum Cut

##### Hierarchic-centric

Build an hierarchical structure (one community in another)

Divisive:

- Recursevely apply Network-centric partitioning
- Edge Betweenness based (iteratevely remove edges with highest betweeness until a network is discomposed into desired number of connected components)

Agglomerative:

- TODO

#### Modularity