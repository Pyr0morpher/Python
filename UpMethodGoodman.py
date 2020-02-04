first = input("First Word: ")
second = input("Second Word: ")

#sorts the two words alphabetically
def sortWords(one, two):
  if (one < two):
    print(one + "\n" + two)
  else:
    print(two + "\n" + one)

#returns the words and puts them in uppercase
sortWords(first.upper(),second.upper())
