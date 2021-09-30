#Fibonacci Sequence
#Add two numbers together 0+1,1+2,2+3, etc..

def fibtime(x,y,z):
    while z <= 255:
        print(z)
        z=(x+y)
        x=y
        y=z
fibtime(0,1,0)