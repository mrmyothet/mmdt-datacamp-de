from data import word_counts, datacamp_tweets

# Import local package
import text_analyzer
from text_analyzer import Document

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweets)

# Print the text attribute of the Document instance
# print(my_document.text)
# print(my_document.tokens)
# print(my_document.word_counts)

# create a new document instance from datacamp_tweets
datacamp_doc = Document(text=datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print("tokens")
print(type(datacamp_doc.tokens))
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print("word_counts")
print(type(datacamp_doc.word_counts))
print(datacamp_doc.word_counts.most_common(5))
