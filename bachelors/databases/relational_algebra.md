# Relational Algebra, exercises

Given the following relational scheme, solve the queries using relational algebra.

```
MAGAZINE(#CodM, NameM, Publisher)
ARTICLE(#CodA, Title, Topic, CodM)
```

1) Titles of motorcycling articles
```
PROJ Title (SEL Topic='motorcycling'(ARTICLE))
```

2) Codes of the magazines which have published at least a motorcycling article
```
PROJ Code (SEL Topic='motorcycling'(ARTICLLE))
```

3) Name of the magazines which have published at least a motorcycling article
```
PROJ NameM (MAGAZINE (JOIN SEL Topic='motorcycling'(ARTICLE)))
```

4) Trovare il codice delle riviste che hanno pubblicato almeno 2 articoli di motociclismo.
```
PROJ CodR (SEL (CodA2!=CodA AND argomento='moticiclismo' AND argomento2='moticiclismo') (ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento (ARTICOLO))))
```

5) Trovare il nome delle riviste che hanno pubblicato almeno 2 articoli di motociclismo.

```
PROJ NomeR (RIVISTA JOIN(SEL (CodA2!=CodA AND argomento='motociclismo' AND
argomento2='motociclismo') (ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento (ARTICOLO)))))
```

6) Trovare gli editori che hanno pubblicato almeno un articolo di motociclismo.
```
PROJ Editore (RIVISTA (JOIN SEL argomento='motociclismo'(ARTICOLO)))
```

7) Trovare il nome delle riviste che non hanno mai pubblicato articoli di motociclismo.
```
(PROJ CodR RIVISTA) - (PROJ CodR (RIVISTA JOIN argomento='motociclismo' (ARTICOLO)))
```

8) Trovare gli editori che non hanno mai pubblicato articoli di motociclismo.
```
(PROJ Editore RIVISTA) - (PROJ CodR (RIVISTA JOIN argomento='motociclismo' (ARTICOLO)))
```

9) Trovare gli editori che hanno pubblicato solo articoli di motociclismo.
```
(PROJ Editore (RIVISTA JOIN (SEL argomento='motociclismo'(ARTICOLO)))) - (PROJ Editore (RIVISTA JOIN (SELargomento!='motociclismo'(ARTICOLO))))
```

10) Trovare gli editori che hanno pubblicato articoli di motociclismo oppure di auto.
```
PROJ Editore (RIVISTA JOIN (SEL (argomento='motociclismo' OR argomento='auto')(ARTICOLO)))
```

11) Trovare gli editori che hanno pubblicato sia articoli di motociclismo sia di auto.
```
PROJ Editore (RIVISTA JOIN (SEL (CodA2!=CodA AND argomento='moticiclismo' AND argomento2='auto')
(ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento (ARTICOLO)))))
```

12) Trovare gli editori che hanno pubblicato almeno 2 articoli di motociclismo.
```
PROJ Editore (RIVISTA JOIN (SEL (CodA2!=CodA AND argomento='moticiclismo' AND
argomento2='motociclismo') (ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento
(ARTICOLO))))) 
```

13) Trovare gli editori che hanno pubblicato un solo articolo (ed uno solo) di motociclismo (possono averpubblicato quanti articoli desiderano relativamente ad altri argomenti).
```
PROJ Editore(((RIVISTA JOIN (ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento (ARTICOLO)))))) - (RIVISTA JOIN (SEL (CodA2!=CodA AND argomento='moticiclismo' AND argomento2='motociclismo') (ARTICOLO JOIN (REN CodA2, Titolo2, Argomento2 <- CodA, Titolo, Argomento
(ARTICOLO))))
```