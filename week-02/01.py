pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print(original[-1]+original[1:-1]+original[0]+pyg)
else:
  print ('empty')