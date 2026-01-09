#done in repl but also done here for future lecture reference
name="Jim"
print(name)

meaning = 42
print(meaning)

print(2+2)
print(4-2)
print(2*2)
print(24/5)
print(24//5) #floor division
print(round(24/5)) #rounding
print(24%5) #modulus operator
print(2**3) #exponentiation
print(2**5) #exponentiation
meaning=42
print(meaning)
meaning=meaning+1 #incrementing
print(meaning)
meaning -= 1
print(meaning)
meaning *= 10
print(meaning)
meaning /= 10 #float division, now is a float
print(meaning)
meaning //= 10 #floor division, can also use round(), now is an int
print(meaning)
full_name = "Jim " + "Smith"
print(full_name)

print(41==42) #equality operator
print(42==42) 
print(41!=42) #inequality operator
print(10>5) #greater than operator
print(5<10) #less than operator
print(10>=10) #greater than or equal to operator
print(10<=10) #less than or equal to operator

true_variable=True
y=False
z=True
print(not true_variable)
print(not y)

# if ( a && b )  true when both a and b are true
print(x and y) #and operator, full evaluation
print(y and x) #and operator, short-circuit evaluation where first false is a false result, no need to evaluate second

# if ( a || b )  true when either a or b is true
print(x or y) #or operator, short-circuit evaluation where first true is a true result, no need to evaluate second
print(x and z) #and operator, both true so result is true
