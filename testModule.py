import os

import parseData

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\metadata.json"

reviews = parseData.parse(path, 10)
products = parseData.parse(pathProduct,10)

reviewList = textProcess.tokenize(reviews)