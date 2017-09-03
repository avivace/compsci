## Simplesso
```
CP=c <<; c<0
RP=b_i / c_i <<; c_i > 0
ElementoPivot = (RP,CP) 
b = colonna termini noti
Variabile NB = Variabile non in base
Variabile B = Variabile in base

While(!(coeff su Riga0 tutti >= 0)) {
    RigaPivot = RigaPivot / ElementoPivot
    foreach (riga i con (i,CP) > 0):
        R_i = R_i + |(i,CP)|*RP
    foreach (riga i con (i,CP) < 0):
        R_i = R_i - |(i,CP)|*RP
    foreach (riga i con (i,CP) = 0):
        R_i = R_i
    }
BFS = (Variabili NB = 0, i-esima variabile B = b_i)

```

## Sensitività
Intervallo di variazione di ciascuna risorsa affinchè la soluzione ottima rimanga ammissibile:

```
t + delta*C_slack_i >= 0
```

Intervalli di variazione del costo dell'attività x_i affinchè la soluzione ottima rimanga tale:
```
R = Riga che sulla colonna di x_i ha coefficiente 1
Per tutti i coeff != 0 e 1 su R:
    coeff_i(R_0) + delta*coeff_i(R) >= 0
```

Calcolare il vettore colonna relativo all'introduzione di una nuova attività x_c con costo ridotto 3 e vettore variabili tecnologiche A = (3,2,1)

```
Vettore Variabili Ombra = Vettore coefficienti variabili ombra sulla Riga 0
CR = Costo Ridotto
A = Vettore variabili tecnologiche

VVO * A - CR = Vettore Colonna nuova attività x_c

```

## Duale

[...]