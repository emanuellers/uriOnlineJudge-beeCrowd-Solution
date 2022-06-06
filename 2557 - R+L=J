def isNumber(value):
    try:
        int(value)
    except ValueError:
        return False
    return True

while True:
    try:
      schema = str(input())
      values = []
      values.append(schema[0:schema.find("+")])
      values.append(schema[schema.find("+")+1:schema.find("=")])
      values.append(schema[schema.find("=")+1::])
      sum =  isNumber(values[0]) and isNumber(values[1]) 
      if sum:
        print(int(values[0]) + int(values[1]))
      elif isNumber(values[0]) and isNumber(values[2]):
        print(int(values[2]) - int(values[0]))
      else:
        print(int(values[2]) - int(values[1]))
    except EOFError:
        break
