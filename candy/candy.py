input = open("data.txt")
first = True

def badadd(num1, num2):
  print(num1, num2)
  result = ""
  if len(num1) > len(num2):
    cnt = 0
    for each in reversed(num1):
      if cnt < len(num2):
        print(each, num2[cnt])
        if (each == "1") ^ (num2[cnt] == "1"):
          result += "1"
        else:
          result += "0"
      else:
        print(each)
        result += each
      cnt+=1
  else:
    cnt = 0
    for each in reversed(num2):
      if cnt < len(num2):
        if each == "1" or num1[cnt] == "1":
          result += "1"
        else:
          result += "0"
        cnt+=1
      else:
        result += each
  return result


def candycount(list):
  # looking for an unbalanced split where Patrick won't cry
  # so start by giving Sean the largest possible value, computing
  # the binary add, and remove items until either the binary values 
  # are equal or Sean can't win
  Sean = 0
  Patrick = 0
  PatsMind = []
  actualItems = []
  for value in list:
    PatsMind.append(str(bin(int(value)))[2:])
    actualItems.append(int(value))
    Sean += value

# for line in input:
#   if not first:
#     array = line.split()
#     if len(array) > 1:
#       candycount(array)
#   else:
#     first = False

print(badadd("1100","101"))
