input = open("bots.txt")
first = True

def sciencetobedone(seq):
  # we are going to use a greedy algorithm. Closest match wins
  # reset the bot's positions
  time   = 0
  Blue   = 1
  Orange = 1
  Bhold  = False
  Ohold  = False
  # print position
  
  # while we have goals left... 
  # we should move to the proper positions. 
  # as things are moved off the sequence we should eventually win
  while seq:
    # each bot needs to have a target position for the start
    # it's possible they'll both need to run forward
    if Bhold or Ohold:
      seq = seq[1:]
      Bhold = False
      Ohold = False

    # identify whose turn it is
    currentturn = seq[0][0]
    currentgoal = seq[0][1]

    # decide Orange's move
    if Bhold or time == 0:
      if currentturn == "O":
        if currentgoal == Orange:
          # pushing the button
          Ohold = True
        elif currentgoal > Orange:
          Orange += 1
        else:
          Orange -= 1

    # decide Blue's move
    if Ohold or time == 0:
      if currentturn == "B":
        if currentgoal == Blue:
          # pushing the button
          Bhold = True
        elif currentgoal > Blue:
          Blue += 1
        else:
          Blue -= 1

    time +=1
  return time

num = 0
for line in input:
  sequence = []
  if not first:
    array = line.split()
    x = 1 
    while x+1 < len(array):
      sequence.append([array[x], int(array[x+1])])
      x+=2
    print("Case #%i: %i" % (num, sciencetobedone(sequence)))
  else:
    first = False
  num += 1
