#### Proprietà del percettrone

Se due classi di punti A e B sono linearmente separabili, allora la convergenza per un percettrone è garantina comunuqe vengano scelti i pesi iniziali. La procedura di apprendimento termina dopo un numero finito di passi.

*Perceptron Convergence Theorem*:
If $X_m = {(x_1, l_1), ...,(x_m,l_m)}$ describes a linearly separable dichotomy, then the fixed-increment perceptron algorithm terminates after a finite number of weight updates.

#### Support Vector Machine

Assumendo di avere due classi di punti A e B, linearmente separabili:

Il problema di identificare la migliore separazione tra le due classi di punti è risolto individuando i vettori di supporto, i quali sono i punti più vicini al margine di separazione.

## SVM

If the training data is linearly separable, we can select two parallel hyperplanes that separate the two classes of data, so that the distance between them is as large as possible. The region bounded by these two hyperplanes is called the "margin", and the maximum-margin hyperplane is the hyperplane that lies halfway between them. With a normalized or standardized dataset, these hyperplanes can be described by the equations.

${\displaystyle {\vec {w}}\cdot {\vec {x}}-b=1}$ (anything on or above this boundary is of one class, with label 1)

and

${\displaystyle {\vec {w}}\cdot {\vec {x}}-b=-1}$ (anything on or below this boundary is of the other class, with label -1).


#### Indicare brevemente cosa sono i Vettori di Supporto nelle SVM

The max-margin hyperplane is completely determined by those ${\displaystyle {\vec {x}}_{i}} {\vec {x}}_{i}$ that lie *nearest* to it. These ${\displaystyle {\vec {x}}_{i}} {\vec {x}}_{i}$ are called **support vectors**.