# compsci

Documentation, resources, projects and lecture notes on the courses I attended at *Università degli Studi di Milano Bicocca* for my Bachelor's and Master's degrees in Computer Science.

You're welcome to report errors, improvements or feedbacks as Issues, or directly Pull Request.

PDF are hosted with `git-lfs`. Be sure to have it installed before cloning (or clone from the GitHub website).

### Contents

- [Master's](#master-s)
    + [Data Technology and Machine Learning](#data-technology-and-machine-learning)
    + [Informatics for industrial applications (Digital systems)](#informatics-for-industrial-applications--digital-systems-)
    + [Probabilistic Models for decision making](#probabilistic-models-for-decision-making)
    + [Methods of Scientific Computing](#methods-of-scientific-computing)
- [Bachelor's](#bachelor-s)
    + [Stage/Thesis](#internship-thesis)
    + [Operations Research](#operations-research)
    + [Information Security](#information-security)
    + [Databases](#databases)
    + [Bioinformatics](#bioinformatics)
    + [Operative Systems](#operative-systems)
    + [Programming Paradigms](#programming-paradigms)
    + [Embedded Systems](#embedded-systems)
- [Resources](#resources)
- [Building](#building)


## Master's

#### Data Technology and Machine Learning

- [Introduction to non-centralized DBMSs](https://github.com/avivace/compsci/raw/master/masters/datatech/2.pdf)
- [Data Quality dimensions](https://github.com/avivace/compsci/raw/master/masters/datatech/dataquality.pdf)
- [Basket Shots](https://github.com/avivace/basket-shots) - Final course project. Predicting Basket Shots outcomes using Suppor Vector Machines.

#### Informatics for industrial applications (Digital systems)

- [VHDLtrafficlights](https://github.com/avivace/) - Final course project. Implement a semaphore with a Xilinx FPGA.

#### Probabilistic Models for decision making

- [kalman2d](https://github.com/avivace/kalman) - Final course project. Interactive 2D simulation of the Kalman Filter in use to reduce input noise.

#### Methods of Scientific Computing

- [MSC1-SparseMatrix](https://github.com/avivace/mcs1-sparsematrix)
- [MSC2-DCT](https://github.com/avivace/mcs2-dct)


## Bachelor's

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

### Resources

### Building

Markdown files are compiled to PDF using _pandoc_.`pandoc $file_base_name.md -o $file_base_name.pdf template.tex`. The LaTeX template used is hosted [here](https://github.com/avivace/dotfiles).