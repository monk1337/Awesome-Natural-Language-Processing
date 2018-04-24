from textblob import TextBlob

from textblob import Word


text = '''Apple is looking at buying U.K. startup for $1 billio
'''

blob = TextBlob(text)
print(blob.tags)
print(blob.noun_phrases)
print(blob.sentiment)

word=Word('did')
print(word.lemmatize('v')) #verb 






#output

[('Apple', 'NNP'), ('is', 'VBZ'), ('looking', 'VBG'), ('at', 'IN'), ('buying', 'VBG'), ('U.K.', 'NNP'), ('startup', 'NN'), ('for', 'IN'), ('1', 'CD'), ('billio', 'NN')]
['apple', 'u.k.']
Sentiment(polarity=0.0, subjectivity=0.0)
do

Process finished with exit code 0
