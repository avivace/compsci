# Modelli Probabilistici per le Decisioni
## Assignment 1
### Antonio Vivace, `793509`, 4 Aprile 2019

### D-separation rules

A and C are d-separated when:

1. A $\leftarrow$ B* $\rightarrow$ C
2. A $\rightarrow$ B*  $\rightarrow$ C
3. A $\rightarrow$ B $\leftarrow$ C

(Elements marked with * are in the evidence set).


Consider the following Bayesian Network:

![Bayesian Network](1.png)

#### 1a. Does R and J d-separate F and S?
Sì.

R e J d-separano F ed S:

- S $\rightarrow$ J* $\rightarrow$ F, d-separata per la regola 2
- S $\rightarrow$ W $\rightarrow$ J* $\rightarrow$ F, W $\rightarrow$ J $\rightarrow$ F è d-separata per la regola 2

- S $\rightarrow$ R* $\rightarrow$ D $\rightarrow$ F, S $\rightarrow$ R $\rightarrow$ D è d-separata per la regola 2
- S $\rightarrow$ R* $\rightarrow$ A $\rightarrow$ D $\rightarrow$ F, S $\rightarrow$ R $\rightarrow$ A è d-separata per la regola 2
- S $\rightarrow$ W $\rightarrow$ R* *$\rightarrow$ A $\rightarrow$ D $\rightarrow$ F,  W $\rightarrow$ R $\rightarrow$ A è d-separata per la regola 2
- S $\rightarrow$ W $\rightarrow$ R* $\rightarrow$ D $\rightarrow$ F,  W $\rightarrow$ R $\rightarrow$ D è d-separata per la regola 2

#### 1b. Does J d-separate F and W?

No.

J d-separa il cammino W $\rightarrow$ J* $\rightarrow$ F, ma W $\rightarrow$ R $\rightarrow$ D $\rightarrow$ F risulta connesso.

#### 1c. Does W and R d-separate D and S?

Sì.

Per la regola 2 questi cammini sono bloccati:

- S $\rightarrow$ R* $\rightarrow$ D
- S $\rightarrow$ W* $\rightarrow$ R* $\rightarrow$ D
- S $\rightarrow$ W* $\rightarrow$ R* $\rightarrow$ A $\rightarrow$ D

S $\rightarrow$ J $\rightarrow$ F $\rightarrow$ D è bloccato dato che in J $\rightarrow$ F $\leftarrow$ D, J e D sono d-separati per la regola 3.

#### 1d. Does R d-separate D and J?

Sì.

- In J $\rightarrow$ W $\rightarrow$ R* $\rightarrow$ D, W ed D sono d-separati da R per la regola 2.
- J $\rightarrow$ F $\leftarrow$ D è bloccato per la regola 3.

#### 2. Write all pairs of nodes which are independent of each other given S, R, D.

- A, W
- A, F
- A, J

S, R, e D bloccano tutti i cammini tra A e gli altri nodi non nell'Evidence Set. J $\rightarrow$ F $\leftarrow$ D è bloccato per la regola 3.