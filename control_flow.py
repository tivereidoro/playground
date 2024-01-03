# EXercise:
# Create list (1,2,3,4,5)  and iterate thru, and if value is 2, print 'the value is 2' or 'the value is not 2' if it isn't.

# If the value is 5, run a while looop to print 'last item' 6 times.


num_list = [1, 2, 3, 4, 5]

#Use for loop to iterate  thru;
for number in num_list:
    if number == 2:
        print('The value is 2')
    elif number == 5:
        repeat = 0
        while repeat < 7:
            print('last item')
            repeat++
    else:
        print('The value is not 2')
