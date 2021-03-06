for fizzbuzz in range(101):
    if fizzbuzz == 0:
        continue
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0 and fizzbuzz != 0:#checks if the current number is equal to a number that's a multiple of 3 and 5, and that the number isn't 0. 
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0 and fizzbuzz != 0:#checks if the current number is equal to a number that's a multiple of 3 only, and that the number isn't 0. 
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0 and fizzbuzz != 0:#checks if the current number is equal to a number that's a multiple 5, and that the number isn't 0. 
        print("buzz")
        continue
    print(fizzbuzz)
