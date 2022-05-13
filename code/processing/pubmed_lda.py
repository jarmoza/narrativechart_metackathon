
# Author: Jonathan Armoza
# Creation date: November 30, 2021
# Purpose: Creates an LDA model of the 14k article PubMed corpus subset

# Imports
import glob
import os

# Third party
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.utils import tokenize

# Custom
from utils.paths import paths

# Main script
def main():

	print("Preparing corpus for modeling...")

	# 1. Create a collection of tokenized PubMed documents
	tokenized_corpus = []

	corpus_docs_path = "{0}{1}data{1}output{1}txt{1}".format(os.getcwd(), os.sep)
	model_output_path = "{0}{1}data{1}output{1}lda_model{1}".format(os.getcwd(), os.sep)

	index = 0
	max_docs = 10
	for filepath in glob.glob(corpus_docs_path + "*.txt"):

		# if index >= max_docs - 1:
		#	 break

		with open(filepath, "r") as txt_file:
			
			# A. Tokenize the txt file with gensim's tokenizer
			tokenized_txt = list(tokenize(txt_file.read()))

			# B. Save tokenized txt
			tokenized_corpus.append(tokenized_txt)

		index += 1

	# 2. Create a gensim dictionary of all tokens in all texts
	pubmed_dictionary = Dictionary(tokenized_corpus)

	# 3. Create a numeric bag of words version of the corpus with token counts
	pubmed_bowcorpus = [pubmed_dictionary.doc2bow(text) for text in tokenized_corpus]

	print("Creating LDA topic model of corpus...")

	# 4. Create an LDA topic model of the corpus
	pubmed_lda = LdaModel(pubmed_bowcorpus, num_topics=100)

	print("Saving model to disk...")

	# 5. Save the model to disk
	model_filename = f"{model_output_path}pubmed_ldamodel"
	pubmed_lda.save(model_filename)

	print("Finished!")


if "__main__" == __name__:
	main()