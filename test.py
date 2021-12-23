#英文情感分析 textblob
from snownlp import SnowNLP
from textblob import TextBlob
import nltk
text = 'I am so happy.'
blob = TextBlob(text)
print(blob)
print(blob.sentences)
print(blob.sentences[0].sentiment)
print(blob.sentences[1].sentiment)
print(blob.sentiment)

# #中文情感分析SnowNLP

# text = u'我很高兴啊.'
# s = SnowNLP(text)
# for sentence in s.sentences:
#     print(sentence)
# s1 = SnowNLP(s.sentences[0])
# s2 = SnowNLP(s.sentences[1])
# print(s1.sentiments)
# print(s2.sentiments)