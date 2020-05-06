import random

def write():
  # append a pre-defined string to file

  f = open("quotes.txt","a")

  #This is a predefined string
  L = ["Think before you act \n","Actions speak louder than words \n"]

  f.writelines(L)
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  print("The following lines are added \n")
  print(quotes[len(quotes)-2])
  print(quotes[len(quotes)-1])  


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
  #Run write function
  write()

  #Run original function
  # primary()
