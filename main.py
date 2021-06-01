# Declare the for loop
for fizzbuzz in range(101): # Iterates through the numbers up to 101.
# If the current number divided by 3's remainder is 0, then we use "Fizz"
  if fizzbuzz % 3 == 0:
    print('Fizz')
# If the current number divided by 5's remainder is 0, then we use "Buzz"
  if fizzbuzz % 5 == 0:
    print('Buzz')
# If both divided by 3, and divided by 5, the remainder is 0, then we use "FizzBuzz"
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print ('FizzBuzz')
# Loop
  else:
    print (fizzbuzz)
