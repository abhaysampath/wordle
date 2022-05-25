prompt = 'Enter the Wordle word: '
wordle = input(prompt).upper()
print('\033[1A' + prompt + '\033[K')
print("Instructions:")
print("  X = Right letter, Right spot")
print("  * = Right letter, Wrong spot")
print("  _ = Wrong letter, Right spot")
print("Guesses must contain {} letters".format(len(wordle)));
print()

unsolved=1
while unsolved:
   status = ['-']*len(wordle)
   print(''.join(status), end = "\r")
   guess = input().upper
   if(len(guess())!=len(wordle)):
      print("Guesses must contain {} letters".format(len(wordle)));
      continue
   for i, s in enumerate(guess()):
#   i = 0
#   for s in guess():
      if s == wordle[i]:
         status[i] = 'X'
      elif s in wordle:
         status[i] = '*'
#      i = i + 1
   if all(ele == 'X' for ele in status):
      unsolved = 0
   print(''.join(status))
   print()