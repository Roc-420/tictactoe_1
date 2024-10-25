# win function here


def win_check(array):
  if (array[0][0] == 1 and array[1][0] == 1 and array[2][0] == 1) or (array[0][1] == 1 and array[1][1] == 1 and array[2][1] == 1) or (array[0][2] == 1 and array[1][2] == 1 and array[2][2] == 1):
    print("P1 Wins")
    return True
  
  elif (array[0][0] == 1 and array[0][1] == 1 and array[0][2] == 1) or (array[1][0] == 1 and array[1][1] == 1 and array[1][2] == 1) or (array[2][0] == 1 and array[2][1] == 1 and array[2][2] == 1):
    print("P1 Wins")
    return True
  
  elif (array[0][0] == 1 and array[1][1] == 1 and array[2][2] == 1) or (array[0][2] == 1 and array[1][1] == 1 and array[2][0] == 1):
    print("P1 Wins")
    return True
  
  else: 
    return False

# theres 8 winning combinations 

 # vertical : TGAME[0][0] TGAME[1][0] TGAME[2][0]
 # TGAME[0][1] TGAME[1][1] TGAME[2][1]
 # TGAME[0][2] TGAME[1][2] TGAME[2][2]

 #test V1 = pass
 #V2 = pass
 #v3 = pass
 #H1# all zontal test pased
 #2H= pass#D1 = pass#D2 = pass




def place_emoji(array,emoji_array,symbol):
  row_counter = 0
  for row in array:
    item_counter = 0
    for item in row:
      if item == 1 :
        emoji_array[row_counter][item_counter] = symbol
      item_counter +=1
    row_counter+=1



  print(emoji_array)

