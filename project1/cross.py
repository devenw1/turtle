import turtle

t = turtle.Turtle()
def main():
  t.color('red')
  t.begin_fill()
  move2location(20,-150)
  medic()
  t.endfill()
  
def left():
  t.lt(90)
  t.fd(50)
  pass
def right():
  t.rt(90)
  t.fd(50)
x=1
t.begin_fill()
left()
left()
while x < 4:
  right()
  right()
  left()
  x=x+1
right()
t.end_fill()
  
