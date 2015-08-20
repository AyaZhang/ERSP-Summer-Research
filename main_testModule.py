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

sample_shoes = dict()
for i in shoes:
  if i['asin'] in labels.keys():
    sample_shoes[i['asin']] = i

sample_reviews = list()
for i in reviews:
  if i['asin'] in labels.keys():
    sample_reviews.append(i)

def feature(key):
  feat = [1]
  feat.append(sample_shoes[key]['price'])  # price feature
  count = 0
  for i in sample_reviews:
    if i['asin'] == key:
      count += 1
  feat.append(count) # popularity feature
  return feat

d1 = dict(sample_shoes.items()[len(sample_shoes)/2:]) # training set
d2 = dict(sample_shoes.items()[:len(sample_shoes)/2]) # test set

y = [labels[key] for key in d1]
X = [feature(key) for key in d1]

theta,residuals,rank,s = numpy.linalg.lstsq(X, y)

### Compute MSE on the training set
Xi = [feature(key) for key in d2]

def mse(x, y, theta):
  total = 0
  for i in range(0,len(x)):
    prediction = sum(x[i][j] * theta[j] for j in range(0, len(theta)))
    total += (y[i] - prediction) ** 2
  return total/len(x)

mse(Xi, y, theta)

##### plot graph
X = numpy.array(x[1] for x in X)
y = numpy.array(y)

import matplotlib.pyplot as plt
plt.plot(X, y, 'o', label='Original data', markersize=10)
plt.plot(X, theta[0]+theta[1]*X[1], 'r', label='Fitted line')
plt.legend()
plt.show()