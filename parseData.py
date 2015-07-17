import json

import string
import nltk
from nltk.stem.porter import *

# parse first n number of reviews from the system path
def parse(path, n = 0):
  data = []
  count = 0
  with open(path) as f:
    if n != 0:
      for line in f:
        data.append(eval(line))
        count += 1
        if count == n:
          break
    else:
      for line in f:
        data.append(eval(line))
  return data

# separate product data by category name key
def parseAndWrite(infile, outfile, key):
  count = 0
  punctuation = set(string.punctuation)
  with open(infile) as inf, open(outfile,'w') as of:
    for line in inf:
      item = eval(line)
      if item.has_key('categories'):
        for cat in item['categories']:
          r = ''.join([c.lower() for c in cat if not c in punctuation])
          print r
          if key in r.split():
            of.write(json.dumps(item))
            of.write(",")
            count += 1
            break
      if count >= 5:
        break
  of.close()

# extract all reviewText sections and put into a list
# return type: [['word','word'],['word']]
def allReviews(data):
  return [d['reviewText'] for d in data]

# tokenize reviews, remove punctuation and capitalization
# return type: [['word','word'],['word']]
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

# ignore capitalization and punctuation with stemming
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