a=int(input("enter 1st Number"))
b=int(input("enter 2nd number"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("b should not be a zero")



while True:
    try:
        a = int(input("enter 1st number"))
        b = int(input("enter 2nd number"))
        c = a / b
        print(c)
        break
    except ValueError:
        print("there should not be a string")
    except ZeroDivisionError:
        print("non zero denominator")




while True:
    try:
        a=int(input("enter a string"))
    except:
        print("string not allowed")



while True:
    try:
        a=int(input("first number:"))
        b=int(input("second number:"))
        c=a/b
        print("div: ", c)
        break
    except ZeroDivisionError as e:
        print(e)




import sys
while True:
    try:
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a / b
        print("div: ", c)
        break
    except:
        print(sys.exc_info())




import sys
while True:
    try:
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a / b
        print("div: ", c)
        break
    except:
        a,b,c=sys.exc_info()
        print("exception class",a)
        print("exception message",b)
        print("line number",c.tb_lineno)




import traceback
while True:
    try:
        a = int(input("first number:"))
        b = int(input("second number:"))
        c = a / b
        print("div: ", c)
        break
    except:
        print(traceback.format_exc())




while True:
    try:
        a=int(input("first number: "))
        b=int(input("second number: "))
        if a<0 or b<0:
            raise Exception("negetive number is not allowed")
        c=a/b
        print("div: ",c)
        break
    except ValueError:
        print("please enter int only")
    except ZeroDivisionError:
        print("please enter non zero denominator")
    except Exception as e:
        print(e)




class NegativeNumberException(Exception):
    pass
while True:
    try:
        a=int(input("first number: "))
        b=int(input("second number: "))
        if a<0 or b<0:
            raise NegativeNumberException("negative number is not allowed")
        c=a/b
        print("div: ",c)
        break
    except ValueError:
        print("please enter int only")
    except ZeroDivisionError:
        print("please enter non zero denominator")
    except NegativeNumberException as e:
        print(e)




try:
    a=int(input("1st number: "))
    b=int(input("2nd number: "))
    c=a/b
    print(c)
except:
    print("dont use zero in denominator")
finally:
    print("hello")
    print("python")




try:
    a=int(input("1st: "))
    b=int(input("2nd: "))
    c=a/b
    print(c)
except:
    print("dont use zero denominator")
else:
    print("python rocks!!")

