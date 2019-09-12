#### feb19

*Se uno studente supera l’esame,  il voto verrà prima o poi verbalizzato;  la verbalizzazione può avvenire solo dopo che la segreteria abbia dato l’autorizzazione.*

G(E->F(V) and U(!V,A))

#### gen19

*Se si è acceso il LED verde, la porta resta bloccata fino a quando il LED si spegne.*

G(V -> U(L,!V))

#### lug19

*Chi acquista un biglietto aereo sul nostro sito sarà rimborsato se comunica la rinuncia prima dell'inizio del check-in*

G(!C and B and A -> FR)

#### bambini e funzioni

Tre bambini A B e C giocano in una grande casa, sorvegliati da alcuni adulti. Supponete che le stanze siano numerate. La funzione f(x) specifica in che stanza si trova il bambino x. La funzione g(x) specifica quanti adulti ci sono nella stanza x.

*Se un adulto si trova nella stessa stanza di A e B, dovrà sempre esserci almeno un adulto fino a quando A esce*

G( (g(f(A))>0 and f(A) = f(B) and f(A) = K) -> W( g(k)>0, k!=f(A) ) )

> W è *weak until*, perchè non è garantito che K!=f(A) succeda (A esce).

*È sempre possibile raggiungere uno stato in cui B e C si trovano nella stessa stanza*

AGEF( f(B) = f(C) )
