from collections import Counter
from io import StringIO
from tokenize import generate_tokens, tokenize


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
