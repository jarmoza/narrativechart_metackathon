# Author: Jonathan Armoza
# Creation date: November 30, 2021
# Purpose: Fix for temporarily malformed corpus.csv

# Imports

# System
import csv
import os

# Custom
from paths import paths

# Main script

def main():

    # 0. Keeping track of malformed row indices
    wellformed_rows = []
    csv_lines = None

    with open(paths["corpus_csv"], "r") as corpus_file:
        csv_reader = csv.DictReader(corpus_file)
        for row in csv_reader:
            print(row["pmid"])

    if True:
        return
        
    # 1. Read in corpus and check for well-formed rows
    with open(paths["corpus_csv"], "r") as corpus_file:

        csv_lines = corpus_file.readlines()

        for index in range(len(csv_lines)):

            # A. Split the line by commas
            line = csv_lines[index]
            line_parts = line.split(",")

            print(line_parts[0])

            # B. If numeric PubMed ID exists in first column,
            # the line is considered well-formed
            if str(line_parts[0]).isnumeric():
                wellformed_rows.append(index)

    if True:
        return

    # 2. Create a collection of well-formed csv rows,
    # incorporating malformed rows
    new_csv_lines = []
    for index in range(len(wellformed_rows)):

        if (len(csv_lines) - 1 == wellformed_rows[index]) or \
           1 == wellformed_rows[index + 1] - wellformed_rows[index]:
           new_csv_lines.append(csv_lines[wellformed_rows[index]])
        else:
            compound_line = [csv_lines[wellformed_rows[index]]]
            while 1 != wellformed_rows[index + 1] - wellformed_rows[index]:
                compound_line.append(csv_lines[wellformed_rows[index + 1]])
                index += 1
            for index2 in range(len(compound_line)):
                compound_line[index2] = compound_line[index2].replace("\"", "\'")
                compound_line[index2] = f"\"{compound_line[index2]}\""
                full_compound_line = " ".join(compound_line)
                new_csv_lines.append(full_compound_line)

    # 3. Write out new csv file
    with open(paths["output"] + "corpus_fixed.csv", "w") as output_file:
        for line in new_csv_lines:
            output_file.write(line)

        # # A. Read in csv into dictionary reader
        # reader = csv.DictReader(corpus_file)

        # # B. Check each line for malformed PubMed article ID
        # for row in reader:

        #     if row["pmid"].isnumeric():

if "__main__" == __name__:
    main()

