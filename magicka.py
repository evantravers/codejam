input = open("magicka.txt")
first = True
def performMagick(line, num):
  array = line.split()
  # num of combinations
  C = int(array[0])
  combinations = array[1:C+1]
  # of diametrically opposed combinations
  D = int(array[C+1])
  diametric = array[C+2:C+D+2]
  # length of the spell
  N = int(array[C+D+2])
  # spell string
  spell = array[C+D+3]
  
  # input done, lets mix some magicka
  result = []
  for char in spell:
    # print(result)
    valid = True
    if result:
      # check to see matches in combinations
      tmpComb1 = "%s%s" % (char, result[-1])
      tmpComb2 = "%s%s" % (result[-1], char)
      if valid:
        for each in combinations:
          if each[0:2] == tmpComb1 or each[0:2] == tmpComb2:
            result = result[0:-1]
            result.append(each[-1])
            valid = False
          break
      if valid:
        for each in diametric:
          if char == each[0:1]:
            if each[1:2] in result:
              valid = False
              result = []
              break
          if char == each[1:2]:
            if each[0:1] in result:
              valid = False
              result = []
              break
    if valid:
      result.append(char)


  endprint = ("Case #%i: %s" % (num, result))
  endprint = endprint.replace("'", "")
  print(endprint)

num = 0
for line in input:
  if not first:
    performMagick(line, num)
  else:
    first = False
  num+=1

