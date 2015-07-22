import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\meta_Clothing,_Shoes_&_Jewelry.txt"
outfile = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_unique.txt"
outfile2 = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes.txt"

# separate shoes data
parseData.parseAndWrite(pathProduct, outfile, "Shoes")
shoes = parseData.parse(outfile)

# record shoes product IDs
productIDs = set()
for item in shoes:
  if item.has_key('asin'):
    productIDs.add(item['asin'])

# extract shoe reviews
parseAndWrite_reviews(path, outfile2, productIDs)