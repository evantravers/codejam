input = open("bots.txt")
first = True

def sciencetobedone(seq):
  # we are going to use a greedy algorithm. Closest match wins
  # reset the bot's positions
  Orange        = 1
  OrangeHolding = False
  Otarget       = 0
  Blue          = 1
  BlueHolding   = False
  Btarget       = 0
  turn          = None
  time          = 1
  first         = True
  # print position
  
  # while we have goals left... 
  # we should move to the proper positions. 
  # as things are moved off the sequence we should eventually win
  while seq:
    # print("========%i========="%(time))
    # print("Orange(%i): %i, Blue(%i) %i, Time: %i" % (Orange, Otarget, Blue, Btarget, time))
    # each bot needs to have a target position for the start
    # it's possible they'll both need to run forward

    # identify whose turn it is
    turn = seq[0][0]
    
    # identify the next goal for Blue
    for remaining in seq:
      if remaining[0] == "B":
        Btarget = remaining[1]
        break

    if OrangeHolding or first or turn == "B":
      if Btarget == Blue:
        # print("Blue staying at", Blue)
        first = False
        BlueHolding = True
        if turn == "B" and BlueHolding:
          # print("Blue pushing button here")
          seq = seq[1:]
      else:
        if Btarget > Blue:
          Blue +=1
        else:
          Blue -=1
        # print("Blue move to", Blue)

    # identify the next goal for Orange
    for remaining in seq:
      if remaining[0] == "O":
        Otarget = remaining[1]
        break

    if BlueHolding or first or turn == "O":
      if Otarget == Orange:
        # print("Orange staying at", Orange)
        first = False
        OrangeHolding = True
        if turn == "O" and OrangeHolding:
          # print("Orange pushing button here")
          seq = seq[1:]
      else:
        if Otarget > Orange:
          Orange +=1
        else:
          Orange -=1
        # print("Orange move to", Orange)
    
    # print("========%i========="%(time))
    time +=1
  return time-1

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
