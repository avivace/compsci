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
    }
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


## KKT

 
1. Ad ogni vincolo, associare una delta_i.
2. Vincoli di *ammissibilità duale* relativi ai delta_i (inverto segni, = variabile senza vincoli)
3. Condizioni di *complementarietà*

    delta_i (i-esimo vincolo) = 0

4. Condizioni sul *gradiente*

    (dFO/dx, dFO/dy) - delta_i (dVi/dx, dVi/dy) = 0 (per tutte le i)

5. Definire 2^n sviluppi, combinare le condizioni

## PERT/CPM

a) Dato il grafo delle precedenze tra le attività di un progetto e la loro durata media, come si determinano le loro attività critiche?

`t_min` di un'attività è il tempo minimo entro cui si possono terminare tutte le fasi necessarie per iniziarla. Le prime hanno t_min = 0, per ogni altra attività sequente A, tmin(A) è la massima somma tra tmin(P)+durata(P) dei predecessori, con P predecessore con tale massimo valore.

`t_max` di un'attività è il massimo tempo entro cui devo iniziare l'attività stessa,  pena un aumento del tempo minimo per completare il progetto. L'ultima attività ha `t_min=t_max`, per ogni altra tmax è la differenza minima tra la durata di P e tmax di un successore A.

Un'**attività critica** è un'attività che ha `slack = 0`. `Slack = t_max - t_min`.
Un percorso critico è la sequenza più lunga di attività critiche.

b) Perchè sono dette critiche?

Un'attività è detta *critica* è un'attività il cui inizio non può essere ritardato nemmeno di un'unità di tempo, altrimenti l'intera durata minima del progetto in esame verrebbe aumentata.