# COMPUTER PROJECT CLASS XI (2022-2023)
# Made by Amartya Bagchi, Aryan Daga and Aman Sinha of Class XI-G, DPSRKP.
# Finished on 26 December 2022.

# Importing Modules
import random
from IPython.display import Image, display

# Defining Objects -------------------------------------------------------------
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " "
avpos = [1,2,3,4,5,6,7,8,9]
af = False
nb = False
bm = False
moved = False
end = False

# Custom Functions -------------------------------------------------------------
def grid(): # Custom Function to print the grid after each turn.
  print("\033[34m")
  print(a1, "|", a2 ,"|", a3)
  print("——————————")
  print(b1, "|", b2 ,"|", b3)
  print("——————————")
  print(c1, "|", c2 ,"|", c3)
  print("\033[0m")
# ----------------

def enter_pos(mark,pos): # Custom Function to enter a position and parse it.
  global a1,a2,a3,b1,b2,b3,c1,c2,c3,avpos
  if pos == 1:
    a1 = mark
    avpos.remove(1)
    grid()
  if pos == 2:
    a2 = mark
    avpos.remove(2)
    grid()
  if pos == 3:
    a3 = mark
    avpos.remove(3)
    grid()
  if pos == 4:
    b1 = mark
    avpos.remove(4)
    grid()
  if pos == 5:
    b2 = mark
    avpos.remove(5)
    grid()
  if pos == 6:
    b3 = mark
    avpos.remove(6)
    grid()
  if pos == 7:
    c1 = mark
    avpos.remove(7)
    grid()
  if pos == 8:
    c2 = mark
    avpos.remove(8)
    grid()
  if pos == 9:
    c3 = mark
    avpos.remove(9)
    grid()
#----------------

def check_win(): # Custom Function to check if a player/engine won.
  global end
  end = False
  print("")
  # Horizontal Win (X)
  if a1 == a2 == a3 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  if b1 == b2 ==  b3 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  if c1 == c2 == c3 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  # Vertical Win (X)
  if a1 == b1 == c1 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  if a2 == b2 == c2 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  if a3 == b3 == c3 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  # Diagonal Win (X)
  if a1 == b2 == c3 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  if a3 == b2 == c1 == "X":
    print("\033[32mRESULT:",p1,"won the game!\033[0m")
    end = True
  # ---------------------------------------
  # Horizontal Win (O)
  if a1 == a2 == a3 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if b1 == b2 ==  b3 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if c1 == c2 == c3 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  # Vertical Win (O)
  if a1 == b1 == c1 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if a2 == b2 == c2 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if a3 == b3 == c3 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  # Diagonal Win (O)
  if a1 == b2 == c3 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if a3 == b2 == c1 == "O":
    print("\033[32mRESULT:",p2,"won the game!\033[0m")
    end = True
  if end == True:
    return "break"
#----------------

def block_win(): # Custom Function for the Engine to block any potential wins.
  global a1,a2,a3,b1,b2,b3,c1,c2,c3,nb
  if (a3  == a2 == "X") or (b1 == c1 == "X") or (b2 == c3 == "X"):
    if a1 != "O":
      a1 = "O"
      avpos.remove(1)
      print("Computer chose Position 1!")
      grid()
      nb = True
      return nb
  if (a1 == a3 == "X") or (b2 == c2 == "X"):
    if a2 != "O":
      a2 = "O"
      avpos.remove(2)
      print("Computer chose Position 2!")
      grid()
      nb = True
      return nb
  if (a1 == a2 == "X") or (b2 == c1 == "X") or (b3 == c3 == "X"):
    if a3 != "O":
      a3 = "O"
      avpos.remove(3)
      print("Computer chose Position 3!")
      grid()
      nb = True
      return nb
  if (a1 == c1 == "X") or (b2 == b3 == "X"):
    if b1 != "O":
      b1 = "O"
      avpos.remove(4)
      print("Computer chose Position 4!")
      grid()
      nb = True
      return nb
  if (a1 == c3 == "X") or (a2 == c2 == "X")  or (a3 == c1 == "X")  or (b3 == b1 == "X"):
    if b2 != "O":
      b2 = "O"
      avpos.remove(5)
      print("Computer chose Position 5!")
      grid()
      nb = True
      return nb
  if (a3 == c3 == "X") or (b1 == b2 == "X"):
    if b3 != "O":
      b3 = "O"
      avpos.remove(6)
      print("Computer chose Position 6!")
      grid()
      nb = True
      return nb
  if (a1 == b1 == "X") or (c2 == c3 == "X") or (a3 == b2 == "X"):
    if c1 != "O":
      c1 = "O"
      avpos.remove(7)
      print("Computer chose Position 7!")
      grid()
      nb = True
      return nb
  if (a2 == b2 == "X") or (c1 == c3 == "X"):
    if c2 != "O":
      c2 = "O"
      avpos.remove(8)
      print("Computer chose Position 8!")
      grid()
      nb = True
      return nb
  if (a3 == b3 == "X") or (a1 == b2 == "X") or (c1 == c2 == "X"):
    if c3 != "O":
      c3 = "O"
      avpos.remove(9)
      print("Computer chose Position 9!")
      grid()
      nb = True
      return nb
  nb = False
  return nb
#-------------

def win_move(): # Custom Function for the Engine to make a winning move.
  global a1,a2,a3,b1,b2,b3,c1,c2,c3,moved
  if (a3 == a2 == "O") or (b1 == c1 == "O") or (b2 == c3 == "O"):
    if a1 != "O" and a1 != "X":
      a1 = "O"
      avpos.remove(1)
      print("Computer chose Position 1!")
      grid()
      moved = True
      return moved
  if (a1 == a3 == "O") or (b2 == c2 == "O"):
    if a2 != "O" and a2 != "X":
      a2 = "O"
      avpos.remove(2)
      print("Computer chose Position 2!")
      grid()
      moved = True
      return moved
  if (a1 == a2 == "O") or (b2 == c1 == "O") or (b3 == c3 == "O"):
    if a3 != "O" and a3 != "X":
      a3 = "O"
      avpos.remove(3)
      print("Computer chose Position 3!")
      grid()
      moved = True
      return moved
  if (a1 == c1 == "O") or (b2 == b3 == "O"):
    if b1 != "O" and b1 != "X":
      b1 = "O"
      avpos.remove(4)
      print("Computer chose Position 4!")
      grid()
      moved = True
      return moved
  if (a1 == c3 == "O") or (a2 == c2 == "O")  or (a3 == c1 == "O")  or (b3 == b1 == "O"):
    if b2 != "O" and b2 != "X":
      b2 = "O"
      avpos.remove(5)
      print("Computer chose Position 5!")
      grid()
      moved = True
      return moved
  if (a3 == c3 == "O") or (b1 == b2 == "O"):
    if b3 != "O" and b3 != "X":
      b3 = "O"
      avpos.remove(6)
      print("Computer chose Position 6!")
      grid()
      moved = True
      return moved
  if (a1 == b1 == "O") or (c2 == b3 == "O") or (a3 == b2 == "O"):
    if c1 != "O" and c1 != "X":
      c1 = "O"
      avpos.remove(7)
      print("Computer chose Position 7!")
      grid()
      moved = True
      return moved
  if (a2 == b2 == "O") or (c1 == c3 == "O"):
    if c2 != "O" and c2 != "X":
      c2 = "O"
      avpos.remove(8)
      print("Computer chose Position 8!")
      grid()
      moved = True
      return moved
  if (a3 == b3 == "O") or (a1 == b2 == "O") or (c1 == c2 == "O"):
    if c3 != "O" and c3 != "X":
      c3 = "O"
      avpos.remove(9)
      print("Computer chose Position 9!")
      grid()
      moved = True
      return moved
  moved = False
  return moved
#----------------

def best_move(): # Custom Function for making a random move.
  global a1,a2,a3,b1,b2,b3,c1,c2,c3,bm
  if nb == moved == False:
    ranpos = random.choice(avpos)
    if ranpos == 1:
        a1 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 2:
        a2 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 3:
        a3 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 4:
        b1 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 5:
        b2 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 6:
        b3 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 7:
        c1 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 8:
        c2 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
    if ranpos == 9:
        c3 = "O"
        avpos.remove(ranpos)
        print(f"Computer chose Position {ranpos}!")
        grid()
        bm = True
        return bm
  bm = False
  return bm
#----------------

def anti_fork(): # Custom function for countering forks.
  global a1,a2,a3,b1,b2,b3,c1,c2,c3,af
  if b2 == "O":
    # X-O-X series (diagonal, rotated)
    if a3 == c1 == "X" and b2 == "O":
      r = [2,4,6,8]
      rc = random.choice(r)
      if rc == 2:
        if a2 != "O" and a2 != "X":
          a2 = "O"
          avpos.remove(2)
          print("Computer chose Position 2!")
          grid()
          af = True
          return af
      if rc == 4:
        if b1 != "O" and b1 != "X":
          b1 = "O"
          avpos.remove(4)
          print("Computer chose Position 4!")
          grid()
          af = True
          return af
      if rc == 6:
        if b3 != "O" and b3 != "X":
          b3 = "O"
          avpos.remove(6)
          print("Computer chose Position 6!")
          grid()
          af = True
          return af
      if rc == 8:
        if c2 != "O" and c2 != "X":
          c2 = "O"
          avpos.remove(8)
          print("Computer chose Position 8!")
          grid()
          af = True
          return af
    if a1 == c3 == "X" and b2 == "O":
      r = [2,4,6,8]
      rc = random.choice(r)
      if rc == 2:
        if a2 != "O" and a2 != "X":
          a2 = "O"
          avpos.remove(2)
          print("Computer chose Position 2!")
          grid()
          af = True
          return af
      if rc == 4:
        if b1 != "O" and b1 != "X":
          b1 = "O"
          avpos.remove(4)
          print("Computer chose Position 4!")
          grid()
          af = True
          return af
      if rc == 6:
        if b3 != "O" and b3 != "X":
          b3 = "O"
          avpos.remove(6)
          print("Computer chose Position 6!")
          grid()
          af = True
          return af
      if rc == 8:
        if c2 != "O" and c2 != "X":
          c2 = "O"
          avpos.remove(8)
          print("Computer chose Position 8!")
          grid()
          af = True
          return af
    # X-O-X series (L-structure, rotated)
    if a2 == b1 == "X" and b2 == "O":
      if a1 != "O" and a1 != "X":
        a1 = "O"
        avpos.remove(1)
        print("Computer chose Position 1!")
        grid()
        af = True
        return af
    if b1 == c2 == "X" and b2 == "O":
      if c1 != "O" and c1 != "X":
        c1 = "O"
        avpos.remove(7)
        print("Computer chose Position 7!")
        grid()
        af = True
        return af
    if c2 == b3 == "X" and b2 == "O":
      if c3 != "O" and c3 != "X":
        c3 = "O"
        avpos.remove(9)
        print("Computer chose Position 9!")
        grid()
        af = True
        return af
    if b2 == a2 == "X" and b2 == "O":
      if a3 != "O" and a3 != "X":
        a3 = "O"
        avpos.remove(3)
        print("Computer chose Position 3!")
        grid()
        af = True
        return af
    # X-O-X series (angled upward, rotated)
    if b1 == a3 == "X" and b2 == "O":
      if a1 != "O" and a1 != "X":
        a1 = "O"
        avpos.remove(1)
        print("Computer chose Position 1!")
        grid()
        af = True
        return af
    if a1 == c2 == "X" and b2 == "O":
      if c1 != "O" and c1 != "X":
        c1 = "O"
        avpos.remove(7)
        print("Computer chose Position 7!")
        grid()
        af = True
        return af
    if c1 == b3 == "X" and b2 == "O":
      if c3 != "O" and c3 != "X":
        c3 = "O"
        avpos.remove(9)
        print("Computer chose Position 9!")
        grid()
        af = True
        return af
    if c3 == a2 == "X" and b2 == "O":
      if a3 != "O" and a3 != "X":
        a3 = "O"
        avpos.remove(3)
        print("Computer chose Position 3!")
        grid()
        af = True
        return af
    # X-O-X series (angled downward, rotated)
    if b1 == c3 == "X" and b2 == "O":
      if c1 != "O" and c1 != "X":
        c1 = "O"
        avpos.remove(7)
        print("Computer chose Position 7!")
        grid()
        af = True
        return af
    if c2 == a3 == "X" and b2 == "O":
      if c3 != "O" and c3 != "X":
        c3 = "O"
        avpos.remove(9)
        print("Computer chose Position 9!")
        grid()
        af = True
        return af
    if a1 == b3 == "X" and b2 == "O":
      if a3 != "O" and a3 != "X":
        a3 = "O"
        avpos.remove(3)
        print("Computer chose Position 3!")
        grid()
        af = True
        return af
    if c1 == a2 == "X" and b2 == "O":
      if a1 != "O" and a1 != "X":
        a1 = "O"
        avpos.remove(1)
        print("Computer chose Position 1!")
        grid()
        af = True
        return af
  if b2 == "X":
    # X-X-O series (vertical and horizontal, rotated)
    if b2 == a2 == "X" and c2 == "O":
      r = [7,9]
      c = random.choice(r)
      if c == 7:
        if c1 != "O" and c1 != "X":
          c1 = "O"
          avpos.remove(7)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
      if c == 9:
        if c3 != "O" and c3 != "X":
          c3 = "O"
          avpos.remove(9)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
    if b1 == b2 == "X" and b3 == "O":
      r = [3,9]
      c = random.choice(r)
      if c == 3:
        if a3 != "O" and a3 != "X":
          a3 = "O"
          avpos.remove(3)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
      if c == 9:
        if c3 != "O" and c3 != "X":
          c3 = "O"
          avpos.remove(9)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
    if b2 == c3 == "X" and a2 == "O":
      r = [1,3]
      c = random.choice(r)
      if c == 1:
        if a1 != "O" and a1 != "X":
          a1 = "O"
          avpos.remove(1)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
      if c == 3:
        if a3 != "O" and a3 != "X":
          a3 = "O"
          avpos.remove(3)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
    if b2 == b3 == "X" and b1 == "O":
      r = [1,7]
      c = random.choice(r)
      if c == 1:
        if a1 != "O" and a1 != "X":
          a1 = "O"
          avpos.remove(1)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
      if c == 7:
        if c1 != "O" and c1 != "X":
          c1 = "O"
          avpos.remove(7)
          print(f"Computer chose Position {c}!")
          grid()
          af = True
          return af
    #X-X-O series (diagonal, rotated)
    if a3 == b2 == "X" and c1 == "O":
      if a1 != "O" and a1 != "X":
        a1 = "O"
        avpos.remove(1)
        print("Computer chose Position 1!")
        grid()
        af = True
        return af
    if a1 == b2 == "X" and c3 == "O":
      if a3 != "O" and a3 != "X":
        a3 = "O"
        avpos.remove(3)
        print("Computer chose Position 3!")
        grid()
        af = True
        return af
    if c1 == b2 == "X" and a3 == "O":
      if c3 != "O" and c3 != "X":
        c3 = "O"
        avpos.remove(9)
        print("Computer chose Position 9!")
        grid()
        af = True
        return af
    if c3 == b2 == "X" and a1 == "O":
      if c1 != "O" and c1 != "X":
        c1 = "O"
        avpos.remove(7)
        print("Computer chose Position 7!")
        grid()
        af = True
        return af
  af = False
  return af
