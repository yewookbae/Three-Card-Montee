#Jan 23,2023
#Three Card Monte
import random
import check_input
print("-THREE CARD MONTE-")
print("Find the queen to double your bet!")
def main():
  bal = 100
  print("\n")
  while bal > 0:
    print("You have $",bal)
    bet = int(check_input.get_int_range("How much you wanna bet? ",1, min(int(bal),50)))
    bal -= bet
    print("+-----+  +-----+  +-----+\n|     |  |     |  |     |\n|  1  |  |  2  |  |  3  |\n|     |  |     |  |     |\n+-----+  +-----+  +-----+")
    guess = int(check_input.get_int_range("Find the queen: ",1,3))
  #face up cards randomization
    queen = random.randint(1,3)
    card1 = card2 = card3 = "K"
    if queen==1:
      card1 = "Q"
    elif queen == 2:
      card2 = "Q"
    else:
      card3 = "Q"
    print("+-----+  +-----+  +-----+\n|     |  |     |  |     |\n| ",card1," |  | ",card2," |  | ",card3," |\n|     |  |     |  |     |\n+-----+  +-----+  +-----+")
    if guess == queen:
      print("You got lucky this time....")
      bal = bet + bet + bal
    else:
      print("Sorry.....You Lose.")
  
    if bal > 0:
      play = check_input.get_yes_no("Play Again? (Y/N): ")
      print()
    else:
      print("You're out of money.  Beat it loser! ")
      
    
      
    
main()
