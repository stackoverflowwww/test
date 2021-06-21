import turtle

with open('new.txt','r') as f:
    line = f.readlines()
    value=list(map(int,line))
    f.close()

turtle.shape('turtle')
size = len(value)

for i in range (0,7,1):
    if i == 0 or i == 2 :
        turtle.forward(value[0])
    else:
        turtle.forward(value[1])
    turtle.right(90)