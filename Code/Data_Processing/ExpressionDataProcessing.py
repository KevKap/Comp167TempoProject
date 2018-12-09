# Imports
import numpy as np
import pandas as pd
import csv
import sys

if __name__ == '__main__':
    # The first argument is the path to the raw downloaded data file, the second is just the expression data taken
    # from the data file, and the third is the full desired file path for the csv file to be saved as.

    raw_data_path = sys.argv[1]
    expression_data_path = sys.argv[2]
    save_path = sys.argv[3]

    # Loading in the raw data from the csv file
    # Sets the column headers to row 16
    raw_data = pd.read_csv(raw_data_path, header=16)

    # Extracting the probe IDs and the Gene Symbols
    probes_to_names = raw_data[['ID', 'Gene Symbol']]

    # Replacing 2-sep to SEPT2 (excel conversion created it was a date)
    probes_to_names = probes_to_names.replace('2-Sep', 'SEPT2')

    # Making data frame into an array
    probes_to_names_matrix = probes_to_names.values

    # Extracting probes and gene names from matrix
    probes = list(probes_to_names_matrix[:, 0])
    gene_names = list(probes_to_names_matrix[:, 1])

    # Looping through and adding probes and gene names and if there are more than one gene name, duplicate the entry
    single_gene_names = []

    for probe in range(len(probes)):
        gene_list = str(gene_names[probe]).split(' /// ')
        for name in gene_list:
            single_gene_names.append([str(probes[probe]), name])

    # Reading in matrix of expression data (patients as columns, genes as rows)
    expression_data = pd.read_excel(expression_data_path, index_col=0)

    gene_name_to_probe_dictionary = {}

    # Adds probes for corresponding gene in the gene_name_to_probe_dictionary (gene is key, probes are values)
    for row in single_gene_names:
        if row[1] in gene_name_to_probe_dictionary:
            gene_name_to_probe_dictionary[row[1]].append(row[0])
        else:
            gene_name_to_probe_dictionary[row[1]] = [row[0]]

    gene_name_to_median_data_dictionary = {}

    # Iterates through all the genes in the gene_name_to_probe dictionary and finds the median of all the gene data
    # that correspond to that gene (multiple probes correspond to one gene). Uses np.nanmedian, which just ignores
    # missing values in the data.

    for key in gene_name_to_probe_dictionary:
        # Getting probes from gene key
        gene_probes = gene_name_to_probe_dictionary[key]
        temp_gene_data = []
        # Iterating through probes and appending data from expression data
        for probe in gene_probes:
            temp_gene_data.append(expression_data.loc[[probe]].values)
        # Getting the median for each column
        median_values = np.nanmedian(np.nanmedian(temp_gene_data, axis=1), axis=0)
        # Assigning median to key in dictionary
        gene_name_to_median_data_dictionary[key] = median_values

    # Writing all of the gene data to a csv file, samples are columns and genes are rows.
    with open(save_path, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(gene_name_to_median_data_dictionary.keys())
        writer.writerows(zip(*gene_name_to_median_data_dictionary.values()))
