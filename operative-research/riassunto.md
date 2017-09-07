# Ricerca Operativa

## Simplesso


```python
MAX cx = MIN -cx

    Problema di MIN

b = colonna termini noti
Variabile NB = Variabile non in base
Variabile B = Variabile in base


PickEP {
    CP=c <<; c<0
    RP=b_i / c_i <<; c_i > 0
    # Se tutti i rapporti b_i/c_i sono negativi, il problema è illimitato
    ElementoPivot = (RP,CP) 
}

prepareSimplex {
    # I termini noti devono essere >= 0
    # Tutti i vincoli del tipo <=
    # La matrice aggiunta delle variabili di Slack deve essere una identità
    # Sopra la matrice identità, i coefficienti devono essere 0
}

prepareSimplex()
while(!(coeff su Riga0 tutti >= 0)) {
    PickEP()
    # La variabile sulla colonna CP va in base, sostituendo quella precedente sulla RP.
    RP = RP / EP
    for each (riga i con (i,CP) > 0):
        R_i = R_i + |(i,CP)|*RP
    foreach (riga i con (i,CP) < 0):
        R_i = R_i - |(i,CP)|*RP
    foreach (riga i con (i,CP) = 0):
        R_i = R_i
    }l
BFS = (Variabili NB = 0, i-esima variabile B = b_i)

```

## Sensitività

### Intervallo di variazione di ciascuna risorsa affinchè la soluzione ottima rimanga ammissibile:

```python
t + delta*C_slack_i >= 0
```

### Intervalli di variazione del costo dell'attività x_i affinchè la soluzione ottima rimanga tale:
```python
R = Riga che sulla colonna di x_i ha coefficiente 1
Per tutti i coeff != 0 e 1 su R:
    coeff_i(R_0) + delta*coeff_i(R) >= 0
```

### (???) Calcolare il vettore colonna relativo all'introduzione di una nuova attività x_c con costo ridotto 3 e vettore variabili tecnologiche A = (3,2,1)
```python
Vettore Variabili Ombra = Vettore coefficienti variabili ombra sulla Riga 0
CR = Costo Ridotto
A = Vettore variabili tecnologiche

VVO * A - CR = Vettore Colonna nuova attività x_c

```

### 

```

```

## Duale

### Teorema Dualità Forte, Debole ed esempi di applicazione



### Complementarietà
```python
y*(b - Ax*) = 0
(y*A - c)x* = 0
```




## PERT/CPM

