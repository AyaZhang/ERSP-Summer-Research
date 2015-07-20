import os

import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\meta_Clothing,_Shoes_&_Jewelry.txt"


reviews = parseData.parse(path, 10)
products = parseData.parse(pathProduct,10)

reviewList = parseData.tokenize(reviews)
commonWords = analysis.commonWords(reviewList,8)
theta = analysis.sentimentAnalysis(commonWords,reviewList,reviews)

cat = set()
for i in products:
  if i.has_key('categories'):
    for j in i['categories']:
      for k in j:
        if k == "Shoes":
          cat.add(i['asin'])