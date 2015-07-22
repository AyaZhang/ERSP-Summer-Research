import random

import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
outfile = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_unique.txt"

# parse shoes data
shoes = parseData.parse(outfile)

len(shoes) # 366654

# randomly choose 100 data
sample = list()
sample = random.sample(shoes, 100)

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