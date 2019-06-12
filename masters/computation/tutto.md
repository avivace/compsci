# Teoria della Computazione
Soluzioni delle prove scritte.

# Riduzioni

## SAT $\leq_p$ 3SAT.

Mapperemo una formula CNF f in una formula g 3CNF tale che g è soddisfacibile se e solo se f lo è. Mostreremo prima il caso in cui f sia una 4CNF. Sia C una clausola di di f. C = u1 OR NOT u2 OR NOT u3 OR u4. Aggiungiamo una nuova variabile z ad f e sostituiamo C con la coppia di clausole C1 = u1 OR u NOT u2 or Z AND C2 = NOT u3 OR u4 or NOT Z. 

Se C è vera, allora c'è un assegnamento per z che soddisfa sia C1 che C2.
Se C è false, qualsiasi assegnamento di z rende o C1 o C2 falsa.

Questa idea può essere applicata ad una clausola generica di dimensione 4 ed in generale di dimensione k (per k > 3) in un equivalente coppia di clausole C1 di dimensione k-1 e C2 di dimensione 3 che dipendono dalle k variabili di C ed una variabile aggiuntiva z.

Applicare questa trasformazione comporta una trasformazione in tempo polinomiale di una formula CNF f in una equivalente formula 3CNF formula g.

## 3SAT $\leq_p$ IND

Ricordiamo che 

- 3SAT = { x : x formula in 3-CNF soddisfacibile}
- IND = {$(G,k)$ : esiste un insieme indipendente del grafo $G=(V,E)$ di dimensione $k$}

## Vertex Cover $\leq_p$ Set Cover

todo

## HAM $\leq_p$ TSP

todo

## Vertex Cover $\leq_p$ IND

todo

# Complessità

Si dica quale delle seguenti affermazione è vera.

`14feb17`

#### Un problema NP-Hard può non essere NP-completo

Vero.

#### Un problema in NP può non essere NP-completo

Vero.

#### Ci sono problemi in NP che si riducono in tempo polinomiale ad un problema in P

Falso.

`17lug17`

#### Esistono problemi NP-Hard che non sono NP-Completi

Vero.

#### Esistono problemi in NP che non sono NP-Hard

Vero.

#### Un problema nella classe di complessità P è risolubile in tempo polinomiale da una MdT non deterministica

Vero.

`22giu17`

#### Non esistono macchine di Turing che non terminano

Falso. Esistono Macchine di Turing che non terminano. Inoltre, non è possibile stabilire in generale se un algoritmo, dato un input finito, termini o continui la sua esecuzione all'infinito (Halting Problem).

#### Un problema in P non è nella classe NP

Falso. Tutti i problemi P sono anche in NP, in quanto le MdT non deterministiche sono più potenti e risolvono in tempo polinomiale anche i problemi risolti in tempo polinomiale dalle macchine deterministiche.

#### Un problema in NP non può essere NP-Hard

Falso. Esistono problemi che sono NP ed NP-Hard (i cosidetti problemi NP-Completi).

`28feb17`

#### Un problema NP-Hard è un problema che sta in NP

Falso. Non necessariamente. Esistono problemi NP-Hard che stanno anche in NP e si chiamano NP-Completi. Alcuni problemi NP-Hard non stanno in NP.

#### Un problema in NP si riduce in tempo polinomiale ad un problema NP-Hard

Vero. Tutti i problemi in NP sono riducibili in tempo polinomiale ad un problema NP-Hard (o NP-Completo).

#### Ci sono problemi in NP che non si riducono in tempo polinomiale a nessun problema in NP

    

(29giu18)

#### Un problema NP-Hard deve essere anche NP-completo

#### Un problema in NP può non essere NP-completo

#### Ci sono problemi in NP che non si riducono in tempo polinomiale a un problema in P

(22feb2018)

#### Esistono problemi in P che non sono in NP

#### Un problema in NP non può essere NP-Completo

#### Un problema NP-difficile deve essere calcolabile da una macchina di Turing non deterministica in tempo polinomiale

(16lug18)

#### Esistono problemi NP-Hard che non sono NP-completi

#### Esistono problemi in NP che non sono NP-Hard

#### Un problema nella classe di complessità P è risolubile in tempo polinomiale da una MdT non deterministica

(12set18)

#### Si dia la definizione di problema NP-Completo

(21feb19)

#### Un problema NP-Completo si riduce in tempo polinomiale ad un problema NP-Hard

#### Un problema NP-Hard può non essere in NP

#### Ci sono problemi in NP che non si riducono in tempo polinomiale ad un problema in NP

(29gen19)

#### Un problema NP-Hard sta in NP

#### Un problema NP-Hard si riduce in tempo polinomiale ad un altro problema NP-Hard

#### Se un problema in NP si risolve polinomialmente, allora P = NP

#### Il minimo albero di copertura di un grafo completo pesato ha un costo maggiore del cammino Hamiltoniano di minimo costo

### 4) Sia A un algoritmo 5/2-approssimante per Vertex-Cover (VC). Sia dato il grafo G = (V,E) dove E = {(1,2),(1,3),(1,4),(4,5),(3,4)}. Dire qual è la massima dimensione di una soluzione restituita da A sul grafo G.

L'ottimo è di dimensione 2 (ad esempio i vertici 1, 4). La più grande soluzione che può dare A è 5/2 * 2 = 5.

### 6) Definire la parola $D_j^k$  per la ricerca approssimata di una stringa S in un testo T tramite algoritmo di Wu-Manber. Fare un esempio esplicativo

Dato 

- $0\leq j \leq n=|T|$ 
- $0 \leq h \leq k$

$D_j^h$ è una parola di $m = |P|$ bit ($D_j^k = d_1 d_2 .. d_m$) tale che:

- $d_i = D^h_j[i] = 1 \leftrightarrow P[1,i] = \text{suff}_h(T[1,j])$
- altrimenti $d_i = D^h_j[i] = 0$

In cui $P[1,i] = \text{suff}_h(T[1,j])$ se $P[1,i]$ occorre come suffisso di $T[1,j]$ con al più h errori.

Esempio:

- T = `absd aabb abc`
- P = `bbab` (m = 4)

$D^1_8$ = `1110`


### 7) Data la BWT B = `gg$ccaacac` di un testo T definito su di un alfabeto {a, c, g, t}, specificare senza ricostruire T (e motivando la risposta) quanti sono i suffissi che iniziano con il simbolo `c` e in che posizione stanno nell'ordinamento lessicografico di tutti i suffissi di T. Determinare inoltre l'FM Index e ricostruire il testo T.

### 8) Descrivere l'algoritmo di ricerca esatta di un pattern P in una stringa S basato sulla BWT (Burrows-Wheeler Transform) di S.

Antonio Vivace - [source](https://github.com/avivace/compsci)