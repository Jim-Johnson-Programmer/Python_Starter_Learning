#video stopped here  https://youtu.be/qwAFL1597eM?t=2472
meaning=42
print('')

# we indent inside of the if statements

if meaning > 10:
    print('Right on!')
    if meaning > 20:
         print('Right on!')
         if meaning >30:
            print('Right on!')
            print('Right on!')
    elif meaning < 15:  
            print('Right on!')
    else:
         print('Nody today')  
    print('Nody today')  
    print('Nody today')  

#this is a ternary operator
# <test case> ? <code block if true> : <code block if false>
# <small code block> if <condition> else <small code block>

#python version of ternary operator
# <code block if true> if <condition> else <code block if false>
print('Right on!' if meaning > 10 else 'Not today')  

