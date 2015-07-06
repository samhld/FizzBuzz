#FizzBuzz

# userInput = raw_input("What would you like FizzBuzz to count to?")
# print "Okay, FizzBuzz will count to {}".format(userInput)


list = range(100)
fizzCount = 0
buzzCount = 0
for n in list:
    if (n % 3 == 0) & (n % 5 == 0):
        print "FizzBuzz"
        fizzCount += 1
        buzzCount += 1        
    elif n % 3 == 0:
        print "Fizz"
        fizzCount += 1
    elif (n % 5 == 0):
        print "Buzz"
        buzzCount += 1
    else:
        print n

print "Finished: Total number of fizzes was {} and total number of buzzes was {}".format(fizzCount,buzzCount)

        
        