import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_Clothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\meta_Clothing,_Shoes_&_Jewelry.txt"
outfile = r"C:\Users\Yijun\Desktop\Amazon\shoes.txt"

# separate shoes data
parseData.parseAndWrite(pathProduct, outfile, "Shoes")
shoes = parseData.parse(outfile)

# record shoes' product IDs
productIDs = set()
for item in shoes:
  if item.has_key('asin'):
    productIDs.add(item['asin'])

########################################################
################ UNDER CONSTRUCTION ####################
########################################################
# extract all the shoe reviews
idFile = r"C:\Users\Yijun\Desktop\Amazon\idFile.txt"
with open(idFile,'w') as outfile:
  json.dump(productIDs, outfile)
  outfile.close()

ids = parseData.parse(idFile)
asins = [c for c in ids[0]]

reviews = parseData.parse(path)