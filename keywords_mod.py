import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import collections




def keyWords(text):
     text = word_tokenize(text)
     BagOfWords = nltk.pos_tag(text)
     nouns = []
     for word in BagOfWords:
          if ((word[1] == 'NNP')):
              nouns.append(word[0])
     counter=collections.Counter(nouns)
     print(counter.most_common(5))
