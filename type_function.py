#Type function allows us to see the datatype of any given value

print(type('hello world')) #str.ing
print(type(4)) #int.eger
print(type(3.14)) #float

print(type('123 fun street'))


#type casting using int() convert data to an int datatype
x = '4'
print(type(x))

x = int(x)
print(type(int(x)))
print(x)

#type casting float() to convert qualifying data into a float datatype
x = float(x)
print(type(x))
print(x)

pi = 3.14
print(pi)

#converting to int always rounds down
ball_park = int(pi)
print(ball_park)

#------ Get a value error because we tried to convert non qualifying data
num = 'four' #must be in actual number within single quoted "number"
int_num = int(num)
print(int_num)

