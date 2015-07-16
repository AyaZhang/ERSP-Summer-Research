import json

import string
import nltk
from nltk.stem.porter import *

# Get rid of the annoying u' (unicode strings)
def byteify(input):
  if isinstance(input, dict):
    return {byteify(key):byteify(value) for key,value in input.iteritems()}
  elif isinstance(input, list):
    return [byteify(element) for element in input]
  elif isinstance(input, unicode):
    return input.encode('utf-8')
  else:
    return input

# Parse first n number of reviews from the system path
def parse(path, n):
  data = []
  count = 0
  with open(path) as f:
    for line in f:
      data.append(byteify(json.loads(line)))
      count += 1
      if count == n:
        break
  return data

# Extract all reviewText sections and put into a list
# Return type: [['word','word'],['word']]
def allReviews(data):
  return [d['reviewText'] for d in data]

# Tokenize reviews, remove punctuation and capitalization
# Return type: [['word','word'],['word']]
def tokenize(data):
  punctuation = set(string.punctuation)
  reviewList = allReviews(data)
  tokenizedList = []
  for r in reviewList:
    tokens = nltk.word_tokenize(r)
    words = [w.lower() for w in tokens if w.isalpha()]
    tokenizedList.append(words)
  return tokenizedList

########################################################
################### NOT WORKING YET ####################
########################################################

# Ignore capitalization and punctuation with stemming
def stemming(tokenizedList):
  stemmer = PorterStemmer()
  stemmedList = []
  for d in tokenizedList:
    words = []
    for w in d:
      w = stemmer.stem(w)
      words.append(w)
    stemmedList.append(words)
  return stemmedList