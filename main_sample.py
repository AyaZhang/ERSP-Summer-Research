import random

import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
outfile = r"C:\Users\Yijun\Desktop\Amazon\shoes.txt"

# parse shoes data
shoes = parseData.parse(outfile)

# record shoes' product IDs
products = list()
productIDs = set()
for item in shoes:
  if item['asin'] not in productIDs:
    products.append(item)
    productIDs.add(item['asin'])

len(products) # 366654

# randomly choose 100 data
sample = list()
sample = random.sample(products, 100)

for i in range(0,100):
  print sample[i]['asin']

for i in range(0,100):
  print sample[i]['title']

for i in range(0,100):
  print sample[i]['imUrl']

for i in range(0,100):
  if sample[i].has_key('price'):
    print sample[i]['price']
  else:
    print

sample