# Author: Jonathan Armoza
# Creation date: November 30, 2021
# Purpose: Defines file paths for the topic-tracing Metackathon project

# Imports

# System
import os

# Globals

paths = {}
paths["data_folder"] = "{0}{1}..{1}..{1}..{1}data{1}".format(os.getcwd(), os.sep)
paths["corpus_csv"] = paths["data_folder"] + "corpus.csv"
paths["output"] = "{0}{1}..{1}data{1}output{1}".format(os.getcwd(), os.sep)
paths["corpus_docs"] = "{0}txt{1}".format(paths["output"], os.sep)
