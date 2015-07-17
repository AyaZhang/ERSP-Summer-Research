import numpy
from collections import defaultdict

# find n most common words in reviewList
# input type: [['word','word'],['word']]
# return type: ['word','word']
def commonWords(reviewList, n):
  wordCount = defaultdict(int)
  for r in reviewList:
    for w in r:
      wordCount[w] += 1
  counts = [(wordCount[w],w) for w in wordCount]
  counts.sort()
  counts.reverse()
  return [x[1] for x in counts[:n]]

# perform sentiment analysis on the most common words
# input type: ['word','word']
# TODO ##############################################
# We can parse reviews with their rating of status/utility
# to avoid passing both reviewList and reviews here
#
# HAVEN'T TESTED YET. DO NOT TRUST.
#####################################################
def sentimentAnalysis(words, reviewList, reviews):
  wordID = dict(zip(words, range(len(words))))
  wordSet = set(words)

  def feature(datum):
    feat = [0]*len(words)
    for w in datum:
      if w in words:
        feat[wordID[w]] += 1
    feat.append(1)	#offset
    return feat

  X = [feature(r) for r in reviewList]
  y = [d['overall'] for d in reviews]
  theta, residuals, rank, s = numpy.linalg.lstsq(X, y)
  return theta[:len(theta)-1]

