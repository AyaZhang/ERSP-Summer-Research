import os

import parseData
import analysis

pathProducts = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_unique.txt"
pathReviews = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes.txt"

products = parseData.parse(pathProducts)
reviews = parseData.parse(pathReviews)

reviewList = parseData.tokenize(reviews)
commonWords = analysis.commonWords(reviewList,8)
theta = analysis.sentimentAnalysis(commonWords,reviewList,reviews)