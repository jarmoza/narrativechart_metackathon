import os

from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.test.utils import common_texts

from utils.utils import debug_section

# Create a corpus from a list of texts
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

debug_section("Common texts")
print(common_texts)
debug_section("Common dictionary")
print(common_dictionary)
debug_section("Common corpus")
print(common_corpus)

# Train the model on the corpus.
# lda = LdaModel(common_corpus, num_topics=10)

# Save model to disk.
# model_filename = f"{os.getcwd()}{os.sep}output{os.sep}gensim_ldamodel"
# lda.save(model_filename)