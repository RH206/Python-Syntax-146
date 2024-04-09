#Math Operations

#Order Operations
#(3+4)+4**2-6*5/4
#PEMDAS
#P=Parenthesis
#E=Exponents
#M=Multiply and Divide tied for third (left to right priority)
#Addition and Subtraction tied for fourth (left to right priority)




#by default division is the only operation that returns a float
#if you incorporate a float in any other math operation a float will be returned


#Addition use '+'
my_sum = 3 + 5 + 7 + 2.2
print(my_sum)

# Addition assign: reassign the cariable to it's current value plus a new value
my_sum += 2
print ('Addition Assign:', my_sum)

#Subtraction use '-'

diff = 10 - 2
print(diff)

#subtract assign

diff -= 1
print ('Subtract Assign1:', diff)

#Multiplication use '*' shift 8
prod= 10 * 3
print(prod)

#multiply assign
prod *= 2
print('Multipli Assign 2:', prod)

#division using '/' always returns  float
quotient = 10 / 2
print(quotient)

#Division Assign
quotient /= 2
print('Division Assign 2:', quotient)

#Floor Division use '//' (rounds down to nearest whole number)
pre_rounded = 10/7
print(pre_rounded)
rounded = 10/7
print(rounded)

#Floor Divide Assign
x = 30 
x //= 4
print('Floor Divide Assign 30 //= 4:',x)

#Modulo use '%' returns remainder of dividion
remainder = 32 % 6
print(remainder)

#Modulo Assign
remainder %= 2
print('Mudulo Assign 2:', remainder)

#Exponents use '**' (how many times we're going to multiply a number by itself)
square = 5**2
print('Squaring 5:', square)

cubing = 5**3
print('Cubing 5:', cubing)

#Exponent Assign
square **= 2

