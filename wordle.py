from colorama import init
from colorama import Fore, Back, Style

def format_match( letter='X' ):
   return Back.GREEN + letter + Back.RESET
def format_contains( letter='X' ):
   return Back.YELLOW + letter + Back.RESET

init()
print()
prompt = 'Enter the Wordle word: '
wordle = input(prompt).upper()
print('\033[1A' + prompt + '\033[K')
print()

print("Instructions:")
print("  " + format_match() + " = Right letter, Right spot")
print("  " + format_contains() + " = Right letter, Wrong spot")
print("  - = Wrong letter, Right spot")
print("Guesses must contain {} letters".format(len(wordle)))
print()

unsolved=1
while unsolved:
   status = ['-']*len(wordle)
   print(''.join(status), end = "\r")
   guess = input().upper()
   if guess == wordle: #all(ele == 'X' for ele in status):
      unsolved = 0
   if(len(guess)!=len(wordle)):
      print("Guesses must contain {} letters".format(len(wordle)))
      continue
   for i, s in enumerate(guess):
      if s == wordle[i]:
         status[i] = format_match(s)
      elif s in wordle:
         status[i] = format_contains(s)
   print(''.join(status))
   print()
print("Congratulations! You have guessed the word correctly!!")