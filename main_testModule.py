import numpy
import scipy.optimize

import parseData
import analysis

pathProducts = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_unique+fifteen_review+price.txt"
pathReviews = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes_unique+fifteen_review+price.txt"
pathLabels = r"C:\Users\Yijun\Desktop\Amazon\labels.txt"

shoes = parseData.parse(pathProducts)
reviews = parseData.parse(pathReviews)
labels = parseData.loadLabels(pathLabels)

sample_shoes = list()
for i in shoes:
  if i['asin'] in labels.keys():
    sample_shoes.append(i)

sample_reviews = list()
for i in reviews:
  if i['asin'] in labels.keys():
    sample_reviews.append(i)

def fearure(datum):
  feat = [0] * len()

y = [labels[r['asin']] for r in sample_reviews]


#########
bgs = [x[1] for x in bigramWordCount[:1000]]
bgsId = dict(zip(bgs, range(len(bgs))))
bgsSet = set(bgs)

def feature(datum):
  feat = [0] * len(bgs)
  r = ''.join([c for c in datum['review/text'].lower() if not c in punctuation])
  r = r.replace('\t', ' ')
  words = r.split()
  for i in range(len(words)-1):
    bg = words[i] + " " + words[i+1]
    if bg in bgs:
      feat[bgsId[bg]] += 1
  feat.append(1) #offset
  return feat

X = [feature(d) for d in data]
y = [d['review/overall'] for d in data]

theta,residuals,rank,s = numpy.linalg.lstsq(X, y)
residuals