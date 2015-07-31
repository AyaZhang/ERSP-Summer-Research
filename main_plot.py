import parseData
import analysis

import numpy
import matplotlib.pyplot
from scipy.stats import gaussian_kde

import operator

outfile2 = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes.txt"
outfile3 = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_hasReview.txt"

shoes = parseData.parse(outfile3)
reviews = parseData.parse(outfile2)

# find out flats that has price
flats = list()
for i in shoes:
  if i.has_key('price'):
    for k in i['categories']:
      for key in k:
        if key == "Flats":
          flats.append(i)

len(flats)		# 2770

# prepare x and y; x is price, y is number of reviews
x = list()
y = list()
for i in flats:
  x.append(i['price'])
  count = 0
  max_time = 0
  min_time = 9999999999
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
      max_time = r['unixReviewTime'] if r['unixReviewTime'] > max_time else max_time
      min_time = r['unixReviewTime'] if r['unixReviewTime'] < min_time else min_time
  time = (max_time - min_time)/15778458.0    # half year
  if time == 0 or count == 0:
    y.append(0)
  else:
    y.append(count/time)

###################################################

avgPrice = sum(x)/len(x)
x = [(i - avgPrice) for i in x]
avgReview = sum(y)/len(y)
y = [(i - avgReview) for i in y]

rank = dict()
for i in range(0, len(x)):
  asin = flats[i]['asin']
  rank[asin] = x[i]*y[i]

sorted_rank = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

####################################################d

# plot the graph
matplotlib.pyplot.scatter(x,y)
matplotlib.pyplot.show()

# density plot, calculate point density
xy = numpy.vstack([x,y])
z = gaussian_kde(xy)(xy)

fig, ax = matplotlib.pyplot.subplots()
ax.scatter(x, y, c=z, edgecolor='')
matplotlib.pyplot.show()

#######################################################
####################### TRIAL 1 #######################
#######################################################

manyReviews = list()
for i in flats:
  count = 0
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
  if count > 20:
    manyReviews.append(i)

len(manyReviews)    # 89

x = list()
y = list()
for i in manyReviews:
  x.append(i['price'])
  count = 0
  max_time = 0
  min_time = 9999999999
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
      max_time = r['unixReviewTime'] if r['unixReviewTime'] > max_time else max_time
      min_time = r['unixReviewTime'] if r['unixReviewTime'] < min_time else min_time
  time = (max_time - min_time)/15778458.0    # half year
  print time
  if time != 0:
    y.append(count/time)
  else:
    y.append(count)

avgPrice = sum(x)/len(x)
x = [(i/avgPrice) for i in x]
avgReview = sum(y)/len(y)
y = [(i/avgReview) for i in y]

rank = dict()
for i in range(0, len(x)):
  asin = manyReviews[i]['asin']
  rank[asin] = x[i]*y[i]

sorted_rank = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)


#######################################################
####################### TRIAL 2 #######################
#######################################################

longTime = list()
for i in flats:
  count = 0
  max_time = 0
  min_time = 9999999999
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
      max_time = r['unixReviewTime'] if r['unixReviewTime'] > max_time else max_time
      min_time = r['unixReviewTime'] if r['unixReviewTime'] < min_time else min_time
  if count != 0 and (max_time - min_time >= 31556926):
    longTime.append(i)

len(longTime)    # 498

x = list()
y = list()
for i in longTime:
  x.append(i['price'])
  count = 0
  max_time = 0
  min_time = 9999999999
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
  y.append(count)

avgPrice = sum(x)/len(x)
x = [(i/avgPrice) for i in x]
avgReview = sum(y)/float(len(y))
y = [(i/avgReview) for i in y]

rank = dict()
for i in range(0, len(x)):
  asin = longTime[i]['asin']
  rank[asin] = x[i]*y[i]

sorted_rank = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
