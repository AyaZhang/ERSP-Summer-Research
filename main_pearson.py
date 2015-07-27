import parseData
import analysis

outfile2 = r"C:\Users\Yijun\Desktop\Amazon\reviews_shoes.txt"
outfile3 = r"C:\Users\Yijun\Desktop\Amazon\meta_shoes_hasReview.txt"

shoes = parseData.parse(outfile3)
reviews = parseData.parse(outfile2)

hasPrice = list()
for i in shoes:
  if i.has_key('price'):
    hasPrice.append(i)

len(hasPrice)		# 40955

# find number of reviews of each product
ids = set(['B0019ZDDJU','B00B70IE32','B0081CP3RO','B003FKAY44','B00ARBSDVA','B007W4SNJW','B004V2C0JM','B00JYPX0UY','B004SFRVNW','B0058YGM6Y','B007PKCWSQ','B00C0IUNDY','B0012YFAB2','B00GCUB56K','B003WQQ6DY','B009THS4XU','B004TJ1RRI','B004GX44S6','B0028N7EA6','B002A1H7K8','B00BPYZQ8Q','B001TK2GKW','B00263JLYK','B0057TAB5I','B00JBPQJ5U','B005LTUD98','B004WNYE80','B004T7QZBI','B000WMWFSQ','B00B06FXAK','B001W6RA72','B00498CYPS','B000YR0Q9Y','B00E1ZY9NO','B009KBJDL2','B00F0IE9JK','B00EQAC95E','B0035WTV0U','B00CIP01TK','B007G72PT4','B00HT8AWBS','B00DSVD3O8','B00H3N8CNO','B001TOE19C','B001D1QOBY','B009RZSYX4','B0065SLIT8','B00GJJY1RO','B00D50CP9Q'])
count = dict()

for i in reviews:
  index = i['asin']
  if index in ids:
    if index in count:
      count[index] = count[index] + 1
    else:
      count[index] = 1
