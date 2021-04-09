for fizzbuzz in range(101): # Iterates through the numbers up to 101.
  if fizzbuzz % 3 == 0:
    print('Fizz')
  if fizzbuzz % 5 == 0:
    print('Buzz')
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print ('FizzBuzz')
  else:
    print (fizzbuzz)
