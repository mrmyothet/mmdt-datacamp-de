from collections import Counter
from io import StringIO
from tokenize import generate_tokens, tokenize

# from yellowbrick.text import plot_counter


class Document:
    def __init__(self, text):
        self.text = text

        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()

        # pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        lst = []
        tokens = generate_tokens(StringIO(self.text).readline)
        for token in tokens:
            lst.append(token.string)

        return lst

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)


'''
    def plot_counts(self, attribute="word_counts", n_most_common=5):
        """
        Plot most common elements of a ``collections.Counter`` instance attribute
        :param attribute: name of ``Counter`` attribute to use as object to plot
        :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
        :return: None; a plot is shown using matplotlib

        >>> doc = Document("duck duck goose is fun when you\'re the goose")
        >>> doc.plot_counts(\'word_counts\', n_most_common=5)  # same as default call\n
        """

        plot_counter(getattr(self, attribute), n_most_common)
'''
