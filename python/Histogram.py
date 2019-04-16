#Program to create a histogram from a given list of integers.

def histogram( items ):
    for n in items:
        result = ''
        while( n > 0 ):
            result =result + '+'
        n = n - 1
        print(result)

histogram([2,8,6])
