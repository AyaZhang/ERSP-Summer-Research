import json
import os
import collections

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
        print eval(line)
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
  unique = set()
  with open(infile) as inf, open(outfile,'w') as of:
    for line in inf:
      item = eval(line)
      if item.has_key('categories'):
        for cat in item['categories']:
          for k in cat:
            if k == key and item['asin'] not in unique:
              of.write(line)
              unique.add(item['asin'])
  inf.close()
  of.close()

# read from infile and extract only the review that are relevant
# idSet: a set of asin numbers of desired products
def parseAndWrite_constraint(infile, outfile, idSet):
  with open(infile) as inf, open(outfile,'w') as of:
    for line in inf:
      item = eval(line)
      if item['asin'] in idSet:
        of.write(line)
  inf.close()
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

# ignore capitalization and punctuation with stemming
# return type: [['word','word'],['word']]
def stemming(tokenizedList):
  stemmer = PorterStemmer()
  stemmedList = []
  for d in tokenizedList:
    words = []
    for w in d:
      w = stemmer.stem(w)
      words.append(str(w))
    stemmedList.append(words)
  return stemmedList

# convert unicode string to string object
def convert(data):
  if isinstance(data, basestring):
    return str(data)
  elif isinstance(data, collections.Mapping):
    return dict(map(convert, data.iteritems()))
  elif isinstance(data, collections.Iterable):
    return type(data)(map(convert, data))
  else:
    return data

# parse labels file
def loadLabels(path):
  with open(path, 'r') as fi:
    labels = json.load(fi)
    fi.close()
  return convert(labels)