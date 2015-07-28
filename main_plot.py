import parseData
import analysis

import numpy
import matplotlib.pyplot
from scipy.stats import gaussian_kde

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
  if count == 1 or count == 0 or max_time == min_time:
    y.append(0)
  else:
    y.append(2629743 * count/(max_time - min_time))

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
################# UNDER CONSTRUCTION ##################
#######################################################

flats = list()
for i in shoes:
  if i.has_key('price'):
    for k in i['categories']:
      for key in k:
        if key == "Flats":
          flats.append(i)

len(flats)

manyReviews = list()
for i in flats:
  count = 0
  for r in reviews:
    if r['asin'] == i['asin']:
      count += 1
  if count > 30:
    manyReviews.append(i)

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
  if count == 1 or count == 0 or max_time == min_time:
    y.append(0)
  else:
    y.append(2629743 * count/(max_time - min_time))

matplotlib.pyplot.scatter(x,y)
matplotlib.pyplot.show()

# density plot, calculate point density
xy = numpy.vstack([x,y])
z = gaussian_kde(xy)(xy)

fig, ax = matplotlib.pyplot.subplots()
ax.scatter(x, y, c=z, edgecolor='')
matplotlib.pyplot.show()