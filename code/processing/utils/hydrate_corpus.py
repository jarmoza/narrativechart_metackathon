# Author: Jonathan Armoza
# Creation date: November 30, 2021
# Purpose: Produce a folder of txt files from the Metackathon corpus csv file

# Imports

# System
import csv
import os

# Custom
from paths import paths

# Main script

def main():

    # 1. Read in corpus csv lines and output the text bodies as documents
    with open(paths["corpus_csv"], "r") as corpus_file:
        reader = csv.DictReader(corpus_file)
        for row in reader:
            filename = "{0}{1}{2}.txt".format(paths["corpus_docs"], os.sep, row["pmid"])
            with open(filename, "w") as corpus_doc:
                corpus_doc.write(row["body"])
        

if "__main__" == __name__:
    main()