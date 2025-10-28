#Paling basic (Print function yang menampilkan string Hello world)

print("hello world")

#Menyimpan string hello world di dalam variabel text 1
text1 = "hello world"


print(text1)
print(text1)
print(text1)
print(text1)
print(text1)
print(text1)



x = "Hello"
y = "World"

print (x + y)

#menyimpan input function di dalam variable userResponse
userResponse = input("say something please")

print(userResponse)


#without integer
x = 4
y = 5.4

print(x+y)

#with integer (tipe data bilangan bulat) (int function within a print function)

x=4
y=5.4

print( int(x+y))

#with float (tipe data bilangan desimal dengan titik pecahan) (float function within a print function)

x=4
y=5.4

print ( float(x+y))

#Exercise: Strings Exercise 
# Write your Python code to do the following
# Assigns the value 34 to a variable of your choice
# Assigns the value Bobby to another variable of your choice
# Both 34 and Bobby are strings
# Prints a statement that will say "Bobby is 34 years old"
# Pay close attention to the spacing among the words


x = " 34 "
y = "Bobby "

print (y+"is"+x+"years old")


#Boolean value/statement. 
# Remember, resulted in false or true. 
#These are what we refer to as the Boolean values or the 
#Boolean operators, and we typically use them whenever we're 
#trying to create loops or conditional statements.
#But typically we may want to write a program that will check 
#to see if something has happened and then if it has happened, 
# meaning if it's true, then do something.
# Or we can also say if this thing hasn't happened. Therefore 
# if it is false, then do something else.


x = 5
y = 10

print(x == y)
print(x < y)


#Boolean value juga bukan hanya kerja pakai comparison operator seperti "="
# "<", ">", tapi juga pakai logic operators seperti "AND" "OR" "NOT"
#All of them will need to be true whenever you're using the "AND" statement.
#BUT If one of them is false, then the answer will be false. 
#The opposite is with "OR". #So if you're saying true or false, it's going to be true.
#If it's true and false, the answer will be false.
#And then obviously for the last one in here "NOT", not a will be false 
#because not a means the opposite of true.

a = True
b = False

print(a and b) 
print(a or b)
print(not a)


#Arithmetic Operators

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

x = 10
#x += 5 #ini short form dari x = x + 5
x -= 5 #ini short form dari x = x - 5
#x /= 5 #ini short form dari x = x / 5
#x *= 5 #ini short form dari x = x * 5 etc.

print(x)


#Operators precedence
#Parantheses()
#Exponentiation **
#Multiplication *
#Division /
#Modulus %
#Addition +
#Subtraction -
#Comparison Operators (<,>,==)
#Logical Operators (and, or, not)

result = 2 + 3 * 4 # karena dalam matematika juga di Python, perkalian didahulukan dari 
#tambahan atau pengurangan

print (result)

result = (2+3) * 4 #addition didahulukan karena masuk dalam bracket

print (result)




#Integer, Arithmetic and Boolean Operators Exercise

#We are going to be working with 6 different variables
#create a variable and assign it the value of the addition of 2,3 and 4
#create a second variable and assign it the value of the multiplication of 4 and 5
#create a third variable and assign it the value of subtracting 3 from the result of dividing 10 by 2

#Once you have created these variables and their respective values
#create a fourth variable and assign it the value of adding 
#the results of the first 3 variables (make sure this value is an integer)
#create a fifth variable that claims the value of the fourth variable is greater than the value of the second variable
#create a sixth variable that claims the value of the third variable is less than the value of the first variable

#At this point you should have six different values, 
#four of which are integers and the remaining two Boolean. 

#Finally I want you to print out the results of the following
#the value of the fourth variable
#first variable is less than the value of the second variable
#NOT the value of the fifth variable
#the value of both the fifth and sixth variables

#If you did the test correctly, 
#your output for the four print statements should be

#31
#True
#False
#True

x = 2 + 3 + 4
y = 4 * 5
z = 10/2 - 3
xyz = (int(x + y + z))
a = (xyz > y)
b = (z < x)

print (xyz)
print (x < y)
print (not a)
print (a and b)
