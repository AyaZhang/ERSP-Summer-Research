import json

# Get rid of the annoying u' (unicode strings)
def byteify(input):
  if isinstance(input, dict):
    return {byteify(key):byteify(value) for key,value in input.iteritems()}
  elif isinstance(input, list):
    return [byteify(element) for element in input]
  elif isinstance(input, unicode):
    return input.encode('utf-8')
  else:
    return input

# Parse first n number of reviews from the system path
def parse(path, n):
  data = []
  count = 0
  with open(path) as f:
    for line in f:
      data.append(byteify(json.loads(line)))
      count += 1
      if count == n:
        break
  return data