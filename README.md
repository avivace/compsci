# compsci

> Lecture notes, projects and various resources on the courses I attended at *Università degli Studi di Milano Bicocca* for my Bachelor's and Master's degrees in *Computer Science*.

You're welcome to report errors, improvements or feedbacks as Issues, or directly propose modifications with Pull Requests.

### Contents

- [General resources](#general-resources)
- [Master's](#masters)
    + [Probabilistic Models for decision making](#probabilistic-models-for-decision-making)
    + [Data Analytics](#data-analytics)
      - [Theory](#theory)
    + [Complex Systems](#complex-systems)
    + [Cloud Computing](#cloud-computing)
    + [Software Design Lab](#software-design-lab)
    + [Theory of Computation](#theory-of-computation)
    + [Concurrent Models](#concurrent-models)
    + [Data Technology and Machine Learning](#data-technology-and-machine-learning)
    + [Informatics for industrial applications (Digital systems)](#informatics-for-industrial-applications--digital-systems-)
    + [Methods of Scientific Computing](#methods-of-scientific-computing)
- [Bachelor's](#bachelors)
    + [Internship/Thesis](#internship-thesis)
    + [Operations Research](#operations-research)
    + [Information Security](#information-security)
    + [Databases](#databases)
    + [Bioinformatics](#bioinformatics)
    + [Operative Systems](#operative-systems)
    + [Programming Paradigms](#programming-paradigms)
    + [Embedded Systems](#embedded-systems)
  * [Building](#building)

## General resources

More courses notes:

- [C. Baldi](https://github.com/crisbal/Appunti-Unimib) (Bachelor's)

Some theses I appreciated and used as examples for the graduating students I advised:

- [M. Rota - *Rilevamento di elementi testuali in immagini digitali*](https://github.com/dubvulture/thesis/blob/master/thesis.pdf) - Fully convutional networks. Advisors: R. Schettini, M.Buzzelli.
- [L. Soligo - *Generazione di reti Bayesiane
a partire da ontologie*](https://gitlab.com/LolloneS/Tesi-Triennale) - Advisors: F. Stella, G. Sottocornola.
- [R. Pozzi - *Aggiornamento e ripristino delle funzionalità in sistemi Linux Embedded*](https://gitlab.com/rpo254/texis/blob/master/Tesi.pdf) - Advisors: L. Mariani, A. Vivace.

## Master's

2018-2020

#### Thesis

- [*Experimental Anomaly Detection on CERN CMS Trigger Rates*](https://github.com/avivace/master-thesis)

#### Probabilistic Models for decision making

- Course project: [kalman2d](https://avivace.github.io/kalman/) - Interactive 2D simulation of the *Kalman Filter* (LQE) in use to reduce (statistical) input noise.

#### Data Analytics

- Course project: [Amazon Reviews Analytics](https://github.com/avivace/reviews-sentiment) - Data exploration, Analytics, Sentiment Analysis, Topic Analysis (LDA) and a web demo exposing the ML trained models.
- [Notes, definitions and solved questions](masters/data-analytics/notes.md)
- Unbalaced data: [Survey of resampling techniques for improving classification performance in unbalanced datasets](https://arxiv.org/abs/1608.06048)
- Community Detection approaches: [Web Structure Mining: Community Detection and Evaluation](https://www.irit.fr/~Yoann.Pitarch/Docs/M2Stats/WebMining/wsm_communities.pdf)
- Spectral Clustering:
    + [On Spectral Clustering: ANalysis and an algorithm - Ng, Jordan, WWeiss](http://ai.stanford.edu/~ang/papers/nips01-spectral.pdf)
    + [Spectral clustering - The intuition and math behind how it works!](https://towardsdatascience.com/spectral-clustering-82d3cff3d3b7)
    + [Spectral Clustering: A quick overview](https://calculatedcontent.com/2012/10/09/spectral-clustering/)
    + (Video) [Spectral Clustering](https://www.youtube.com/watch?v=zkgm0i77jQ8)
    + (Video) [Spectral Clustering Algorithm](https://www.youtube.com/watch?v=P-LEH-AFovE)

#### Complex Systems

- Course project: [Physarum](https://github.com/avivace/Physarum) - Final course project. Physarum polycephalum slime mould computing simulations

#### Cloud Computing

- [Cloud Computing and Distributed Systems](https://github.com/Cinofix/Afternotes) - Afternotes by Antonio E. Cinà from the course at University Ca' Foscari of Venice, master in Computer Science - Data Management and Analytics.

#### Software Design Lab

- Course project: [Smart Home Automation](https://github.com/avivace/sha) - A Rasberry Pi integrated domotic solution with MQTT supporting sensors, actuators and a thermostat. Controllable from a fancy web application, smart speakers or a basic SMS interface. Documentation (Software Requirements Specification, Software Architecture, Testing, Deploy and Implementation) and a software implementation in Connexion (OpenAPI 3) and VueJS.


#### Theory of Computation

- [Notes](https://github.com/avivace/compsci/blob/master/masters/computation-theory/notes.pdf)

#### Concurrent Models

- [Axiomatic semantics solved exercises](masters/concurrent-models) (Hoare triples)
- [Paolo Mancarella (Università degli studi di Pisa) - *Note di semantica assiomatica*](http://pages.di.unipi.it/corradini/Didattica/LPP-13/Logica%20di%20Hoare.pdf)
- [Luca Aceto - Reactive Systems: Modelling, Specification and Verification](http://www.cs.ioc.ee/yik/schools/win2007/ingolfsdottir/sv-book-part1.pdf)
- [Linear Temporal Logic examples](http://www.dis.uniroma1.it/liberato/ar/ltl/ltl.html)

#### Data Technology and Machine Learning

- Course project: [Basket Shots](https://github.com/avivace/basket-shots) - Predicting Basket Shots outcomes using Suppor Vector Machines ([documentation](https://github.com/avivace/basket-shots/raw/master/docs/index.pdf)).
- Notes: [Introduction to non-centralized DBMSs](https://github.com/avivace/compsci/blob/master/masters/data-technology/2.pdf), [Data Quality dimensions](https://github.com/avivace/compsci/blob/master/masters/data-technology/dataquality.pdf).


#### Informatics for industrial applications (Digital systems)

- Course project: [VHDLtrafficlights](https://github.com/avivace/VHDLtrafficlights) - Implement a semaphore with a Xilinx FPGA.
- [Elementi di Programmazione Logica](https://elearning.unimib.it/pluginfile.php/477370/mod_resource/content/2/DispenseInformaticaIndustriale.pdf)


#### Methods of Scientific Computing

Final course projects:

- [MSC1-SparseMatrix](https://github.com/avivace/mcs1-sparsematrix) - Comparing open source and propetary solvers for sparse matrices.
- [MSC2-DCT](https://github.com/avivace/mcs2-dct) - Comparing naïve and scipy implementations of *Discrete Cosine Transform* 2 (and its inverse) and exposing the scipy implementation on a web appplication allowing to apply it on user provided images (BMP format).


## Bachelor's

2014-2017

#### Internship/Thesis

- [DNA Recombination](https://github.com/avivace/dna-recombination).  Approaching a Computational Biology problem with integer linear programming tools.

#### Operations Research

- [Soluzioni domande esami scritti](https://github.com/avivace/compsci/blob/master/bachelors/operative-research/risposte.pdf)

#### Information Security

- [Applicazioni](https://github.com/avivace/compsci/blob/master/bachelors/sicurezza/1applicazioni.pdf)
- [Crittografia](https://github.com/avivace/compsci/blob/master/bachelors/sicurezza/2crittografia.pdf)
- [Sistemi Operativi](https://github.com/avivace/compsci/blob/master/bachelors/sicurezza/3sistemi_operativi.pdf)
- [Reti](https://github.com/avivace/compsci/blob/master/bachelors/sicurezza/4reti.pdf)

#### Databases

- [Relational algebra exercises](https://github.com/avivace/compsci/blob/master/bachelors/databases/relational_algebra.md)
- [Logic programming](https://github.com/avivace/compsci/raw/master/bachelors/databases/teoria_progLogica.pdf)
- [Relational algebra](https://github.com/avivace/compsci/blob/master/bachelors/databases/teoria_AlgebraRelazionale.pdf)
- [SQL](https://github.com/avivace/compsci/blob/master/bachelors/databases/teoria_SQL.pdf)

#### Bioinformatics

- Theory: [Pattern Matching, Suffix Trees and Alignment](https://github.com/avivace/compsci/raw/master/bachelors/bioinformatics/bio.pdf)
- Final project: [scripts](https://github.com/avivace/bio-p), [final PR](https://github.com/avivace/rgfa). Add a method to compare sequence graphs to the RGFA library (Ruby).

#### Operative Systems

- [Process Synchronization, deadlocks](https://avivace.com/assets/OS.pdf)

#### Programming Paradigms

- Theory: [Functional Programming and Lisp](https://github.com/avivace/compsci/raw/master/bachelors/programming-paradigms/FP_Lisp.pdf)
- [Final project](https://github.com/avivace/mvpoli). Two libraries (Prolog and Common Lisp) to manipulate multivariate polynomials. Available predicates allows parsing, sorting, operations(sum, product), evaluating and printing polynomials.

#### Embedded Systems

- [Theory](https://github.com/avivace/compsci/raw/master/bachelors/embedded-systems/teoria.pdf)
- [Final Project](https://github.com/avivace/EmbeddedSystems-8051). Implement in C, on a Silicon Labs C8051F020 board (and an additional board driven via SMBus):
    + continuos detection of the inclination and the temperature, 
    + continuos display of the value on the LCD display, 
    + LCD controls (turn on, off, backlight intensity) with an hardware button.

    Using interrupts and PWM techniques.

### Building

Markdown files are compiled to PDF using _pandoc_.

```bash
pandoc $file_base_name.md -o $file_base_name.pdf template.tex
```

The LaTeX template used is hosted [here](https://github.com/avivace/dotfiles).
