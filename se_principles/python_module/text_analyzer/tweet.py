import text_analyzer
from text_analyzer import SocialMedia


# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__()
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars="RT")
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)


def filter_lines(text, first_chars):
    """
    Filter lines by beginning characters (case sensitive)
    :param text:  multi-line text to filter
    :param first_chars: required characters for line to start with to be returned
    :return: text with only lines starting with first_chars included
    
    >>> text = 'humpty dumptyn sat on a wall nhumpty dumpty nhad a great fall
    >>> filter_lines(text, \'h\')\n    \'humpty dumpty\\\\nhumpty dumpty\\\\nhad a great fall\
    >>> filter_lines(text, \'humpty\')\n    \'humpty dumpty\\\\nhumpty dumpty\'\n    """

    n_chars = len(first_chars)
    lines = text.split("\\n")

    filtered_lines = [l for l in lines if l[:n_chars] == first_chars]

    return "\\n".join(filtered_lines)
