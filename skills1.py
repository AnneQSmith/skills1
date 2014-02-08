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

a = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer']
print a
a = all_odd(a) 
print a



#print all_odd(a)



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


b = ['1','2','2','3',4,5,6,7,8,9,'qowieur','qiwer']
print b
b = all_even(b) 
print b

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return []

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None