#---------------- TTT Functions End


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\033[32mCOMPUTER PROJECT CLASS XI (2022-2023)")
print("Made by Amartya Bagchi, Aryan Daga and Aman Sinha of Class XI-G, DPSRKP.")
print("Finished on 26 December 2022.\033[0m")
print(" ")
while True: # Accepting the user's game of choice.
  game = input('Enter the game you want to play below, out of the codes given for each game: \n(Tic Tac Toe = "ttt", Rock Paper Scissors = "rps", Wordle = "wrd", Guess The Number = "gtn", Guess the Flag = "gtf") ')
  if game.lower() == 'rps' or game.lower() == 'ttt' or game.lower() == 'wrd' or game.lower() == 'gtn' or game.lower() == 'gtf':
    game = game.lower()
    break
  else:
    print('\033[31mPlease retry and enter a valid game!\033[0m\n')
print(" ")
if game == 'ttt': # Tic Tac Toe ------------------------------------------------------------------------------------------------------------------------------------------
  # Printing Introduction --------------------------------------------------------
  print("\033[32mWelcome to the Tic Tac Toe game!")
  print("This was made by Amartya Bagchi and Aryan Daga as a part of the Computer Science Project.\033[0m")
  print("")
  print("")
  print("\033[34mPlease use the following guide for positions to mark on your turn!")
  print("1 | 2 | 3")
  print("——————————")
  print("4 | 5 | 6")
  print("——————————")
  print("7 | 8 | 9\033[0m")
  print("")
  # ========================== MAIN TIC-TAC-TOE PROGRAM ========================
  while True:
    print("\033[34m"); choice = input("Would you like to (S) play single-player versus a Computer, or (D) play a one-versus-one with another player (Enter 'S' or 'D' only): ").upper()
    if choice == "S":
      mode = "S"
      while True:
      # Difficulty of Tic Tac Toe
        hard = input("Would like the difficulty of the Computer to be (E) Easy, (M) Medium, (H) Hard, or (I) Impossible? (Enter 'E','M','H', or 'I' only): ").upper(); print("\033[0m",end = "")
        if hard == 'E' or hard == 'M' or hard == 'H' or hard == "I":
          break
        else:
          print("\033[31mError: Please enter only 'E','M','H', or 'I' as your input!\033[0m\n")
      break
    if choice == "D":
      mode = "D"
      break
    else:
      print("\033[31mError: Please enter only 'S' or 'D' as your input!\033[0m\n")
  print()
  # -------------------------- MAIN GAME PROGRAM -------------------------------

  # -------------------------- Singleplayer Mode -------------------------------
  if mode == "S":
    # Accepting Player Name ----------------------------------------------------
    print(" ")
    #--------------------- Player - Computer Block (IMPOSSIBLE) ----------------
    if hard == "I":
      print("\033[1m\033[33mCOMPUTER:\033[0m \033[3mAh, so you have decided to challenge me? Let's do this.\033[0m")
      print(" ")
      p1 = input("Enter name of Player 1 (playing X) here: ")
      p2 = "Computer"
      grid()
      # Player Turn 1 ----------------------------------------------------------
      while True:
        try:
          print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
          pos = int(input(""))
          if pos in avpos:
            break
          else:
            print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
        except ValueError:
            print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
      mark = "X"
      enter_pos(mark, pos)
      print("")
      # Engine Turn 1 ----------------------------------------------------------
      print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
      if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 6 or pos == 7 or pos == 8 or pos == 9:
        #Player chose a non-center value
        print("Computer chose Position 5!")
        b2 = "O"
        avpos.remove(5)
        grid()
      elif pos == 5: # If Player chose center
        mark = "O"
        corner = [1,3,7,9]
        cpos = random.choice(corner)
        enter_pos(mark,cpos)
      print(" ")
      #-------------------------- Loop For Turn 2 Onwards ----------------------
      while end == False:
        # Player Turn 2 onwards ------------------------------------------------
        while True:
          try:
            print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
            pos = int(input(""))
            if pos in avpos:
              break
            else:
              print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
          except ValueError:
            print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
        mark = "X"
        enter_pos(mark,pos)
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
            print(f"\n\033[1m\033[33mCOMPUTER:\033[0m \033[3mAt least you tried, {p1}, but you were warned.\033[0m")
            break
        if len(avpos) == 0:
            print(f"\033[1m\033[33mCOMPUTER:\033[0m \033[3mWhile it may seem like it, we aren't equal, {p1}. Try again.\033[0m\n")
            print("\033[32mRESULT: The game was a draw!\033[0m")
            break
        # AI Turn 2 Onwards ----------------------------------------------------
        if end == False:
          print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
          w = win_move() # Trying to find a winning move.
          if w == False:
            b = block_win() # Blocking immediate threats.
            if b == False:
              a = anti_fork() # Blocking tactical moves with counter-tactics.
              if a == False:
                best_move() # Random move if nothing else works, will lead to a draw.
          # Checking For Potential Wins after a turn ---------------------------
          res = check_win()
          if res == "break":
              print(f"\n\033[1m\033[33mCOMPUTER:\033[0m \033[3mAt least you tried, {p1}, but you were warned.\033[0m")
              break
          if len(avpos) == 0:
              print(f"\033[1m\033[33mCOMPUTER:\033[0m \033[3mWhile it may seem like it, we aren't equal, {p1}. Try again.\033[0m\n")
              print("\033[32mRESULT: The game was a draw!\033[0m")
              break
        elif end == True:
          break
    #------------------------ Player - Computer Block (HARD) -------------------
    if hard == "H":
      p1 = input("Enter name of Player 1 (playing X) here: ")
      p2 = "Computer"
      grid()
      # Player Turn 1 ----------------------------------------------------------
      while True:
        try:
          print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
          pos = int(input(""))
          if pos in avpos:
            break
          else:
            print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
        except ValueError:
            print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
      mark = "X"
      enter_pos(mark, pos)
      print("")
      # Engine Turn 1 ----------------------------------------------------------
      print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
      if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 6 or pos == 7 or pos == 8 or pos == 9:
        #Player chose a non-center value
        print("Computer chose Position 5!")
        b2 = "O"
        avpos.remove(5)
        grid()
      elif pos == 5: # If Player chose center
        mark = "O"
        cpos = random.choice(avpos)
        enter_pos(mark,cpos)
      print(" ")
      #-------------------------- Loop For Turn 2 Onwards ----------------------
      while end == False:
        # Player Turn 2 onwards ------------------------------------------------
        while True:
          try:
            print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
            pos = int(input(""))
            if pos in avpos:
              break
            else:
              print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
          except ValueError:
              print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
        mark = "X"
        enter_pos(mark,pos)
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
          break
        if len(avpos) == 0:
          print("\033[32mRESULT: The game was a draw!\033[0m")
          break
        # Engine Turn 2 Onwards ----------------------------------------------------
        if end == False:
          print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
          w = win_move() # Trying to find a winning move.
          if w == False:
            b = block_win() # Blocking immediate threats.
            if b == False:
                best_move() # Random move, will occasionally cause Computer to lose.
          # Checking For Potential Wins after a turn ---------------------------
          res = check_win()
          if res == "break":
            break
          if len(avpos) == 0:
            print("\033[32mRESULT: The game was a draw!\033[0m")
            break
        elif end == True:
          break
    # ---------------------- Player - Computer Block (MEDIUM) ------------------
    if hard == "M":
      p1 = input("Enter name of Player 1 (playing X) here: ")
      p2 = "Computer"
      grid()
      while end == False:
        # Player Turn Loop -----------------------------------------------------
        while True:
          try:
            print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
            pos = int(input(""))
            if pos in avpos:
              break
            else:
              print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
          except ValueError:
            print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
        mark = "X"
        enter_pos(mark,pos)
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
          break
        if len(avpos) == 0:
          print("\033[32mRESULT: The game was a draw!\033[0m")
          break
        # Computer Turn --------------------------------------------------------
        print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
        b = block_win() # Blocking immediate threats.
        if b == False:
          best_move() # Just randomising, if unable to block. Loss likely.
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
          break
        if len(avpos) == 0:
          print("\033[32mRESULT: The game was a draw!\033[0m")
          break
        elif end == True:
          break
    # ---------------------- Player - Computer Block (Easy) --------------------
    if hard == "E":
      p1 = input("Enter name of Player 1 (playing X) here: ")
      p2 = "Computer"
      grid()
      while end == False:
        # Player Turn Loop -----------------------------------------------------
        while True:
          try:
            print("Your turn,", p1 ,", enter a position \033[36m(out of ",avpos,")\033[0m to mark X: ", end = "")
            pos = int(input(""))
            if pos in avpos:
              break
            else:
              print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
          except ValueError:
            print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
        mark = "X"
        enter_pos(mark,pos)
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
          break
        if len(avpos) == 0:
          print("\033[32mRESULT: The game was a draw!\033[0m")
          break
        # Computer Turn --------------------------------------------------------
        print("Computer's turn, entering a position \033[36m(out of ",avpos,")\033[0m to mark O.")
        best_move() # Completely random moves, Computer should lose in almost all cases.
        # Checking For Potential Wins after a turn -----------------------------
        res = check_win()
        if res == "break":
          break
        if len(avpos) == 0:
          print("\033[32mRESULT: The game was a draw!\033[0m")
          break
        elif end == True:
          break
  # ----------------------------------------------------------------------------

  # ------------------------------ MULTIPLAYER MODE ----------------------------
  if mode == "D":
    # Accepting Player Names ---------------------------------------------------
    print(" ")
    p1 = input("Enter name of Player 1 (playing X) here: ")
    p2 = input("Enter name of Player 2 (playing O) here: ")
    grid()
    # --------------------------- Multiplayer Loop------------------------------
    while end == False:
      # Player 1's Turn --------------------------------------------------------
      while True:
        try:
          print("Your turn,", p1 ,", enter a position (out of ",avpos,") to mark X: ", end = "")
          pos = int(input(""))
          if pos in avpos:
            break
          else:
            print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
        except ValueError:
          print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
      mark = "X"
      enter_pos(mark,pos)
      # Checking For Potential Wins after a turn -------------------------------
      res = check_win()
      if res == "break":
        break
      if len(avpos) == 0:
        print("\033[32mRESULT: The game was a draw!\033[0m")
        break
      # Player 2's Turn --------------------------------------------------------
      while True:
        try:
          print("Your turn,", p2 ,", enter a position (out of ",avpos,") to mark X: ", end = "")
          pos = int(input(""))
          if pos in avpos:
            break
          else:
            print("\033[31mError: That position is already invalid/occupied, please retry!\033[0m\n")
        except ValueError:
          print("\033[31mError: Please retry with a valid numeric value!\033[0m\n")
      mark = "O"
      enter_pos(mark,pos)
      # Checking For Potential Wins after a turn -------------------------------
      res = check_win()
      if res == "break":
        break
      if len(avpos) == 0:
        print("\033[32mRESULT: The game was a draw!\033[0m")
        break
  # Multiplayer Mode End -------------------------------------------------------

  #------------------------- END OF THE TTT PROGRAM. ---------------------------

if game == 'rps': # Rock Paper Scissor ------------------------------------------------------------------------------------------------------------------------------------------
  # Printing Introduction
  print("\033[32mWelcome to the Rock Paper Scissors game!")
  print("This was made By Aman Sinha as a part of the Computer Science Project.\033[0m")
  print(" ")
  while True:
    # Making them choose Rock Paper or Scissors
    choice=input('Choose Rock/Paper/Scissors: ')
    if choice.lower() == 'rock' or choice.lower() == "r" or choice.lower() == 'paper' or choice.lower() == "p" or choice.lower() == 'scissors' or choice.lower() == "s":
      break
    else:
      print('\033[31mPlease input either Rock, Paper or Scissors!\033[0m\n')
  # Making the Bot choose
  bot = random.choice(['🗿', '✂️', '📰'])
  #Changing all the words to emojis for "aesthetics".
  if choice.lower() == 'rock' or choice.lower() == "r":
    choice = '🗿'
  elif choice.lower() == 'paper' or choice.lower() == "p":
    choice = '📰'
  elif choice.lower() == 'scissors' or choice.lower() == "s":
    choice = '✂️'
  # Win, draw or loss checking
  if choice == '🗿' and bot == '✂️' or choice == '📰' and bot == '🗿' or choice == '✂️' and bot == '📰':
    print(f'You chose {choice}\nBot chose {bot}\n\033[32mRESULT: You won the game\033[0m')
  elif choice == bot:
    print(f"You chose {choice}\nBot chose {bot}\n\033[32mRESULT: It's a draw\033[0m")
  else:
    print(f'You chose {choice}\nBot chose {bot}\n\033[31mRESULT: You lost the game\033[0m')
  # Rock Paper Scissor Loop End -----------------------------------------------------------

if game == "wrd": # Wordle ------------------------------------------------------------------------------------------------------------------------------------------
  word = random.choice([ "which", "there", "their", "about", "would", "these", "other", "words", "could", "write", "first", "water", "after", "where", "right", "think", "three", "years", "place", "sound", "great", "again", "still", "every", "small", "found", "those", "never", "under", "might", "house", "world", "below", "asked", "going", "large", "until", "along", "shall", "being", "often", "earth", "began", "since", "study", "night", "light", "above", "paper", "parts", "young", "story", "point", "times", "heard", "whole", "white", "given", "means", "music", "miles", "thing", "today", "later", "using", "money", "lines", "order", "group", "among", "learn", "known", "space", "table", "early", "trees", "short", "hands", "state", "black", "these", "other", "words", "could", "write", "first", "water", "after", "where", "right", "think", "three", "years", "place", "sound", "great", "again", "still", "every", "small", "found", "those", "never", "under", "might", "house", "world", "below", "asked", "going", "large", "until", "along", "shall", "being", "often", "earth", "began", "since", "study", "night", "light", "above", "paper", "parts", "young", "story", "point", "times", "heard", "whole", "white", "given", "means", "music", "miles", "thing", "today", "later", "using", "money", "lines", "order", "group", "among", "learn", "known", "space", "table", "early", "trees", "short", "hands", "state", "black", "shown", "stood", "front", "voice", "kinds", "makes", "comes", "close", "power", "lived", "vowel", "taken", "built", "heart", "ready", "quite", "round", "horse", "shows", "piece", "green", "stand", "birds", "start", "river", "tried", "least", "field", "whose", "girls", "leave", "added", "color", "third", "hours", "moved", "plant", "doing", "names", "forms", "heavy", "ideas", "cried", "check", "floor", "begin", "woman", "alone", "plane", "spell", "watch", "carry", "wrote", "clear", "named", "books", "child", "glass", "human", "takes", "party", "build", "seems", "blood", "sides", "seven", "mouth", "solve", "north", "value", "death", "maybe", "happy", "tells", "gives", "looks", "shape", "lives", "steps", "areas", "sense", "speak", "force", "ocean", "speed", "women", "metal", "south", "grass", "scale", "cells", "lower", "sleep", "wrong", "pages", "ships", "needs", "rocks", "eight", "major", "level", "total", "ahead", "reach", "stars", "store", "sight", "works", "board", "cover", "songs", "equal", "stone", "waves", "guess", "dance", "spoke", "radio", "weeks", "lands", "basic", "liked", "trade", "fresh", "final", "fight", "meant", "drive", "spent", "local", "waxes", "knows", "train", "bread", "homes", "teeth", "coast", "thick", "brown", "clean", "quiet", "sugar", "facts", "steel", "forth", "rules", "notes", "units", "peace", "month", "verbs", "seeds", "helps", "sharp", "visit", "woods", "chief", "walls", "cross", "wings", "grown", "cases", "foods", "crops", "fruit", "stick", "wants", "stage", "sheep", "nouns", "plain", "drink", "bones", "apart", "turns", "moves", "touch", "angle", "based", "range", "marks", "tired", "older", "farms", "spend", "shoes", "goods", "chair", "twice", "cents", "empty", "alike", "style", "broke", "pairs", "count", "enjoy", "score", "shore", "roots", "paint", "heads", "shook", "serve", "angry", "crowd", "wheel", "quick", "dress", "share", "alive", "noise", "solid", "cloth", "signs", "hills", "types", "drawn", "worth", "truck", "piano", "upper", "loved", "usual", "faces", "drove", "cabin", "boats", "towns", "proud", "court", "model", "prime", "fifty", "plans", "yards", "prove", "tools", "price", "sheet", "smell", "boxes", "raise", "match", "truth", "roads", "threw", "enemy", "lunch", "chart", "scene", "graph", "doubt", "guide", "winds", "block", "grain", "smoke", "mixed", "games", "wagon", "sweet", "topic", "extra", "plate", "title", "knife", "fence", "falls", "cloud", "wheat", "plays", "enter", "broad", "steam", "atoms", "press", "lying", "basis", "clock", "taste", "grows", "thank", "storm", "agree", "brain", "track", "smile", "funny", "beach", "stock", "hurry", "saved", "sorry", "giant", "trail", "offer", "ought", "rough", "daily", "avoid", "keeps", "allow", "cream", "laugh", "edges", "teach", "frame", "bells", "dream", "magic", "occur", "ended", "chord", "false", "skill", "holes", "dozen", "brave", "apple", "climb", "outer", "pitch", "ruler", "holds", "fixed", "costs", "calls", "blank", "staff", "labor", "eaten", "youth", "tones", "honor", "globe", "gases", "doors", "poles", "loose", "apply", "tears", "exact", "brush", "chest", "layer", "whale", "minor", "faith", "tests", "judge", "items", "worry", "waste", "hoped", "strip", "begun", "aside", "lakes", "bound", "depth", "candy", "event", "worse", "aware", "shell", "rooms", "ranch", "image", "snake", "aloud", "dried", "likes", "motor", "pound", "knees", "refer", "fully", "chain", "shirt", "flour", "drops", "spite", "orbit", "banks", "shoot", "curve", "tribe", "tight", "blind", "slept", "shade", "claim", "flies", "theme", "queen", "fifth", "union", "hence", "straw", "entry", "issue", "birth", "feels", "anger", "brief", "rhyme", "glory", "guard", "flows", "flesh", "owned", "trick", "yours", "sizes", "noted", "width", "burst", "route", "lungs", "uncle", "bears", "royal", "kings", "forty", "trial", "cards", "brass", "opera", "chose", "owner", "vapor", "beats", "mouse", "tough", "wires", "meter", "tower", "finds", "inner", "stuck", "arrow", "poems", "label", "swing", "solar", "truly", "tense", "beans", "split", "rises", "weigh", "hotel", "stems", "pride", "swung", "grade", "digit", "badly", "boots", "pilot", "sales", "swept", "lucky", "prize", "stove", "tubes", "acres", "wound", "steep", "slide", "trunk", "error", "porch", "slave", "exist", "faced", "mines", "marry", "juice", "raced", "waved", "goose", "trust", "fewer", "favor", "mills", "views", "joint", "eager", "spots", "blend", "rings", "adult", "index", "nails", "horns", "balls", "flame", "rates", "drill", "trace", "skins", "waxed", "seats", "stuff", "ratio", "minds", "dirty", "silly", "coins", "hello", "trips", "leads", "rifle", "hopes", "bases", "shine", "bench", "moral", "fires", "meals", "shake", "shops", "cycle", "movie", "slope", "canoe", "teams", "folks", "fired", "bands", "thumb", "shout", "canal", "habit", "reply", "ruled", "fever", "crust", "shelf", "walks", "midst", "crack", "print", "tales", "coach", "stiff", "flood", "verse", "awake", "rocky", "march", "fault", "swift", "faint", "civil", "ghost", "feast", "blade", "limit", "germs", "reads", "ducks", "dairy", "worst", "gifts", "lists", "stops", "rapid", "brick", "claws", "beads", "beast", "skirt", "cakes", "lions", "frogs", "tries", "nerve", "grand", "armed", "treat", "honey", "moist", "legal", "penny", "crown", "shock", "taxes", "sixty", "altar", "pulls", "sport", "drums", "talks", "dying", "dates", "drank", "blows", "lever", "wages", "proof", "drugs", "tanks", "sings", "tails", "pause", "herds", "arose", "hated", "clues", "novel", "shame", "burnt", "races", "flash", "weary", "heels", "token", "coats", "spare", "shiny", "alarm", "dimes", "sixth", "clerk", "mercy", "sunny", "guest", "float", "shone", "pipes", "worms", "bills", "sweat", "suits", "smart", "upset", "rains", "sandy", "rainy", "parks", "sadly", "fancy", "rider", "unity", "bunch", "rolls", "crash", "craft", "newly", "gates", "hatch", "paths", "funds", "wider", "grace", "grave", "tides", "admit", "shift", "sails", "pupil", "tiger", "angel", "cruel", "agent", "drama", "urged", "patch", "nests", "vital", "sword", "blame", "weeds", "screw", "vocal", "bacon", "chalk", "cargo", "crazy", "acted", "goats", "arise", "witch", "loves", "queer", "dwell", "backs", "ropes", "shots", "merry", "phone", "cheek", "peaks", "ideal", "beard", "eagle", "creek", "cries", "ashes", "stall", "yield", "mayor", "opens", "input", "fleet", "tooth", "cubic", "wives", "burns", "poets", "apron", "spear", "organ", "cliff", "stamp", "paste", "rural", "baked", "chase", "slice", "slant", "knock", "noisy", "sorts", "stays", "wiped", "blown", "piled", "clubs", "cheer", "widow", "twist", "tenth", "hides", "comma", "sweep", "spoon", "stern", "crept", "maple", "deeds", "rides", "muddy", "crime", "jelly", "ridge", "drift", "dusty", "devil", "tempo", "humor", "sends", "steal", "tents", "waist", "roses", "reign", "noble", "cheap", "dense", "linen", "geese", "woven", "posts", "hired", "wrath", "salad", "bowed", "tires", "shark", "belts", "grasp", "blast", "polar", "fungi", "tends", "pearl", "loads", "jokes", "veins", "frost", "hears", "loses", "hosts", "diver", "phase", "toads", "alert", "tasks", "seams", "coral", "focus", "naked", "puppy", "jumps", "spoil", "quart", "macro", "fears", "flung", "spark", "vivid", "brook", "steer", "spray", "decay", "ports", "socks", "urban", "goals", "grant", "minus", "films", "tunes", "shaft", "firms", "skies", "bride", "wreck", "flock", "stare", "hobby", "bonds", "dared", "faded", "thief", "crude", "pants", "flute", "votes", "tonal", "radar", "wells", "skull", "hairs", "argue", "wears", "dolls", "voted", "caves", "cared", "broom", "scent", "panel", "fairy", "olive", "bends", "prism", "lamps", "cable", "peach", "ruins", "rally", "schwa", "lambs", "sells", "cools", "draft", "charm", "limbs", "brake", "gazed", "cubes", "delay", "beams", "fetch", "ranks", "array", "harsh", "camel", "vines", "picks", "naval", "purse", "rigid", "crawl", "toast", "soils", "sauce", "basin", "ponds", "twins", "wrist", "fluid", "pools", "brand", "stalk", "robot", "reeds", "hoofs", "buses", "sheer", "grief", "bloom", "dwelt", "melts", "risen", "flags", "knelt", "fiber", "roofs", "freed", "armor", "piles", "aimed", "algae", "twigs", "lemon", "ditch", "drunk", "rests", "chill", "slain", "panic", "cords", "tuned", "crisp", "ledge", "dived", "swamp", "clung", "stole", "molds", "yarns", "liver", "gauge", "breed", "stool", "gulls", "awoke", "gross", "diary", "rails", "belly", "trend", "flask", "stake", "fried", "draws", "actor", "handy", "bowls", "haste", "scope", "deals", "knots", "moons", "essay", "thump", "hangs", "bliss", "dealt", "gains", "bombs", "clown", "palms", "cones", "roast", "tidal", "bored", "chant", "acids", "dough", "camps", "swore", "lover", "hooks", "males", "cocoa", "punch", "award", "reins", "ninth", "noses", "links", "drain", "fills", "nylon", "lunar", "pulse", "flown", "elbow", "fatal", "sites", "moths", "meats", "foxes", "mined", "attic", "fiery", "mount", "usage", "swear", "snowy", "rusty", "scare", "traps", "relax", "react", "valid", "robin", "cease", "gills", "prior", "safer", "polio", "loyal", "swell", "salty", "marsh", "vague", "weave", "mound", "seals", "mules", "virus", "scout", "acute", "windy", "stout", "folds", "seize", "hilly", "joins", "pluck", "stack", "lords", "dunes", "burro", "hawks", "trout", "feeds", "scarf", "halls", "coals", "towel", "souls", "elect", "buggy", "pumps", "loans", "spins", "files", "oxide", "pains", "photo", "rival", "flats", "syrup", "rodeo", "sands", "moose", "pints", "curly", "comic", "cloak", "onion", "clams", "scrap", "didst", "couch", "codes", "fails", "ounce", "lodge", "greet", "gypsy", "utter", "paved", "zones", "fours", "alley", "tiles", "bless", "crest", "elder", "kills", "yeast", "erect", "bugle", "medal", "roles", "hound", "snail", "alter", "ankle", "relay", "loops", "zeros", "bites", "modes", "debts", "realm", "glove", "rayon", "swims", "poked", "stray", "lifts", "maker", "lumps", "graze", "dread", "barns", "docks", "masts", "pours", "wharf", "curse", "plump", "robes", "seeks", "cedar", "curls", "jolly", "myths", "cages", "gloom", "locks", "pedal", "beets", "crows", "anode", "slash", "creep", "rowed", "chips", "fists", "wines", "cares", "valve", "newer", "motel", "ivory", "necks", "clamp", "barge", "blues", "alien", "frown", "strap", "crews", "shack", "gonna", "saves", "stump", "ferry", "idols", "cooks", "juicy", "glare", "carts", "alloy", "bulbs", "lawns", "lasts", "fuels", "oddly", "crane", "filed", "weird", "shawl", "slips", "troop", "bolts", "suite", "sleek", "quilt", "tramp", "blaze", "atlas", "odors", "scrub", "crabs", "probe", "logic", "adobe", "exile", "rebel", "grind", "sting", "spine", "cling", "desks", "grove", "leaps", "prose", "lofty", "agony", "snare", "tusks", "bulls", "moods", "humid", "finer", "dimly", "plank", "china", "pines", "guilt", "sacks", "brace", "quote", "lathe", "gaily", "fonts", "scalp", "adopt", "foggy", "ferns", "grams", "clump", "perch", "tumor", "teens", "crank", "fable", "hedge", "genes", "sober", "boast", "tract", "cigar", "unite", "owing", "thigh", "haiku", "swish", "dikes", "wedge", "booth", "eased", "frail", "cough", "tombs", "darts", "forts", "choir", "pouch", "pinch", "hairy", "buyer", "torch", "vigor", "waltz", "heats", "herbs", "users", "flint", "click", "madam", "bleak", "blunt", "aided", "lacks", "masks", "waded", "risks", "nurse", "chaos", "sewed", "cured", "ample", "lease", "steak", "sinks", "merit", "bluff", "bathe", "gleam", "bonus", "colts", "shear", "gland", "silky", "skate", "birch", "anvil", "sleds", "groan", "maids", "meets", "speck", "hymns", "hints", "drown", "bosom", "slick", "quest", "coils", "spied", "snows", "stead", "snack", "plows", "blond", "tamed", "thorn", "waits", "glued", "banjo", "tease", "arena", "bulky", "carve", "stunt", "warms", "shady", "razor", "folly", "leafy", "notch", "fools", "otter", "pears", "flush", "genus", "ached", "fives", "flaps", "spout", "smote", "fumes", "adapt", "cuffs", "tasty", "stoop", "clips", "disks", "sniff", "lanes", "brisk", "imply", "demon", "furry", "raged", "growl", "texts", "hardy", "stung", "typed", "hates", "wiser", "timid", "serum", "beaks", "rotor", "casts", "baths", "glide", "plots", "trait", "resin", "slums", "lyric", "puffs", "decks", "brood", "mourn", "aloft", "abuse", "whirl", "edged", "ovary", "quack", "heaps", "slang", "await", "civic", "saint", "bevel", "sonar", "aunts", "packs", "froze", "tonic", "corps", "swarm", "frank", "repay", "gaunt", "wired", "niece", "cello", "needy", "chuck", "stony", "media", "surge", "hurts", "repel", "husky", "dated", "hunts", "mists", "exert", "dries", "mates", "sworn", "baker", "spice", "oasis", "boils", "spurs", "doves", "sneak", "paces", "colon", "siege", "strum", "drier", "cacao", "humus", "bales", "piped", "nasty", "rinse", "boxer", "shrub", "amuse", "tacks", "cited", "slung", "delta", "laden", "larva", "rents", "yells", "spool", "spill", "crush", "jewel", "snaps", "stain", "kicks", "tying", "slits", "rated", "eerie", "smash", "plums", "zebra", "earns", "bushy", "scary", "squad", "tutor", "silks", "slabs", "bumps", "evils", "fangs", "snout", "peril", "pivot", "yacht", "lobby", "jeans", "grins", "viola", "liner", "comet", "scars", "chops", "raids", "eater", "slate", "skips", "soles", "misty", "urine", "knobs", "sleet", "holly", "pests", "forks", "grill", "trays", "pails", "borne", "tenor", "wares", "carol", "woody", "canon", "wakes", "kitty", "miner", "polls", "shaky", "nasal", "scorn", "chess", "taxis", "crate", "shyly", "tulip", "forge", "nymph", "budge", "lowly", "abide", "depot", "oases", "asses", "sheds", "fudge", "pills", "rivet", "thine", "groom", "lanky", "boost", "broth", "heave", "gravy", "beech", "timed", "quail", "inert", "gears", "chick", "hinge", "trash", "clash", "sighs", "renew", "bough", "dwarf", "slows", "quill", "shave", "spore", "sixes", "chunk", "madly", "paced", "braid", "fuzzy", "motto", "spies", "slack", "mucus", "magma", "awful", "discs", "erase", "posed", "asset", "cider", "taper", "theft", "churn", "satin", "slots", "taxed", "bully", "sloth", "shale", "tread", "raked", "curds", "manor", "aisle", "bulge", "loins", "stair", "tapes", "leans", "bunks", "squat", "towed", "lance", "panes", "sakes", "heirs", "caste", "dummy", "pores", "fauna", "crook", "poise", "epoch", "risky", "warns", "fling", "berry", "grape", "flank", "drags", "squid", "pelts", "icing", "irony", "irons", "barks", "whoop", "choke", "diets", "whips", "tally", "dozed", "twine", "kites", "bikes", "ticks", "riots", "roars", "vault", "looms", "scold", "blink", "dandy", "pupae", "sieve", "spike", "ducts", "lends", "pizza", "brink", "widen", "plumb", "pagan", "feats", "bison", "soggy", "scoop", "argon", "nudge", "skiff", "amber", "sexes", "rouse", "salts", "hitch", "exalt", "leash", "dined", "chute", "snort", "gusts", "melon", "cheat", "reefs", "llama", "lasso", "debut", "quota", "oaths", "prone", "mixes", "rafts", "dives", "stale", "inlet", "flick", "pinto", "brows", "untie", "batch", "greed", "chore", "stirs", "blush", "onset", "barbs", "volts", "beige", "swoop", "paddy", "laced", "shove", "jerky", "poppy", "leaks", "fares", "dodge", "godly", "squaw", "affix", "brute", "nicer", "undue", "snarl", "merge", "doses", "showy", "daddy", "roost", "vases", "swirl", "petty", "colds", "curry", "cobra", "genie", "flare", "messy", "cores", "soaks", "ripen", "whine", "amino", "plaid", "spiny", "mowed", "baton", "peers", "vowed", "pious", "swans", "exits", "afoot", "plugs", "idiom", "chili", "rites", "serfs", "cleft", "berth", "grubs", "annex", "dizzy", "hasty", "latch", "wasps", "mirth", "baron", "plead", "aloof", "aging", "pixel", "bared", "mummy", "hotly", "auger", "buddy", "chaps", "badge", "stark", "fairs", "gully", "mumps", "emery", "filly", "ovens", "drone", "gauze", "idiot", "fussy", "annoy", "shank", "gouge", "bleed", "elves", "roped", "unfit", "baggy", "mower", "scant", "grabs", "fleas", "lousy", "album", "sawed", "cooky", "murky", "infer", "burly", "waged", "dingy", "brine", "kneel", "creak", "vanes", "smoky", "spurt", "combs", "easel", "laces", "humps", "rumor", "aroma", "horde", "swiss", "leapt", "opium", "slime", "afire", "pansy", "mares", "soaps", "husks", "snips", "hazel", "lined", "cafes", "naive", "wraps", "sized", "piers", "beset", "agile", "tongs", "steed", "fraud", "booty", "valor", "downy", "witty", "mossy", "psalm", "scuba", "tours", "polka", "milky", "gaudy", "shrug", "tufts", "wilds", "laser", "truss", "hares", "creed", "lilac", "siren", "tarry", "bribe", "swine", "muted", "flips", "cures", "sinew", "boxed", "hoops", "gasps", "hoods", "niche", "yucca", "glows", "sewer", "whack", "fuses", "gowns", "droop", "bucks", "pangs", "mails", "whisk", "haven", "clasp", "sling", "stint", "urges", "champ", "piety", "chirp", "pleat", "posse", "sunup", "menus", "howls", "quake", "knack", "plaza", "fiend", "caked", "bangs", "erupt", "poker", "olden", "cramp", "voter", "poses", "manly", "slump", "fined", "grips", "gaped", "purge", "hiked", "maize", "fluff", "strut", "sloop", "prowl", "roach", "cocks", "bland", "dials", "plume", "slaps", "soups", "dully", "wills", "foams", "solos", "skier", "eaves", "totem", "fused", "latex", "veils", "mused", "mains", "myrrh", "racks", "galls", "gnats", "bouts", "sisal", "shuts", "hoses", "dryly", "hover", "gloss", "seeps", "denim", "putty", "guppy", "leaky", "dusky", "filth", "oboes", "spans", "fowls", "adorn", "glaze", "haunt", "dares", "obeys", "bakes", "abyss", "smelt", "gangs", "aches", "trawl", "claps", "undid", "spicy", "hoist", "fades", "vicar", "acorn", "pussy", "gruff", "musty", "tarts", "snuff", "hunch", "truce", "tweed", "dryer", "loser", "sheaf", "moles", "lapse", "tawny", "vexed", "autos", "wager", "domes", "sheen", "clang", "spade", "sowed", "broil", "slyly", "studs", "grunt", "donor", "slugs", "aspen", "homer", "croak", "tithe", "halts", "avert", "havoc", "hogan", "glint", "ruddy", "jeeps", "flaky", "ladle", "taunt", "snore", "fines", "props", "prune", "pesos", "radii", "pokes", "tiled", "daisy", "heron", "villa", "farce", "binds", "cites", "fixes", "jerks", "livid", "waked", "inked", "booms", "chews", "licks", "hyena", "scoff", "lusty", "sonic", "smith", "usher", "tucks", "vigil", "molts", "sects", "spars", "dumps", "scaly", "wisps", "sores", "mince", "panda", "flier", "axles", "plied", "booby", "patio", "rabbi", "petal", "polyp", "tints", "grate", "troll", "tolls", "relic", "phony", "bleat", "flaws", "flake", "snags", "aptly", "drawl", "ulcer", "soapy", "bossy", "monks", "crags", "caged", "twang", "diner", "taped", "cadet", "grids", "spawn", "guile", "noose", "mores", "girth", "slimy", "aides", "spasm", "burrs", "alibi", "lymph", "saucy", "muggy", "liter", "joked", "goofy", "exams", "enact", "stork", "lured", "toxic", "omens", "nears", "covet", "wrung", "forum", "venom", "moody", "alder", "sassy", "flair", "guild", "prays", "wrens", "hauls", "stave", "tilts", "pecks", "stomp", "gales", "tempt", "capes", "mesas", "omits", "tepee", "harry", "wring", "evoke", "limes", "cluck", "lunge", "highs", "canes", "giddy", "lithe", "verge", "khaki", "queue", "loath", "foyer", "outdo", "fared", "deter", "crumb", "astir", "spire", "jumpy", "extol", "buoys", "stubs", "lucid", "thong", "afore", "whiff", "maxim", "hulls", "clogs", "slats", "jiffy", "arbor", "cinch", "igloo", "goody", "gazes", "dowel", "calms", "bitch", "scowl", "gulps", "coded", "waver", "mason", "lobes", "ebony", "flail", "isles", "clods", "dazed", "adept", "oozed", "sedan", "clays", "warts", "ketch", "skunk", "manes", "adore", "sneer", "mango", "fiord", "flora", "roomy", "minks", "thaws", "watts", "freer", "exult", "plush", "paled", "twain", "clink", "scamp", "pawed", "grope", "bravo", "gable", "stink", "sever", "waned", "rarer", "regal", "wards", "fawns", "babes", "unify", "amend", "oaken", "glade", "visor", "hefty", "nines", "throb", "pecan", "butts", "pence", "sills", "jails", "flyer", "saber", "nomad", "miter", "beeps", "domed", "gulfs", "curbs", "heath", "moors", "aorta", "larks", "tangy", "wryly", "cheep", "rages", "evade", "lures", "freak", "vogue", "tunic", "slams", "knits", "dumpy", "mania", "spits", "firth", "hikes", "trots", "nosed", "clank", "dogma", "bloat", "balsa", "graft", "middy", "stile", "keyed", "finch", "sperm", "chaff", "wiles", "amigo", "copra", "amiss", "eying", "twirl", "lurch", "popes", "chins", "smock", "tines", "guise", "grits", "junks", "shoal", "cache", "tapir", "atoll", "deity", "toils", "spree", "mocks", "scans", "shorn", "revel", "raven", "hoary", "reels", "scuff", "mimic", "weedy", "corny", "truer", "rouge", "ember", "floes", "torso", "wipes", "edict", "sulky", "recur", "groin", "baste", "kinks", "surer", "piggy", "moldy", "franc", "liars", "inept", "gusty", "facet", "jetty", "equip", "leper", "slink", "soars", "cater", "dowry", "sided", "yearn", "decoy", "taboo", "ovals", "heals", "pleas", "beret", "spilt", "gayly", "rover", "endow", "pygmy", "carat", "abbey", "vents", "waken", "chimp", "fumed", "sodas", "vinyl", "clout", "wades", "mites", "smirk", "bores", "bunny", "surly", "frock", "foray", "purer", "milks", "query", "mired", "blare", "froth", "gruel", "navel", "paler", "puffy", "casks", "grime", "derby", "mamma", "gavel", "teddy", "vomit", "moans", "allot", "defer", "wield", "viper", "louse", "erred", "hewed", "abhor", "wrest", "waxen", "adage", "ardor", "stabs", "pored", "rondo", "loped", "fishy", "bible", "hires", "foals", "feuds", "jambs", "thuds", "jeers", "knead", "quirk", "rugby", "expel", "greys", "rigor", "ester", "lyres", "aback", "glues", "lotus", "lurid", "rungs", "hutch", "thyme", "valet", "tommy", "yokes", "epics", "trill", "pikes", "ozone", "caper", "chime", "frees", "famed", "leech", "smite", "neigh", "erode", "robed", "hoard", "salve", "conic", "gawky", "craze", "jacks", "gloat", "mushy", "rumps", "fetus", "wince", "pinks", "shalt", "toots", "glens", "cooed", "rusts", "stews", "shred", "parka", "chugs", "winks", "clots", "shrew", "booed", "filmy", "juror", "dents", "gummy", "grays", "hooky", "butte", "dogie", "poled", "reams", "fifes", "spank", "gayer", "tepid", "spook", "taint", "flirt", "rogue", "spiky", "opals", "miser", "cocky", "coyly", "balmy", "slosh", "brawl", "aphid", "faked", "hydra", "brags", "chide", "yanks", "allay", "video", "altos", "eases", "meted", "chasm", "longs", "excel", "taffy", "impel", "savor", "koala", "quays", "dawns", "proxy", "clove", "duets", "dregs", "tardy", "briar", "grimy", "ultra", "meaty", "halve", "wails", "suede", "mauve", "envoy", "arson", "coves", "gooey", "brews", "sofas", "chums", "amaze", "zooms", "abbot", "halos", "scour", "suing", "cribs", "sagas", "enema", "wordy", "harps", "coupe", "molar", "flops", "weeps", "mints", "ashen", "felts", "askew", "munch", "mewed", "divan", "vices", "jumbo", "blobs", "blots", "spunk", "acrid", "topaz", "cubed", "clans", "flees", "slurs", "gnaws", "welds", "fords", "emits", "agate", "pumas", "mends", "darks", "dukes", "plies", "canny", "hoots", "oozes", "lamed", "fouls", "clefs", "nicks", "mated", "skims", "brunt", "tuber", "tinge", "fates", "ditty", "thins", "frets", "eider", "bayou", "mulch", "fasts", "amass", "damps", "morns", "friar", "palsy", "vista", "croon", "conch", "udder", "tacos", "skits", "mikes", "quits", "preen", "aster", "adder", "elegy", "pulpy", "scows", "baled", "hovel", "lavas", "crave", "optic", "welts", "busts", "knave", "razed", "shins", "totes", "scoot", "dears", "crock", "mutes", "trims", "skein", "doted", "shuns", "veers", "fakes", "yoked", "wooed", "hacks", "sprig", "wands", "lulls", "seers", "snobs", "nooks", "pined", "perky", "mooed", "frill", "dines", "booze", "tripe", "prong", "drips", "odder", "levee", "antic", "sidle", "pithy", "corks", "yelps", "joker", "fleck", "buffs", "scram", "tiers", "bogey", "doled", "irate", "vales", "coped", "hails", "elude", "bulks", "aired", "vying", "stags", "strew", "cocci", "pacts", "scabs", "silos", "dusts", "yodel", "terse", "jaded", "baser", "jibes", "foils", "sways", "forgo", "slays", "preys", "treks", "quell", "peeks", "assay", "lurks", "eject", "boars", "trite", "belch", "gnash", "wanes", "lutes", "whims", "dosed", "chewy", "snipe", "umbra", "teems", "dozes", "kelps", "upped", "brawn", "doped", "shush", "rinds", "slush", "moron", "voile", "woken", "fjord", "sheik", "jests", "kayak", "slews", "toted", "saner", "drape", "patty", "raves", "sulfa", "grist", "skied", "vixen", "civet", "vouch", "tiara", "homey", "moped", "runts", "serge", "kinky", "rills", "corns", "brats", "pries", "amble", "fries", "loons", "tsars", "datum", "musky", "pigmy", "gnome", "ravel", "ovule", "icily", "liken", "lemur", "frays", "silts", "sifts", "plods", "ramps", "tress", "earls", "dudes", "waive", "karat", "jolts", "peons", "beers", "horny", "pales", "wreak", "lairs", "lynch", "stank", "swoon", "idler", "abort", "blitz", "ensue", "atone", "bingo", "roves", "kilts", "scald", "adios", "cynic", "dulls", "memos", "elfin", "dales", "peels", "peals", "bares", "sinus", "crone", "sable", "hinds", "shirk", "enrol", "wilts", "roams", "duped", "cysts", "mitts", "safes", "spats", "coops", "filet", "knell", "refit", "covey", "punks", "kilns", "fitly", "abate", "talcs", "heeds", "duels", "wanly", "ruffs", "gauss", "lapel", "jaunt", "whelp", "cleat", "gauzy", "dirge", "edits", "wormy", "moats", "smear", "prods", "bowel", "frisk", "vests", "bayed", "rasps", "tames", "delve", "embed", "befit", "wafer", "ceded", "novas", "feign", "spews", "larch", "huffs", "doles", "mamas", "hulks", "pried", "brims", "irked", "aspic", "swipe", "mealy", "skimp", "bluer", "slake", "dowdy", "penis", "brays", "pupas", "egret", "flunk", "phlox", "gripe", "peony", "douse", "blurs", "darns", "slunk", "lefts", "chats", "inane", "vials", "stilt", "rinks", "woofs", "wowed", "bongs", "frond", "ingot", "evict", "singe", "shyer", "flied", "slops", "dolts", "drool", "dells", "whelk", "hippy", "feted", "ether", "cocos", "hives", "jibed", "mazes", "trios", "sirup", "squab", "laths", "leers", "pasta", "rifts", "lopes", "alias", "whirs", "diced", "slags", "lodes", "foxed", "idled", "prows", "plait", "malts", "chafe", "cower", "toyed", "chefs", "keels", "sties", "racer", "etude", "sucks", "sulks", "micas", "czars", "copse", "ailed", "abler", "rabid", "golds", "croup", "snaky", "visas", "palls", "mopes", "boned", "wispy", "raved", "swaps", "junky", "doily", "pawns", "tamer", "poach", "baits", "damns", "gumbo", "daunt", "prank", "hunks", "buxom", "heres", "honks", "stows", "unbar", "idles", "routs", "sages", "goads", "remit", "copes", "deign", "culls", "girds", "haves", "lucks", "stunk", "dodos", "shams", "snubs", "icons", "usurp", "dooms", "hells", "soled", "comas", "paves", "maths", "perks", "limps", "wombs", "blurb", "daubs", "cokes", "sours", "stuns", "cased", "musts", "coeds", "cowed", "aping", "zoned", "rummy", "fetes", "skulk", "quaff", "rajah", "deans", "reaps", "galas", "tills", "roved", "kudos", "toned", "pared", "scull", "vexes", "punts", "snoop", "bails", "dames", "hazes", "lores", "marts", "voids", "ameba", "rakes", "adzes", "harms", "rears", "satyr", "swill", "hexes", "colic", "leeks", "hurls", "yowls", "ivies", "plops", "musks", "papaw", "jells", "bused", "cruet", "bided", "filch", "zests", "rooks", "laxly", "rends", "loams", "basks", "sires", "carps", "pokey", "flits", "muses", "bawls", "shuck", "viler", "lisps", "peeps", "sorer", "lolls", "prude", "diked", "floss", "flogs", "scums", "dopes", "bogie", "pinky", "leafs", "tubas", "scads", "lowed", "yeses", "biked", "qualm", "evens", "caned", "gawks", "whits", "wooly", "gluts", "romps", "bests", "dunce", "crony", "joist", "tunas", "boner", "malls", "parch", "avers", "crams", "pares", "dally", "bigot", "kales", "flays", "leach", "gushy", "pooch", "huger", "slyer", "golfs", "mires", "flues", "loafs", "arced", "acnes", "neons", "fiefs", "dints", "dazes", "pouts", "cored", "yules", "lilts", "beefs", "mutts", "fells", "cowls", "spuds", "lames", "jawed", "dupes", "deads", "bylaw", "noons", "nifty", "clued", "vireo", "gapes", "metes", "cuter", "maims", "droll", "cupid", "mauls", "sedge", "papas", "wheys", "eking", "loots", "hilts", "meows", "beaus", "dices", "peppy", "riper", "fogey", "gists", "yogas", "gilts", "skews", "cedes", "zeals", "alums", "okays", "elope", "grump", "wafts", "soots", "blimp", "hefts", "mulls", "hosed", "cress", "doffs", "ruder", "pixie", "waifs", "ousts", "pucks", "biers", "gulch", "suets", "hobos", "lints", "brans", "teals", "garbs", "pewee", "helms", "turfs", "quips", "wends", "banes", "napes", "icier", "swats", "bagel", "hexed", "ogres", "goner", "gilds", "pyres", "lards", "bides", "paged", "talon", "flout", "medic", "veals", "putts", "dirks", "dotes", "tippy", "blurt", "piths", "acing", "barer", "whets", "gaits", "wools", "dunks", "heros", "swabs", "dirts", "jutes", "hemps", "surfs", "okapi", "chows", "shoos", "dusks", "parry", "decal", "furls", "cilia", "sears", "novae", "murks", "warps", "slues", "lamer", "saris", "weans", "purrs", "dills", "togas", "newts", "meany", "bunts", "razes", "goons", "wicks", "ruses", "vends", "geode", "drake", "judos", "lofts", "pulps", "lauds", "mucks", "vises", "mocha", "oiled", "roman", "ethyl", "gotta", "fugue", "smack", "gourd", "bumpy", "radix", "fatty", "borax", "cubit", "cacti", "gamma", "focal", "avail", "papal", "golly", "elite", "versa", "billy", "adieu", "annum", "howdy", "rhino", "norms", "bobby", "axiom", "setup", "yolks", "terns", "mixer", "genre", "knoll", "abode", "junta", "gorge", "combo", "alpha", "overt", "kinda", "spelt", "prick", "nobly", "ephod", "audio", "modal", "veldt", "warty", "fluke", "bonny", "bream", "rosin", "bolls", "doers", "downs", "beady", "motif", "humph", "fella", "mould", "crepe", "kerns", "aloha", "glyph", "azure", "riser", "blest", "locus", "lumpy", "beryl", "wanna", "brier", "tuner", "rowdy", "mural", "timer", "canst", "krill", "quoth", "lemme", "triad", "tenon", "amply", "deeps", "padre", "leant", "pacer", "octal", "dolly", "trans", "sumac", "foamy", "lolly", "giver", "quipu", "codex", "manna", "unwed", "vodka", "ferny", "salon", "duple", "boron", "revue", "crier", "alack", "inter", "dilly", "whist", "cults", "spake", "reset", "loess", "decor", "mover", "verve", "ethic", "gamut", "lingo", "dunno", "align", "sissy", "incur", "reedy", "avant", "piper", "waxer", "calyx", "basil", "coons", "seine", "piney", "lemma", "trams", "winch", "whirr", "saith", "ionic", "heady", "harem", "tummy", "sally", "shied", "dross", "farad", "saver", "tilde", "jingo", "bower", "serif", "facto", "belle", "inset", "bogus", "caved", "forte", "sooty", "bongo", "toves", "credo", "basal", "yella", "aglow", "glean", "gusto", "hymen", "ethos", "terra", "brash", "scrip", "swash", "aleph", "tinny", "itchy", "wanta", "trice", "jowls", "gongs", "garde", "boric", "twill", "sower", "henry", "awash", "libel", "spurn", "sabre", "rebut", "penal", "obese", "sonny", "quirt", "mebbe", "tacit", "greek", "xenon", "hullo", "pique", "roger", "negro", "hadst", "gecko", "beget", "uncut", "aloes", "louis", "quint", "clunk", "raped", "salvo", "diode", "matey", "hertz", "xylem", "kiosk", "apace", "cawed", "peter", "wench", "cohos", "sorta", "gamba", "bytes", "tango", "nutty", "axial", "aleck", "natal", "clomp", "gored", "siree", "bandy", "gunny", "runic", "whizz", "rupee", "fated", "wiper", "bards", "briny", "staid", "hocks", "ochre", "yummy", "gents", "soupy", "roper", "swath", "cameo", "edger", "spate", "gimme", "ebbed", "breve", "theta", "deems", "dykes", "servo", "telly", "tabby", "tares", "blocs", "welch", "ghoul", "vitae", "cumin", "dinky", "bronc", "tabor", "teeny", "comer", "borer", "sired", "privy", "mammy", "deary", "gyros", "sprit", "conga", "quire", "thugs", "furor", "bloke", "runes", "bawdy", "cadre", "toxin", "annul", "egged", "anion", "nodes", "picky", "stein", "jello", "audit", "echos", "fagot", "letup", "eyrie", "fount", "caped", "axons", "amuck", "banal", "riled", "petit", "umber", "miler", "fibre", "agave", "bated", "bilge", "vitro", "feint", "pudgy", "mater", "manic", "umped", "pesky", "strep", "slurp", "pylon", "puree", "caret", "temps", "newel", "yawns", "seedy", "treed", "coups", "rangy", "brads", "mangy", "loner", "circa", "tibia", "afoul", "mommy", "titer", "carne", "kooky", "motes", "amity", "suave", "hippo", "curvy", "samba", "newsy", "anise", "imams", "tulle", "aways", "liven", "hallo", "wales", "opted", "canto", "idyll", "bodes", "curio", "wrack", "hiker", "chive", "yokel", "dotty", "demur", "cusps", "specs", "quads", "laity", "toner", "decry", "writs", "saute", "clack", "aught", "logos", "tipsy", "natty", "ducal", "bidet", "bulgy", "metre", "lusts", "unary", "goeth", "baler", "sited", "shies", "hasps", "brung", "holed", "swank", "looky", "melee", "huffy", "loamy", "pimps", "titan", "binge", "shunt", "femur", "libra", "seder", "honed", "annas", "coypu", "shims", "zowie", "jihad", "savvy", "nadir", "basso", "monic", "maned", "mousy", "omega", "laver", "prima", "picas", "folio", "mecca", "reals", "troth", "testy", "balky", "crimp", "chink", "abets", "splat", "abaci", "vaunt", "cutie", "pasty", "moray", "levis", "ratty", "islet", "joust", "motet", "viral", "nukes", "grads", "comfy", "voila", "woozy", "blued", "whomp", "sward", "metro", "skeet", "chine", "aerie", "bowie", "tubby", "emirs", "coati", "unzip", "slobs", "trike", "funky", "ducat", "dewey", "skoal", "wadis", "oomph", "taker", "minim", "getup", "stoic", "synod", "runty", "flyby", "braze", "inlay", "venue", "louts", "peaty", "orlon", "humpy", "radon", "beaut", "raspy", "unfed", "crick", "nappy", "vizor", "yipes", "rebus", "divot", "kiwis", "vetch", "squib", "sitar", "kiddo", "dyers", "cotta", "matzo", "lager", "zebus", "crass", "dacha", "kneed", "dicta", "fakir", "knurl", "runny", "unpin", "julep", "globs", "nudes", "sushi", "tacky", "stoke", "kaput", "butch", "hulas", "croft", "achoo", "genii", "nodal", "outgo", "spiel", "viols", "fetid", "cagey", "fudgy", "epoxy", "leggy", "hanky", "lapis", "felon", "beefy", "coots", "melba", "caddy", "segue", "betel", "frizz", "drear", "kooks", "turbo", "hoagy", "moult", "helix", "zonal", "arias", "nosey", "paean", "lacey", "banns", "swain", "fryer", "retch", "tenet", "gigas", "whiny", "ogled", "rumen", "begot", "cruse", "abuts", "riven", "balks", "sines", "sigma", "abase", "ennui", "gores", "unset", "augur", "sated", "odium", "latin", "dings", "moire", "scion", "henna", "kraut", "dicks", "lifer", "prigs", "bebop", "gages", "gazer", "fanny", "gibes", "aural", "tempi", "hooch", "rapes", "snuck", "harts", "techs", "emend", "ninny", "guava", "scarp", "liege", "tufty", "sepia", "tomes", "carob", "emcee", "prams", "poser", "verso", "hubba", "joule", "baize", "blips", "scrim", "cubby", "clave", "winos", "rearm", "liens", "lumen", "chump", "nanny", "trump", "fichu", "chomp", "homos", "purty", "maser", "woosh", "patsy", "shill", "rusks", "avast", "swami", "boded", "ahhhh", "lobed", "natch", "shish", "tansy", "snoot", "payer", "altho", "sappy", "laxer", "hubby", "aegis", "riles", "ditto", "jazzy", "dingo", "quasi", "septa", "peaky", "lorry", "heerd", "bitty", "payee", "seamy", "apses", "imbue", "belie", "chary", "spoof", "phyla", "clime", "babel", "wacky", "sumps", "skids", "khans", "crypt", "inure", "nonce", "outen", "faire", "hooey", "anole", "kazoo", "calve", "limbo", "argot", "ducky", "faker", "vibes", "gassy", "unlit", "nervy", "femme", "biter", "fiche", "boors", "gaffe", "saxes", "recap", "synch", "facie", "dicey", "ouija", "hewer", "legit", "gurus", "edify", "tweak", "caron", "typos", "rerun", "polly", "surds", "hamza", "nulls", "hater", "lefty", "mogul", "mafia", "debug", "pates", "blabs", "splay", "talus", "moola", "nixed", "kilos", "snide", "horsy", "gesso", "jaggy", "trove", "nixes", "creel", "pater", "iotas", "cadge", "skyed", "hokum", "furze", "ankhs", "curie", "nutsy", "hilum", "remix", "angst", "burls", "jimmy", "veiny", "tryst", "codon", "befog", "gamed", "flume", "axman", "doozy", "lubes", "rheas", "bozos", "butyl", "kelly", "mynah", "jocks", "donut", "avian", "wurst", "chock", "quash", "quals", "hayed", "bombe", "cushy", "spacy", "puked", "leery", "thews", "prink", "amens", "tesla", "intro", "fiver", "frump", "capos", "opine", "coder", "namer", "jowly", "pukes", "haled", "chard", "duffs", "bruin", "reuse", "whang", "toons", "frats", "silty", "telex", "cutup", "nisei", "neato", "decaf", "softy", "bimbo", "adlib", "loony", "shoed", "agues", "peeve", "noway", "gamey", "sarge", "reran", "epact", "potty", "coned", "upend", "narco", "ikats", "whorl", "jinks", "tizzy", "weepy", "posit", "marge", "vegan", "clops", "numbs", "reeks", "rubes", "rower", "biped", "tiffs", "hocus", "hammy", "bunco", "fixit", "tykes", "chaws", "yucky", "hokey", "resew", "maven", "adman", "scuzz", "slogs", "souse", "nacho", "mimed", "melds", "boffo", "debit", "pinup", "vagus", "gulag", "randy", "bosun", "educe", "faxes", "auras", "pesto", "antsy", "betas", "fizzy", "dorky", "snits", "moxie", "thane", "mylar", "nobby", "gamin", "gouty", "esses", "goyim", "paned", "druid", "jades", "rehab", "gofer", "tzars", "octet", "homed", "socko", "dorks", "eared", "anted", "elide", "fazes", "oxbow", "dowse", "situs", "macaw", "scone", "drily", "hyper", "salsa", "mooch", "gated", "unjam", "lipid", "mitre", "venal", "knish", "ritzy", "divas", "torus", "mange", "dimer", "recut", "meson", "wined", "fends", "phage", "fiats", "caulk", "cavil", "panty", "roans", "bilks", "hones", "botch", "estop", "sully", "sooth", "gelds", "ahold", "raper", "pager", "fixer", "infix", "hicks", "tuxes", "plebe", "twits", "abash", "twixt", "wacko", "primp", "nabla", "girts", "miffs", "emote", "xerox", "rebid", "shahs", "rutty", "grout", "grift", "deify", "biddy", "kopek", "semis", "bries", "acmes", "piton", "hussy", "torts", "disco", "whore", "boozy", "gibed", "vamps", "amour", "soppy", "gonzo", "durst", "wader", "tutus", "perms", "catty", "glitz", "brigs", "nerds", "barmy", "gizmo", "owlet", "sayer", "molls", "shard", "whops", "comps", "corer", "colas", "matte", "droid", "ploys", "vapid", "cairn", "deism", "mixup", "yikes", "prosy", "raker", "flubs", "whish", "reify", "craps", "shags", "clone", "hazed", "macho", "recto", "refix", "drams", "biker", "aquas", "porky", "doyen", "exude", "goofs", "divvy", "noels", "jived", "hulky", "cager", "harpy", "oldie", "vivas", "admix", "codas", "zilch", "deist", "orcas", "retro", "pilaf", "parse", "rants", "zingy", "toddy", "chiff", "micro", "veeps", "girly", "nexus", "demos", "bibbs", "antes", "lulus", "gnarl", "zippy", "ivied", "epees", "wimps", "tromp", "grail", "yoyos", "poufs", "hales", "roust", "cabal", "rawer", "pampa", "mosey", "kefir", "burgs", "unmet", "cuspy", "boons", "hypes", "dynes", "nards", "lanai", "yogis", "sepal", "quark", "toked", "prate", "ayins", "hawed", "swigs", "vitas", "toker", "doper", "bossa", "linty", "foist", "mondo", "stash", "kayos", "twerp", "zesty", "capon", "wimpy", "rewed", "fungo", "tarot", "frosh", "kabob", "pinko", "redid", "mimeo", "heist", "tarps", "lamas", "sutra", "dinar", "whams", "busty", "spays", "mambo", "nabob", "preps", "odour", "cabby", "conks", "sluff", "dados", "houri", "swart", "balms", "gutsy", "faxed", "egads", "pushy", "retry", "agora", "drubs", "daffy", "chits", "mufti", "karma", "lotto", "toffs", "burps", "deuce", "zings", "kappa", "clads", "doggy", "duper", "scams", "ogler", "mimes", "throe", "zetas", "waled", "promo", "blats", "muffs", "oinks", "viand", "coset", "finks", "faddy", "minis", "snafu", "sauna", "usury", "muxes", "craws", "stats", "condo", "coxes", "loopy", "dorms", "ascot", "dippy", "execs", "dopey", "envoi", "umpty", "gismo", "fazed", "strop", "jives", "slims", "batik", "pings", "sonly", "leggo", "pekoe", "prawn", "luaus", "campy", "oodle", "prexy", "proms", "touts", "ogles", "tweet", "toady", "naiad", "hider", "nuked", "fatso", "sluts", "obits", "narcs", "tyros", "delis", "wooer", "hyped", "poset", "byway", "texas", "scrod", "avows", "futon", "torte", "tuple", "carom", "kebab", "tamps", "jilts", "duals", "artsy", "repro", "modem", "toped", "psych", "sicko", "klutz", "tarns", "coxed", "drays", "cloys", "anded", "piker", "aimer", "suras", "limos", "flack", "hapax", "dutch", "mucky", "shire", "klieg", "staph", "layup", "tokes", "axing", "toper", "duvet", "cowry", "profs", "blahs", "addle", "sudsy", "batty", "coifs", "suety", "gabby", "hafta", "pitas", "gouda", "deice", "taupe", "topes", "duchy", "nitro", "carny", "limey", "orals", "hirer", "taxer", "roils", "ruble", "elate", "dolor", "wryer", "snots", "quais", "coked", "gimel", "gorse", "minas", "goest", "agape", "manta", "jings", "iliac", "admen", "offen", "cills", "offal", "lotta", "bolas", "thwap", "alway", "boggy", "donna", "locos", "belay", "gluey", "bitsy", "mimsy", "hilar", "outta", "vroom", "fetal", "raths", "renal", "dyads", "crocs", "vires", "culpa", "kivas", "feist", "teats", "thats", "yawls", "whens", "abaca", "ohhhh", "aphis", "fusty", "eclat", "perdu", "mayst", "exeat", "molly", "supra", "wetly", "plasm", "buffa", "semen", "pukka", "tagua", "paras", "stoat", "secco", "carte", "haute", "molal", "shads", "forma", "ovoid", "pions", "modus", "bueno", "rheum", "scurf", "parer", "ephah", "doest", "sprue", "flams", "molto", "dieth", "choos", "miked", "bronx", "goopy", "bally", "plumy", "moony", "morts", "yourn", "bipod", "spume", "algal", "ambit", "mucho", "spued", "dozer", "harum", "groat", "skint", "laude", "thrum", "pappy", "oncet", "rimed", "gigue", "limed", "plein", "redly", "humpf", "lites", "seest", "grebe", "absit", "thanx", "pshaw", "yawps", "plats", "payed", "areal", "tilth", "youse", "gwine", "thees", "watsa", "lento", "spitz", "yawed", "gipsy", "sprat", "cornu", "amahs", "blowy", "wahoo", "lubra", "mecum", "whooo", "coqui", "sabra", "edema", "mrads", "dicot", "astro", "kited", "ouzel", "didos", "grata", "bonne", "axmen", "klunk", "summa", "laves", "purls", "yawny", "teary", "masse", "largo", "bazar", "pssst", "sylph", "lulab", "toque", "fugit", "plunk", "ortho", "lucre", "cooch", "whipt", "folky", "tyres", "wheee", "corky", "injun", "solon", "didot", "kerfs", "rayed", "wassa", "chile", "begat", "nippy", "litre", "magna", "rebox", "hydro", "milch", "brent", "gyves", "lazed", "feued", "mavis", "inapt", "baulk", "casus", "scrum", "wised", "fossa", "dower", "kyrie", "bhoys", "scuse", "feuar", "ohmic", "juste", "ukase", "beaux", "tusky", "orate", "musta", "lardy", "intra", "quiff", "epsom", "neath", "ocher", "tared", "homme", "mezzo", "corms", "psoas", "beaky", "terry", "infra", "spivs", "tuans", "belli", "bergs", "anima", "weirs", "mahua", "scops", "manse", "titre", "curia", "kebob", "cycad", "talky", "fucks", "tapis", "amide", "dolce", "sloes", "jakes", "russe", "blash", "tutti", "pruta", "panga", "blebs", "tench", "swarf", "herem", "missy", "merse", "pawky", "limen", "vivre", "chert", "unsee", "tiros", "brack", "foots", "welsh", "fosse", "knops", "ileum", "noire", "firma", "podgy", "laird", "thunk", "shute", "rowan", "shoji", "poesy", "uncap", "fames", "glees", "costa", "turps", "fores", "solum", "imago", "byres", "fondu", "coney", "polis", "dictu", "kraal", "sherd", "mumbo", "wroth", "chars", "unbox", "vacuo", "slued", "weest", "hades", "wiled", "syncs", "muser", "excon", "hoars", "sibyl", "passe", "joeys", "lotsa", "lepta", "shays", "bocks", "endue", "darer", "nones", "ileus", "plash", "busby", "wheal", "buffo", "yobbo", "biles", "poxes", "rooty", "licit", "terce", "bromo", "hayey", "dweeb", "imbed", "saran", "bruit", "punky", "softs", "biffs", "loppy", "agars", "aquae", "livre", "biome", "bunds", "shews", "diems", "ginny", "degum", "polos", "desex", "unman", "dungy", "vitam", "wedgy", "glebe", "apers", "ridgy", "roids", "wifey", "vapes", "whoas", "bunko", "yolky", "ulnas", "reeky", "bodge", "brant", "davit", "deque", "liker", "jenny", "tacts", "fulls", "treap", "ligne", "acked", "refry", "vower", "aargh", "churl", "momma", "gaols", "whump", "arras", "marls", "tiler", "grogs", "memes", "midis", "tided", "haler", "duces", "twiny", "poste", "unrig", "prise", "drabs", "quids", "facer", "spier", "baric", "geoid", "remap", "trier", "gunks", "steno", "stoma", "airer", "ovate", "torah", "apian", "smuts", "pocks", "yurts", "exurb", "defog", "nuder", "bosky", "nimbi", "mothy", "joyed", "labia", "pards", "jammy", "bigly", "faxer", "hoppy", "nurbs", "cotes", "dishy", "vised", "celeb", "pismo", "casas", "withs", "dodgy", "scudi", "mungs", "muons", "ureas", "ioctl", "unhip", "krone", "sager", "verst", "expat", "gronk", "uvula", "shawm", "bilgy", "braes", "cento", "webby", "lippy", "gamic", "lordy", "mazed", "tings", "shoat", "faery", "wirer", "diazo", "carer", "rater", "greps", "rente", "zloty", "viers", "unapt", "poops", "fecal", "kepis", "taxon", "eyers", "wonts", "spina", "stoae", "yenta", "pooey", "buret", "japan", "bedew", "hafts", "selfs", "oared", "herby", "pryer", "oakum", "dinks", "titty", "sepoy", "penes", "fusee", "winey", "gimps", "nihil", "rille", "giber", "ousel", "umiak", "cuppy", "hames", "shits", "azine", "glads", "tacet", "bumph", "coyer", "honky", "gamer", "gooky", "waspy", "sedgy", "bents", "varia", "djinn", "junco", "pubic", "wilco", "lazes", "idyls", "lupus", "rives", "snood", "schmo", "spazz", "finis", "noter", "pavan", "orbed", "bates", "pipet", "baddy", "goers", "shako", "stets", "sebum", "seeth", "lobar", "raver", "ajuga", "riced", "velds", "dribs", "ville", "dhows", "unsew", "halma", "krona", "limby", "jiffs", "treys", "bauds", "pffft", "mimer", "plebs", "caner", "jiber", "cuppa", "washy", "chuff", "unarm", "yukky", "styes", "waker", "flaks", "maces", "rimes", "gimpy", "guano", "liras", "kapok", "scuds", "bwana", "oring", "aider", "prier", "klugy", "monte", "golem", "velar", "firer", "pieta", "umbel", "campo", "unpeg", "fovea", "abeam", "boson", "asker", "goths", "vocab", "vined", "trows", "tikis", "loper", "indie", "boffs", "spang", "grapy", "tater", "ichor", "kilty", "lochs", "supes", "degas", "flics", "torsi", "beths", "weber", "resaw", "lawny", "coven", "mujik", "relet", "therm", "heigh", "shnor", "trued", "zayin", "liest", "barfs", "bassi", "qophs", "roily", "flabs", "punny", "okras", "hanks", "dipso", "nerfs", "fauns", "calla", "pseud", "lurer", "magus", "obeah", "atria", "twink", "palmy", "pocky", "pends", "recta", "plonk", "slaws", "keens", "nicad", "pones", "inker", "whews", "groks", "mosts", "trews", "ulnar", "gyppy", "cocas", "expos", "eruct", "oiler", "vacua", "dreck", "dater", "arums", "tubal", "voxel", "dixit", "beery", "assai", "lades", "actin", "ghoti", "buzzy", "meads", "grody", "ribby", "clews", "creme", "email", "pyxie", "kulak", "bocci", "rived", "duddy", "hoper", "lapin", "wonks", "petri", "phial", "fugal", "holon", "boomy", "duomo", "musos", "shier", "hayer", "porgy", "hived", "litho", "fisty", "stagy", "luvya", "maria", "smogs", "asana", "yogic", "slomo", "fawny", "amine", "wefts", "gonad", "twirp", "brava", "plyer", "fermi", "loges", "niter", "revet", "unate", "gyved", "totty", "zappy", "honer", "giros", "dicer", "calks", "luxes", "monad", "cruft", "quoin", "fumer", "amped", "shlep", "vinca", "yahoo", "vulva", "zooey", "dryad", "nixie", "moper", "iambs", "lunes", "nudie", "limns", "weals", "nohow", "miaow", "gouts", "mynas", "mazer", "kikes", "oxeye", "stoup", "jujus", "debar", "pubes", "taels", "defun", "rands", "blear", "paver", "goosy", "sprog", "oleos", "toffy", "pawer", "maced", "crits", "kluge", "tubed", "sahib", "ganef", "scats", "sputa", "vaned", "acned", "taxol", "plink", "oweth", "tribs", "resay", "boule", "thous", "haply", "glans", "maxis", "bezel", "antis", "porks", "quoit", "alkyd", "glary", "beamy", "hexad", "bonks", "tecum", "kerbs", "filar", "frier", "redux", "abuzz", "fader", "shoer", "couth", "trues", "guyed", "goony", "booky", "fuzes", "hurly", "genet", "hodad", "calix", "filer", "pawls", "iodic", "utero", "henge", "unsay", "liers", "piing", "weald", "sexed", "folic", "poxed", "cunts", "anile", "kiths", "becks", "tatty", "plena", "rebar", "abled", "toyer", "attar", "teaks", "aioli", "awing", "anent", "feces", "redip", "wists", "prats", "mesne", "muter", "smurf", "owest", "bahts", "lossy", "ftped", "hunky", "hoers", "slier", "sicks", "fatly", "delft", "hiver", "himbo", "pengo", "busks", "loxes", "zonks", "ilium", "aport", "ikons", "mulct", "reeve", "civvy", "canna", "barfy", "kaiak", "scudo", "knout", "gaper", "bhang", "pease", "uteri", "lases", "paten", "rasae", "axels", "stoas", "ombre", "styli", "gunky", "hazer", "kenaf", "ahoys", "ammos", "weeny", "urger", "kudzu", "paren", "bolos", "fetor", "nitty", "techy", "lieth", "somas", "darky", "villi", "gluon", "janes", "cants", "farts", "socle", "jinns", "ruing", "slily", "ricer", "hadda", "wowee", "rices", "nerts", "cauls", "swive", "lilty", "micks", "arity", "pasha", "finif", "oinky", "gutty", "tetra", "wises", "wolds", "balds", "picot", "whats", "shiki", "bungs", "snarf", "legos", "dungs", "stogy", "berms", "tangs", "vails", "roods", "morel", "sware", "elans", "latus", "gules", "razer", "doxie", "buena", "overs", "gutta", "zincs", "nates", "kirks", "tikes", "donee", "jerry", "mohel", "ceder", "doges", "unmap", "folia", "rawly", "snark", "topoi", "ceils", "immix", "yores", "diest", "bubba", "pomps", "forky", "turdy", "lawzy", "poohs", "worts", "gloms", "beano", "muley", "barky", "tunny", "auric", "funks", "gaffs", "cordy", "curdy", "lisle", "toric", "soyas", "reman", "mungy", "carpy", "apish", "oaten", "gappy", "aurae", "bract", "rooky", "axled", "burry", "sizer", "proem", "turfy", "impro", "mashy", "miens", "nonny", "olios", "grook", "sates", "agley", "corgi", "dashy", "doser", "dildo", "apsos", "xored", "laker", "playa", "selah", "malty", "dulse", "frigs", "demit", "whoso", "rials", "sawer", "spics", "bedim", "snugs", "fanin", "azoic", "icers", "suers", "wizen", "koine", "topos", "shirr", "rifer", "feral", "laded", "lased", "turds", "swede", "easts", "cozen", "unhit", "pally", "aitch", "sedum", "coper", "ruche", "geeks", "swags", "etext", "algin", "offed", "ninja", "holer", "doter", "toter", "besot", "dicut", "macer", "peens", "pewit", "redox", "poler", "yecch", "fluky", "doeth", "twats", "cruds", "bebug", "bider", "stele", "hexer", "wests", "gluer", "pilau", "abaft", "whelm", "lacer", "inode", "tabus", "gator", "cuing", "refly", "luted", "cukes", "bairn", "bight", "arses", "crump", "loggy", "blini", "spoor", "toyon", "harks", "wazoo", "fenny", "naves", "keyer", "tufas", "morph", "rajas", "typal", "spiff", "oxlip", "unban", "mussy", "finny", "rimer", "login", "molas", "cirri", "huzza", "agone", "unsex", "unwon", "peats", "toile", "zombi", "dewed", "nooky", "alkyl", "ixnay", "dovey", "holey", "cuber", "amyls", "podia", "chino", "apnea", "prims", "lycra", "johns", "primo", "fatwa", "egger", "hempy", "snook", "hying", "fuzed", "barms", "crink", "moots", "yerba", "rhumb", "unarc", "direr", "munge", "eland", "nares", "wrier", "noddy", "atilt", "jukes", "ender", "thens", "unfix", "doggo", "zooks", "diddy", "shmoo", "brusk", "prest", "curer", "pasts", "kelpy", "bocce", "kicky", "taros", "lings", "dicky", "nerdy", "abend", "stela", "biggy", "laved", "baldy", "pubis", "gooks", "wonky", "stied", "hypos", "assed", "spumy", "osier", "roble", "rumba", "biffy", "pupal"])
  # Printing Introduction --------------------------------------------------------
  print("\033[32mWelcome to the Wordle game!")
  print("This was made by Aryan Daga as a part of the Computer Science Project.\033[0m")
  print(" ")
  print("\033[34mMake sure the words you type are of 5 letters. \n⬜ means the letter is not in the word \n🟨 means the letter is in the word but not at the correct position \n🟩 means the letter is in the word at the correct position\033[0m")
  print("")
  gamedesc = ['⬛⬛⬛⬛⬛ - Empty', '⬛⬛⬛⬛⬛ - Empty', '⬛⬛⬛⬛⬛ - Empty', '⬛⬛⬛⬛⬛ - Empty', '⬛⬛⬛⬛⬛ - Empty', '⬛⬛⬛⬛⬛ - Empty']
  options = {'yellow': '🟨', 'grey': '⬜', 'green': '🟩', 'black': '⬛'}
  print("\n".join(gamedesc))
  answer = word
  word = [x for x in word]
  # Inputting guess --------------------------------------------------------------
  def inputword():
    while True:
      global guess
      guess = input('Enter your guess: ').lower()
      if len(guess) == 5:
        break
      else:
        print('\033[31mPlease input a 5 letter word!\033[0m\n')
  # Looping the turn and changing colours
  for i in range(6):
    result = ''
    inputword()
    guess = [x for x in guess]
    for j in range(len(guess)):
      if guess[j] == word[j]:
        result += options['green']
      elif guess[j] in word:
        result += options['yellow']
      else:
        result += options['grey']
    gamedesc[i] = result + ' - ' + "".join(guess)
    print("\n".join(gamedesc))
    if result == '🟩🟩🟩🟩🟩':
      print('Congratulations you got the word -', answer)
      break
  else:
    print('You lost, the word was', answer)

if game == "gtn": # Guess The Numbers ------------------------------------------------------------------------------------------------------------------------------------------
  # Printing Introduction --------------------------------------------------------
  print("\033[32mWelcome to the Guess the Number game!")
  print("This was made by Aman Sinha as a part of the Computer Science Project.\033[0m")
  print(" ")
  while True:
      try:
        rangefornum = int(input(f'Choose the range you want to keep for this game like 100 or 1000: '))
        break
      except ValueError:
        print('\033[31mPlease enter a valid number!\033[0m\n')
  corrg = random.randint(1,rangefornum)
  #print(corrg)
  for i in range(9,-1,-1):
    while True:
      try:
        guessg = int(input(f'Choose a number between 1 to {rangefornum}, you have {i+1} tries remaining: '))
        if 0 < guessg < rangefornum:
          break
        else:
          print(f'\033[31mPlease enter a valid number from 1 to {rangefornum}!\033[0m\n')
      except ValueError:
        print(f'\033[31mPlease enter a valid number from 1 to {rangefornum}!\033[0m\n')
    if guessg == corrg:
      print(f'\033[32mCongratulations! You guessed the number correctly in {10-i} tries!\033[0m\n')
      break
    elif guessg > corrg:
      print(f'\033[31m{guessg} is greater than the number you need to guess!\033[0m\n')
    elif guessg < corrg:
      print(f'\033[31m{guessg} is smaller than the number you need to guess!\033[0m\n')
  else:
    print(f'\033[31mYou lost the game! The number was {corrg}\033[0m')

if game == "gtf": # Guess The Flag ------------------------------------------------------------------------------------------------------------------------------------------
  # Printing Introduction --------------------------------------------------------
  print("\033[32mWelcome to the Guess the Flag game!")
  print("This was made by Aryan Daga as a part of the Computer Science Project.\033[0m")
  print(" ")

  # Data of countries ------------------------------------------------------------
  country = [{"id":4,"alpha2":"af","alpha3":"afg","ar":"أفغانستان","bg":"Афганистан","cs":"Afghánistán","da":"Afghanistan","de":"Afghanistan","el":"Αφγανιστάν","en":"Afghanistan","eo":"Afganio","es":"Afganistán","et":"Afganistan","eu":"Afganistan","fi":"Afganistan","fr":"Afghanistan","hu":"Afganisztán","hy":"Աֆղանստան","it":"Afghanistan","ja":"アフガニスタン","ko":"아프가니스탄","lt":"Afganistanas","nl":"Afghanistan","no":"Afghanistan","pl":"Afganistan","pt":"Afeganistão","ro":"Afganistan","ru":"Афганистан","sk":"Afganistan","sv":"Afghanistan","th":"อัฟกานิสถาน","uk":"Афганістан","zh":"阿富汗","zh-tw":"阿富汗"},
  {"id":8,"alpha2":"al","alpha3":"alb","ar":"ألبانيا","bg":"Албания","cs":"Albánie","da":"Albanien","de":"Albanien","el":"Αλβανία","en":"Albania","eo":"Albanio","es":"Albania","et":"Albaania","eu":"Albania","fi":"Albania","fr":"Albanie","hu":"Albánia","hy":"Ալբանիա","it":"Albania","ja":"アルバニア","ko":"알바니아","lt":"Albanija","nl":"Albanië","no":"Albania","pl":"Albania","pt":"Albânia","ro":"Albania","ru":"Албания","sk":"Albánsko","sv":"Albanien","th":"แอลเบเนีย","uk":"Албанія","zh":"阿尔巴尼亚","zh-tw":"阿爾巴尼亞"},
  {"id":12,"alpha2":"dz","alpha3":"dza","ar":"الجزائر","bg":"Алжир","cs":"Alžírsko","da":"Algeriet","de":"Algerien","el":"Αλγερία","en":"Algeria","eo":"Alĝerio","es":"Argelia","et":"Alžeeria","eu":"Aljeria","fi":"Algeria","fr":"Algérie","hu":"Algéria","hy":"Ալժիր","it":"Algeria","ja":"アルジェリア","ko":"알제리","lt":"Alžyras","nl":"Algerije","no":"Algerie","pl":"Algieria","pt":"Argélia","ro":"Algeria","ru":"Алжир","sk":"Alžírsko","sv":"Algeriet","th":"แอลจีเรีย","uk":"Алжир","zh":"阿尔及利亚","zh-tw":"阿爾及利亞"},
  {"id":20,"alpha2":"ad","alpha3":"and","ar":"أندورا","bg":"Андора","cs":"Andorra","da":"Andorra","de":"Andorra","el":"Ανδόρρα","en":"Andorra","eo":"Andoro","es":"Andorra","et":"Andorra","eu":"Andorra","fi":"Andorra","fr":"Andorre","hu":"Andorra","hy":"Անդորրա","it":"Andorra","ja":"アンドラ","ko":"안도라","lt":"Andora","nl":"Andorra","no":"Andorra","pl":"Andora","pt":"Andorra","ro":"Andorra","ru":"Андорра","sk":"Andorra","sv":"Andorra","th":"อันดอร์รา","uk":"Андорра","zh":"安道尔","zh-tw":"安道爾"},
  {"id":24,"alpha2":"ao","alpha3":"ago","ar":"أنغولا","bg":"Ангола","cs":"Angola","da":"Angola","de":"Angola","el":"Ανγκόλα","en":"Angola","eo":"Angolo","es":"Angola","et":"Angola","eu":"Angola","fi":"Angola","fr":"Angola","hu":"Angola","hy":"Անգոլա","it":"Angola","ja":"アンゴラ","ko":"앙골라","lt":"Angola","nl":"Angola","no":"Angola","pl":"Angola","pt":"Angola","ro":"Angola","ru":"Ангола","sk":"Angola","sv":"Angola","th":"แองโกลา","uk":"Ангола","zh":"安哥拉","zh-tw":"安哥拉"},
  {"id":28,"alpha2":"ag","alpha3":"atg","ar":"أنتيغوا وباربودا","bg":"Антигуа и Барбуда","cs":"Antigua a Barbuda","da":"Antigua og Barbuda","de":"Antigua und Barbuda","el":"Αντίγκουα και Μπαρμπούντα","en":"Antigua and Barbuda","eo":"Antigvo kaj Barbudo","es":"Antigua y Barbuda","et":"Antigua ja Barbuda","eu":"Antigua eta Barbuda","fi":"Antigua ja Barbuda","fr":"Antigua-et-Barbuda","hu":"Antigua és Barbuda","hy":"Անտիգուա և Բարբուդա","it":"Antigua e Barbuda","ja":"アンティグア・バーブーダ","ko":"앤티가 바부다","lt":"Antigva ir Barbuda","nl":"Antigua en Barbuda","no":"Antigua og Barbuda","pl":"Antigua i Barbuda","pt":"Antígua e Barbuda","ro":"Antigua și Barbuda","ru":"Антигуа и Барбуда","sk":"Antigua a Barbuda","sv":"Antigua och Barbuda","th":"แอนทีกาและบาร์บิวดา","uk":"Антигуа і Барбуда","zh":"安提瓜和巴布达","zh-tw":"安地卡及巴布達"},
  {"id":32,"alpha2":"ar","alpha3":"arg","ar":"الأرجنتين","bg":"Аржентина","cs":"Argentina","da":"Argentina","de":"Argentinien","el":"Αργεντινή","en":"Argentina","eo":"Argentino","es":"Argentina","et":"Argentina","eu":"Argentina","fi":"Argentiina","fr":"Argentine","hu":"Argentína","hy":"Արգենտինա","it":"Argentina","ja":"アルゼンチン","ko":"아르헨티나","lt":"Argentina","nl":"Argentinië","no":"Argentina","pl":"Argentyna","pt":"Argentina","ro":"Argentina","ru":"Аргентина","sk":"Argentína","sv":"Argentina","th":"อาร์เจนตินา","uk":"Аргентина","zh":"阿根廷","zh-tw":"阿根廷"},
  {"id":51,"alpha2":"am","alpha3":"arm","ar":"أرمينيا","bg":"Армения","cs":"Arménie","da":"Armenien","de":"Armenien","el":"Αρμενία","en":"Armenia","eo":"Armenio","es":"Armenia","et":"Armeenia","eu":"Armenia","fi":"Armenia","fr":"Arménie","hu":"Örményország","hy":"Հայաստան","it":"Armenia","ja":"アルメニア","ko":"아르메니아","lt":"Armėnija","nl":"Armenië","no":"Armenia","pl":"Armenia","pt":"Armênia","ro":"Armenia","ru":"Армения","sk":"Arménsko","sv":"Armenien","th":"อาร์มีเนีย","uk":"Вірменія","zh":"亚美尼亚","zh-tw":"亞美尼亞"},
  {"id":36,"alpha2":"au","alpha3":"aus","ar":"أستراليا","bg":"Австралия","cs":"Austrálie","da":"Australien","de":"Australien","el":"Αυστραλία","en":"Australia","eo":"Aŭstralio","es":"Australia","et":"Austraalia","eu":"Australia","fi":"Australia","fr":"Australie","hu":"Ausztrália","hy":"Ավստրալիա","it":"Australia","ja":"オーストラリア","ko":"오스트레일리아","lt":"Australija","nl":"Australië","no":"Australia","pl":"Australia","pt":"Austrália","ro":"Australia","ru":"Австралия","sk":"Austrália","sv":"Australien","th":"ออสเตรเลีย","uk":"Австралія","zh":"澳大利亚","zh-tw":"澳大利亞"},
  {"id":40,"alpha2":"at","alpha3":"aut","ar":"النمسا","bg":"Австрия","cs":"Rakousko","da":"Østrig","de":"Österreich","el":"Αυστρία","en":"Austria","eo":"Aŭstrio","es":"Austria","et":"Austria","eu":"Austria","fi":"Itävalta","fr":"Autriche","hu":"Ausztria","hy":"Ավստրիա","it":"Austria","ja":"オーストリア","ko":"오스트리아","lt":"Austrija","nl":"Oostenrijk","no":"Østerrike","pl":"Austria","pt":"Áustria","ro":"Austria","ru":"Австрия","sk":"Rakúsko","sv":"Österrike","th":"ออสเตรีย","uk":"Австрія","zh":"奥地利","zh-tw":"奧地利"},
  {"id":31,"alpha2":"az","alpha3":"aze","ar":"أذربيجان","bg":"Азербайджан","cs":"Ázerbájdžán","da":"Aserbajdsjan","de":"Aserbaidschan","el":"Αζερμπαϊτζάν","en":"Azerbaijan","eo":"Azerbajĝano","es":"Azerbaiyán","et":"Aserbaidžaan","eu":"Azerbaijan","fi":"Azerbaidžan","fr":"Azerbaïdjan","hu":"Azerbajdzsán","hy":"Ադրբեջան","it":"Azerbaigian","ja":"アゼルバイジャン","ko":"아제르바이잔","lt":"Azerbaidžanas","nl":"Azerbeidzjan","no":"Aserbajdsjan","pl":"Azerbejdżan","pt":"Azerbaijão","ro":"Azerbaidjan","ru":"Азербайджан","sk":"Azerbajdžan","sv":"Azerbajdzjan","th":"อาเซอร์ไบจาน","uk":"Азербайджан","zh":"阿塞拜疆","zh-tw":"亞塞拜然"},
  {"id":44,"alpha2":"bs","alpha3":"bhs","ar":"باهاماس","bg":"Бахамски острови","cs":"Bahamy","da":"Bahamas","de":"Bahamas","el":"Μπαχάμες","en":"Bahamas","eo":"Bahamoj","es":"Bahamas","et":"Bahama","eu":"Bahamak","fi":"Bahama","fr":"Bahamas","hu":"Bahama-szigetek","hy":"Բահամներ","it":"Bahamas","ja":"バハマ","ko":"바하마","lt":"Bahamos","nl":"Bahama's","no":"Bahamas","pl":"Bahamy","pt":"Bahamas","ro":"Bahamas","ru":"Багамские Острова","sk":"Bahamy","sv":"Bahamas","th":"บาฮามาส","uk":"Багамські Острови","zh":"巴哈马","zh-tw":"巴哈馬"},
  {"id":48,"alpha2":"bh","alpha3":"bhr","ar":"البحرين","bg":"Бахрейн","cs":"Bahrajn","da":"Bahrain","de":"Bahrain","el":"Μπαχρέιν","en":"Bahrain","eo":"Barejno","es":"Baréin","et":"Bahrein","eu":"Bahrain","fi":"Bahrain","fr":"Bahreïn","hu":"Bahrein","hy":"Բահրեյն","it":"Bahrein","ja":"バーレーン","ko":"바레인","lt":"Bahreinas","nl":"Bahrein","no":"Bahrain","pl":"Bahrajn","pt":"Barém","ro":"Bahrain","ru":"Бахрейн","sk":"Bahrajn","sv":"Bahrain","th":"บาห์เรน","uk":"Бахрейн","zh":"巴林","zh-tw":"巴林"},
  {"id":50,"alpha2":"bd","alpha3":"bgd","ar":"بنغلاديش","bg":"Бангладеш","cs":"Bangladéš","da":"Bangladesh","de":"Bangladesch","el":"Μπανγκλαντές","en":"Bangladesh","eo":"Bangladeŝo","es":"Bangladés","et":"Bangladesh","eu":"Bangladesh","fi":"Bangladesh","fr":"Bangladesh","hu":"Banglades","hy":"Բանգլադեշ","it":"Bangladesh","ja":"バングラデシュ","ko":"방글라데시","lt":"Bangladešas","nl":"Bangladesh","no":"Bangladesh","pl":"Bangladesz","pt":"Bangladexe","ro":"Bangladesh","ru":"Бангладеш","sk":"Bangladéš","sv":"Bangladesh","th":"บังกลาเทศ","uk":"Бангладеш","zh":"孟加拉国","zh-tw":"孟加拉"},
  {"id":52,"alpha2":"bb","alpha3":"brb","ar":"باربادوس","bg":"Барбадос","cs":"Barbados","da":"Barbados","de":"Barbados","el":"Μπαρμπάντος","en":"Barbados","eo":"Barbado","es":"Barbados","et":"Barbados","eu":"Barbados","fi":"Barbados","fr":"Barbade","hu":"Barbados","hy":"Բարբադոս","it":"Barbados","ja":"バルバドス","ko":"바베이도스","lt":"Barbadosas","nl":"Barbados","no":"Barbados","pl":"Barbados","pt":"Barbados","ro":"Barbados","ru":"Барбадос","sk":"Barbados","sv":"Barbados","th":"บาร์เบโดส","uk":"Барбадос","zh":"巴巴多斯","zh-tw":"巴貝多"},
  {"id":112,"alpha2":"by","alpha3":"blr","ar":"بيلاروس","bg":"Беларус","cs":"Bělorusko","da":"Hviderusland","de":"Belarus","el":"Λευκορωσία","en":"Belarus","eo":"Belorusio","es":"Bielorrusia","et":"Valgevene","eu":"Bielorrusia","fi":"Valko-Venäjä","fr":"Biélorussie","hu":"Fehéroroszország","hy":"Բելառուս","it":"Bielorussia","ja":"ベラルーシ","ko":"벨라루스","lt":"Baltarusija","nl":"Wit-Rusland","no":"Belarus","pl":"Białoruś","pt":"Bielorrússia","ro":"Belarus","ru":"Белоруссия","sk":"Bielorusko","sv":"Belarus","th":"เบลารุส","uk":"Білорусь","zh":"白俄罗斯","zh-tw":"白俄羅斯"},
  {"id":56,"alpha2":"be","alpha3":"bel","ar":"بلجيكا","bg":"Белгия","cs":"Belgie","da":"Belgien","de":"Belgien","el":"Βέλγιο","en":"Belgium","eo":"Belgio","es":"Bélgica","et":"Belgia","eu":"Belgika","fi":"Belgia","fr":"Belgique","hu":"Belgium","hy":"Բելգիա","it":"Belgio","ja":"ベルギー","ko":"벨기에","lt":"Belgija","nl":"België","no":"Belgia","pl":"Belgia","pt":"Bélgica","ro":"Belgia","ru":"Бельгия","sk":"Belgicko","sv":"Belgien","th":"เบลเยียม","uk":"Бельгія","zh":"比利时","zh-tw":"比利時"},
  {"id":84,"alpha2":"bz","alpha3":"blz","ar":"بليز","bg":"Белиз","cs":"Belize","da":"Belize","de":"Belize","el":"Μπελίζ","en":"Belize","eo":"Belizo","es":"Belice","et":"Belize","eu":"Belize","fi":"Belize","fr":"Belize","hu":"Belize","hy":"Բելիզ","it":"Belize","ja":"ベリーズ","ko":"벨리즈","lt":"Belizas","nl":"Belize","no":"Belize","pl":"Belize","pt":"Belize","ro":"Belize","ru":"Белиз","sk":"Belize","sv":"Belize","th":"เบลีซ","uk":"Беліз","zh":"伯利兹","zh-tw":"貝里斯"},
  {"id":204,"alpha2":"bj","alpha3":"ben","ar":"بنين","bg":"Бенин","cs":"Benin","da":"Benin","de":"Benin","el":"Μπενίν","en":"Benin","eo":"Benino","es":"Benín","et":"Benin","eu":"Benin","fi":"Benin","fr":"Bénin","hu":"Benin","hy":"Բենին","it":"Benin","ja":"ベナン","ko":"베냉","lt":"Beninas","nl":"Benin","no":"Benin","pl":"Benin","pt":"Benim","ro":"Benin","ru":"Бенин","sk":"Benin","sv":"Benin","th":"เบนิน","uk":"Бенін","zh":"贝宁","zh-tw":"貝南"},
  {"id":64,"alpha2":"bt","alpha3":"btn","ar":"بوتان","bg":"Бутан","cs":"Bhútán","da":"Bhutan","de":"Bhutan","el":"Μπουτάν","en":"Bhutan","eo":"Butano","es":"Bután","et":"Bhutan","eu":"Bhutan","fi":"Bhutan","fr":"Bhoutan","hu":"Bhután","hy":"Բութան","it":"Bhutan","ja":"ブータン","ko":"부탄","lt":"Butanas","nl":"Bhutan","no":"Bhutan","pl":"Bhutan","pt":"Butão","ro":"Bhutan","ru":"Бутан","sk":"Bhután","sv":"Bhutan","th":"ภูฏาน","uk":"Бутан","zh":"不丹","zh-tw":"不丹"},
  {"id":68,"alpha2":"bo","alpha3":"bol","ar":"بوليفيا","bg":"Боливия","cs":"Bolívie","da":"Bolivia","de":"Bolivien","el":"Βολιβία","en":"Bolivia (Plurinational State of)","eo":"Bolivio","es":"Bolivia","et":"Boliivia","eu":"Bolivia","fi":"Bolivia","fr":"Bolivie","hu":"Bolívia","hy":"Բոլիվիա","it":"Bolivia","ja":"ボリビア多民族国","ko":"볼리비아","lt":"Bolivija","nl":"Bolivia","no":"Bolivia","pl":"Boliwia","pt":"Bolívia","ro":"Bolivia","ru":"Боливия","sk":"Bolívia","sv":"Bolivia","th":"โบลิเวีย","uk":"Болівія","zh":"玻利维亚","zh-tw":"玻利維亞"},
  {"id":70,"alpha2":"ba","alpha3":"bih","ar":"البوسنة والهرسك","bg":"Босна и Херцеговина","cs":"Bosna a Hercegovina","da":"Bosnien-Hercegovina","de":"Bosnien und Herzegowina","el":"Βοσνία-Ερζεγοβίνη","en":"Bosnia and Herzegovina","eo":"Bosnio kaj Hercegovino","es":"Bosnia y Herzegovina","et":"Bosnia ja Hertsegoviina","eu":"Bosnia-Herzegovina","fi":"Bosnia ja Hertsegovina","fr":"Bosnie-Herzégovine","hu":"Bosznia-Hercegovina","hy":"Բոսնիա և Հերցեգովինա","it":"Bosnia ed Erzegovina","ja":"ボスニア・ヘルツェゴビナ","ko":"보스니아 헤르체고비나","lt":"Bosnija ir Hercegovina","nl":"Bosnië en Herzegovina","no":"Bosnia-Hercegovina","pl":"Bośnia i Hercegowina","pt":"Bósnia e Herzegovina","ro":"Bosnia și Herțegovina","ru":"Босния и Герцеговина","sk":"Bosna a Hercegovina","sv":"Bosnien och Hercegovina","th":"บอสเนียและเฮอร์เซโกวีนา","uk":"Боснія і Герцеговина","zh":"波黑","zh-tw":"波士尼亞與赫塞哥維納"},
  {"id":72,"alpha2":"bw","alpha3":"bwa","ar":"بوتسوانا","bg":"Ботсвана","cs":"Botswana","da":"Botswana","de":"Botswana","el":"Μποτσουάνα","en":"Botswana","eo":"Bocvano","es":"Botsuana","et":"Botswana","eu":"Botswana","fi":"Botswana","fr":"Botswana","hu":"Botswana","hy":"Բոտսվանա","it":"Botswana","ja":"ボツワナ","ko":"보츠와나","lt":"Botsvana","nl":"Botswana","no":"Botswana","pl":"Botswana","pt":"Botsuana","ro":"Botswana","ru":"Ботсвана","sk":"Botswana","sv":"Botswana","th":"บอตสวานา","uk":"Ботсвана","zh":"博茨瓦纳","zh-tw":"波札那"},
  {"id":76,"alpha2":"br","alpha3":"bra","ar":"البرازيل","bg":"Бразилия","cs":"Brazílie","da":"Brasilien","de":"Brasilien","el":"Βραζιλία","en":"Brazil","eo":"Brazilo","es":"Brasil","et":"Brasiilia","eu":"Brasil","fi":"Brasilia","fr":"Brésil","hu":"Brazília","hy":"Բրազիլիա","it":"Brasile","ja":"ブラジル","ko":"브라질","lt":"Brazilija","nl":"Brazilië","no":"Brasil","pl":"Brazylia","pt":"Brasil","ro":"Brazilia","ru":"Бразилия","sk":"Brazília","sv":"Brasilien","th":"บราซิล","uk":"Бразилія","zh":"巴西","zh-tw":"巴西"},
  {"id":96,"alpha2":"bn","alpha3":"brn","ar":"بروناي","bg":"Бруней","cs":"Brunej","da":"Brunei","de":"Brunei","el":"Μπρουνέι","en":"Brunei Darussalam","eo":"Brunejo","es":"Brunéi","et":"Brunei","eu":"Brunei","fi":"Brunei","fr":"Brunei","hu":"Brunei","hy":"Բրունեյ","it":"Brunei","ja":"ブルネイ・ダルサラーム","ko":"브루나이","lt":"Brunėjus","nl":"Brunei","no":"Brunei","pl":"Brunei","pt":"Brunei","ro":"Brunei","ru":"Бруней","sk":"Brunej","sv":"Brunei","th":"บรูไน","uk":"Бруней","zh":"文莱","zh-tw":"汶萊"},
  {"id":100,"alpha2":"bg","alpha3":"bgr","ar":"بلغاريا","bg":"България","cs":"Bulharsko","da":"Bulgarien","de":"Bulgarien","el":"Βουλγαρία","en":"Bulgaria","eo":"Bulgario","es":"Bulgaria","et":"Bulgaaria","eu":"Bulgaria","fi":"Bulgaria","fr":"Bulgarie","hu":"Bulgária","hy":"Բուլղարիա","it":"Bulgaria","ja":"ブルガリア","ko":"불가리아","lt":"Bulgarija","nl":"Bulgarije","no":"Bulgaria","pl":"Bułgaria","pt":"Bulgária","ro":"Bulgaria","ru":"Болгария","sk":"Bulharsko","sv":"Bulgarien","th":"บัลแกเรีย","uk":"Болгарія","zh":"保加利亚","zh-tw":"保加利亞"},
  {"id":854,"alpha2":"bf","alpha3":"bfa","ar":"بوركينا فاسو","bg":"Буркина Фасо","cs":"Burkina Faso","da":"Burkina Faso","de":"Burkina Faso","el":"Μπουρκίνα Φάσο","en":"Burkina Faso","eo":"Burkino","es":"Burkina Faso","et":"Burkina Faso","eu":"Burkina Faso","fi":"Burkina Faso","fr":"Burkina Faso","hu":"Burkina Faso","hy":"Բուրկինա Ֆասո","it":"Burkina Faso","ja":"ブルキナファソ","ko":"부르키나파소","lt":"Burkina Faso","nl":"Burkina Faso","no":"Burkina Faso","pl":"Burkina Faso","pt":"Burquina Fasso","ro":"Burkina Faso","ru":"Буркина-Фасо","sk":"Burkina","sv":"Burkina Faso","th":"บูร์กินาฟาโซ","uk":"Буркіна-Фасо","zh":"布基纳法索","zh-tw":"布吉納法索"},
  {"id":108,"alpha2":"bi","alpha3":"bdi","ar":"بوروندي","bg":"Бурунди","cs":"Burundi","da":"Burundi","de":"Burundi","el":"Μπουρούντι","en":"Burundi","eo":"Burundo","es":"Burundi","et":"Burundi","eu":"Burundi","fi":"Burundi","fr":"Burundi","hu":"Burundi","hy":"Բուրունդի","it":"Burundi","ja":"ブルンジ","ko":"부룬디","lt":"Burundis","nl":"Burundi","no":"Burundi","pl":"Burundi","pt":"Burundi","ro":"Burundi","ru":"Бурунди","sk":"Burundi","sv":"Burundi","th":"บุรุนดี","uk":"Бурунді","zh":"布隆迪","zh-tw":"蒲隆地"},
  {"id":116,"alpha2":"kh","alpha3":"khm","ar":"كمبوديا","bg":"Камбоджа","cs":"Kambodža","da":"Cambodja","de":"Kambodscha","el":"Καμπότζη","en":"Cambodia","eo":"Kamboĝo","es":"Camboya","et":"Kambodža","eu":"Kanbodia","fi":"Kambodža","fr":"Cambodge","hu":"Kambodzsa","hy":"Կամբոջա","it":"Cambogia","ja":"カンボジア","ko":"캄보디아","lt":"Kambodža","nl":"Cambodja","no":"Kambodsja","pl":"Kambodża","pt":"Camboja","ro":"Cambodgia","ru":"Камбоджа","sk":"Kambodža","sv":"Kambodja","th":"กัมพูชา","uk":"Камбоджа","zh":"柬埔寨","zh-tw":"柬埔寨"},
  {"id":120,"alpha2":"cm","alpha3":"cmr","ar":"الكاميرون","bg":"Камерун","cs":"Kamerun","da":"Cameroun","de":"Kamerun","el":"Καμερούν","en":"Cameroon","eo":"Kameruno","es":"Camerún","et":"Kamerun","eu":"Kamerun","fi":"Kamerun","fr":"Cameroun","hu":"Kamerun","hy":"Կամերուն","it":"Camerun","ja":"カメルーン","ko":"카메룬","lt":"Kamerūnas","nl":"Kameroen","no":"Kamerun","pl":"Kamerun","pt":"Camarões","ro":"Camerun","ru":"Камерун","sk":"Kamerun","sv":"Kamerun","th":"แคเมอรูน","uk":"Камерун","zh":"喀麦隆","zh-tw":"喀麥隆"},
  {"id":124,"alpha2":"ca","alpha3":"can","ar":"كندا","bg":"Канада","cs":"Kanada","da":"Canada","de":"Kanada","el":"Καναδάς","en":"Canada","eo":"Kanado","es":"Canadá","et":"Kanada","eu":"Kanada","fi":"Kanada","fr":"Canada","hu":"Kanada","hy":"Կանադա","it":"Canada","ja":"カナダ","ko":"캐나다","lt":"Kanada","nl":"Canada","no":"Canada","pl":"Kanada","pt":"Canadá","ro":"Canada","ru":"Канада","sk":"Kanada","sv":"Kanada","th":"แคนาดา","uk":"Канада","zh":"加拿大","zh-tw":"加拿大"},
  {"id":132,"alpha2":"cv","alpha3":"cpv","ar":"الرأس الأخضر","bg":"Кабо Верде","cs":"Kapverdy","da":"Kap Verde","de":"Kap Verde","el":"Πράσινο Ακρωτήρι","en":"Cabo Verde","eo":"Kaboverdo","es":"Cabo Verde","et":"Roheneemesaared","eu":"Cabo Verde","fi":"Kap Verde","fr":"Cap-Vert","hu":"Zöld-foki Köztársaság","hy":"Կաբո Վերդե","it":"Capo Verde","ja":"カーボベルデ","ko":"카보베르데","lt":"Žaliasis Kyšulys","nl":"Kaapverdië","no":"Kapp Verde","pl":"Republika Zielonego Przylądka","pt":"Cabo Verde","ro":"Republica Capului Verde","ru":"Кабо-Верде","sk":"Kapverdy","sv":"Kap Verde","th":"กาบูเวร์ดี","uk":"Кабо-Верде","zh":"佛得角","zh-tw":"維德角"},
  {"id":140,"alpha2":"cf","alpha3":"caf","ar":"جمهورية أفريقيا الوسطى","bg":"Централноафриканска република","cs":"Středoafrická republika","da":"Centralafrikanske Republik","de":"Zentralafrikanische Republik","el":"Κεντροαφρικανική Δημοκρατία","en":"Central African Republic","eo":"Centr-Afrika Respubliko","es":"República Centroafricana","et":"Kesk-Aafrika Vabariik","eu":"Afrika Erdiko Errepublika","fi":"Keski-Afrikan tasavalta","fr":"République centrafricaine","hu":"Közép-Afrika","hy":"Կենտրոնաաֆրիկյան Հանրապետություն","it":"Rep. Centrafricana","ja":"中央アフリカ共和国","ko":"중앙아프리카 공화국","lt":"Centrinės Afrikos Respublika","nl":"Centraal-Afrikaanse Republiek","no":"Den sentralafrikanske republikk","pl":"Republika Środkowoafrykańska","pt":"República Centro-Africana","ro":"Republica Centrafricană","ru":"ЦАР","sk":"Stredoafrická republika","sv":"Centralafrikanska republiken","th":"สาธารณรัฐแอฟริกากลาง","uk":"Центральноафриканська Республіка","zh":"中非","zh-tw":"中非"},
  {"id":148,"alpha2":"td","alpha3":"tcd","ar":"تشاد","bg":"Чад","cs":"Čad","da":"Tchad","de":"Tschad","el":"Τσαντ","en":"Chad","eo":"Ĉado","es":"Chad","et":"Tšaad","eu":"Txad","fi":"Tšad","fr":"Tchad","hu":"Csád","hy":"Չադ","it":"Ciad","ja":"チャド","ko":"차드","lt":"Čadas","nl":"Tsjaad","no":"Tsjad","pl":"Czad","pt":"Chade","ro":"Ciad","ru":"Чад","sk":"Čad","sv":"Tchad","th":"ชาด","uk":"Чад","zh":"乍得","zh-tw":"查德"},
  {"id":152,"alpha2":"cl","alpha3":"chl","ar":"تشيلي","bg":"Чили","cs":"Chile","da":"Chile","de":"Chile","el":"Χιλή","en":"Chile","eo":"Ĉilio","es":"Chile","et":"Tšiili","eu":"Txile","fi":"Chile","fr":"Chili","hu":"Chile","hy":"Չիլի","it":"Cile","ja":"チリ","ko":"칠레","lt":"Čilė","nl":"Chili","no":"Chile","pl":"Chile","pt":"Chile","ro":"Chile","ru":"Чили","sk":"Čile","sv":"Chile","th":"ชิลี","uk":"Чилі","zh":"智利","zh-tw":"智利"},
  {"id":156,"alpha2":"cn","alpha3":"chn","ar":"الصين","bg":"Китай","cs":"Čína","da":"Kina","de":"Volksrepublik China","el":"Κίνα","en":"China","eo":"Ĉinio","es":"China","et":"Hiina","eu":"Txina","fi":"Kiina","fr":"Chine","hu":"Kína","hy":"Չինաստան","it":"Cina","ja":"中華人民共和国","ko":"중국","lt":"Kinija","nl":"China","no":"Kina","pl":"Chiny","pt":"China","ro":"Republica Populară Chineză","ru":"Китай (Китайская Народная Республика)","sk":"Čína","sv":"Kina","th":"จีน","uk":"Китайська Народна Республіка","zh":"中国","zh-tw":"中國"},
  {"id":170,"alpha2":"co","alpha3":"col","ar":"كولومبيا","bg":"Колумбия","cs":"Kolumbie","da":"Colombia","de":"Kolumbien","el":"Κολομβία","en":"Colombia","eo":"Kolombio","es":"Colombia","et":"Colombia","eu":"Kolonbia","fi":"Kolumbia","fr":"Colombie","hu":"Kolumbia","hy":"Կոլումբիա","it":"Colombia","ja":"コロンビア","ko":"콜롬비아","lt":"Kolumbija","nl":"Colombia","no":"Colombia","pl":"Kolumbia","pt":"Colômbia","ro":"Columbia","ru":"Колумбия","sk":"Kolumbia","sv":"Colombia","th":"โคลอมเบีย","uk":"Колумбія","zh":"哥伦比亚","zh-tw":"哥倫比亞"},
  {"id":174,"alpha2":"km","alpha3":"com","ar":"جزر القمر","bg":"Коморски острови","cs":"Komory","da":"Comorerne","de":"Komoren","el":"Κομόρες","en":"Comoros","eo":"Komoroj","es":"Comoras","et":"Komoorid","eu":"Komoreak","fi":"Komorit","fr":"Comores","hu":"Comore-szigetek","hy":"Կոմորներ","it":"Comore","ja":"コモロ","ko":"코모로","lt":"Komorai","nl":"Comoren","no":"Komorene","pl":"Komory","pt":"Comores","ro":"Comore","ru":"Коморы","sk":"Komory","sv":"Komorerna","th":"คอโมโรส","uk":"Коморські Острови","zh":"科摩罗","zh-tw":"葛摩"},
  {"id":178,"alpha2":"cg","alpha3":"cog","ar":"جمهورية الكونغو","bg":"Република Конго","cs":"Kongo","da":"Congo","de":"Kongo, Republik","el":"Κογκό","en":"Congo","eo":"Respubliko Kongo","es":"República del Congo","et":"Kongo Vabariik","eu":"Kongoko Errepublika","fi":"Kongon tasavalta","fr":"République du Congo","hu":"Kongói Köztársaság (Kongó)","hy":"Կոնգոյի Հանրապետություն","it":"Rep. del Congo","ja":"コンゴ共和国","ko":"콩고 공화국","lt":"Kongo Respublika","nl":"Congo-Brazzaville","no":"Kongo, Republikken","pl":"Kongo","pt":"República do Congo","ro":"Congo","ru":"Республика Конго","sk":"Kongo","sv":"Kongo-Brazzaville","th":"สาธารณรัฐคองโก","uk":"Республіка Конго","zh":"刚果共和国","zh-tw":"剛果共和國"},
  {"id":180,"alpha2":"cd","alpha3":"cod","ar":"جمهورية الكونغو الديمقراطية","bg":"Демократична република Конго","cs":"Konžská demokratická republika","da":"Demokratiske Republik Congo","de":"Kongo, Demokratische Republik","el":"Λαϊκή Δημοκρατία του Κογκό","en":"Congo, Democratic Republic of the","eo":"Demokratia Respubliko Kongo","es":"República Democrática del Congo","et":"Kongo Demokraatlik Vabariik","eu":"Kongoko Errepublika Demokratikoa","fi":"Kongon demokraattinen tasavalta","fr":"République démocratique du Congo","hu":"Kongói Demokratikus Köztársaság (Zaire)","hy":"Կոնգոյի Դեմոկրատական Հանրապետություն","it":"RD del Congo","ja":"コンゴ民主共和国","ko":"콩고 민주 공화국","lt":"Kongo Demokratinė Respublika","nl":"Congo-Kinshasa","no":"Kongo, Den demokratiske republikken","pl":"Demokratyczna Republika Konga","pt":"República Democrática do Congo","ro":"Republica Democrată Congo","ru":"ДР Конго","sk":"Konžská demokratická republika","sv":"Kongo-Kinshasa","th":"สาธารณรัฐประชาธิปไตยคองโก","uk":"ДР Конго","zh":"刚果民主共和国","zh-tw":"剛果民主共和國"},
  {"id":188,"alpha2":"cr","alpha3":"cri","ar":"كوستاريكا","bg":"Коста Рика","cs":"Kostarika","da":"Costa Rica","de":"Costa Rica","el":"Κόστα Ρίκα","en":"Costa Rica","eo":"Kostariko","es":"Costa Rica","et":"Costa Rica","eu":"Costa Rica","fi":"Costa Rica","fr":"Costa Rica","hu":"Costa Rica","hy":"Կոստա Ռիկա","it":"Costa Rica","ja":"コスタリカ","ko":"코스타리카","lt":"Kosta Rika","nl":"Costa Rica","no":"Costa Rica","pl":"Kostaryka","pt":"Costa Rica","ro":"Costa Rica","ru":"Коста-Рика","sk":"Kostarika","sv":"Costa Rica","th":"คอสตาริกา","uk":"Коста-Рика","zh":"哥斯达黎加","zh-tw":"哥斯大黎加"},
  {"id":384,"alpha2":"ci","alpha3":"civ","ar":"ساحل العاج","bg":"Кот д'Ивоар","cs":"Pobřeží slonoviny","da":"Elfenbenskysten","de":"Elfenbeinküste","el":"Ακτή Ελεφαντοστού","en":"Côte d'Ivoire","eo":"Ebura Bordo","es":"Costa de Marfil","et":"Elevandiluurannik","eu":"Boli Kosta","fi":"Norsunluurannikko","fr":"Côte d'Ivoire","hu":"Elefántcsontpart","hy":"Կոտ դ'Իվուար","it":"Costa d'Avorio","ja":"コートジボワール","ko":"코트디부아르","lt":"Dramblio Kaulo Krantas","nl":"Ivoorkust","no":"Elfenbenskysten","pl":"Wybrzeże Kości Słoniowej","pt":"Costa do Marfim","ro":"Coasta de Fildeș","ru":"Кот-д’Ивуар","sk":"Pobrežie Slonoviny","sv":"Elfenbenskusten","th":"โกตดิวัวร์","uk":"Кот-д'Івуар","zh":"科特迪瓦","zh-tw":"象牙海岸"},
  {"id":191,"alpha2":"hr","alpha3":"hrv","ar":"كرواتيا","bg":"Хърватия","cs":"Chorvatsko","da":"Kroatien","de":"Kroatien","el":"Κροατία","en":"Croatia","eo":"Kroatio","es":"Croacia","et":"Horvaatia","eu":"Kroazia","fi":"Kroatia","fr":"Croatie","hu":"Horvátország","hy":"Խորվաթիա","it":"Croazia","ja":"クロアチア","ko":"크로아티아","lt":"Kroatija","nl":"Kroatië","no":"Kroatia","pl":"Chorwacja","pt":"Croácia","ro":"Croația","ru":"Хорватия","sk":"Chorvátsko","sv":"Kroatien","th":"โครเอเชีย","uk":"Хорватія","zh":"克罗地亚","zh-tw":"克羅埃西亞"},
  {"id":192,"alpha2":"cu","alpha3":"cub","ar":"كوبا","bg":"Куба","cs":"Kuba","da":"Cuba","de":"Kuba","el":"Κούβα","en":"Cuba","eo":"Kubo","es":"Cuba","et":"Kuuba","eu":"Kuba","fi":"Kuuba","fr":"Cuba","hu":"Kuba","hy":"Կուբա","it":"Cuba","ja":"キューバ","ko":"쿠바","lt":"Kuba","nl":"Cuba","no":"Cuba","pl":"Kuba","pt":"Cuba","ro":"Cuba","ru":"Куба","sk":"Kuba","sv":"Kuba","th":"คิวบา","uk":"Куба","zh":"古巴","zh-tw":"古巴"},
  {"id":196,"alpha2":"cy","alpha3":"cyp","ar":"قبرص","bg":"Кипър","cs":"Kypr","da":"Cypern","de":"Zypern","el":"Κύπρος","en":"Cyprus","eo":"Kipro","es":"Chipre","et":"Küpros","eu":"Zipre","fi":"Kypros","fr":"Chypre","hu":"Ciprus","hy":"Կիպրոս","it":"Cipro","ja":"キプロス","ko":"키프로스","lt":"Kipras","nl":"Cyprus","no":"Kypros","pl":"Cypr","pt":"Chipre","ro":"Cipru","ru":"Кипр","sk":"Cyprus","sv":"Cypern","th":"ไซปรัส","uk":"Кіпр","zh":"塞浦路斯","zh-tw":"賽普勒斯"},
  {"id":203,"alpha2":"cz","alpha3":"cze","ar":"جمهورية التشيك","bg":"Чехия","cs":"Česko","da":"Tjekkiet","de":"Tschechien","el":"Τσεχία","en":"Czechia","eo":"Ĉeĥio","es":"República Checa","et":"Tšehhi","eu":"Txekia","fi":"Tšekki","fr":"Tchéquie","hu":"Csehország","hy":"Չեխիա","it":"Rep. Ceca","ja":"チェコ","ko":"체코","lt":"Čekija","nl":"Tsjechië","no":"Tsjekkia","pl":"Czechy","pt":"Chéquia","ro":"Cehia","ru":"Чехия","sk":"Česko","sv":"Tjeckien","th":"เช็กเกีย","uk":"Чехія","zh":"捷克","zh-tw":"捷克"},
  {"id":208,"alpha2":"dk","alpha3":"dnk","ar":"الدنمارك","bg":"Дания","cs":"Dánsko","da":"Danmark","de":"Dänemark","el":"Δανία","en":"Denmark","eo":"Danio","es":"Dinamarca","et":"Taani","eu":"Danimarka","fi":"Tanska","fr":"Danemark","hu":"Dánia","hy":"Դանիա","it":"Danimarca","ja":"デンマーク","ko":"덴마크","lt":"Danija","nl":"Denemarken","no":"Danmark","pl":"Dania","pt":"Dinamarca","ro":"Danemarca","ru":"Дания","sk":"Dánsko","sv":"Danmark","th":"เดนมาร์ก","uk":"Данія","zh":"丹麦","zh-tw":"丹麥"},
  {"id":262,"alpha2":"dj","alpha3":"dji","ar":"جيبوتي","bg":"Джибути","cs":"Džibutsko","da":"Djibouti","de":"Dschibuti","el":"Τζιμπουτί","en":"Djibouti","eo":"Ĝibutio","es":"Yibuti","et":"Djibouti","eu":"Djibuti","fi":"Djibouti","fr":"Djibouti","hu":"Dzsibuti","hy":"Ջիբութի","it":"Gibuti","ja":"ジブチ","ko":"지부티","lt":"Džibutis","nl":"Djibouti","no":"Djibouti","pl":"Dżibuti","pt":"Djibuti","ro":"Djibouti","ru":"Джибути","sk":"Džibutsko","sv":"Djibouti","th":"จิบูตี","uk":"Джибуті","zh":"吉布提","zh-tw":"吉布地"},
  {"id":212,"alpha2":"dm","alpha3":"dma","ar":"دومينيكا","bg":"Доминика","cs":"Dominika","da":"Dominica","de":"Dominica","el":"Δομινίκα","en":"Dominica","eo":"Dominiko","es":"Dominica","et":"Dominica","eu":"Dominika","fi":"Dominica","fr":"Dominique","hu":"Dominikai Közösség","hy":"Դոմինիկա","it":"Dominica","ja":"ドミニカ国","ko":"도미니카 연방","lt":"Dominika","nl":"Dominica","no":"Dominica","pl":"Dominika","pt":"Dominica","ro":"Dominica","ru":"Доминика","sk":"Dominika","sv":"Dominica","th":"ดอมินีกา","uk":"Домініка","zh":"多米尼克","zh-tw":"多米尼克"},
  {"id":214,"alpha2":"do","alpha3":"dom","ar":"جمهورية الدومينيكان","bg":"Доминиканска република","cs":"Dominikánská republika","da":"Dominikanske Republik","de":"Dominikanische Republik","el":"Δομινικανή Δημοκρατία","en":"Dominican Republic","eo":"Dominika Respubliko","es":"República Dominicana","et":"Dominikaani Vabariik","eu":"Dominikar Errepublika","fi":"Dominikaaninen tasavalta","fr":"République dominicaine","hu":"Dominikai Köztársaság","hy":"Դոմինիկյան Հանրապետություն","it":"Rep. Dominicana","ja":"ドミニカ共和国","ko":"도미니카 공화국","lt":"Dominikos Respublika","nl":"Dominicaanse Republiek","no":"Den dominikanske republikk","pl":"Dominikana","pt":"República Dominicana","ro":"Republica Dominicană","ru":"Доминиканская Республика","sk":"Dominikánska republika","sv":"Dominikanska republiken","th":"สาธารณรัฐโดมินิกัน","uk":"Домініканська Республіка","zh":"多米尼加","zh-tw":"多明尼加"},
  {"id":218,"alpha2":"ec","alpha3":"ecu","ar":"الإكوادور","bg":"Еквадор","cs":"Ekvádor","da":"Ecuador","de":"Ecuador","el":"Ισημερινός","en":"Ecuador","eo":"Ekvadoro","es":"Ecuador","et":"Ecuador","eu":"Ekuador","fi":"Ecuador","fr":"Équateur","hu":"Ecuador","hy":"Էկվադոր","it":"Ecuador","ja":"エクアドル","ko":"에콰도르","lt":"Ekvadoras","nl":"Ecuador","no":"Ecuador","pl":"Ekwador","pt":"Equador","ro":"Ecuador","ru":"Эквадор","sk":"Ekvádor","sv":"Ecuador","th":"เอกวาดอร์","uk":"Еквадор","zh":"厄瓜多尔","zh-tw":"厄瓜多"},
  {"id":818,"alpha2":"eg","alpha3":"egy","ar":"مصر","bg":"Египет","cs":"Egypt","da":"Egypten","de":"Ägypten","el":"Αίγυπτος","en":"Egypt","eo":"Egiptio","es":"Egipto","et":"Egiptus","eu":"Egipto","fi":"Egypti","fr":"Égypte","hu":"Egyiptom","hy":"Եգիպտոս","it":"Egitto","ja":"エジプト","ko":"이집트","lt":"Egiptas","nl":"Egypte","no":"Egypt","pl":"Egipt","pt":"Egito","ro":"Egipt","ru":"Египет","sk":"Egypt","sv":"Egypten","th":"อียิปต์","uk":"Єгипет","zh":"埃及","zh-tw":"埃及"},
  {"id":222,"alpha2":"sv","alpha3":"slv","ar":"السلفادور","bg":"Салвадор","cs":"Salvador","da":"El Salvador","de":"El Salvador","el":"Ελ Σαλβαδόρ","en":"El Salvador","eo":"Salvadoro","es":"El Salvador","et":"El Salvador","eu":"El Salvador","fi":"El Salvador","fr":"Salvador","hu":"Salvador","hy":"Սալվադոր","it":"El Salvador","ja":"エルサルバドル","ko":"엘살바도르","lt":"Salvadoras","nl":"El Salvador","no":"El Salvador","pl":"Salwador","pt":"El Salvador","ro":"El Salvador","ru":"Сальвадор","sk":"Salvádor","sv":"El Salvador","th":"เอลซัลวาดอร์","uk":"Сальвадор","zh":"萨尔瓦多","zh-tw":"薩爾瓦多"},
  {"id":226,"alpha2":"gq","alpha3":"gnq","ar":"غينيا الاستوائية","bg":"Екваториална Гвинея","cs":"Rovníková Guinea","da":"Ækvatorialguinea","de":"Äquatorialguinea","el":"Ισημερινή Γουινέα","en":"Equatorial Guinea","eo":"Ekvatora Gvineo","es":"Guinea Ecuatorial","et":"Ekvatoriaal-Guinea","eu":"Ekuatore Ginea","fi":"Päiväntasaajan Guinea","fr":"Guinée équatoriale","hu":"Egyenlítői-Guinea","hy":"Հասարակածային Գվինեա","it":"Guinea Equatoriale","ja":"赤道ギニア","ko":"적도 기니","lt":"Pusiaujo Gvinėja","nl":"Equatoriaal-Guinea","no":"Ekvatorial-Guinea","pl":"Gwinea Równikowa","pt":"Guiné Equatorial","ro":"Guineea Ecuatorială","ru":"Экваториальная Гвинея","sk":"Rovníková Guinea","sv":"Ekvatorialguinea","th":"อิเควทอเรียลกินี","uk":"Екваторіальна Гвінея","zh":"赤道几内亚","zh-tw":"赤道幾內亞"},
  {"id":232,"alpha2":"er","alpha3":"eri","ar":"إريتريا","bg":"Еритрея","cs":"Eritrea","da":"Eritrea","de":"Eritrea","el":"Ερυθραία","en":"Eritrea","eo":"Eritreo","es":"Eritrea","et":"Eritrea","eu":"Eritrea","fi":"Eritrea","fr":"Érythrée","hu":"Eritrea","hy":"Էրիտրեա","it":"Eritrea","ja":"エリトリア","ko":"에리트레아","lt":"Eritrėja","nl":"Eritrea","no":"Eritrea","pl":"Erytrea","pt":"Eritreia","ro":"Eritreea","ru":"Эритрея","sk":"Eritrea","sv":"Eritrea","th":"เอริเทรีย","uk":"Еритрея","zh":"厄立特里亚","zh-tw":"厄利垂亞"},
  {"id":233,"alpha2":"ee","alpha3":"est","ar":"إستونيا","bg":"Естония","cs":"Estonsko","da":"Estland","de":"Estland","el":"Εσθονία","en":"Estonia","eo":"Estonio","es":"Estonia","et":"Eesti","eu":"Estonia","fi":"Viro","fr":"Estonie","hu":"Észtország","hy":"Էստոնիա","it":"Estonia","ja":"エストニア","ko":"에스토니아","lt":"Estija","nl":"Estland","no":"Estland","pl":"Estonia","pt":"Estónia","ro":"Estonia","ru":"Эстония","sk":"Estónsko","sv":"Estland","th":"เอสโตเนีย","uk":"Естонія","zh":"爱沙尼亚","zh-tw":"愛沙尼亞"},
  {"id":231,"alpha2":"et","alpha3":"eth","ar":"إثيوبيا","bg":"Етиопия","cs":"Etiopie","da":"Etiopien","de":"Äthiopien","el":"Αιθιοπία","en":"Ethiopia","eo":"Etiopio","es":"Etiopía","et":"Etioopia","eu":"Etiopia","fi":"Etiopia","fr":"Éthiopie","hu":"Etiópia","hy":"Եթովպիա","it":"Etiopia","ja":"エチオピア","ko":"에티오피아","lt":"Etiopija","nl":"Ethiopië","no":"Etiopia","pl":"Etiopia","pt":"Etiópia","ro":"Etiopia","ru":"Эфиопия","sk":"Etiópia","sv":"Etiopien","th":"เอธิโอเปีย","uk":"Ефіопія","zh":"埃塞俄比亚","zh-tw":"衣索比亞"},
  {"id":242,"alpha2":"fj","alpha3":"fji","ar":"فيجي","bg":"Фиджи","cs":"Fidži","da":"Fiji","de":"Fidschi","el":"Φίτζι","en":"Fiji","eo":"Fiĝio","es":"Fiyi","et":"Fidži","eu":"Fiji","fi":"Fidži","fr":"Fidji","hu":"Fidzsi","hy":"Ֆիջի","it":"Figi","ja":"フィジー","ko":"피지","lt":"Fidžis","nl":"Fiji","no":"Fiji","pl":"Fidżi","pt":"Fiji","ro":"Fiji","ru":"Фиджи","sk":"Fidži","sv":"Fiji","th":"ฟีจี","uk":"Фіджі","zh":"斐济","zh-tw":"斐濟"},
  {"id":246,"alpha2":"fi","alpha3":"fin","ar":"فنلندا","bg":"Финландия","cs":"Finsko","da":"Finland","de":"Finnland","el":"Φινλανδία","en":"Finland","eo":"Finnlando","es":"Finlandia","et":"Soome","eu":"Finlandia","fi":"Suomi","fr":"Finlande","hu":"Finnország","hy":"Ֆինլանդիա","it":"Finlandia","ja":"フィンランド","ko":"핀란드","lt":"Suomija","nl":"Finland","no":"Finland","pl":"Finlandia","pt":"Finlândia","ro":"Finlanda","ru":"Финляндия","sk":"Fínsko","sv":"Finland","th":"ฟินแลนด์","uk":"Фінляндія","zh":"芬兰","zh-tw":"芬蘭"},
  {"id":250,"alpha2":"fr","alpha3":"fra","ar":"فرنسا","bg":"Франция","cs":"Francie","da":"Frankrig","de":"Frankreich","el":"Γαλλία","en":"France","eo":"Francio","es":"Francia","et":"Prantsusmaa","eu":"Frantzia","fi":"Ranska","fr":"France","hu":"Franciaország","hy":"Ֆրանսիա","it":"Francia","ja":"フランス","ko":"프랑스","lt":"Prancūzija","nl":"Frankrijk","no":"Frankrike","pl":"Francja","pt":"França","ro":"Franța","ru":"Франция","sk":"Francúzsko","sv":"Frankrike","th":"ฝรั่งเศส","uk":"Франція","zh":"法国","zh-tw":"法國"},
  {"id":266,"alpha2":"ga","alpha3":"gab","ar":"الغابون","bg":"Габон","cs":"Gabon","da":"Gabon","de":"Gabun","el":"Γκαμπόν","en":"Gabon","eo":"Gabono","es":"Gabón","et":"Gabon","eu":"Gabon","fi":"Gabon","fr":"Gabon","hu":"Gabon","hy":"Գաբոն","it":"Gabon","ja":"ガボン","ko":"가봉","lt":"Gabonas","nl":"Gabon","no":"Gabon","pl":"Gabon","pt":"Gabão","ro":"Gabon","ru":"Габон","sk":"Gabon","sv":"Gabon","th":"กาบอง","uk":"Габон","zh":"加蓬","zh-tw":"加彭"},
  {"id":270,"alpha2":"gm","alpha3":"gmb","ar":"غامبيا","bg":"Гамбия","cs":"Gambie","da":"Gambia","de":"Gambia","el":"Γκάμπια","en":"Gambia","eo":"Gambio","es":"Gambia","et":"Gambia","eu":"Gambia","fi":"Gambia","fr":"Gambie","hu":"Gambia","hy":"Գամբիա","it":"Gambia","ja":"ガンビア","ko":"감비아","lt":"Gambija","nl":"Gambia","no":"Gambia","pl":"Gambia","pt":"Gâmbia","ro":"Gambia","ru":"Гамбия","sk":"Gambia","sv":"Gambia","th":"แกมเบีย","uk":"Гамбія","zh":"冈比亚","zh-tw":"甘比亞"},
  {"id":268,"alpha2":"ge","alpha3":"geo","ar":"جورجيا","bg":"Грузия","cs":"Gruzie","da":"Georgien","de":"Georgien","el":"Γεωργία","en":"Georgia","eo":"Kartvelio","es":"Georgia","et":"Gruusia","eu":"Georgia","fi":"Georgia","fr":"Géorgie","hu":"Grúzia","hy":"Վրաստան","it":"Georgia","ja":"ジョージア","ko":"조지아","lt":"Gruzija","nl":"Georgië","no":"Georgia","pl":"Gruzja","pt":"Geórgia","ro":"Georgia","ru":"Грузия","sk":"Gruzínsko","sv":"Georgien","th":"จอร์เจีย","uk":"Грузія","zh":"格鲁吉亚","zh-tw":"喬治亞"},
  {"id":276,"alpha2":"de","alpha3":"deu","ar":"ألمانيا","bg":"Германия","cs":"Německo","da":"Tyskland","de":"Deutschland","el":"Γερμανία","en":"Germany","eo":"Germanio","es":"Alemania","et":"Saksamaa","eu":"Alemania","fi":"Saksa","fr":"Allemagne","hu":"Németország","hy":"Գերմանիա","it":"Germania","ja":"ドイツ","ko":"독일","lt":"Vokietija","nl":"Duitsland","no":"Tyskland","pl":"Niemcy","pt":"Alemanha","ro":"Germania","ru":"Германия","sk":"Nemecko","sv":"Tyskland","th":"เยอรมนี","uk":"Німеччина","zh":"德国","zh-tw":"德國"},
  {"id":288,"alpha2":"gh","alpha3":"gha","ar":"غانا","bg":"Гана","cs":"Ghana","da":"Ghana","de":"Ghana","el":"Γκάνα","en":"Ghana","eo":"Ganao","es":"Ghana","et":"Ghana","eu":"Ghana","fi":"Ghana","fr":"Ghana","hu":"Ghána","hy":"Գանա","it":"Ghana","ja":"ガーナ","ko":"가나","lt":"Gana","nl":"Ghana","no":"Ghana","pl":"Ghana","pt":"Gana","ro":"Ghana","ru":"Гана","sk":"Ghana","sv":"Ghana","th":"กานา","uk":"Гана","zh":"加纳","zh-tw":"迦納"},
  {"id":300,"alpha2":"gr","alpha3":"grc","ar":"اليونان","bg":"Гърция","cs":"Řecko","da":"Grækenland","de":"Griechenland","el":"Ελλάδα","en":"Greece","eo":"Grekio","es":"Grecia","et":"Kreeka","eu":"Grezia","fi":"Kreikka","fr":"Grèce","hu":"Görögország","hy":"Հունաստան","it":"Grecia","ja":"ギリシャ","ko":"그리스","lt":"Graikija","nl":"Griekenland","no":"Hellas","pl":"Grecja","pt":"Grécia","ro":"Grecia","ru":"Греция","sk":"Grécko","sv":"Grekland","th":"กรีซ","uk":"Греція","zh":"希腊","zh-tw":"希臘"},
  {"id":308,"alpha2":"gd","alpha3":"grd","ar":"غرينادا","bg":"Гренада","cs":"Grenada","da":"Grenada","de":"Grenada","el":"Γρενάδα","en":"Grenada","eo":"Grenado","es":"Granada","et":"Grenada","eu":"Grenada","fi":"Grenada","fr":"Grenade","hu":"Grenada","hy":"Գրենադա","it":"Grenada","ja":"グレナダ","ko":"그레나다","lt":"Grenada","nl":"Grenada","no":"Grenada","pl":"Grenada","pt":"Granada","ro":"Grenada","ru":"Гренада","sk":"Grenada","sv":"Grenada","th":"กรีเนดา","uk":"Гренада","zh":"格林纳达","zh-tw":"格瑞那達"},
  {"id":320,"alpha2":"gt","alpha3":"gtm","ar":"غواتيمالا","bg":"Гватемала","cs":"Guatemala","da":"Guatemala","de":"Guatemala","el":"Γουατεμάλα","en":"Guatemala","eo":"Gvatemalo","es":"Guatemala","et":"Guatemala","eu":"Guatemala","fi":"Guatemala","fr":"Guatemala","hu":"Guatemala","hy":"Գվատեմալա","it":"Guatemala","ja":"グアテマラ","ko":"과테말라","lt":"Gvatemala","nl":"Guatemala","no":"Guatemala","pl":"Gwatemala","pt":"Guatemala","ro":"Guatemala","ru":"Гватемала","sk":"Guatemala","sv":"Guatemala","th":"กัวเตมาลา","uk":"Гватемала","zh":"危地马拉","zh-tw":"瓜地馬拉"},
  {"id":324,"alpha2":"gn","alpha3":"gin","ar":"غينيا","bg":"Гвинея","cs":"Guinea","da":"Guinea","de":"Guinea","el":"Γουινέα","en":"Guinea","eo":"Gvineo","es":"Guinea","et":"Guinea","eu":"Ginea","fi":"Guinea","fr":"Guinée","hu":"Guinea","hy":"Գվինեա","it":"Guinea","ja":"ギニア","ko":"기니","lt":"Gvinėja","nl":"Guinee","no":"Guinea","pl":"Gwinea","pt":"Guiné","ro":"Guineea","ru":"Гвинея","sk":"Guinea","sv":"Guinea","th":"กินี","uk":"Гвінея","zh":"几内亚","zh-tw":"幾內亞"},
  {"id":624,"alpha2":"gw","alpha3":"gnb","ar":"غينيا بيساو","bg":"Гвинея-Бисау","cs":"Guinea-Bissau","da":"Guinea-Bissau","de":"Guinea-Bissau","el":"Γουινέα-Μπισσάου","en":"Guinea-Bissau","eo":"Gvineo Bisaŭa","es":"Guinea-Bisáu","et":"Guinea-Bissau","eu":"Ginea-Bissau","fi":"Guinea-Bissau","fr":"Guinée-Bissau","hu":"Bissau-Guinea","hy":"Գվինեա-Բիսաու","it":"Guinea-Bissau","ja":"ギニアビサウ","ko":"기니비사우","lt":"Bisau Gvinėja","nl":"Guinee-Bissau","no":"Guinea-Bissau","pl":"Gwinea Bissau","pt":"Guiné-Bissau","ro":"Guineea-Bissau","ru":"Гвинея-Бисау","sk":"Guinea-Bissau","sv":"Guinea-Bissau","th":"กินี-บิสเซา","uk":"Гвінея-Бісау","zh":"几内亚比绍","zh-tw":"幾內亞比索"},
  {"id":328,"alpha2":"gy","alpha3":"guy","ar":"غيانا","bg":"Гвиана","cs":"Guyana","da":"Guyana","de":"Guyana","el":"Γουιάνα","en":"Guyana","eo":"Gujano","es":"Guyana","et":"Guyana","eu":"Guyana","fi":"Guyana","fr":"Guyana","hu":"Guyana","hy":"Գայանա","it":"Guyana","ja":"ガイアナ","ko":"가이아나","lt":"Gajana","nl":"Guyana","no":"Guyana","pl":"Gujana","pt":"Guiana","ro":"Guyana","ru":"Гайана","sk":"Guyana","sv":"Guyana","th":"กายอานา","uk":"Гаяна","zh":"圭亚那","zh-tw":"蓋亞那"},
  {"id":332,"alpha2":"ht","alpha3":"hti","ar":"هايتي","bg":"Хаити","cs":"Haiti","da":"Haiti","de":"Haiti","el":"Αϊτή","en":"Haiti","eo":"Haitio","es":"Haití","et":"Haiti","eu":"Haiti","fi":"Haiti","fr":"Haïti","hu":"Haiti","hy":"Հայիթի","it":"Haiti","ja":"ハイチ","ko":"아이티","lt":"Haitis","nl":"Haïti","no":"Haiti","pl":"Haiti","pt":"Haiti","ro":"Haiti","ru":"Гаити","sk":"Haiti","sv":"Haiti","th":"เฮติ","uk":"Гаїті","zh":"海地","zh-tw":"海地"},
  {"id":340,"alpha2":"hn","alpha3":"hnd","ar":"هندوراس","bg":"Хондурас","cs":"Honduras","da":"Honduras","de":"Honduras","el":"Ονδούρα","en":"Honduras","eo":"Honduro","es":"Honduras","et":"Honduras","eu":"Honduras","fi":"Honduras","fr":"Honduras","hu":"Honduras","hy":"Հոնդուրաս","it":"Honduras","ja":"ホンジュラス","ko":"온두라스","lt":"Hondūras","nl":"Honduras","no":"Honduras","pl":"Honduras","pt":"Honduras","ro":"Honduras","ru":"Гондурас","sk":"Honduras","sv":"Honduras","th":"ฮอนดูรัส","uk":"Гондурас","zh":"洪都拉斯","zh-tw":"宏都拉斯"},
  {"id":348,"alpha2":"hu","alpha3":"hun","ar":"المجر","bg":"Унгария","cs":"Maďarsko","da":"Ungarn","de":"Ungarn","el":"Ουγγαρία","en":"Hungary","eo":"Hungario","es":"Hungría","et":"Ungari","eu":"Hungaria","fi":"Unkari","fr":"Hongrie","hu":"Magyarország","hy":"Հունգարիա","it":"Ungheria","ja":"ハンガリー","ko":"헝가리","lt":"Vengrija","nl":"Hongarije","no":"Ungarn","pl":"Węgry","pt":"Hungria","ro":"Ungaria","ru":"Венгрия","sk":"Maďarsko","sv":"Ungern","th":"ฮังการี","uk":"Угорщина","zh":"匈牙利","zh-tw":"匈牙利"},
  {"id":352,"alpha2":"is","alpha3":"isl","ar":"آيسلندا","bg":"Исландия","cs":"Island","da":"Island","de":"Island","el":"Ισλανδία","en":"Iceland","eo":"Islando","es":"Islandia","et":"Island","eu":"Islandia","fi":"Islanti","fr":"Islande","hu":"Izland","hy":"Իսլանդիա","it":"Islanda","ja":"アイスランド","ko":"아이슬란드","lt":"Islandija","nl":"IJsland","no":"Island","pl":"Islandia","pt":"Islândia","ro":"Islanda","ru":"Исландия","sk":"Island","sv":"Island","th":"ไอซ์แลนด์","uk":"Ісландія","zh":"冰岛","zh-tw":"冰島"},
  {"id":356,"alpha2":"in","alpha3":"ind","ar":"الهند","bg":"Индия","cs":"Indie","da":"Indien","de":"Indien","el":"Ινδία","en":"India","eo":"Barato","es":"India","et":"India","eu":"India","fi":"Intia","fr":"Inde","hu":"India","hy":"Հնդկաստան","it":"India","ja":"インド","ko":"인도","lt":"Indija","nl":"India","no":"India","pl":"Indie","pt":"Índia","ro":"India","ru":"Индия","sk":"India","sv":"Indien","th":"อินเดีย","uk":"Індія","zh":"印度","zh-tw":"印度"},
  {"id":360,"alpha2":"id","alpha3":"idn","ar":"إندونيسيا","bg":"Индонезия","cs":"Indonésie","da":"Indonesien","de":"Indonesien","el":"Ινδονησία","en":"Indonesia","eo":"Indonezio","es":"Indonesia","et":"Indoneesia","eu":"Indonesia","fi":"Indonesia","fr":"Indonésie","hu":"Indonézia","hy":"Ինդոնեզիա","it":"Indonesia","ja":"インドネシア","ko":"인도네시아","lt":"Indonezija","nl":"Indonesië","no":"Indonesia","pl":"Indonezja","pt":"Indonésia","ro":"Indonezia","ru":"Индонезия","sk":"Indonézia","sv":"Indonesien","th":"อินโดนีเซีย","uk":"Індонезія","zh":"印度尼西亚","zh-tw":"印度尼西亞"},
  {"id":364,"alpha2":"ir","alpha3":"irn","ar":"إيران","bg":"Иран","cs":"Írán","da":"Iran","de":"Iran","el":"Ιράν","en":"Iran (Islamic Republic of)","eo":"Irano","es":"Irán","et":"Iraan","eu":"Iran","fi":"Iran","fr":"Iran","hu":"Irán","hy":"Իրան","it":"Iran","ja":"イラン・イスラム共和国","ko":"이란","lt":"Iranas","nl":"Iran","no":"Iran","pl":"Iran","pt":"Irã","ro":"Iran","ru":"Иран","sk":"Irán","sv":"Iran","th":"อิหร่าน","uk":"Іран","zh":"伊朗","zh-tw":"伊朗"},
  {"id":368,"alpha2":"iq","alpha3":"irq","ar":"العراق","bg":"Ирак","cs":"Irák","da":"Irak","de":"Irak","el":"Ιράκ","en":"Iraq","eo":"Irako","es":"Irak","et":"Iraak","eu":"Irak","fi":"Irak","fr":"Irak","hu":"Irak","hy":"Իրաք","it":"Iraq","ja":"イラク","ko":"이라크","lt":"Irakas","nl":"Irak","no":"Irak","pl":"Irak","pt":"Iraque","ro":"Irak","ru":"Ирак","sk":"Irak","sv":"Irak","th":"อิรัก","uk":"Ірак","zh":"伊拉克","zh-tw":"伊拉克"},
  {"id":372,"alpha2":"ie","alpha3":"irl","ar":"أيرلندا","bg":"Ирландия","cs":"Irsko","da":"Irland","de":"Irland","el":"Ιρλανδία","en":"Ireland","eo":"Irlando","es":"Irlanda","et":"Iirimaa","eu":"Irlandako Errepublika","fi":"Irlanti","fr":"Irlande","hu":"Írország","hy":"Իռլանդիա","it":"Irlanda","ja":"アイルランド","ko":"아일랜드","lt":"Airija","nl":"Ierland","no":"Irland","pl":"Irlandia","pt":"Irlanda","ro":"Republica Irlanda","ru":"Ирландия","sk":"Írsko","sv":"Irland","th":"ไอร์แลนด์","uk":"Ірландія","zh":"爱尔兰","zh-tw":"愛爾蘭"},
  {"id":376,"alpha2":"il","alpha3":"isr","ar":"إسرائيل","bg":"Израел","cs":"Izrael","da":"Israel","de":"Israel","el":"Ισραήλ","en":"Israel","eo":"Israelo","es":"Israel","et":"Iisrael","eu":"Israel","fi":"Israel","fr":"Israël","hu":"Izrael","hy":"Իսրայել","it":"Israele","ja":"イスラエル","ko":"이스라엘","lt":"Izraelis","nl":"Israël","no":"Israel","pl":"Izrael","pt":"Israel","ro":"Israel","ru":"Израиль","sk":"Izrael","sv":"Israel","th":"อิสราเอล","uk":"Ізраїль","zh":"以色列","zh-tw":"以色列"},
  {"id":380,"alpha2":"it","alpha3":"ita","ar":"إيطاليا","bg":"Италия","cs":"Itálie","da":"Italien","de":"Italien","el":"Ιταλία","en":"Italy","eo":"Italio","es":"Italia","et":"Itaalia","eu":"Italia","fi":"Italia","fr":"Italie","hu":"Olaszország","hy":"Իտալիա","it":"Italia","ja":"イタリア","ko":"이탈리아","lt":"Italija","nl":"Italië","no":"Italia","pl":"Włochy","pt":"Itália","ro":"Italia","ru":"Италия","sk":"Taliansko","sv":"Italien","th":"อิตาลี","uk":"Італія","zh":"意大利","zh-tw":"義大利"},
  {"id":388,"alpha2":"jm","alpha3":"jam","ar":"جامايكا","bg":"Ямайка","cs":"Jamajka","da":"Jamaica","de":"Jamaika","el":"Τζαμάικα","en":"Jamaica","eo":"Jamajko","es":"Jamaica","et":"Jamaica","eu":"Jamaika","fi":"Jamaika","fr":"Jamaïque","hu":"Jamaica","hy":"Ճամայկա","it":"Giamaica","ja":"ジャマイカ","ko":"자메이카","lt":"Jamaika","nl":"Jamaica","no":"Jamaica","pl":"Jamajka","pt":"Jamaica","ro":"Jamaica","ru":"Ямайка","sk":"Jamajka","sv":"Jamaica","th":"จาเมกา","uk":"Ямайка","zh":"牙买加","zh-tw":"牙買加"},
  {"id":392,"alpha2":"jp","alpha3":"jpn","ar":"اليابان","bg":"Япония","cs":"Japonsko","da":"Japan","de":"Japan","el":"Ιαπωνία","en":"Japan","eo":"Japanio","es":"Japón","et":"Jaapan","eu":"Japonia","fi":"Japani","fr":"Japon","hu":"Japán","hy":"Ճապոնիա","it":"Giappone","ja":"日本","ko":"일본","lt":"Japonija","nl":"Japan","no":"Japan","pl":"Japonia","pt":"Japão","ro":"Japonia","ru":"Япония","sk":"Japonsko","sv":"Japan","th":"ญี่ปุ่น","uk":"Японія","zh":"日本","zh-tw":"日本"},
  {"id":400,"alpha2":"jo","alpha3":"jor","ar":"الأردن","bg":"Йордания","cs":"Jordánsko","da":"Jordan","de":"Jordanien","el":"Ιορδανία","en":"Jordan","eo":"Jordanio","es":"Jordania","et":"Jordaania","eu":"Jordania","fi":"Jordania","fr":"Jordanie","hu":"Jordánia","hy":"Հորդանան","it":"Giordania","ja":"ヨルダン","ko":"요르단","lt":"Jordanija","nl":"Jordanië","no":"Jordan","pl":"Jordania","pt":"Jordânia","ro":"Iordania","ru":"Иордания","sk":"Jordánsko","sv":"Jordanien","th":"จอร์แดน","uk":"Йорданія","zh":"约旦","zh-tw":"約旦"},
  {"id":398,"alpha2":"kz","alpha3":"kaz","ar":"كازاخستان","bg":"Казахстан","cs":"Kazachstán","da":"Kasakhstan","de":"Kasachstan","el":"Καζακστάν","en":"Kazakhstan","eo":"Kazaĥio","es":"Kazajistán","et":"Kasahstan","eu":"Kazakhstan","fi":"Kazakstan","fr":"Kazakhstan","hu":"Kazahsztán","hy":"Ղազախստան","it":"Kazakistan","ja":"カザフスタン","ko":"카자흐스탄","lt":"Kazachstanas","nl":"Kazachstan","no":"Kasakhstan","pl":"Kazachstan","pt":"Cazaquistão","ro":"Kazahstan","ru":"Казахстан","sk":"Kazachstan","sv":"Kazakstan","th":"คาซัคสถาน","uk":"Казахстан","zh":"哈萨克斯坦","zh-tw":"哈薩克"},
  {"id":404,"alpha2":"ke","alpha3":"ken","ar":"كينيا","bg":"Кения","cs":"Keňa","da":"Kenya","de":"Kenia","el":"Κένυα","en":"Kenya","eo":"Kenjo","es":"Kenia","et":"Keenia","eu":"Kenya","fi":"Kenia","fr":"Kenya","hu":"Kenya","hy":"Քենիա","it":"Kenya","ja":"ケニア","ko":"케냐","lt":"Kenija","nl":"Kenia","no":"Kenya","pl":"Kenia","pt":"Quênia","ro":"Kenya","ru":"Кения","sk":"Keňa","sv":"Kenya","th":"เคนยา","uk":"Кенія","zh":"肯尼亚","zh-tw":"肯亞"},
  {"id":296,"alpha2":"ki","alpha3":"kir","ar":"كيريباتي","bg":"Кирибати","cs":"Kiribati","da":"Kiribati","de":"Kiribati","el":"Κιριμπάτι","en":"Kiribati","eo":"Kiribato","es":"Kiribati","et":"Kiribati","eu":"Kiribati","fi":"Kiribati","fr":"Kiribati","hu":"Kiribati","hy":"Կիրիբատի","it":"Kiribati","ja":"キリバス","ko":"키리바시","lt":"Kiribatis","nl":"Kiribati","no":"Kiribati","pl":"Kiribati","pt":"Quiribáti","ro":"Kiribati","ru":"Кирибати","sk":"Kiribati","sv":"Kiribati","th":"คิริบาส","uk":"Кірибаті","zh":"基里巴斯","zh-tw":"吉里巴斯"},
  {"id":408,"alpha2":"kp","alpha3":"prk","ar":"كوريا الشمالية","bg":"Северна Корея","cs":"Severní Korea","da":"Nordkorea","de":"Korea, Nord (Nordkorea)","el":"Βόρεια Κορέα","en":"Korea (Democratic People's Republic of)","eo":"Nord-Koreio","es":"Corea del Norte","et":"Põhja-Korea","eu":"Ipar Korea","fi":"Korean demokraattinen kansantasavalta","fr":"Corée du Nord","hu":"Észak-Korea (Koreai NDK)","hy":"Հյուսիսային Կորեա","it":"Corea del Nord","ja":"朝鮮民主主義人民共和国","ko":"조선민주주의인민공화국","lt":"Šiaurės Korėja","nl":"Noord-Korea","no":"Nord-Korea","pl":"Korea Północna","pt":"Coreia do Norte","ro":"Coreea de Nord","ru":"КНДР (Корейская Народно-Демократическая Республика)","sk":"Kórejská ľudovodemokratická republika","sv":"Nordkorea","th":"เกาหลีเหนือ","uk":"Північна Корея","zh":"朝鲜","zh-tw":"北韓"},
  {"id":410,"alpha2":"kr","alpha3":"kor","ar":"كوريا الجنوبية","bg":"Южна Корея","cs":"Jižní Korea","da":"Sydkorea","de":"Korea, Süd (Südkorea)","el":"Νότια Κορέα","en":"Korea, Republic of","eo":"Sud-Koreio","es":"Corea del Sur","et":"Lõuna-Korea","eu":"Hego Korea","fi":"Korean tasavalta","fr":"Corée du Sud","hu":"Dél-Korea (Koreai Köztársaság)","hy":"Հարավային Կորեա","it":"Corea del Sud","ja":"大韓民国","ko":"대한민국","lt":"Pietų Korėja","nl":"Zuid-Korea","no":"Sør-Korea","pl":"Korea Południowa","pt":"Coreia do Sul","ro":"Coreea de Sud","ru":"Республика Корея","sk":"Kórejská republika","sv":"Sydkorea","th":"เกาหลีใต้","uk":"Південна Корея","zh":"韩国","zh-tw":"南韓"},
  {"id":414,"alpha2":"kw","alpha3":"kwt","ar":"الكويت","bg":"Кувейт","cs":"Kuvajt","da":"Kuwait","de":"Kuwait","el":"Κουβέιτ","en":"Kuwait","eo":"Kuvajto","es":"Kuwait","et":"Kuveit","eu":"Kuwait","fi":"Kuwait","fr":"Koweït","hu":"Kuvait","hy":"Քուվեյթ","it":"Kuwait","ja":"クウェート","ko":"쿠웨이트","lt":"Kuveitas","nl":"Koeweit","no":"Kuwait","pl":"Kuwejt","pt":"Kuwait","ro":"Kuweit","ru":"Кувейт","sk":"Kuvajt","sv":"Kuwait","th":"คูเวต","uk":"Кувейт","zh":"科威特","zh-tw":"科威特"},
  {"id":417,"alpha2":"kg","alpha3":"kgz","ar":"قيرغيزستان","bg":"Киргизстан","cs":"Kyrgyzstán","da":"Kirgisistan","de":"Kirgisistan","el":"Κιργιζία","en":"Kyrgyzstan","eo":"Kirgizio","es":"Kirguistán","et":"Kõrgõzstan","eu":"Kirgizistan","fi":"Kirgisia","fr":"Kirghizistan","hu":"Kirgizisztán","hy":"Ղրղզստան","it":"Kirghizistan","ja":"キルギス","ko":"키르기스스탄","lt":"Kirgizija","nl":"Kirgizië","no":"Kirgisistan","pl":"Kirgistan","pt":"Quirguistão","ro":"Kârgâzstan","ru":"Киргизия","sk":"Kirgizsko","sv":"Kirgizistan","th":"คีร์กีซสถาน","uk":"Киргизстан","zh":"吉尔吉斯斯坦","zh-tw":"吉爾吉斯"},
  {"id":418,"alpha2":"la","alpha3":"lao","ar":"لاوس","bg":"Лаос","cs":"Laos","da":"Laos","de":"Laos","el":"Λάος","en":"Lao People's Democratic Republic","eo":"Laoso","es":"Laos","et":"Laos","eu":"Laos","fi":"Laos","fr":"Laos","hu":"Laosz","hy":"Լաոս","it":"Laos","ja":"ラオス人民民主共和国","ko":"라오스","lt":"Laosas","nl":"Laos","no":"Laos","pl":"Laos","pt":"Laos","ro":"Laos","ru":"Лаос","sk":"Laos","sv":"Laos","th":"ลาว","uk":"Лаос","zh":"老挝","zh-tw":"寮國"},
  {"id":428,"alpha2":"lv","alpha3":"lva","ar":"لاتفيا","bg":"Латвия","cs":"Lotyšsko","da":"Letland","de":"Lettland","el":"Λεττονία","en":"Latvia","eo":"Latvio","es":"Letonia","et":"Läti","eu":"Letonia","fi":"Latvia","fr":"Lettonie","hu":"Lettország","hy":"Լատվիա","it":"Lettonia","ja":"ラトビア","ko":"라트비아","lt":"Latvija","nl":"Letland","no":"Latvia","pl":"Łotwa","pt":"Letônia","ro":"Letonia","ru":"Латвия","sk":"Lotyšsko","sv":"Lettland","th":"ลัตเวีย","uk":"Латвія","zh":"拉脱维亚","zh-tw":"拉脫維亞"},
  {"id":422,"alpha2":"lb","alpha3":"lbn","ar":"لبنان","bg":"Ливан","cs":"Libanon","da":"Libanon","de":"Libanon","el":"Λίβανος","en":"Lebanon","eo":"Libano","es":"Líbano","et":"Liibanon","eu":"Libano","fi":"Libanon","fr":"Liban","hu":"Libanon","hy":"Լիբանան","it":"Libano","ja":"レバノン","ko":"레바논","lt":"Libanas","nl":"Libanon","no":"Libanon","pl":"Liban","pt":"Líbano","ro":"Liban","ru":"Ливан","sk":"Libanon","sv":"Libanon","th":"เลบานอน","uk":"Ліван","zh":"黎巴嫩","zh-tw":"黎巴嫩"},
  {"id":426,"alpha2":"ls","alpha3":"lso","ar":"ليسوتو","bg":"Лесото","cs":"Lesotho","da":"Lesotho","de":"Lesotho","el":"Λεσότο","en":"Lesotho","eo":"Lesoto","es":"Lesoto","et":"Lesotho","eu":"Lesotho","fi":"Lesotho","fr":"Lesotho","hu":"Lesotho","hy":"Լեսոթո","it":"Lesotho","ja":"レソト","ko":"레소토","lt":"Lesotas","nl":"Lesotho","no":"Lesotho","pl":"Lesotho","pt":"Lesoto","ro":"Lesotho","ru":"Лесото","sk":"Lesotho","sv":"Lesotho","th":"เลโซโท","uk":"Лесото","zh":"莱索托","zh-tw":"賴索托"},
  {"id":430,"alpha2":"lr","alpha3":"lbr","ar":"ليبيريا","bg":"Либерия","cs":"Libérie","da":"Liberia","de":"Liberia","el":"Λιβερία","en":"Liberia","eo":"Liberio","es":"Liberia","et":"Libeeria","eu":"Liberia","fi":"Liberia","fr":"Liberia","hu":"Libéria","hy":"Լիբերիա","it":"Liberia","ja":"リベリア","ko":"라이베리아","lt":"Liberija","nl":"Liberia","no":"Liberia","pl":"Liberia","pt":"Libéria","ro":"Liberia","ru":"Либерия","sk":"Libéria","sv":"Liberia","th":"ไลบีเรีย","uk":"Ліберія","zh":"利比里亚","zh-tw":"賴比瑞亞"},
  {"id":434,"alpha2":"ly","alpha3":"lby","ar":"ليبيا","bg":"Либия","cs":"Libye","da":"Libyen","de":"Libyen","el":"Λιβύη","en":"Libya","eo":"Libio","es":"Libia","et":"Liibüa","eu":"Libia","fi":"Libya","fr":"Libye","hu":"Líbia","hy":"Լիբիա","it":"Libia","ja":"リビア","ko":"리비아","lt":"Libija","nl":"Libië","no":"Libya","pl":"Libia","pt":"Líbia","ro":"Libia","ru":"Ливия","sk":"Líbya","sv":"Libyen","th":"ลิเบีย","uk":"Лівія","zh":"利比亚","zh-tw":"利比亞"},
  {"id":438,"alpha2":"li","alpha3":"lie","ar":"ليختنشتاين","bg":"Лихтенщайн","cs":"Lichtenštejnsko","da":"Liechtenstein","de":"Liechtenstein","el":"Λίχτενσταϊν","en":"Liechtenstein","eo":"Liĥtenŝtejno","es":"Liechtenstein","et":"Liechtenstein","eu":"Liechtenstein","fi":"Liechtenstein","fr":"Liechtenstein","hu":"Liechtenstein","hy":"Լիխտենշտայն","it":"Liechtenstein","ja":"リヒテンシュタイン","ko":"리히텐슈타인","lt":"Lichtenšteinas","nl":"Liechtenstein","no":"Liechtenstein","pl":"Liechtenstein","pt":"Listenstaine","ro":"Liechtenstein","ru":"Лихтенштейн","sk":"Lichtenštajnsko","sv":"Liechtenstein","th":"ลีชเทินชไตน์","uk":"Ліхтенштейн","zh":"列支敦士登","zh-tw":"列支敦斯登"},
  {"id":440,"alpha2":"lt","alpha3":"ltu","ar":"ليتوانيا","bg":"Литва","cs":"Litva","da":"Litauen","de":"Litauen","el":"Λιθουανία","en":"Lithuania","eo":"Litovio","es":"Lituania","et":"Leedu","eu":"Lituania","fi":"Liettua","fr":"Lituanie","hu":"Litvánia","hy":"Լիտվա","it":"Lituania","ja":"リトアニア","ko":"리투아니아","lt":"Lietuva","nl":"Litouwen","no":"Litauen","pl":"Litwa","pt":"Lituânia","ro":"Lituania","ru":"Литва","sk":"Litva","sv":"Litauen","th":"ลิทัวเนีย","uk":"Литва","zh":"立陶宛","zh-tw":"立陶宛"},
  {"id":442,"alpha2":"lu","alpha3":"lux","ar":"لوكسمبورغ","bg":"Люксембург","cs":"Lucembursko","da":"Luxembourg","de":"Luxemburg","el":"Λουξεμβούργο","en":"Luxembourg","eo":"Luksemburgo","es":"Luxemburgo","et":"Luksemburg","eu":"Luxenburgo","fi":"Luxemburg","fr":"Luxembourg","hu":"Luxemburg","hy":"Լյուքսեմբուրգ","it":"Lussemburgo","ja":"ルクセンブルク","ko":"룩셈부르크","lt":"Liuksemburgas","nl":"Luxemburg","no":"Luxembourg","pl":"Luksemburg","pt":"Luxemburgo","ro":"Luxemburg","ru":"Люксембург","sk":"Luxembursko","sv":"Luxemburg","th":"ลักเซมเบิร์ก","uk":"Люксембург","zh":"卢森堡","zh-tw":"盧森堡"},
  {"id":807,"alpha2":"mk","alpha3":"mkd","ar":"مقدونيا","bg":"Северна Македония","cs":"Severní Makedonie","da":"Nordmakedonien","de":"Nordmazedonien","el":"Βόρεια Μακεδονία","en":"North Macedonia","eo":"Nord-Makedonio","es":"Macedonia del Norte","et":"Põhja-Makedoonia","eu":"Ipar Mazedonia","fi":"Pohjois-Makedonia","fr":"Macédoine du Nord","hu":"Észak-Macedónia","hy":"Հյուսիսային Մակեդոնիա","it":"Macedonia del Nord","ja":"北マケドニア","ko":"북마케도니아","lt":"Makedonija","nl":"Noord-Macedonië","no":"Nord-Makedonia, Republikken","pl":"Macedonia Północna","pt":"Macedônia do Norte","ro":"Republica Macedonia","ru":"Северная Македония","sk":"Severné Macedónsko","sv":"Nordmakedonien","th":"นอร์ทมาซิโดเนีย","uk":"Північна Македонія","zh":"北马其顿","zh-tw":"北馬其頓"},
  {"id":450,"alpha2":"mg","alpha3":"mdg","ar":"مدغشقر","bg":"Мадагаскар","cs":"Madagaskar","da":"Madagaskar","de":"Madagaskar","el":"Μαδαγασκάρη","en":"Madagascar","eo":"Madagaskaro","es":"Madagascar","et":"Madagaskar","eu":"Madagaskar","fi":"Madagaskar","fr":"Madagascar","hu":"Madagaszkár","hy":"Մադագասկար","it":"Madagascar","ja":"マダガスカル","ko":"마다가스카르","lt":"Madagaskaras","nl":"Madagaskar","no":"Madagaskar","pl":"Madagaskar","pt":"Madagáscar","ro":"Madagascar","ru":"Мадагаскар","sk":"Madagaskar","sv":"Madagaskar","th":"มาดากัสการ์","uk":"Мадагаскар","zh":"马达加斯加","zh-tw":"馬達加斯加"},
  {"id":454,"alpha2":"mw","alpha3":"mwi","ar":"مالاوي","bg":"Малави","cs":"Malawi","da":"Malawi","de":"Malawi","el":"Μαλάουι","en":"Malawi","eo":"Malavio","es":"Malaui","et":"Malawi","eu":"Malawi","fi":"Malawi","fr":"Malawi","hu":"Malawi","hy":"Մալավի","it":"Malawi","ja":"マラウイ","ko":"말라위","lt":"Malavis","nl":"Malawi","no":"Malawi","pl":"Malawi","pt":"Maláui","ro":"Malawi","ru":"Малави","sk":"Malawi","sv":"Malawi","th":"มาลาวี","uk":"Малаві","zh":"马拉维","zh-tw":"馬拉威"},
  {"id":458,"alpha2":"my","alpha3":"mys","ar":"ماليزيا","bg":"Малайзия","cs":"Malajsie","da":"Malaysia","de":"Malaysia","el":"Μαλαισία","en":"Malaysia","eo":"Malajzio","es":"Malasia","et":"Malaisia","eu":"Malaysia","fi":"Malesia","fr":"Malaisie","hu":"Malajzia","hy":"Մալայզիա","it":"Malaysia","ja":"マレーシア","ko":"말레이시아","lt":"Malaizija","nl":"Maleisië","no":"Malaysia","pl":"Malezja","pt":"Malásia","ro":"Malaezia","ru":"Малайзия","sk":"Malajzia","sv":"Malaysia","th":"มาเลเซีย","uk":"Малайзія","zh":"马来西亚","zh-tw":"馬來西亞"},
  {"id":462,"alpha2":"mv","alpha3":"mdv","ar":"جزر المالديف","bg":"Малдиви","cs":"Maledivy","da":"Maldiverne","de":"Malediven","el":"Μαλδίβες","en":"Maldives","eo":"Maldivoj","es":"Maldivas","et":"Maldiivid","eu":"Maldivak","fi":"Malediivit","fr":"Maldives","hu":"Maldív-szigetek","hy":"Մալդիվներ","it":"Maldive","ja":"モルディブ","ko":"몰디브","lt":"Maldyvai","nl":"Malediven","no":"Maldivene","pl":"Malediwy","pt":"Maldivas","ro":"Maldive","ru":"Мальдивы","sk":"Maldivy","sv":"Maldiverna","th":"มัลดีฟส์","uk":"Мальдіви","zh":"马尔代夫","zh-tw":"馬爾地夫"},
  {"id":466,"alpha2":"ml","alpha3":"mli","ar":"مالي","bg":"Мали","cs":"Mali","da":"Mali","de":"Mali","el":"Μάλι","en":"Mali","eo":"Malio","es":"Malí","et":"Mali","eu":"Mali","fi":"Mali","fr":"Mali","hu":"Mali","hy":"Մալի","it":"Mali","ja":"マリ","ko":"말리","lt":"Malis","nl":"Mali","no":"Mali","pl":"Mali","pt":"Mali","ro":"Mali","ru":"Мали","sk":"Mali","sv":"Mali","th":"มาลี","uk":"Малі","zh":"马里","zh-tw":"馬利"},
  {"id":470,"alpha2":"mt","alpha3":"mlt","ar":"مالطا","bg":"Малта","cs":"Malta","da":"Malta","de":"Malta","el":"Μάλτα","en":"Malta","eo":"Malto","es":"Malta","et":"Malta","eu":"Malta","fi":"Malta","fr":"Malte","hu":"Málta","hy":"Մալթա","it":"Malta","ja":"マルタ","ko":"몰타","lt":"Malta","nl":"Malta","no":"Malta","pl":"Malta","pt":"Malta","ro":"Malta","ru":"Мальта","sk":"Malta","sv":"Malta","th":"มอลตา","uk":"Мальта","zh":"马耳他","zh-tw":"馬爾他"},
  {"id":584,"alpha2":"mh","alpha3":"mhl","ar":"جزر مارشال","bg":"Маршалови острови","cs":"Marshallovy ostrovy","da":"Marshalløerne","de":"Marshallinseln","el":"Νήσοι Μάρσαλ","en":"Marshall Islands","eo":"Marŝala Insularo","es":"Islas Marshall","et":"Marshalli Saared","eu":"Marshall Uharteak","fi":"Marshallinsaaret","fr":"Îles Marshall","hu":"Marshall-szigetek","hy":"Մարշալյան կղզիներ","it":"Isole Marshall","ja":"マーシャル諸島","ko":"마셜 제도","lt":"Maršalo salos","nl":"Marshalleilanden","no":"Marshalløyene","pl":"Wyspy Marshalla","pt":"Ilhas Marshall","ro":"Insulele Marshall","ru":"Маршалловы Острова","sk":"Marshallove ostrovy","sv":"Marshallöarna","th":"หมู่เกาะมาร์แชลล์","uk":"Маршаллові Острови","zh":"马绍尔群岛","zh-tw":"馬紹爾群島"},
  {"id":478,"alpha2":"mr","alpha3":"mrt","ar":"موريتانيا","bg":"Мавритания","cs":"Mauritánie","da":"Mauretanien","de":"Mauretanien","el":"Μαυριτανία","en":"Mauritania","eo":"Maŭritanio","es":"Mauritania","et":"Mauritaania","eu":"Mauritania","fi":"Mauritania","fr":"Mauritanie","hu":"Mauritánia","hy":"Մավրիտանիա","it":"Mauritania","ja":"モーリタニア","ko":"모리타니","lt":"Mauritanija","nl":"Mauritanië","no":"Mauritania","pl":"Mauretania","pt":"Mauritânia","ro":"Mauritania","ru":"Мавритания","sk":"Mauritánia","sv":"Mauretanien","th":"มอริเตเนีย","uk":"Мавританія","zh":"毛里塔尼亚","zh-tw":"茅利塔尼亞"},
  {"id":480,"alpha2":"mu","alpha3":"mus","ar":"موريشيوس","bg":"Мавриций","cs":"Mauricius","da":"Mauritius","de":"Mauritius","el":"Μαυρίκιος","en":"Mauritius","eo":"Maŭricio","es":"Mauricio","et":"Mauritius","eu":"Maurizio","fi":"Mauritius","fr":"Maurice","hu":"Mauritius","hy":"Մավրիկիոս","it":"Mauritius","ja":"モーリシャス","ko":"모리셔스","lt":"Mauricijus","nl":"Mauritius","no":"Mauritius","pl":"Mauritius","pt":"Ilhas Maurícias","ro":"Mauritius","ru":"Маврикий","sk":"Maurícius","sv":"Mauritius","th":"มอริเชียส","uk":"Маврикій","zh":"毛里求斯","zh-tw":"模里西斯"},
  {"id":484,"alpha2":"mx","alpha3":"mex","ar":"المكسيك","bg":"Мексико","cs":"Mexiko","da":"Mexico","de":"Mexiko","el":"Μεξικό","en":"Mexico","eo":"Meksiko","es":"México","et":"Mehhiko","eu":"Mexiko","fi":"Meksiko","fr":"Mexique","hu":"Mexikó","hy":"Մեքսիկա","it":"Messico","ja":"メキシコ","ko":"멕시코","lt":"Meksika","nl":"Mexico","no":"Mexico","pl":"Meksyk","pt":"México","ro":"Mexic","ru":"Мексика","sk":"Mexiko","sv":"Mexiko","th":"เม็กซิโก","uk":"Мексика","zh":"墨西哥","zh-tw":"墨西哥"},
  {"id":583,"alpha2":"fm","alpha3":"fsm","ar":"ولايات ميكرونيسيا المتحدة","bg":"Микронезия","cs":"Mikronésie","da":"Mikronesien","de":"Mikronesien","el":"Ομόσπονδες Πολιτείες της Μικρονησίας","en":"Micronesia (Federated States of)","eo":"Federacio de Mikronezio","es":"Micronesia","et":"Mikroneesia Liiduriigid","eu":"Mikronesiako Estatu Federatuak","fi":"Mikronesian liittovaltio","fr":"États fédérés de Micronésie","hu":"Mikronézia","hy":"Միկրոնեզիա","it":"Micronesia","ja":"ミクロネシア連邦","ko":"미크로네시아 연방","lt":"Mikronezija","nl":"Micronesië","no":"Mikronesiaføderasjonen","pl":"Mikronezja","pt":"Estados Federados da Micronésia","ro":"Micronezia","ru":"Микронезия","sk":"Mikronézia","sv":"Mikronesiska federationen","th":"ไมโครนีเชีย","uk":"Федеративні Штати Мікронезії","zh":"密克罗尼西亚联邦","zh-tw":"密克羅尼西亞聯邦"},
  {"id":504,"alpha2":"ma","alpha3":"mar","ar":"المغرب","bg":"Мароко","cs":"Maroko","da":"Marokko","de":"Marokko","el":"Μαρόκο","en":"Morocco","eo":"Maroko","es":"Marruecos","et":"Maroko","eu":"Maroko","fi":"Marokko","fr":"Maroc","hu":"Marokkó","hy":"Մարոկկո","it":"Marocco","ja":"モロッコ","ko":"모로코","lt":"Marokas","nl":"Marokko","no":"Marokko","pl":"Maroko","pt":"Marrocos","ro":"Maroc","ru":"Марокко","sk":"Maroko","sv":"Marocko","th":"โมร็อกโก","uk":"Марокко","zh":"摩洛哥","zh-tw":"摩洛哥"},
  {"id":498,"alpha2":"md","alpha3":"mda","ar":"مولدوفا","bg":"Молдова","cs":"Moldavsko","da":"Moldova","de":"Moldau","el":"Μολδαβία","en":"Moldova, Republic of","eo":"Moldavio","es":"Moldavia","et":"Moldova","eu":"Moldavia","fi":"Moldova","fr":"Moldavie","hu":"Moldova","hy":"Մոլդովա","it":"Moldavia","ja":"モルドバ共和国","ko":"몰도바","lt":"Moldavija","nl":"Moldavië","no":"Moldova","pl":"Mołdawia","pt":"Moldávia","ro":"Republica Moldova","ru":"Молдавия","sk":"Moldavsko","sv":"Moldavien","th":"มอลโดวา","uk":"Молдова","zh":"摩尔多瓦","zh-tw":"摩爾多瓦"},
  {"id":492,"alpha2":"mc","alpha3":"mco","ar":"موناكو","bg":"Монако","cs":"Monako","da":"Monaco","de":"Monaco","el":"Μονακό","en":"Monaco","eo":"Monako","es":"Mónaco","et":"Monaco","eu":"Monako","fi":"Monaco","fr":"Monaco","hu":"Monaco","hy":"Մոնակո","it":"Monaco","ja":"モナコ","ko":"모나코","lt":"Monakas","nl":"Monaco","no":"Monaco","pl":"Monako","pt":"Mónaco","ro":"Monaco","ru":"Монако","sk":"Monako","sv":"Monaco","th":"โมนาโก","uk":"Монако","zh":"摩纳哥","zh-tw":"摩納哥"},
  {"id":496,"alpha2":"mn","alpha3":"mng","ar":"منغوليا","bg":"Монголия","cs":"Mongolsko","da":"Mongoliet","de":"Mongolei","el":"Μογγολία","en":"Mongolia","eo":"Mongolio","es":"Mongolia","et":"Mongoolia","eu":"Mongolia","fi":"Mongolia","fr":"Mongolie","hu":"Mongólia","hy":"Մոնղոլիա","it":"Mongolia","ja":"モンゴル","ko":"몽골","lt":"Mongolija","nl":"Mongolië","no":"Mongolia","pl":"Mongolia","pt":"Mongólia","ro":"Mongolia","ru":"Монголия","sk":"Mongolsko","sv":"Mongoliet","th":"มองโกเลีย","uk":"Монголія","zh":"蒙古","zh-tw":"蒙古"},
  {"id":499,"alpha2":"me","alpha3":"mne","ar":"الجبل الأسود","bg":"Черна гора","cs":"Černá Hora","da":"Montenegro","de":"Montenegro","el":"Μαυροβούνιο","en":"Montenegro","eo":"Montenegro","es":"Montenegro","et":"Montenegro","eu":"Montenegro","fi":"Montenegro","fr":"Monténégro","hu":"Montenegró","hy":"Չեռնոգորիա","it":"Montenegro","ja":"モンテネグロ","ko":"몬테네그로","lt":"Juodkalnija","nl":"Montenegro","no":"Montenegro","pl":"Czarnogóra","pt":"Montenegro","ro":"Muntenegru","ru":"Черногория","sk":"Čierna Hora","sv":"Montenegro","th":"มอนเตเนโกร","uk":"Чорногорія","zh":"黑山","zh-tw":"蒙特內哥羅"},
  {"id":508,"alpha2":"mz","alpha3":"moz","ar":"موزمبيق","bg":"Мозамбик","cs":"Mosambik","da":"Mozambique","de":"Mosambik","el":"Μοζαμβίκη","en":"Mozambique","eo":"Mozambiko","es":"Mozambique","et":"Mosambiik","eu":"Mozambike","fi":"Mosambik","fr":"Mozambique","hu":"Mozambik","hy":"Մոզամբիկ","it":"Mozambico","ja":"モザンビーク","ko":"모잠비크","lt":"Mozambikas","nl":"Mozambique","no":"Mosambik","pl":"Mozambik","pt":"Moçambique","ro":"Mozambic","ru":"Мозамбик","sk":"Mozambik","sv":"Moçambique","th":"โมซัมบิก","uk":"Мозамбік","zh":"莫桑比克","zh-tw":"莫三比克"},
  {"id":104,"alpha2":"mm","alpha3":"mmr","ar":"ميانمار","bg":"Мианмар","cs":"Myanmar","da":"Burma","de":"Myanmar","el":"Μιανμάρ","en":"Myanmar","eo":"Birmo","es":"Birmania","et":"Birma","eu":"Myanmar","fi":"Myanmar","fr":"Birmanie","hu":"Mianmar","hy":"Մյանմա","it":"Birmania","ja":"ミャンマー","ko":"미얀마","lt":"Mianmaras","nl":"Myanmar","no":"Myanmar","pl":"Mjanma","pt":"Mianmar","ro":"Myanmar","ru":"Мьянма","sk":"Mjanmarsko","sv":"Myanmar","th":"พม่า","uk":"М'янма","zh":"缅甸","zh-tw":"緬甸"},
  {"id":516,"alpha2":"na","alpha3":"nam","ar":"ناميبيا","bg":"Намибия","cs":"Namibie","da":"Namibia","de":"Namibia","el":"Ναμίμπια","en":"Namibia","eo":"Namibio","es":"Namibia","et":"Namiibia","eu":"Namibia","fi":"Namibia","fr":"Namibie","hu":"Namíbia","hy":"Նամիբիա","it":"Namibia","ja":"ナミビア","ko":"나미비아","lt":"Namibija","nl":"Namibië","no":"Namibia","pl":"Namibia","pt":"Namíbia","ro":"Namibia","ru":"Намибия","sk":"Namíbia","sv":"Namibia","th":"นามิเบีย","uk":"Намібія","zh":"纳米比亚","zh-tw":"納米比亞"},
  {"id":520,"alpha2":"nr","alpha3":"nru","ar":"ناورو","bg":"Науру","cs":"Nauru","da":"Nauru","de":"Nauru","el":"Ναουρού","en":"Nauru","eo":"Nauro","es":"Nauru","et":"Nauru","eu":"Nauru","fi":"Nauru","fr":"Nauru","hu":"Nauru","hy":"Նաուրու","it":"Nauru","ja":"ナウル","ko":"나우루","lt":"Nauru","nl":"Nauru","no":"Nauru","pl":"Nauru","pt":"Nauru","ro":"Nauru","ru":"Науру","sk":"Nauru","sv":"Nauru","th":"นาอูรู","uk":"Науру","zh":"瑙鲁","zh-tw":"諾魯"},
  {"id":524,"alpha2":"np","alpha3":"npl","ar":"نيبال","bg":"Непал","cs":"Nepál","da":"Nepal","de":"Nepal","el":"Νεπάλ","en":"Nepal","eo":"Nepalo","es":"Nepal","et":"Nepal","eu":"Nepal","fi":"Nepal","fr":"Népal","hu":"Nepál","hy":"Նեպալ","it":"Nepal","ja":"ネパール","ko":"네팔","lt":"Nepalas","nl":"Nepal","no":"Nepal","pl":"Nepal","pt":"Nepal","ro":"Nepal","ru":"Непал","sk":"Nepál","sv":"Nepal","th":"เนปาล","uk":"Непал","zh":"尼泊尔","zh-tw":"尼泊爾"},
  {"id":528,"alpha2":"nl","alpha3":"nld","ar":"هولندا","bg":"Нидерландия","cs":"Nizozemsko","da":"Holland","de":"Niederlande","el":"Ολλανδία (Κάτω Χώρες)","en":"Netherlands","eo":"Nederlando","es":"Países Bajos","et":"Holland","eu":"Herbehereak","fi":"Alankomaat","fr":"Pays-Bas","hu":"Hollandia","hy":"Նիդերլանդներ","it":"Paesi Bassi","ja":"オランダ","ko":"네덜란드","lt":"Nyderlandai","nl":"Nederland","no":"Nederland","pl":"Holandia","pt":"Países Baixos","ro":"Țările de Jos","ru":"Нидерланды","sk":"Holandsko","sv":"Nederländerna","th":"เนเธอร์แลนด์","uk":"Нідерланди","zh":"荷兰","zh-tw":"荷蘭"},
  {"id":554,"alpha2":"nz","alpha3":"nzl","ar":"نيوزيلندا","bg":"Нова Зеландия","cs":"Nový Zéland","da":"New Zealand","de":"Neuseeland","el":"Νέα Ζηλανδία","en":"New Zealand","eo":"Nov-Zelando","es":"Nueva Zelanda","et":"Uus-Meremaa","eu":"Zeelanda Berria","fi":"Uusi-Seelanti","fr":"Nouvelle-Zélande","hu":"Új-Zéland","hy":"Նոր Զելանդիա","it":"Nuova Zelanda","ja":"ニュージーランド","ko":"뉴질랜드","lt":"Naujoji Zelandija","nl":"Nieuw-Zeeland","no":"New Zealand","pl":"Nowa Zelandia","pt":"Nova Zelândia","ro":"Noua Zeelandă","ru":"Новая Зеландия","sk":"Nový Zéland","sv":"Nya Zeeland","th":"นิวซีแลนด์","uk":"Нова Зеландія","zh":"新西兰","zh-tw":"紐西蘭"},
  {"id":558,"alpha2":"ni","alpha3":"nic","ar":"نيكاراغوا","bg":"Никарагуа","cs":"Nikaragua","da":"Nicaragua","de":"Nicaragua","el":"Νικαράγουα","en":"Nicaragua","eo":"Nikaragvo","es":"Nicaragua","et":"Nicaragua","eu":"Nikaragua","fi":"Nicaragua","fr":"Nicaragua","hu":"Nicaragua","hy":"Նիկարագուա","it":"Nicaragua","ja":"ニカラグア","ko":"니카라과","lt":"Nikaragva","nl":"Nicaragua","no":"Nicaragua","pl":"Nikaragua","pt":"Nicarágua","ro":"Nicaragua","ru":"Никарагуа","sk":"Nikaragua","sv":"Nicaragua","th":"นิการากัว","uk":"Нікарагуа","zh":"尼加拉瓜","zh-tw":"尼加拉瓜"},
  {"id":562,"alpha2":"ne","alpha3":"ner","ar":"النيجر","bg":"Нигер","cs":"Niger","da":"Niger","de":"Niger","el":"Νίγηρας","en":"Niger","eo":"Niĝero","es":"Níger","et":"Niger","eu":"Niger","fi":"Niger","fr":"Niger","hu":"Niger","hy":"Նիգեր","it":"Niger","ja":"ニジェール","ko":"니제르","lt":"Nigeris","nl":"Niger","no":"Niger","pl":"Niger","pt":"Níger","ro":"Niger","ru":"Нигер","sk":"Niger","sv":"Niger","th":"ไนเจอร์","uk":"Нігер","zh":"尼日尔","zh-tw":"尼日"},
  {"id":566,"alpha2":"ng","alpha3":"nga","ar":"نيجيريا","bg":"Нигерия","cs":"Nigérie","da":"Nigeria","de":"Nigeria","el":"Νιγηρία","en":"Nigeria","eo":"Niĝerio","es":"Nigeria","et":"Nigeeria","eu":"Nigeria","fi":"Nigeria","fr":"Nigeria","hu":"Nigéria","hy":"Նիգերիա","it":"Nigeria","ja":"ナイジェリア","ko":"나이지리아","lt":"Nigerija","nl":"Nigeria","no":"Nigeria","pl":"Nigeria","pt":"Nigéria","ro":"Nigeria","ru":"Нигерия","sk":"Nigéria","sv":"Nigeria","th":"ไนจีเรีย","uk":"Нігерія","zh":"尼日利亚","zh-tw":"奈及利亞"},
  {"id":578,"alpha2":"no","alpha3":"nor","ar":"النرويج","bg":"Норвегия","cs":"Norsko","da":"Norge","de":"Norwegen","el":"Νορβηγία","en":"Norway","eo":"Norvegio","es":"Noruega","et":"Norra","eu":"Norvegia","fi":"Norja","fr":"Norvège","hu":"Norvégia","hy":"Նորվեգիա","it":"Norvegia","ja":"ノルウェー","ko":"노르웨이","lt":"Norvegija","nl":"Noorwegen","no":"Norge","pl":"Norwegia","pt":"Noruega","ro":"Norvegia","ru":"Норвегия","sk":"Nórsko","sv":"Norge","th":"นอร์เวย์","uk":"Норвегія","zh":"挪威","zh-tw":"挪威"},
  {"id":512,"alpha2":"om","alpha3":"omn","ar":"عمان","bg":"Оман","cs":"Omán","da":"Oman","de":"Oman","el":"Ομάν","en":"Oman","eo":"Omano","es":"Omán","et":"Omaan","eu":"Oman","fi":"Oman","fr":"Oman","hu":"Omán","hy":"Օման","it":"Oman","ja":"オマーン","ko":"오만","lt":"Omanas","nl":"Oman","no":"Oman","pl":"Oman","pt":"Omã","ro":"Oman","ru":"Оман","sk":"Omán","sv":"Oman","th":"โอมาน","uk":"Оман","zh":"阿曼","zh-tw":"阿曼"},
  {"id":586,"alpha2":"pk","alpha3":"pak","ar":"باكستان","bg":"Пакистан","cs":"Pákistán","da":"Pakistan","de":"Pakistan","el":"Πακιστάν","en":"Pakistan","eo":"Pakistano","es":"Pakistán","et":"Pakistan","eu":"Pakistan","fi":"Pakistan","fr":"Pakistan","hu":"Pakisztán","hy":"Պակիստան","it":"Pakistan","ja":"パキスタン","ko":"파키스탄","lt":"Pakistanas","nl":"Pakistan","no":"Pakistan","pl":"Pakistan","pt":"Paquistão","ro":"Pakistan","ru":"Пакистан","sk":"Pakistan","sv":"Pakistan","th":"ปากีสถาน","uk":"Пакистан","zh":"巴基斯坦","zh-tw":"巴基斯坦"},
  {"id":585,"alpha2":"pw","alpha3":"plw","ar":"بالاو","bg":"Палау","cs":"Palau","da":"Palau","de":"Palau","el":"Παλάου","en":"Palau","eo":"Palaŭo","es":"Palaos","et":"Belau","eu":"Palau","fi":"Palau","fr":"Palaos","hu":"Palau","hy":"Պալաու","it":"Palau","ja":"パラオ","ko":"팔라우","lt":"Palau","nl":"Palau","no":"Palau","pl":"Palau","pt":"Palau","ro":"Palau","ru":"Палау","sk":"Palau","sv":"Palau","th":"ปาเลา","uk":"Палау","zh":"帕劳","zh-tw":"帛琉"},
  {"id":591,"alpha2":"pa","alpha3":"pan","ar":"بنما","bg":"Панама","cs":"Panama","da":"Panama","de":"Panama","el":"Παναμάς","en":"Panama","eo":"Panamo","es":"Panamá","et":"Panama","eu":"Panama","fi":"Panama","fr":"Panama","hu":"Panama","hy":"Պանամա","it":"Panama","ja":"パナマ","ko":"파나마","lt":"Panama","nl":"Panama","no":"Panama","pl":"Panama","pt":"Panamá","ro":"Panama","ru":"Панама","sk":"Panama","sv":"Panama","th":"ปานามา","uk":"Панама","zh":"巴拿马","zh-tw":"巴拿馬"},
  {"id":598,"alpha2":"pg","alpha3":"png","ar":"بابوا غينيا الجديدة","bg":"Папуа Нова Гвинея","cs":"Papua Nová Guinea","da":"Papua Ny Guinea","de":"Papua-Neuguinea","el":"Παπούα Νέα Γουινέα","en":"Papua New Guinea","eo":"Papuo-Nov-Gvineo","es":"Papúa Nueva Guinea","et":"Paapua Uus-Guinea","eu":"Papua Ginea Berria","fi":"Papua-Uusi-Guinea","fr":"Papouasie-Nouvelle-Guinée","hu":"Pápua Új-Guinea","hy":"Պապուա Նոր Գվինեա","it":"Papua Nuova Guinea","ja":"パプアニューギニア","ko":"파푸아뉴기니","lt":"Papua Naujoji Gvinėja","nl":"Papoea-Nieuw-Guinea","no":"Papua Ny-Guinea","pl":"Papua-Nowa Gwinea","pt":"Papua-Nova Guiné","ro":"Papua Noua Guinee","ru":"Папуа — Новая Гвинея","sk":"Papua-Nová Guinea","sv":"Papua Nya Guinea","th":"ปาปัวนิวกินี","uk":"Папуа Нова Гвінея","zh":"巴布亚新几内亚","zh-tw":"巴布亞紐幾內亞"},
  {"id":600,"alpha2":"py","alpha3":"pry","ar":"باراغواي","bg":"Парагвай","cs":"Paraguay","da":"Paraguay","de":"Paraguay","el":"Παραγουάη","en":"Paraguay","eo":"Paragvajo","es":"Paraguay","et":"Paraguay","eu":"Paraguai","fi":"Paraguay","fr":"Paraguay","hu":"Paraguay","hy":"Պարագվայ","it":"Paraguay","ja":"パラグアイ","ko":"파라과이","lt":"Paragvajus","nl":"Paraguay","no":"Paraguay","pl":"Paragwaj","pt":"Paraguai","ro":"Paraguay","ru":"Парагвай","sk":"Paraguaj","sv":"Paraguay","th":"ปารากวัย","uk":"Парагвай","zh":"巴拉圭","zh-tw":"巴拉圭"},
  {"id":604,"alpha2":"pe","alpha3":"per","ar":"بيرو","bg":"Перу","cs":"Peru","da":"Peru","de":"Peru","el":"Περού","en":"Peru","eo":"Peruo","es":"Perú","et":"Peruu","eu":"Peru","fi":"Peru","fr":"Pérou","hu":"Peru","hy":"Պերու","it":"Perù","ja":"ペルー","ko":"페루","lt":"Peru","nl":"Peru","no":"Peru","pl":"Peru","pt":"Peru","ro":"Peru","ru":"Перу","sk":"Peru","sv":"Peru","th":"เปรู","uk":"Перу","zh":"秘鲁","zh-tw":"秘魯"},
  {"id":608,"alpha2":"ph","alpha3":"phl","ar":"الفلبين","bg":"Филипини","cs":"Filipíny","da":"Filippinerne","de":"Philippinen","el":"Φιλιππίνες","en":"Philippines","eo":"Filipinoj","es":"Filipinas","et":"Filipiinid","eu":"Filipinak","fi":"Filippiinit","fr":"Philippines","hu":"Fülöp-szigetek","hy":"Ֆիլիպիններ","it":"Filippine","ja":"フィリピン","ko":"필리핀","lt":"Filipinai","nl":"Filipijnen","no":"Filippinene","pl":"Filipiny","pt":"Filipinas","ro":"Filipine","ru":"Филиппины","sk":"Filipíny","sv":"Filippinerna","th":"ฟิลิปปินส์","uk":"Філіппіни","zh":"菲律宾","zh-tw":"菲律賓"},
  {"id":616,"alpha2":"pl","alpha3":"pol","ar":"بولندا","bg":"Полша","cs":"Polsko","da":"Polen","de":"Polen","el":"Πολωνία","en":"Poland","eo":"Pollando","es":"Polonia","et":"Poola","eu":"Polonia","fi":"Puola","fr":"Pologne","hu":"Lengyelország","hy":"Լեհաստան","it":"Polonia","ja":"ポーランド","ko":"폴란드","lt":"Lenkija","nl":"Polen","no":"Polen","pl":"Polska","pt":"Polónia","ro":"Polonia","ru":"Польша","sk":"Poľsko","sv":"Polen","th":"โปแลนด์","uk":"Польща","zh":"波兰","zh-tw":"波蘭"},
  {"id":620,"alpha2":"pt","alpha3":"prt","ar":"البرتغال","bg":"Португалия","cs":"Portugalsko","da":"Portugal","de":"Portugal","el":"Πορτογαλία","en":"Portugal","eo":"Portugalio","es":"Portugal","et":"Portugal","eu":"Portugal","fi":"Portugali","fr":"Portugal","hu":"Portugália","hy":"Պորտուգալիա","it":"Portogallo","ja":"ポルトガル","ko":"포르투갈","lt":"Portugalija","nl":"Portugal","no":"Portugal","pl":"Portugalia","pt":"Portugal","ro":"Portugalia","ru":"Португалия","sk":"Portugalsko","sv":"Portugal","th":"โปรตุเกส","uk":"Португалія","zh":"葡萄牙","zh-tw":"葡萄牙"},
  {"id":634,"alpha2":"qa","alpha3":"qat","ar":"قطر","bg":"Катар","cs":"Katar","da":"Qatar","de":"Katar","el":"Κατάρ","en":"Qatar","eo":"Kataro","es":"Catar","et":"Katar","eu":"Qatar","fi":"Qatar","fr":"Qatar","hu":"Katar","hy":"Կատար","it":"Qatar","ja":"カタール","ko":"카타르","lt":"Kataras","nl":"Qatar","no":"Qatar","pl":"Katar","pt":"Catar","ro":"Qatar","ru":"Катар","sk":"Katar","sv":"Qatar","th":"กาตาร์","uk":"Катар","zh":"卡塔尔","zh-tw":"卡達"},
  {"id":642,"alpha2":"ro","alpha3":"rou","ar":"رومانيا","bg":"Румъния","cs":"Rumunsko","da":"Rumænien","de":"Rumänien","el":"Ρουμανία","en":"Romania","eo":"Rumanio","es":"Rumania","et":"Rumeenia","eu":"Errumania","fi":"Romania","fr":"Roumanie","hu":"Románia","hy":"Ռումինիա","it":"Romania","ja":"ルーマニア","ko":"루마니아","lt":"Rumunija","nl":"Roemenië","no":"Romania","pl":"Rumunia","pt":"Roménia","ro":"România","ru":"Румыния","sk":"Rumunsko","sv":"Rumänien","th":"โรมาเนีย","uk":"Румунія","zh":"罗马尼亚","zh-tw":"羅馬尼亞"},
  {"id":643,"alpha2":"ru","alpha3":"rus","ar":"روسيا","bg":"Русия","cs":"Rusko","da":"Rusland","de":"Russland","el":"Ρωσία","en":"Russian Federation","eo":"Rusio","es":"Rusia","et":"Venemaa","eu":"Errusia","fi":"Venäjä","fr":"Russie","hu":"Oroszország","hy":"Ռուսաստան","it":"Russia","ja":"ロシア連邦","ko":"러시아","lt":"Rusija","nl":"Rusland","no":"Russland","pl":"Rosja","pt":"Rússia","ro":"Rusia","ru":"Россия","sk":"Rusko","sv":"Ryssland","th":"รัสเซีย","uk":"Росія","zh":"俄罗斯","zh-tw":"俄羅斯"},
  {"id":646,"alpha2":"rw","alpha3":"rwa","ar":"رواندا","bg":"Руанда","cs":"Rwanda","da":"Rwanda","de":"Ruanda","el":"Ρουάντα","en":"Rwanda","eo":"Ruando","es":"Ruanda","et":"Rwanda","eu":"Ruanda","fi":"Ruanda","fr":"Rwanda","hu":"Ruanda","hy":"Ռուանդա","it":"Ruanda","ja":"ルワンダ","ko":"르완다","lt":"Ruanda","nl":"Rwanda","no":"Rwanda","pl":"Rwanda","pt":"Ruanda","ro":"Rwanda","ru":"Руанда","sk":"Rwanda","sv":"Rwanda","th":"รวันดา","uk":"Руанда","zh":"卢旺达","zh-tw":"盧安達"},
  {"id":659,"alpha2":"kn","alpha3":"kna","ar":"سانت كيتس ونيفيس","bg":"Сейнт Китс и Невис","cs":"Svatý Kryštof a Nevis","da":"Saint Kitts og Nevis","de":"St. Kitts und Nevis","el":"Άγιος Χριστόφορος και Νέβις","en":"Saint Kitts and Nevis","eo":"Sankta-Kito kaj Neviso","es":"San Cristóbal y Nieves","et":"Saint Kitts ja Nevis","eu":"Saint Kitts eta Nevis","fi":"Saint Kitts ja Nevis","fr":"Saint-Christophe-et-Niévès","hu":"Saint Kitts és Nevis","hy":"Սենտ Կիտս և Նևիս","it":"Saint Kitts e Nevis","ja":"セントクリストファー・ネイビス","ko":"세인트키츠 네비스","lt":"Sent Kitsas ir Nevis","nl":"Saint Kitts en Nevis","no":"Saint Kitts og Nevis","pl":"Saint Kitts i Nevis","pt":"São Cristóvão e Neves","ro":"Sfântul Kitts și Nevis","ru":"Сент-Китс и Невис","sk":"Svätý Krištof a Nevis","sv":"Saint Kitts och Nevis","th":"เซนต์คิตส์และเนวิส","uk":"Сент-Кіттс і Невіс","zh":"圣基茨和尼维斯","zh-tw":"聖克里斯多福及尼維斯"},
  {"id":662,"alpha2":"lc","alpha3":"lca","ar":"سانت لوسيا","bg":"Сейнт Лусия","cs":"Svatá Lucie","da":"Saint Lucia","de":"St. Lucia","el":"Αγία Λουκία","en":"Saint Lucia","eo":"Sankta Lucio","es":"Santa Lucía","et":"Saint Lucia","eu":"Santa Luzia","fi":"Saint Lucia","fr":"Sainte-Lucie","hu":"Saint Lucia","hy":"Սենթ Լյուսիա","it":"Saint Lucia","ja":"セントルシア","ko":"세인트루시아","lt":"Sent Lusija","nl":"Saint Lucia","no":"Saint Lucia","pl":"Saint Lucia","pt":"Santa Lúcia","ro":"Sfânta Lucia","ru":"Сент-Люсия","sk":"Svätá Lucia","sv":"Saint Lucia","th":"เซนต์ลูเชีย","uk":"Сент-Люсія","zh":"圣卢西亚","zh-tw":"聖露西亞"},
  {"id":670,"alpha2":"vc","alpha3":"vct","ar":"سانت فينسنت والغرينادين","bg":"Сейнт Винсент и Гренадини","cs":"Svatý Vincenc a Grenadiny","da":"Saint Vincent og Grenadinerne","de":"St. Vincent und die Grenadinen","el":"Άγιος Βικέντιος και Γρεναδίνες","en":"Saint Vincent and the Grenadines","eo":"Sankta Vincento kaj la Grenadinoj","es":"San Vicente y las Granadinas","et":"Saint Vincent ja Grenadiinid","eu":"Saint Vincent eta Grenadinak","fi":"Saint Vincent ja Grenadiinit","fr":"Saint-Vincent-et-les-Grenadines","hu":"Saint Vincent és a Grenadine-szigetek","hy":"Սենտ Վինսենտ և Գրենադիներ","it":"Saint Vincent e Grenadine","ja":"セントビンセントおよびグレナディーン諸島","ko":"세인트빈센트 그레나딘","lt":"Sent Vinsentas ir Grenadinai","nl":"Saint Vincent en de Grenadines","no":"Saint Vincent og Grenadinene","pl":"Saint Vincent i Grenadyny","pt":"São Vicente e Granadinas","ro":"Sfântul Vincent și Grenadine","ru":"Сент-Винсент и Гренадины","sk":"Svätý Vincent a Grenadíny","sv":"Saint Vincent och Grenadinerna","th":"เซนต์วินเซนต์และเกรนาดีนส์","uk":"Сент-Вінсент і Гренадини","zh":"圣文森特和格林纳丁斯","zh-tw":"聖文森及格瑞那丁"},
  {"id":882,"alpha2":"ws","alpha3":"wsm","ar":"ساموا","bg":"Самоа","cs":"Samoa","da":"Samoa","de":"Samoa","el":"Σαμόα","en":"Samoa","eo":"Samoo","es":"Samoa","et":"Samoa","eu":"Samoa","fi":"Samoa","fr":"Samoa","hu":"Szamoa","hy":"Սամոա","it":"Samoa","ja":"サモア","ko":"사모아","lt":"Samoa","nl":"Samoa","no":"Samoa","pl":"Samoa","pt":"Samoa","ro":"Samoa","ru":"Самоа","sk":"Samoa","sv":"Samoa","th":"ซามัว","uk":"Самоа","zh":"萨摩亚","zh-tw":"薩摩亞"},
  {"id":674,"alpha2":"sm","alpha3":"smr","ar":"سان مارينو","bg":"Сан Марино","cs":"San Marino","da":"San Marino","de":"San Marino","el":"Άγιος Μαρίνος","en":"San Marino","eo":"San-Marino","es":"San Marino","et":"San Marino","eu":"San Marino","fi":"San Marino","fr":"Saint-Marin","hu":"San Marino","hy":"Սան Մարինո","it":"San Marino","ja":"サンマリノ","ko":"산마리노","lt":"San Marinas","nl":"San Marino","no":"San Marino","pl":"San Marino","pt":"San Marino","ro":"San Marino","ru":"Сан-Марино","sk":"San Maríno","sv":"San Marino","th":"ซานมารีโน","uk":"Сан-Марино","zh":"圣马力诺","zh-tw":"聖馬利諾"},
  {"id":678,"alpha2":"st","alpha3":"stp","ar":"ساو تومي وبرينسيب","bg":"Сао Томе и Принсипи","cs":"Svatý Tomáš a Princův ostrov","da":"São Tomé og Príncipe","de":"São Tomé und Príncipe","el":"Σάο Τομέ και Πρίνσιπε","en":"Sao Tome and Principe","eo":"Santomeo kaj Principeo","es":"Santo Tomé y Príncipe","et":"São Tomé ja Príncipe","eu":"Sao Tome eta Principe","fi":"São Tomé ja Príncipe","fr":"Sao Tomé-et-Principe","hu":"São Tomé és Príncipe","hy":"Սան Տոմե և Պրինսիպի","it":"São Tomé e Príncipe","ja":"サントメ・プリンシペ","ko":"상투메 프린시페","lt":"San Tomė ir Prinsipė","nl":"Sao Tomé en Principe","no":"São Tomé og Príncipe","pl":"Wyspy Świętego Tomasza i Książęca","pt":"São Tomé e Príncipe","ro":"Sao Tome și Principe","ru":"Сан-Томе и Принсипи","sk":"Svätý Tomáš a Princov ostrov","sv":"São Tomé och Príncipe","th":"เซาตูแมอีปริงซีป","uk":"Сан-Томе і Принсіпі","zh":"圣多美和普林西比","zh-tw":"聖多美普林西比"},
  {"id":682,"alpha2":"sa","alpha3":"sau","ar":"السعودية","bg":"Саудитска Арабия","cs":"Saúdská Arábie","da":"Saudi-Arabien","de":"Saudi-Arabien","el":"Σαουδική Αραβία","en":"Saudi Arabia","eo":"Sauda Arabio","es":"Arabia Saudita","et":"Saudi Araabia","eu":"Saudi Arabia","fi":"Saudi-Arabia","fr":"Arabie saoudite","hu":"Szaúd-Arábia","hy":"Սաուդյան Արաբիա","it":"Arabia Saudita","ja":"サウジアラビア","ko":"사우디아라비아","lt":"Saudo Arabija","nl":"Saoedi-Arabië","no":"Saudi-Arabia","pl":"Arabia Saudyjska","pt":"Arábia Saudita","ro":"Arabia Saudită","ru":"Саудовская Аравия","sk":"Saudská Arábia","sv":"Saudiarabien","th":"ซาอุดีอาระเบีย","uk":"Саудівська Аравія","zh":"沙特阿拉伯","zh-tw":"沙烏地阿拉伯"},
  {"id":686,"alpha2":"sn","alpha3":"sen","ar":"السنغال","bg":"Сенегал","cs":"Senegal","da":"Senegal","de":"Senegal","el":"Σενεγάλη","en":"Senegal","eo":"Senegalo","es":"Senegal","et":"Senegal","eu":"Senegal","fi":"Senegal","fr":"Sénégal","hu":"Szenegál","hy":"Սենեգալ","it":"Senegal","ja":"セネガル","ko":"세네갈","lt":"Senegalas","nl":"Senegal","no":"Senegal","pl":"Senegal","pt":"Senegal","ro":"Senegal","ru":"Сенегал","sk":"Senegal","sv":"Senegal","th":"เซเนกัล","uk":"Сенегал","zh":"塞内加尔","zh-tw":"塞內加爾"},
  {"id":688,"alpha2":"rs","alpha3":"srb","ar":"صربيا","bg":"Сърбия","cs":"Srbsko","da":"Serbien","de":"Serbien","el":"Σερβία","en":"Serbia","eo":"Serbio","es":"Serbia","et":"Serbia","eu":"Serbia","fi":"Serbia","fr":"Serbie","hu":"Szerbia","hy":"Սերբիա","it":"Serbia","ja":"セルビア","ko":"세르비아","lt":"Serbija","nl":"Servië","no":"Serbia","pl":"Serbia","pt":"Sérvia","ro":"Serbia","ru":"Сербия","sk":"Srbsko","sv":"Serbien","th":"เซอร์เบีย","uk":"Сербія","zh":"塞尔维亚","zh-tw":"塞爾維亞"},
  {"id":690,"alpha2":"sc","alpha3":"syc","ar":"سيشل","bg":"Сейшелски острови","cs":"Seychely","da":"Seychellerne","de":"Seychellen","el":"Σεϋχέλλες","en":"Seychelles","eo":"Sejŝeloj","es":"Seychelles","et":"Seišellid","eu":"Seychelleak","fi":"Seychellit","fr":"Seychelles","hu":"Seychelle-szigetek","hy":"Սեյշելներ","it":"Seychelles","ja":"セーシェル","ko":"세이셸","lt":"Seišeliai","nl":"Seychellen","no":"Seychellene","pl":"Seszele","pt":"Seicheles","ro":"Seychelles","ru":"Сейшельские Острова","sk":"Seychely","sv":"Seychellerna","th":"เซเชลส์","uk":"Сейшельські Острови","zh":"塞舌尔","zh-tw":"塞席爾"},
  {"id":694,"alpha2":"sl","alpha3":"sle","ar":"سيراليون","bg":"Сиера Леоне","cs":"Sierra Leone","da":"Sierra Leone","de":"Sierra Leone","el":"Σιέρα Λεόνε","en":"Sierra Leone","eo":"Sieraleono","es":"Sierra Leona","et":"Sierra Leone","eu":"Sierra Leona","fi":"Sierra Leone","fr":"Sierra Leone","hu":"Sierra Leone","hy":"Սիեռա Լեոնե","it":"Sierra Leone","ja":"シエラレオネ","ko":"시에라리온","lt":"Siera Leonė","nl":"Sierra Leone","no":"Sierra Leone","pl":"Sierra Leone","pt":"Serra Leoa","ro":"Sierra Leone","ru":"Сьерра-Леоне","sk":"Sierra Leone","sv":"Sierra Leone","th":"เซียร์ราลีโอน","uk":"Сьєрра-Леоне","zh":"塞拉利昂","zh-tw":"獅子山"},
  {"id":702,"alpha2":"sg","alpha3":"sgp","ar":"سنغافورة","bg":"Сингапур","cs":"Singapur","da":"Singapore","de":"Singapur","el":"Σιγκαπούρη","en":"Singapore","eo":"Singapuro","es":"Singapur","et":"Singapur","eu":"Singapur","fi":"Singapore","fr":"Singapour","hu":"Szingapúr","hy":"Սինգապուր","it":"Singapore","ja":"シンガポール","ko":"싱가포르","lt":"Singapūras","nl":"Singapore","no":"Singapore","pl":"Singapur","pt":"Singapura","ro":"Singapore","ru":"Сингапур","sk":"Singapur","sv":"Singapore","th":"สิงคโปร์","uk":"Сінгапур","zh":"新加坡","zh-tw":"新加坡"},
  {"id":703,"alpha2":"sk","alpha3":"svk","ar":"سلوفاكيا","bg":"Словакия","cs":"Slovensko","da":"Slovakiet","de":"Slowakei","el":"Σλοβακία","en":"Slovakia","eo":"Slovakio","es":"Eslovaquia","et":"Slovakkia","eu":"Eslovakia","fi":"Slovakia","fr":"Slovaquie","hu":"Szlovákia","hy":"Սլովակիա","it":"Slovacchia","ja":"スロバキア","ko":"슬로바키아","lt":"Slovakija","nl":"Slowakije","no":"Slovakia","pl":"Słowacja","pt":"Eslováquia","ro":"Slovacia","ru":"Словакия","sk":"Slovensko","sv":"Slovakien","th":"สโลวาเกีย","uk":"Словаччина","zh":"斯洛伐克","zh-tw":"斯洛伐克"},
  {"id":705,"alpha2":"si","alpha3":"svn","ar":"سلوفينيا","bg":"Словения","cs":"Slovinsko","da":"Slovenien","de":"Slowenien","el":"Σλοβενία","en":"Slovenia","eo":"Slovenio","es":"Eslovenia","et":"Sloveenia","eu":"Eslovenia","fi":"Slovenia","fr":"Slovénie","hu":"Szlovénia","hy":"Սլովենիա","it":"Slovenia","ja":"スロベニア","ko":"슬로베니아","lt":"Slovėnija","nl":"Slovenië","no":"Slovenia","pl":"Słowenia","pt":"Eslovênia","ro":"Slovenia","ru":"Словения","sk":"Slovinsko","sv":"Slovenien","th":"สโลวีเนีย","uk":"Словенія","zh":"斯洛文尼亚","zh-tw":"斯洛維尼亞"},
  {"id":90,"alpha2":"sb","alpha3":"slb","ar":"جزر سليمان","bg":"Соломонови острови","cs":"Šalomounovy ostrovy","da":"Salomonøerne","de":"Salomonen","el":"Νήσοι Σολομώντα","en":"Solomon Islands","eo":"Salomonoj","es":"Islas Salomón","et":"Saalomoni Saared","eu":"Salomon Uharteak","fi":"Salomonsaaret","fr":"Îles Salomon","hu":"Salamon-szigetek","hy":"Սողոմոնյան Կղզիներ","it":"Isole Salomone","ja":"ソロモン諸島","ko":"솔로몬 제도","lt":"Saliamono Salos","nl":"Salomonseilanden","no":"Salomonøyene","pl":"Wyspy Salomona","pt":"Ilhas Salomão","ro":"Insulele Solomon","ru":"Соломоновы Острова","sk":"Šalamúnove ostrovy","sv":"Salomonöarna","th":"หมู่เกาะโซโลมอน","uk":"Соломонові Острови","zh":"所罗门群岛","zh-tw":"索羅門群島"},
  {"id":706,"alpha2":"so","alpha3":"som","ar":"الصومال","bg":"Сомалия","cs":"Somálsko","da":"Somalia","de":"Somalia","el":"Σομαλία","en":"Somalia","eo":"Somalio","es":"Somalia","et":"Somaalia","eu":"Somalia","fi":"Somalia","fr":"Somalie","hu":"Szomália","hy":"Սոմալի","it":"Somalia","ja":"ソマリア","ko":"소말리아","lt":"Somalis","nl":"Somalië","no":"Somalia","pl":"Somalia","pt":"Somália","ro":"Somalia","ru":"Сомали","sk":"Somálsko","sv":"Somalia","th":"โซมาเลีย","uk":"Сомалі","zh":"索马里","zh-tw":"索馬利亞"},
  {"id":710,"alpha2":"za","alpha3":"zaf","ar":"جنوب أفريقيا","bg":"ЮАР","cs":"Jihoafrická republika","da":"Sydafrika","de":"Südafrika","el":"Νότια Αφρική","en":"South Africa","eo":"Sud-Afriko","es":"Sudáfrica","et":"Lõuna-Aafrika Vabariik","eu":"Hegoafrika","fi":"Etelä-Afrikka","fr":"Afrique du Sud","hu":"Dél-afrikai Köztársaság","hy":"Հարավաֆրիկյան Հանրապետություն","it":"Sudafrica","ja":"南アフリカ","ko":"남아프리카 공화국","lt":"PAR","nl":"Zuid-Afrika","no":"Sør-Afrika","pl":"Południowa Afryka","pt":"África do Sul","ro":"Africa de Sud","ru":"ЮАР","sk":"Južná Afrika","sv":"Sydafrika","th":"แอฟริกาใต้","uk":"ПАР","zh":"南非","zh-tw":"南非"},
  {"id":728,"alpha2":"ss","alpha3":"ssd","ar":"جنوب السودان","bg":"Южен Судан","cs":"Jižní Súdán","da":"Sydsudan","de":"Südsudan","el":"Νότιο Σουδάν","en":"South Sudan","eo":"Sud-Sudano","es":"Sudán del Sur","et":"Lõuna-Sudaan","eu":"Hego Sudan","fi":"Etelä-Sudan","fr":"Soudan du Sud","hu":"Dél-Szudán","hy":"Հարավային Սուդան","it":"Sudan del Sud","ja":"南スーダン","ko":"남수단","lt":"Pietų Sudanas","nl":"Zuid-Soedan","no":"Sør-Sudan","pl":"Sudan Południowy","pt":"Sudão do Sul","ro":"Sudanul de Sud","ru":"Южный Судан","sk":"Južný Sudán","sv":"Sydsudan","th":"ซูดานใต้","uk":"Південний Судан","zh":"南苏丹","zh-tw":"南蘇丹"},
  {"id":724,"alpha2":"es","alpha3":"esp","ar":"إسبانيا","bg":"Испания","cs":"Španělsko","da":"Spanien","de":"Spanien","el":"Ισπανία","en":"Spain","eo":"Hispanio","es":"España","et":"Hispaania","eu":"Espainia","fi":"Espanja","fr":"Espagne","hu":"Spanyolország","hy":"Իսպանիա","it":"Spagna","ja":"スペイン","ko":"스페인","lt":"Ispanija","nl":"Spanje","no":"Spania","pl":"Hiszpania","pt":"Espanha","ro":"Spania","ru":"Испания","sk":"Španielsko","sv":"Spanien","th":"สเปน","uk":"Іспанія","zh":"西班牙","zh-tw":"西班牙"},
  {"id":144,"alpha2":"lk","alpha3":"lka","ar":"سريلانكا","bg":"Шри Ланка","cs":"Srí Lanka","da":"Sri Lanka","de":"Sri Lanka","el":"Σρι Λάνκα","en":"Sri Lanka","eo":"Srilanko","es":"Sri Lanka","et":"Sri Lanka","eu":"Sri Lanka","fi":"Sri Lanka","fr":"Sri Lanka","hu":"Srí Lanka","hy":"Շրի Լանկա","it":"Sri Lanka","ja":"スリランカ","ko":"스리랑카","lt":"Šri Lanka","nl":"Sri Lanka","no":"Sri Lanka","pl":"Sri Lanka","pt":"Seri Lanca","ro":"Sri Lanka","ru":"Шри-Ланка","sk":"Srí Lanka","sv":"Sri Lanka","th":"ศรีลังกา","uk":"Шрі-Ланка","zh":"斯里兰卡","zh-tw":"斯里蘭卡"},
  {"id":729,"alpha2":"sd","alpha3":"sdn","ar":"السودان","bg":"Судан","cs":"Súdán","da":"Sudan","de":"Sudan","el":"Σουδάν","en":"Sudan","eo":"Sudano","es":"Sudán","et":"Sudaan","eu":"Sudan","fi":"Sudan","fr":"Soudan","hu":"Szudán","hy":"Սուդան","it":"Sudan","ja":"スーダン","ko":"수단","lt":"Sudanas","nl":"Soedan","no":"Sudan","pl":"Sudan","pt":"Sudão","ro":"Sudan","ru":"Судан","sk":"Sudán","sv":"Sudan","th":"ซูดาน","uk":"Судан","zh":"苏丹","zh-tw":"蘇丹"},
  {"id":740,"alpha2":"sr","alpha3":"sur","ar":"سورينام","bg":"Суринам","cs":"Surinam","da":"Surinam","de":"Suriname","el":"Σουρινάμ","en":"Suriname","eo":"Surinamo","es":"Surinam","et":"Suriname","eu":"Surinam","fi":"Suriname","fr":"Suriname","hu":"Suriname","hy":"Սուրինամ","it":"Suriname","ja":"スリナム","ko":"수리남","lt":"Surinamas","nl":"Suriname","no":"Surinam","pl":"Surinam","pt":"Suriname","ro":"Surinam","ru":"Суринам","sk":"Surinam","sv":"Surinam","th":"ซูรินาม","uk":"Суринам","zh":"苏里南","zh-tw":"蘇利南"},
  {"id":748,"alpha2":"sz","alpha3":"swz","ar":"إسواتيني","bg":"Есватини","cs":"Svazijsko","da":"Swaziland","de":"Eswatini","el":"Εσουατίνι","en":"Eswatini","eo":"Svazilando","es":"Suazilandia","et":"Svaasimaa","eu":"Eswatini","fi":"Swazimaa","fr":"Eswatini","hu":"Szváziföld","hy":"Էսվատինի","it":"eSwatini","ja":"エスワティニ","ko":"에스와티니","lt":"Svazilendas","nl":"Swaziland","no":"Eswatini","pl":"Eswatini","pt":"Essuatíni","ro":"Eswatini","ru":"Эсватини","sk":"Svazijsko","sv":"Swaziland","th":"เอสวาตีนี","uk":"Есватіні","zh":"斯威士兰","zh-tw":"史瓦帝尼"},
  {"id":752,"alpha2":"se","alpha3":"swe","ar":"السويد","bg":"Швеция","cs":"Švédsko","da":"Sverige","de":"Schweden","el":"Σουηδία","en":"Sweden","eo":"Svedio","es":"Suecia","et":"Rootsi","eu":"Suedia","fi":"Ruotsi","fr":"Suède","hu":"Svédország","hy":"Շվեդիա","it":"Svezia","ja":"スウェーデン","ko":"스웨덴","lt":"Švedija","nl":"Zweden","no":"Sverige","pl":"Szwecja","pt":"Suécia","ro":"Suedia","ru":"Швеция","sk":"Švédsko","sv":"Sverige","th":"สวีเดน","uk":"Швеція","zh":"瑞典","zh-tw":"瑞典"},
  {"id":756,"alpha2":"ch","alpha3":"che","ar":"سويسرا","bg":"Швейцария","cs":"Švýcarsko","da":"Schweiz","de":"Schweiz","el":"Ελβετία","en":"Switzerland","eo":"Svislando","es":"Suiza","et":"Šveits","eu":"Suitza","fi":"Sveitsi","fr":"Suisse","hu":"Svájc","hy":"Շվեյցարիա","it":"Svizzera","ja":"スイス","ko":"스위스","lt":"Šveicarija","nl":"Zwitserland","no":"Sveits","pl":"Szwajcaria","pt":"Suíça","ro":"Elveția","ru":"Швейцария","sk":"Švajčiarsko","sv":"Schweiz","th":"สวิตเซอร์แลนด์","uk":"Швейцарія","zh":"瑞士","zh-tw":"瑞士"},
  {"id":760,"alpha2":"sy","alpha3":"syr","ar":"سوريا","bg":"Сирия","cs":"Sýrie","da":"Syrien","de":"Syrien","el":"Συρία","en":"Syrian Arab Republic","eo":"Sirio","es":"Siria","et":"Süüria","eu":"Siria","fi":"Syyria","fr":"Syrie","hu":"Szíria","hy":"Սիրիա","it":"Siria","ja":"シリア・アラブ共和国","ko":"시리아","lt":"Sirija","nl":"Syrië","no":"Syria","pl":"Syria","pt":"Síria","ro":"Siria","ru":"Сирия","sk":"Sýria","sv":"Syrien","th":"ซีเรีย","uk":"Сирія","zh":"叙利亚","zh-tw":"敘利亞"},
  {"id":762,"alpha2":"tj","alpha3":"tjk","ar":"طاجيكستان","bg":"Таджикистан","cs":"Tádžikistán","da":"Tadsjikistan","de":"Tadschikistan","el":"Τατζικιστάν","en":"Tajikistan","eo":"Taĝikio","es":"Tayikistán","et":"Tadžikistan","eu":"Tajikistan","fi":"Tadžikistan","fr":"Tadjikistan","hu":"Tádzsikisztán","hy":"Տաջիկստան","it":"Tagikistan","ja":"タジキスタン","ko":"타지키스탄","lt":"Tadžikija","nl":"Tadzjikistan","no":"Tadsjikistan","pl":"Tadżykistan","pt":"Tajiquistão","ro":"Tadjikistan","ru":"Таджикистан","sk":"Tadžikistan","sv":"Tadzjikistan","th":"ทาจิกิสถาน","uk":"Таджикистан","zh":"塔吉克斯坦","zh-tw":"塔吉克"},
  {"id":834,"alpha2":"tz","alpha3":"tza","ar":"تنزانيا","bg":"Танзания","cs":"Tanzanie","da":"Tanzania","de":"Tansania","el":"Τανζανία","en":"Tanzania, United Republic of","eo":"Tanzanio","es":"Tanzania","et":"Tansaania","eu":"Tanzania","fi":"Tansania","fr":"Tanzanie","hu":"Tanzánia","hy":"Տանզանիա","it":"Tanzania","ja":"タンザニア","ko":"탄자니아","lt":"Tanzanija","nl":"Tanzania","no":"Tanzania","pl":"Tanzania","pt":"Tanzânia","ro":"Tanzania","ru":"Танзания","sk":"Tanzánia","sv":"Tanzania","th":"แทนซาเนีย","uk":"Танзанія","zh":"坦桑尼亚","zh-tw":"坦尚尼亞"},
  {"id":764,"alpha2":"th","alpha3":"tha","ar":"تايلاند","bg":"Тайланд","cs":"Thajsko","da":"Thailand","de":"Thailand","el":"Ταϊλάνδη","en":"Thailand","eo":"Tajlando","es":"Tailandia","et":"Tai","eu":"Thailandia","fi":"Thaimaa","fr":"Thaïlande","hu":"Thaiföld","hy":"Թաիլանդ","it":"Thailandia","ja":"タイ","ko":"태국","lt":"Tailandas","nl":"Thailand","no":"Thailand","pl":"Tajlandia","pt":"Tailândia","ro":"Thailanda","ru":"Таиланд","sk":"Thajsko","sv":"Thailand","th":"ไทย","uk":"Таїланд","zh":"泰国","zh-tw":"泰國"},
  {"id":626,"alpha2":"tl","alpha3":"tls","ar":"تيمور الشرقية","bg":"Източен Тимор","cs":"Východní Timor","da":"Østtimor","de":"Osttimor","el":"Ανατολικό Τιμόρ","en":"Timor-Leste","eo":"Orienta Timoro","es":"Timor Oriental","et":"Ida-Timor","eu":"Ekialdeko Timor","fi":"Itä-Timor","fr":"Timor oriental","hu":"Kelet-Timor","hy":"Արևելյան Թիմոր","it":"Timor Est","ja":"東ティモール","ko":"동티모르","lt":"Rytų Timoras","nl":"Oost-Timor","no":"Øst-Timor","pl":"Timor Wschodni","pt":"Timor-Leste","ro":"Timorul de Est","ru":"Восточный Тимор","sk":"Východný Timor","sv":"Östtimor","th":"ติมอร์-เลสเต","uk":"Східний Тимор","zh":"东帝汶","zh-tw":"東帝汶"},
  {"id":768,"alpha2":"tg","alpha3":"tgo","ar":"توغو","bg":"Того","cs":"Togo","da":"Togo","de":"Togo","el":"Τόγκο","en":"Togo","eo":"Togolando","es":"Togo","et":"Togo","eu":"Togo","fi":"Togo","fr":"Togo","hu":"Togo","hy":"Տոգո","it":"Togo","ja":"トーゴ","ko":"토고","lt":"Togas","nl":"Togo","no":"Togo","pl":"Togo","pt":"Togo","ro":"Togo","ru":"Того","sk":"Togo","sv":"Togo","th":"โตโก","uk":"Того","zh":"多哥","zh-tw":"多哥"},
  {"id":776,"alpha2":"to","alpha3":"ton","ar":"تونغا","bg":"Тонга","cs":"Tonga","da":"Tonga","de":"Tonga","el":"Τόγκα","en":"Tonga","eo":"Tongo","es":"Tonga","et":"Tonga","eu":"Tonga","fi":"Tonga","fr":"Tonga","hu":"Tonga","hy":"Տոնգա","it":"Tonga","ja":"トンガ","ko":"통가","lt":"Tonga","nl":"Tonga","no":"Tonga","pl":"Tonga","pt":"Tonga","ro":"Tonga","ru":"Тонга","sk":"Tonga","sv":"Tonga","th":"ตองงา","uk":"Тонга","zh":"汤加","zh-tw":"東加"},
  {"id":780,"alpha2":"tt","alpha3":"tto","ar":"ترينيداد وتوباغو","bg":"Тринидад и Тобаго","cs":"Trinidad a Tobago","da":"Trinidad og Tobago","de":"Trinidad und Tobago","el":"Τρινιντάντ και Τομπάγκο","en":"Trinidad and Tobago","eo":"Trinidado kaj Tobago","es":"Trinidad y Tobago","et":"Trinidad ja Tobago","eu":"Trinidad eta Tobago","fi":"Trinidad ja Tobago","fr":"Trinité-et-Tobago","hu":"Trinidad és Tobago","hy":"Տրինիդադ և Տոբագո","it":"Trinidad e Tobago","ja":"トリニダード・トバゴ","ko":"트리니다드 토바고","lt":"Trinidadas ir Tobagas","nl":"Trinidad en Tobago","no":"Trinidad og Tobago","pl":"Trynidad i Tobago","pt":"Trinidad e Tobago","ro":"Trinidad și Tobago","ru":"Тринидад и Тобаго","sk":"Trinidad a Tobago","sv":"Trinidad och Tobago","th":"ตรินิแดดและโตเบโก","uk":"Тринідад і Тобаго","zh":"特立尼达和多巴哥","zh-tw":"千里達及托巴哥"},
  {"id":788,"alpha2":"tn","alpha3":"tun","ar":"تونس","bg":"Тунис","cs":"Tunisko","da":"Tunesien","de":"Tunesien","el":"Τυνησία","en":"Tunisia","eo":"Tunizio","es":"Túnez","et":"Tuneesia","eu":"Tunisia","fi":"Tunisia","fr":"Tunisie","hu":"Tunézia","hy":"Թունիս","it":"Tunisia","ja":"チュニジア","ko":"튀니지","lt":"Tunisas","nl":"Tunesië","no":"Tunisia","pl":"Tunezja","pt":"Tunísia","ro":"Tunisia","ru":"Тунис","sk":"Tunisko","sv":"Tunisien","th":"ตูนิเซีย","uk":"Туніс","zh":"突尼斯","zh-tw":"突尼西亞"},
  {"id":792,"alpha2":"tr","alpha3":"tur","ar":"تركيا","bg":"Турция","cs":"Turecko","da":"Tyrkiet","de":"Türkei","el":"Τουρκία","en":"Türkiye","eo":"Turkio","es":"Turquía","et":"Türgi","eu":"Turkia","fi":"Turkki","fr":"Turquie","hu":"Törökország","hy":"Թուրքիա","it":"Turchia","ja":"トルコ","ko":"튀르키예","lt":"Turkija","nl":"Turkije","no":"Tyrkia","pl":"Turcja","pt":"Turquia","ro":"Turcia","ru":"Турция","sk":"Turecko","sv":"Turkiet","th":"ตุรกี","uk":"Туреччина","zh":"土耳其","zh-tw":"土耳其"},
  {"id":795,"alpha2":"tm","alpha3":"tkm","ar":"تركمانستان","bg":"Туркменистан","cs":"Turkmenistán","da":"Turkmenistan","de":"Turkmenistan","el":"Τουρκμενιστάν","en":"Turkmenistan","eo":"Turkmenio","es":"Turkmenistán","et":"Türkmenistan","eu":"Turkmenistan","fi":"Turkmenistan","fr":"Turkménistan","hu":"Türkmenisztán","hy":"Թուրքմենստան","it":"Turkmenistan","ja":"トルクメニスタン","ko":"투르크메니스탄","lt":"Turkmėnija","nl":"Turkmenistan","no":"Turkmenistan","pl":"Turkmenistan","pt":"Turcomenistão","ro":"Turkmenistan","ru":"Туркменистан","sk":"Turkménsko","sv":"Turkmenistan","th":"เติร์กเมนิสถาน","uk":"Туркменістан","zh":"土库曼斯坦","zh-tw":"土庫曼"},
  {"id":798,"alpha2":"tv","alpha3":"tuv","ar":"توفالو","bg":"Тувалу","cs":"Tuvalu","da":"Tuvalu","de":"Tuvalu","el":"Τουβαλού","en":"Tuvalu","eo":"Tuvalo","es":"Tuvalu","et":"Tuvalu","eu":"Tuvalu","fi":"Tuvalu","fr":"Tuvalu","hu":"Tuvalu","hy":"Տուվալու","it":"Tuvalu","ja":"ツバル","ko":"투발루","lt":"Tuvalu","nl":"Tuvalu","no":"Tuvalu","pl":"Tuvalu","pt":"Tuvalu","ro":"Tuvalu","ru":"Тувалу","sk":"Tuvalu","sv":"Tuvalu","th":"ตูวาลู","uk":"Тувалу","zh":"图瓦卢","zh-tw":"吐瓦魯"},
  {"id":800,"alpha2":"ug","alpha3":"uga","ar":"أوغندا","bg":"Уганда","cs":"Uganda","da":"Uganda","de":"Uganda","el":"Ουγκάντα","en":"Uganda","eo":"Ugando","es":"Uganda","et":"Uganda","eu":"Uganda","fi":"Uganda","fr":"Ouganda","hu":"Uganda","hy":"Ուգանդա","it":"Uganda","ja":"ウガンダ","ko":"우간다","lt":"Uganda","nl":"Oeganda","no":"Uganda","pl":"Uganda","pt":"Uganda","ro":"Uganda","ru":"Уганда","sk":"Uganda","sv":"Uganda","th":"ยูกันดา","uk":"Уганда","zh":"乌干达","zh-tw":"烏干達"},
  {"id":804,"alpha2":"ua","alpha3":"ukr","ar":"أوكرانيا","bg":"Украйна","cs":"Ukrajina","da":"Ukraine","de":"Ukraine","el":"Ουκρανία","en":"Ukraine","eo":"Ukrainio","es":"Ucrania","et":"Ukraina","eu":"Ukraina","fi":"Ukraina","fr":"Ukraine","hu":"Ukrajna","hy":"Ուկրաինա","it":"Ucraina","ja":"ウクライナ","ko":"우크라이나","lt":"Ukraina","nl":"Oekraïne","no":"Ukraina","pl":"Ukraina","pt":"Ucrânia","ro":"Ucraina","ru":"Украина","sk":"Ukrajina","sv":"Ukraina","th":"ยูเครน","uk":"Україна","zh":"乌克兰","zh-tw":"烏克蘭"},
  {"id":784,"alpha2":"ae","alpha3":"are","ar":"الإمارات العربية المتحدة","bg":"ОАЕ","cs":"Spojené arabské emiráty","da":"Forenede Arabiske Emirater","de":"Vereinigte Arabische Emirate","el":"Ηνωμένα Αραβικά Εμιράτα","en":"United Arab Emirates","eo":"Unuiĝintaj Arabaj Emirlandoj","es":"Emiratos Árabes Unidos","et":"Araabia Ühendemiraadid","eu":"Arabiar Emirerri Batuak","fi":"Arabiemiirikunnat","fr":"Émirats arabes unis","hu":"Egyesült Arab Emírségek","hy":"Արաբական Միացյալ Էմիրություններ","it":"Emirati Arabi Uniti","ja":"アラブ首長国連邦","ko":"아랍에미리트","lt":"Jungtiniai Arabų Emyratai","nl":"Verenigde Arabische Emiraten","no":"De forente arabiske emirater","pl":"Zjednoczone Emiraty Arabskie","pt":"Emirados Árabes Unidos","ro":"Emiratele Arabe Unite","ru":"ОАЭ","sk":"Spojené arabské emiráty","sv":"Förenade Arabemiraten","th":"สหรัฐอาหรับเอมิเรตส์","uk":"ОАЕ","zh":"阿联酋","zh-tw":"阿聯"},
  {"id":826,"alpha2":"gb","alpha3":"gbr","ar":"المملكة المتحدة","bg":"Великобритания","cs":"Spojené království Velké Británie a Severního Irska","da":"Storbritannien","de":"Vereinigtes Königreich","el":"Ηνωμένο Βασίλειο","en":"United Kingdom of Great Britain and Northern Ireland","eo":"Britio","es":"Reino Unido","et":"Suurbritannia","eu":"Erresuma Batua","fi":"Yhdistynyt kuningaskunta","fr":"Royaume-Uni","hu":"Egyesült Királyság","hy":"Մեծ Բրիտանիա","it":"Regno Unito","ja":"イギリス","ko":"영국","lt":"Jungtinė Karalystė","nl":"Verenigd Koninkrijk","no":"Storbritannia","pl":"Wielka Brytania","pt":"Reino Unido","ro":"Regatul Unit","ru":"Великобритания","sk":"Spojené kráľovstvo","sv":"Storbritannien","th":"สหราชอาณาจักร","uk":"Велика Британія","zh":"英国","zh-tw":"英國"},
  {"id":840,"alpha2":"us","alpha3":"usa","ar":"الولايات المتحدة","bg":"САЩ","cs":"Spojené státy americké","da":"USA","de":"Vereinigte Staaten","el":"Ηνωμένες Πολιτείες Αμερικής","en":"United States of America","eo":"Usono","es":"Estados Unidos","et":"Ameerika Ühendriigid","eu":"AEB","fi":"Yhdysvallat","fr":"États-Unis","hu":"Amerikai Egyesült Államok","hy":"ԱՄՆ","it":"Stati Uniti","ja":"アメリカ合衆国","ko":"미국","lt":"Jungtinės Valstijos","nl":"Verenigde Staten","no":"USA","pl":"Stany Zjednoczone","pt":"Estados Unidos","ro":"Statele Unite ale Americii","ru":"США","sk":"Spojené štáty","sv":"USA","th":"สหรัฐ","uk":"США","zh":"美国","zh-tw":"美國"},
  {"id":858,"alpha2":"uy","alpha3":"ury","ar":"الأوروغواي","bg":"Уругвай","cs":"Uruguay","da":"Uruguay","de":"Uruguay","el":"Ουρουγουάη","en":"Uruguay","eo":"Urugvajo","es":"Uruguay","et":"Uruguay","eu":"Uruguai","fi":"Uruguay","fr":"Uruguay","hu":"Uruguay","hy":"Ուրուգվայ","it":"Uruguay","ja":"ウルグアイ","ko":"우루과이","lt":"Urugvajus","nl":"Uruguay","no":"Uruguay","pl":"Urugwaj","pt":"Uruguai","ro":"Uruguay","ru":"Уругвай","sk":"Uruguaj","sv":"Uruguay","th":"อุรุกวัย","uk":"Уругвай","zh":"乌拉圭","zh-tw":"烏拉圭"},
  {"id":860,"alpha2":"uz","alpha3":"uzb","ar":"أوزبكستان","bg":"Узбекистан","cs":"Uzbekistán","da":"Usbekistan","de":"Usbekistan","el":"Ουζμπεκιστάν","en":"Uzbekistan","eo":"Uzbekio","es":"Uzbekistán","et":"Usbekistan","eu":"Uzbekistan","fi":"Uzbekistan","fr":"Ouzbékistan","hu":"Üzbegisztán","hy":"Ուզբեկստան","it":"Uzbekistan","ja":"ウズベキスタン","ko":"우즈베키스탄","lt":"Uzbekistanas","nl":"Oezbekistan","no":"Usbekistan","pl":"Uzbekistan","pt":"Uzbequistão","ro":"Uzbekistan","ru":"Узбекистан","sk":"Uzbekistan","sv":"Uzbekistan","th":"อุซเบกิสถาน","uk":"Узбекистан","zh":"乌兹别克斯坦","zh-tw":"烏茲別克"},
  {"id":548,"alpha2":"vu","alpha3":"vut","ar":"فانواتو","bg":"Вануату","cs":"Vanuatu","da":"Vanuatu","de":"Vanuatu","el":"Βανουάτου","en":"Vanuatu","eo":"Vanuatuo","es":"Vanuatu","et":"Vanuatu","eu":"Vanuatu","fi":"Vanuatu","fr":"Vanuatu","hu":"Vanuatu","hy":"Վանուատու","it":"Vanuatu","ja":"バヌアツ","ko":"바누아투","lt":"Vanuatu","nl":"Vanuatu","no":"Vanuatu","pl":"Vanuatu","pt":"Vanuatu","ro":"Vanuatu","ru":"Вануату","sk":"Vanuatu","sv":"Vanuatu","th":"วานูวาตู","uk":"Вануату","zh":"瓦努阿图","zh-tw":"萬那杜"},
  {"id":862,"alpha2":"ve","alpha3":"ven","ar":"فنزويلا","bg":"Венецуела","cs":"Venezuela","da":"Venezuela","de":"Venezuela","el":"Βενεζουέλα","en":"Venezuela (Bolivarian Republic of)","eo":"Venezuelo","es":"Venezuela","et":"Venezuela","eu":"Venezuela","fi":"Venezuela","fr":"Venezuela","hu":"Venezuela","hy":"Վենեսուելա","it":"Venezuela","ja":"ベネズエラ・ボリバル共和国","ko":"베네수엘라","lt":"Venesuela","nl":"Venezuela","no":"Venezuela","pl":"Wenezuela","pt":"Venezuela","ro":"Venezuela","ru":"Венесуэла","sk":"Venezuela","sv":"Venezuela","th":"เวเนซุเอลา","uk":"Венесуела","zh":"委内瑞拉","zh-tw":"委內瑞拉"},
  {"id":704,"alpha2":"vn","alpha3":"vnm","ar":"فيتنام","bg":"Виетнам","cs":"Vietnam","da":"Vietnam","de":"Vietnam","el":"Βιετνάμ","en":"Viet Nam","eo":"Vjetnamio","es":"Vietnam","et":"Vietnam","eu":"Vietnam","fi":"Vietnam","fr":"Viêt Nam","hu":"Vietnám","hy":"Վիետնամ","it":"Vietnam","ja":"ベトナム","ko":"베트남","lt":"Vietnamas","nl":"Vietnam","no":"Vietnam","pl":"Wietnam","pt":"Vietname","ro":"Vietnam","ru":"Вьетнам","sk":"Vietnam","sv":"Vietnam","th":"เวียดนาม","uk":"В'єтнам","zh":"越南","zh-tw":"越南"},
  {"id":887,"alpha2":"ye","alpha3":"yem","ar":"اليمن","bg":"Йемен","cs":"Jemen","da":"Yemen","de":"Jemen","el":"Υεμένη","en":"Yemen","eo":"Jemeno","es":"Yemen","et":"Jeemen","eu":"Yemen","fi":"Jemen","fr":"Yémen","hu":"Jemen","hy":"Եմեն","it":"Yemen","ja":"イエメン","ko":"예멘","lt":"Jemenas","nl":"Jemen","no":"Jemen","pl":"Jemen","pt":"Iêmen","ro":"Yemen","ru":"Йемен","sk":"Jemen","sv":"Jemen","th":"เยเมน","uk":"Ємен","zh":"也门","zh-tw":"葉門"},
  {"id":894,"alpha2":"zm","alpha3":"zmb","ar":"زامبيا","bg":"Замбия","cs":"Zambie","da":"Zambia","de":"Sambia","el":"Ζάμπια","en":"Zambia","eo":"Zambio","es":"Zambia","et":"Sambia","eu":"Zambia","fi":"Sambia","fr":"Zambie","hu":"Zambia","hy":"Զամբիա","it":"Zambia","ja":"ザンビア","ko":"잠비아","lt":"Zambija","nl":"Zambia","no":"Zambia","pl":"Zambia","pt":"Zâmbia","ro":"Zambia","ru":"Замбия","sk":"Zambia","sv":"Zambia","th":"แซมเบีย","uk":"Замбія","zh":"赞比亚","zh-tw":"尚比亞"},
  {"id":716,"alpha2":"zw","alpha3":"zwe","ar":"زيمبابوي","bg":"Зимбабве","cs":"Zimbabwe","da":"Zimbabwe","de":"Simbabwe","el":"Ζιμπάμπουε","en":"Zimbabwe","eo":"Zimbabvo","es":"Zimbabue","et":"Zimbabwe","eu":"Zimbabwe","fi":"Zimbabwe","fr":"Zimbabwe","hu":"Zimbabwe","hy":"Զիմբաբվե","it":"Zimbabwe","ja":"ジンバブエ","ko":"짐바브웨","lt":"Zimbabvė","nl":"Zimbabwe","no":"Zimbabwe","pl":"Zimbabwe","pt":"Zimbábue","ro":"Zimbabwe","ru":"Зимбабве","sk":"Zimbabwe","sv":"Zimbabwe","th":"ซิมบับเว","uk":"Зімбабве","zh":"津巴布韦","zh-tw":"辛巴威"}]
  # Data done -----------------------------------------------------

  # Choosing a dictionary from the list
  data = random.sample(country, len(country))

  # Getting the name of the country from the dictionary
  namec = data[0]["en"]

  # Optional, answer
  #print(data[0]["en"])

  for i in range(9,-1,-1):
    # Printing the flag
    display(Image(f'https://raw.githubusercontent.com/stefangabos/world_countries/355734c9f667abb5cbbf86b05f5bccf0995494d0/data/flags/128x128/{data[0]["alpha2"]}.png', height=100))
    guessc = input(f'Guess the name of the country [Tries: {i+1}]: ')
    if guessc.lower() == namec.lower():
      print(f'\033[32mCongratulations! You guessed the name of the country correctly in {10-i} tries!\033[0m')
      break
    else:
      print(f'Incorrect guess! Try again, you have {i} tries remaining')
  else:
    print(f'\033[31mYou lost the game! The country was {namec}\033[0m')
  #-------------------------------------------------------------------- All Games Loop Finished --------------------------------------------------------------------------------------------------------------------------
