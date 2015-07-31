import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\meta_Clothing,_Shoes_&_Jewelry.txt"
outfile = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_unique.txt"
outfile2 = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes.txt"
outfile3 = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_hasReview.txt"

# separate shoes data
parseData.parseAndWrite(pathProduct, outfile, "Shoes")
shoes = parseData.parse(outfile)

# extract shoe reviews
productIDs = set()
for item in shoes:
  if item.has_key('asin'):
    productIDs.add(item['asin'])

parseData.parseAndWrite_constraint(path, outfile2, productIDs)

# extract shoe product data that has review
reviews = parseData.parse(outfile2)

len(reviews)	# 1521651

unique = set()
for i in reviews:
  unique.add(i['asin'])

del reviews 	# free memory

parseData.parseAndWrite_constraint(outfile, outfile3, unique)
shoes_hasReview = parseData.parse(outfile3)

len(shoes_hasReview)	# 210076

# shoe product data only if it has price attribute
hasPrice = list()
for i in shoes_hasReview:
  if i.has_key('price'):
    hasPrice.append(i)

len(hasPrice)		# 40955