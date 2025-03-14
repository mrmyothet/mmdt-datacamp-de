from collections import Counter
from io import StringIO
import re

# from yellowbrick.text import plot_counter


class Document:
    def __init__(self, text):
        self.text = text

        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()

        # pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

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


# Complete the function's docstring
def tokenize(text, regex=r"[a-zA-z]+"):
    """Split text into tokens using a regular expression

    :param text: text to be tokenized
    :param regex: regular expression used to match tokens using re.findall
    :return: a list of resulting tokens

    >>> tokenize('the rain in spain')
    ['the', 'rain', 'in', 'spain']
    """
    return re.findall(regex, text, flags=re.IGNORECASE)
