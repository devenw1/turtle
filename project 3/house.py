import turtle

t= turtle.Turtle()



def house():
  t.penup()
  t.goto(-80,-80)
  t.pendown()
  x= 1
  while x < 5:
    t.fd(150)
    t.lt(90)
    x = x + 1 
    pass
  pass
def roof():
  t.penup()
  t.goto(-80,70)
  t.pendown()
  t.lt(45)
  t.fd(106)
  t.rt(90)
  t.fd(106)
  pass
def chimney():
  t.penup()
  t.goto(50,90)
  t.pendown()
  t.lt(135)
  t.fd(60)
  t.lt(90)
  t.fd(30)
  t.lt(90)
  t.fd(30)
  pass
def door():
  t.penup()
  t.goto(-20,-80)
  t.pendown()
  t.rt(180)
  t.fd(50)
  t.rt(90)
  t.fd(35)
  t.rt(90)
  t.fd(50)
  
  

house()
roof()
chimney()
door()
