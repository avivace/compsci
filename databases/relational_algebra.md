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

