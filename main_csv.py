import csv

path = r"C:\Users\Yijun\Desktop\Amazon\Batch_2048158_batch_results.csv"

with open(path, 'rb') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    print ', '.join(row)


