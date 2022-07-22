#Q:1.What are the two values of the Boolean data type? How do you write them?
#A:1.
    #Two values are TRUE and FALSE of Boolean DataType. They can be used to check the validation as given in one example below:
a=0
b=1
print(a==b)


#Q:2. What are the three different types of Boolean operators?
#A:2.
    #AND, OR, and NOT are the primary operators of Boolean DataType.
    # Also == and != are also important operators of Boolean DataTypes.


#Q:3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
#A:3.
    #AND Operator:
        #A=TRUE, B=TRUE, Output=True;
        #A=TRUE, B=FALSE, Output=FALSE;
        #A=FALSE, B=TRUE, Output=FALSE;
        #A=FALSE, B=FALSE, Output=FALSE
    #OR Operator:
        #A=TRUE, B=TRUE, Output=TRUE;
        #A=TRUE, B=FALSE, Output=TRUE;
        #A=FALSE, B=TRUE, Output=TRUE;
        #A=FALSE, B=FALSE, Output=FALSE
    #NOT Operator:
        #A=TRUE, Condition=Not A, Output=FALSE;
        #A=FALSE, Condition=Not A, Output=TRUE


#Q:4. What are the values of the following expressions?
#A:4.
    #(5 > 4) and (3 == 5)
        #Values: TRUE And FALSE; Output= FALSE
    #not (5 > 4)
        #Values: FALSE
    #(5 > 4) or (3 == 5)
        #Values: TRUE Or FALSE; Output= TRUE
    #not ((5 > 4) or (3 == 5))
        #Values: TRUE
    #(True and True) and (True == False)
        #Values: TRUE And FALSE; Output=FALSE
    #(not False) or (not True)
        #Values: TRUE


#Q:5. What are the six comparison operators?
#A:5.
    #Greater Than: >
    #Less Than: <
    #Equal To: ==
    #Not Equal To: !=
    #Greater Than Or Equal To: >=
    #Less Than Or Equal To: <=


#Q:6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.
#A:6.
    #Assigment Operators can be used to assign values to the declared variables. OR while declaring the variable we give the primary value to it.
    #On the other hand equal to == will be used while checking the validation of two variables. It is mostly used when using if, elif, loop, functions.
    # =, +=, -=, *=, /=, %=, etc are the assignment variables which means, the values will be computed first to the right side valiable and then it will be assigned to the left side variable.
    #Example: a+=b which means, first sum of a And b should be computed and then the output of that computation will be assigned to a as a new value of a.


#Q:7. Identify the three blocks in this code:
    #spam = 0
    #if spam == 10:
    #print('eggs')
    #if spam > 5:
    #print('bacon')
    #else:
    #print('ham')
    #print('spam')
    #print('spam')
#A:7.
    #1st Block: Indentation Errors at each line of print statement
    #2nd Block: in else condition, spam is entered in print statement in string form, which is why instead of printing value of spam it is printing word as 'spam'
    #3rd Block: 2 if conditions mentioned, hence, if the value of spam=10 then it will print both 'eggs' and 'baacon'. Instead, elif condition could have been used here.


#Q:8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
#A:8.
spam=1
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")

#Q:9. If your programme is stuck in an endless loop, what keys you’ll press?
#A:9.
    #Stop OR
    #Stop Background Process


#Q:10. How can you tell the difference between break and continue?
#A:10.
    #Break will treminate the statement wheras Continue will skip the error if any and then move to next line of the statement.


#Q:11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
#A:11.
    #range(10), range(0,10) and range(0,10,1) all three are same and will pick the values from 0 to 9 as it will eliminate the upper bound=10.
for i in range(10):
    print(i)
for j in range(0,10):
    print(j)
for k in range(0,10,1):
    print(k)


#Q:12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
#A:12.
for i in range(11):
    print(i)
a=0
while a<=10:
    print(a)
    a=a+1


#Q:13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
#A:13.
#import.spam
#spam.bacon()
