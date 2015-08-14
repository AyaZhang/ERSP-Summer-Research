import csv

path = r"C:\Users\Yijun\Desktop\Amazon\Batch_2048158_batch_results.csv"

# convert csv file into a list of lists
result = list()
with open(path, 'rb') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    hit = list()
    for i in row:
      if i.isdigit():
        i = int(i)
      hit.append(i)
    result.append(hit)

labels = dict()
index = 1
while index < 26:
  for i in range(0, 10):
    # check if product exists
    asin = result[index][i]
    if asin == '':
      continue
    array = [0 for k in range(0,6)]
    for j in range(0, 5):
      rating = result[index+j][10+i]
      array[rating] = array[rating] + 1
    # if >= 3 people agree on one label, use it
    for k in range(0,6):
      if array[k] >= 3:
        labels[asin] = k
        break
    # if >= 4 people are on the same side of the scale,
    # use their average
    if asin not in labels:
      lower_count = array[1] + array[2] + array[3]
      higher_count = array[3] + array[4] + array[5]
      if lower_count >= 4:
        lower_sum = array[1] + 2 * array[2] + 3 * array[3]
        labels[asin] = 1.0 * lower_sum / lower_count
      elif higher_count >= 4:
        higher_sum = 3 * array[3] + 4 * array[4] + 5 * array[5]
        labels[asin] = 1.0 * higher_sum / higher_count
      else:
        labels[asin] = 0
  index += 5