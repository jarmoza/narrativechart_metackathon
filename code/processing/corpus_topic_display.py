# Author: Jonathan Armoza
# Created: May 13, 2022
# Purpose: Displays the topics of a corpous from MALLET outputs

# Imports

# Standard libraries
import json
import os

# Globals

paths = {

    "data": {
        "mallet": "{0}{1}..{1}..{1}code{1}twic{1}data{1}output{1}mallet{1}".format(os.getcwd(), os.sep),
        "root": f"{os.getcwd()}{os.sep}"
    }
}

def main():

    # Calculate topic proportions of corpus
    with open(f"{paths['data']['root']}twic_corpusmap.json", "w") as input_file:
        corpus_map = json.load(input_file)



if "__main__" == __name__:
    main()