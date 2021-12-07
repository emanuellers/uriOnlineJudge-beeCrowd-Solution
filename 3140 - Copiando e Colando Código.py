arrayStrings = []
number = 0
begin = 0
end = 0
while True:
  try:
    tag = input()
    number += 1
    if tag.find("<body>") != -1:
      begin = number
    if tag.find("</body>") != -1:
      end = number
    arrayStrings.append(tag)
  except EOFError:
    break

for i in range(begin, end-1):
  print(arrayStrings[i])
