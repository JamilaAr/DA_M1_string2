# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    if len(s) >=3:
        if s.endswith ('ing'):
           return s + "ly" 
        else:
          return s + "ing"
    else:    
         return(s)
print(verbing("hail")) 
print(verbing("swimming"))
print(verbing("do"))


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    not_index = s.find("not")
    bad_index = s.find("bad")
    if not_index != -1 and bad_index != -1 and not_index < bad_index:
         s = s[:not_index] + 'good' + s[bad_index + 3:]
    return  s     
print(not_bad("this dinner is not that bad!"))    
print(not_bad("this movie is not that bad !"))
print(not_bad("this tea is hot"))
print(not_bad("it's good  "))


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    def split_half(s):
        length = len(s)
        half = (length + 1) // 2  # if odd, extra char goes to the front half
        return s[:half], s[half:]
    a_front, a_back = split_half(a)
    b_front, b_back = split_half(b)
        
    return a_front + b_front + a_back + b_back

print(front_back('abcd', 'xy'))     
print(front_back('abcde', 'xyz'))   
print(front_back('kitten', 'donut'))

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
