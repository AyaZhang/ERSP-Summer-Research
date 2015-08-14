import csv
import parseData

path = r"C:\Users\Yijun\Desktop\Amazon\Batch_2048158_batch_results.csv"
outfile = r"C:\Users\Yijun\Desktop\Amazon\labels.txt"


# convert csv file into a list of lists
result = list()
with open(path, 'rb') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    hit = list()
    for i in row:
      # read numbers as numbers
      if i.isdigit(): i = int(i)
      hit.append(i)
    result.append(hit)


# build a dictionary of asin and labels
labels = dict()
index = 1

while index < 26:
  for i in range(0, 10):\

    # check if product exists
    asin = result[index][i]
    if asin == '':
      continue\

    array = [0 for k in range(0,6)]
    for j in range(0, 5):
      rating = result[index+j][10+i]
      array[rating] = array[rating] + 1\

    # if >= 3 people agree on one label, use it
    for k in range(0,6):
      if array[k] >= 3:
        labels[asin] = k * 1.0
        break\

    # if >= 4 people are on the same side of the scale,
    # use their average
    if asin not in labels:
      lower_count = sum(array[k] for k in range(1,4))
      higher_count = sum(array[k] for k in range(3,6))\

      # lower side of the scale
      if lower_count >= 4:
        lower_sum = sum(k * array[k] for k in range(1,4))
        labels[asin] = 1.0 * lower_sum / lower_count\

      # higher side of the scale
      elif higher_count >= 4:
        higher_sum = sum(k * array[k] for k in range(3, 6))
        labels[asin] = 1.0 * higher_sum / higher_count\

      # controversial, set to 0
      else:
        labels[asin] = 0\

  index += 5

with open(outfile, 'w') as fp:
  json.dump(labels, fp)
  fp.close()