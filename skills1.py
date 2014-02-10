# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):

    new_list = []
    for i in range(len(some_list)):
        
        if type(some_list[i]) == int:
            if some_list[i] % 2 == 1:
               new_list.append(some_list[i])
        
        elif type(some_list[i]) == str:
            if some_list[i].isdigit():  
                if int(some_list[i]) % 2 == 1:
                    new_list.append(some_list[i])

    return new_list



# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    
    new_list = []
    for i in range(len(some_list)):
        
        if type(some_list[i]) == int:
            if some_list[i] % 2 == 0:
               new_list.append(some_list[i])
        
        elif type(some_list[i]) == str:
            if some_list[i].isdigit():  
                if int(some_list[i]) % 2 == 0:
                    new_list.append(some_list[i])

    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    
    new_list = []
    for i in range(len(word_list)):
        
        if type(word_list[i]) == str:
            if len(word_list[i]) >= 4:
                new_list.append(word_list[i])

    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
       
    firstvalidnumber = None
    smallnumber = None
    for i in range(len(some_list)):
        if type(some_list[i]) == int:
            if firstvalidnumber == None:
                smallnumber = firstvalidnumber = some_list[i]
            if some_list[i] < smallnumber:
                smallnumber = some_list[i]

    return smallnumber


# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
          
    firstvalidnumber = None
    largenumber = None
    for i in range(len(some_list)):
        if type(some_list[i]) == int:
            if firstvalidnumber == None:
                largenumber = firstvalidnumber = some_list[i]
            if some_list[i] > largenumber:
                largenumber = some_list[i]

    return largenumber

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):

    new_list = []
    for i in range(len(some_list)):
        
        if type(some_list[i]) == (int or float):
             new_list.append(some_list[i]/2.0)

    return new_list


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for i in range(len(word_list)):
        if type(word_list[i]) == str:
            new_list.append(len(word_list[i]))

    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):

    summation = 0

    print len(numbers)
    for i in range(len(numbers)):
        
        if type(numbers[i]) == int:
            summation += numbers[i]
        elif type(numbers[i]) == float:
            summation += numbers[i]
    return summation


# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    prodnumbers = 1
    for i in range(len(numbers)):
    
        if type(numbers[i]) == float:
            prodnumbers *= numbers[i] 
        elif type(numbers[i]) == int:
            prodnumbers *= numbers[i]

    return prodnumbers


# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):

    newstring = ''
    for i in range(len(string_list)):
        if type(string_list[i]) == str:

            newstring += string_list[i]

    return newstring


# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):

    summation = 0
    j = 0
    aver = 0.0

    for i in range(len(numbers)):
        if type(numbers[i]) == int:
            summation += numbers[i]
            j +=1

    if j > 0:
        aver = float(summation) / float(j)
    else:
        aver = None


    return aver

