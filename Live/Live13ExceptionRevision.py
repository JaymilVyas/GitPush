try:
    a=10
    b=a/10
    print(b)
except Exception as e:
    print(e)
    print("This will be my final code after handling an exception")

try:
    f=open("Jimmy56.txt","r")
except Exception as e:
    print(e)
try:
    f=open("Jimmy.txt","r")
    f.write("This is my suspicious code")
except Exception as e:
    print(e)
    print("this is not my susp[icious code")
finally:
    print("this block will be executed anytime")

def askint():
    try:
        val=int(input("Please enter an integer "))
    except:
        print("You have not entered an integer")
        try:
            val=int(input("Please enter an integer "))
        except:
            print("We are unable to handle mistake even on 2nd attempt")
    finally:
        print("Finally will be executed anyhow")
print(askint())

def askintcontinue():
    while True:
        try:
            val=int(input("Please try to input an integer"))
            break
        except:
            print("Looks like you have entered other than integer value")
            continue
print(askintcontinue())
