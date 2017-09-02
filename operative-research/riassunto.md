## Simplesso

[...]

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