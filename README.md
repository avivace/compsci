# compsci

> Documentation, resources, projects and lecture notes on the courses I attended at *Università degli Studi di Milano Bicocca* for my Bachelor's and Master's degrees in *Computer Science*.

You're welcome to report errors, improvements or feedbacks as Issues, or directly propose modifications with a Pull Request.

PDF are hosted with `git-lfs`. Be sure to have it installed before cloning (or click [here](https://github.com/avivace/compsci/archive/master.zip) for the full zip).

### Table of contents

- [General resources](#general-resources)
- [Master's](#masters)
    + Design Lab
    + Theory of Computation
    + Concurrent Models
    + Data Technology and Machine Learning
    + Informatics for industrial applications (Digital systems)
    + Probabilistic Models for decision making
    + Methods of Scientific Computing
- [Bachelor's](#bachelors)
    + Internship/Thesis
    + Operations Research
    + Information Security
    + Databases
    + Bioinformatics
    + Operative Systems
    + Programming Paradigms
    + Embedded Systems
- [Building](#building)

## General resources

More courses notes:

- [C. Baldi](https://github.com/crisbal/Appunti-Unimib) (Bachelor's)

Some theses I appreciated / used as examples for the graduating students I advised:

- [M. Rota - *Rilevamento di elementi testuali in immagini digitali*](https://github.com/dubvulture/thesis/blob/master/thesis.pdf) - Fully convutional networks. Advisors: R. Schettini, M.Buzzelli.
- [L. Soligo - *Generazione di reti Bayesiane
a partire da ontologie*](https://gitlab.com/LolloneS/Tesi-Triennale) - Advisors: F. Stella, G. Sottocornola.
- [R. Pozzi - A*ggiornamento e ripristino delle funzionalità in sistemi Linux Embedded*](https://gitlab.com/rpo254/texis/blob/master/Tesi.pdf) - Advisors: L. Mariani, A. Vivace.

## Master's

2018-2019

#### Design Lab

- [Smart Home Automation](https://github.com/avivace/sha) - Final course project. A Rasberry Pi integrated domotic solution with MQTT supporting sensors, actuators and thermostat. Controllable from a fancy VueJS web application, smart speakers or a basic SMS interface. Documentation (Software Requirements Specification, Software Architecture, Testing, Deploy and Implementation) and a software implementation in Connexion (OpenAPI 3) and VueJS.


#### Theory of Computation

- [Notes](https://github.com/avivace/compsci/blob/master/masters/computation/notes.pdf)

#### Concurrent Models

- [Paolo Mancarella (Università degli studi di Pisa) - *Note di semantica assiomatica*](http://pages.di.unipi.it/corradini/Didattica/LPP-13/Logica%20di%20Hoare.pdf)
- [Luca Aceto - Reactive Systems: Modelling, Specification and Verification](http://www.cs.ioc.ee/yik/schools/win2007/ingolfsdottir/sv-book-part1.pdf)

#### Data Technology and Machine Learning

- [Basket Shots](https://github.com/avivace/basket-shots) - Final course project. Predicting Basket Shots outcomes using Suppor Vector Machines ([documentation](https://github.com/avivace/basket-shots/raw/master/docs/index.pdf)).
- Notes: [Introduction to non-centralized DBMSs](https://github.com/avivace/compsci/raw/master/masters/datatech/2.pdf), [Data Quality dimensions](https://github.com/avivace/compsci/raw/master/masters/datatech/dataquality.pdf).


#### Informatics for industrial applications (Digital systems)

- [VHDLtrafficlights](https://github.com/avivace/) - Final course project. Implement a semaphore with a Xilinx FPGA.

#### Probabilistic Models for decision making

- [kalman2d](https://avivace.github.io/kalman/) - Final course project. Interactive 2D simulation of the *Kalman Filter* (LQE) in use to reduce (statistical) input noise.

#### Methods of Scientific Computing

Final course projects:

- [MSC1-SparseMatrix](https://github.com/avivace/mcs1-sparsematrix) - Comparing open source and propetary solvers for sparse matrices.
- [MSC2-DCT](https://github.com/avivace/mcs2-dct) - Comparing naïve and scipy implementations of *Discrete Cosine Transform* 2 (and its inverse) and exposing the scipy implementation on a web appplication allowing to apply it on user provided images (BMP format).


## Bachelor's

2014-2017

#### Internship/Thesis

- [DNA Recombination](https://github.com/avivace/dna-recombination).  Approaching a Computational Biology problem with integer linear programming tools.

#### Operations Research

- [Soluzioni domande esami scritti](https://github.com/avivace/compsci/blob/master/operative-research/risposte.pdf)

#### Information Security

- [Applicazioni](https://github.com/avivace/compsci/blob/master/sicurezza/1applicazioni.pdf)
- [Crittografia](https://github.com/avivace/compsci/blob/master/sicurezza/2crittografia.pdf)
- [Sistemi Operativi](https://github.com/avivace/compsci/blob/master/sicurezza/3sistemi_operativi.pdf)
- [Reti](https://github.com/avivace/compsci/blob/master/sicurezza/4reti.pdf)

#### Databases
- [Relational algebra exercises](https://github.com/avivace/compsci/blob/master/databases/relational_algebra.md)
- [Logic programming](https://github.com/avivace/compsci/raw/master/databases/teoria_progLogica.pdf)
- [Relational algebra](https://github.com/avivace/compsci/blob/master/databases/teoria_AlgebraRelazionale.pdf)
- [SQL](https://github.com/avivace/compsci/blob/master/databases/teoria_SQL.pdf)

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
