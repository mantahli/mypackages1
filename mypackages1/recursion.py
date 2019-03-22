def sum_array(array):
    for i in array:
        return sum(array)


    '''Return sum of all items in array'''


def fibonacci(n):
    if n <=1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def factorial(n):
    if n <1:
        return 1
    else:
        return n * factorial( n- 1 )

def reverse(word):
    if word == "":
        return word
    else:
        return  reverse(word[1:]) + word[0]
