import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  # Print more than 1 quote  
  rnd2 = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[rnd2])

  # Print without extra line  
  # print(quotes[rnd], end='')

if __name__== "__main__":
  primary()
