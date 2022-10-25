my_own_tuple = ()

fn = input("what is your first name? ")
mn = input("what is your middle name? ")
ln = input("what is your last name? ")
age = input("what is your age? ")

my_own_tuple = tuple((fn, mn, ln, age))

print ("\n")
for loop in my_own_tuple:
  print(loop, "\n")