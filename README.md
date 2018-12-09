# Comp167TempoProject

This is our final group project for CS167: Computational Biology. In this project, we utilized Temporal Modeling of Pathway Outliers, referred to as TEMPO, to analyze temporal dysregulation in gene expression in Parkinson's patients using microarray data. The TEMPO model and project documentation can be found at: http://bcb.cs.tufts.edu/tempo/ and was developed by Pietras et al. The dataset utilized in this project comes from the Gene Expression Omnibus, GEO, with ID GSE20295 and represents post-mortem brain samples originating in the prefrontal area 9, putamen, and the substantia nigra from control patients and patients who had Parkinson's. 

## Installing and Running TEMPO

Follow instructions found at http://bcb.cs.tufts.edu/tempo/ to install the TEMPO in R. Furthermore, the readxl package (https://cran.r-project.org/web/packages/readxl/index.html) should also be installed. Once installed, the MainTempoScript.R can be run once the paths to the following files are updated:

* row_labelled_expression_data_path
* matrix_expression_data_path
* age_data_path
* phenotype_data_path
* gene_sets_path

The script to generate the expression data files from the original dataset can be found in the Data_Processing folder in the ExpressionDataProcessing.py . The age data and phenotype data were extracted by hand from the original data file using excel and were formatted as described by http://bcb.cs.tufts.edu/tempo/. 

Locally, TEMPO can be run using 4 permutations and 4 cores, however to obtain statistically signficant results, permutations should be set to 500. This project was run on the Tufts red-giant compute cluster, utilizing a total of 24 cores.

## Resources

TEMPO Project:

* http://bcb.cs.tufts.edu/tempo/

* Pietras, Christopher, Faith Ocitti, and Donna Slomin. “TEMPO: Detecting Pathway-Specific Temporal Dysregulation of Gene Expression in Disease.” ResearchGate, 2018. http://dx.doi.org/10.1145/3233547.3233559.

Dataset:

* Middleton, Frank A. “GEO Accession Viewer.” Series GSE20295, February 10, 2018. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE20295.
