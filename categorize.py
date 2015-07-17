import parseData
import analysis

path = r"C:\Users\Yijun\Desktop\Amazon\reviews_reviewClothing,_Shoes_&_Jewelry.txt"
pathProduct = r"C:\Users\Yijun\Desktop\Amazon\metadata.json"
outfile = r"C:\Users\Yijun\Desktop\Amazon\movies.txt"

parseData.parseAndWrite(pathProduct, outfile, 'movies')
movies = parseData.parse(outfile)

# unpack the dictionary
for i in movies:
  d = [j for j in i]