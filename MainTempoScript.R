.libPaths( "/h/kkapne01/CS167/Project/" )

library("tempoR")
library("readxl")

row_labelled_expression_data_path <- '/h/kkapne01/CS167/Project/Median_Data_AgeAdjusted.xlsx'
matrix_expression_data_path <- '/h/kkapne01/CS167/Project/Unlabelled_Median_Data_AgeAdjusted.xlsx'
age_data_path <- '/h/kkapne01/CS167/Project/patient_age_AgeAdjusted.xlsx'
phenotype_data_path <- '/h/kkapne01/CS167/Project/Disease_status_AgeAdjusted.xlsx'
gene_sets_path <- '/h/kkapne01/CS167/Project/GeneSets.gmt'

row_Labelled_expression_data <- t(read_excel(row_labelled_expression_data_path))
age_data <- t(read_excel(age_data_path))
phenotype_data <- read_excel(phenotype_data_path)
gene_sets <- loadGMT(gene_sets_path)
final_data <- t(read_excel(matrix_expression_data_path, sheet = 1, col_name = FALSE))

ages <- as.integer(unlist(age_data[2,]))
sample_ids <- age_data[1,]
names(ages) <- sample_ids
ages <- list(ages)

gene_names <- row_Labelled_expression_data[1,]

rownames(final_data) <- sample_ids
colnames(final_data) <- gene_names

disease_states <- as.logical(unlist(phenotype_data[,2]))
opposite_disease_states <- !disease_states

Parkinsons = list()
Parkinsons$ctrl <- sample_ids[opposite_disease_states]
Parkinsons$test <- sample_ids[disease_states]
Parkinsons$age <- unlist(ages)

results = tempo.run(ctrl = Parkinsons$ctrl,
                    test = Parkinsons$test,
                    genesets = gene_sets,
                    X = final_data,
                    Y = Parkinsons$age,
                    numPerms = 500,
                    nCores = 24,
                    output = "/h/kkapne01/CS167/Project/AgeAdjustedResults",
                    pCutoff = 1,
                    fdrCutoff = 2,
                    pMseCutoff = 1)