from turtle import *
from random import *

def border():
	p = Turtle()
	p.speed(0)
	p.ht()
	p.pu()
	p.width(10)
	p.color("#ffffe6")
	p.goto(-200,200)
	p.pendown()
	p.begin_fill()
	for i in range(4):
		p.forward(400)
		p.right(90)

	p.end_fill()



class Player(Turtle):
  def __init__(self, x, y, color, fire_k, left_k, right_k):
    super().__init__()
    self.speed(2)
    self.shape("turtle")
    self.pu()
    self.ht()
    self.goto(x, y)
    self.color(color)
    self.left(90)
    self.st()
    self.list = []
    self.zlist = []
    self.status = "true" 
    screen.onkey(self.fire, fire_k)
    screen.onkey(self.turnright, right_k)
    screen.onkey(self.turnleft, left_k)
  def death(self, z, p):
    if z.distance(p) < 20:
      p.ht()
      p.goto(300,300)
      self.status = "false"
  def movement(self):
    
    new_x= self.xcor()+ 5
    new_y= self.ycor()+ 5
    if new_x< 195 and new_x >  -195:
      if new_y<195 and new_y> -195:
        self.forward(2)
      elif new_y>195 or new_y< -195:
        n_head = 0 - self.heading()
        self.setheading(n_head)
        self.forward(2)
    elif new_x> 195 or new_x < -195:
      n_head = 180 - self.heading()
      self.setheading(n_head)
      self.forward(2)
      
  def turnleft(self):
    self.left(3)
    
  def turnright(self):
    self.right(3)
    
  def fire(self):
    if len(self.list) <= 5:
      self.list.append(Bullet(self))
    
class Bullet(Turtle):  
  def __init__(self, player):
    super().__init__()
    self.speed(0)
    self.pu()
    self.ht()
    self.goto(player.xcor(),player.ycor())
    self.shape("classic")
    self.setheading(player.heading())
    self.forward(20)
    self.showturtle()
    self.player = player
  def move(self):
    self.forward(10)
    if self.xcor() <= -195:
      self.delete()
    elif self.xcor() >= 195:
      self.delete()
    elif self.ycor() >= 195:
      self.delete()
  def delete(self, ):
    self.ht()
    self.goto(300, 300)
    self.player.list.remove(self)

class Prize(Turtle):
  def __init__(self, x, y, sp):
    super().__init__()
    self.ht()
    self.pu()
    self.speed(0)
    self.shape("circle")
    self.color("yellow")
    self.goto(randint(-200,200),randint(-200,200))
    self.sp = sp
    self.st()
    
  def collisions(self, player):
    if self.distance(player) < 20:
      
      self.hideturtle()
      self.goto(randint(-200,200),randint(-200,200))
      player1.zlist.append(Zombies(player1, self.sp))
      player2.zlist.append(Zombies(player2, self.sp))
      self.showturtle()
      
      
  
  def mp(self, ):
        
        del_x = randint(-5,5)
        del_y = randint(-5,5)
        new_x= self.xcor()+ del_x
        new_y= self.ycor()+ del_y
        if new_x> 199 or new_x <  -199:
          new_x = self.xcor()+ del_x*-1
        if new_y > 199 or new_y< -199: 
            new_y = self.ycor()+del_y*-1
        self.goto(new_x, new_y)

class Zombies(Turtle):
  def __init__(self, player,speed):
    super().__init__()
    self.penup()
    self.hideturtle()
    self.color("black")
    self.shape("circle")
    self.speed(0)
    self.goto(randint(-200,200),randint(-200,200))
    self.player = player
    self.sp = speed
    
    self.showturtle()
  def zombie_movement(self):
    self.setheading((self.towards(self.player)))
    self.forward(self.sp)

  def delete(self,):
    self.ht()
    self.goto(300, 300)
    self.player.zlist.remove(self)
### SCREEN ###
screen = Screen()
screen.bgcolor("black")  
border()

screen.listen()
player1 = Player( 60, -180, "maroon", "Up", "Left", "Right")
player2 = Player( -60, -180, "purple", "w", "a", "d")

def update():
  for b in player1.list:
    b.move()
    for z in player1.zlist :
      if b.distance(z) < 25:
        z.delete()
        b.delete()
    for z in player2.zlist :
      if b.distance(z) < 25:
        z.delete()
        b.delete()

  for b in player2.list:
    b.move()
    for z in player2.zlist :
      if b.distance(z) < 25:
        z.delete()
        b.delete()
    for z in player1.zlist :
      if b.distance(z) < 25:
        z.delete()
        b.delete()

        
def z_moves():
  for z in player1.zlist:
    z.zombie_movement()
  for z in player2.zlist:
    z.zombie_movement()
def dead():
  for z in player2.zlist:
    player1.death(z, player1)
  for z in player1.zlist:
    player1.death(z, player1)
  for z in player2.zlist:
    player2.death(z, player2)
  for z in player1.zlist:
    player2.death(z, player2)



def game():
  turt = Turtle() 
  turt.ht()
  
  diffuculty = int(input("What diffuculty do you want to play. 1=Easy, 2=Medium, 3=Hard: "))  
  prize = Prize(0, 200, diffuculty)
  while player1.status and player2.status == "true":
    
    tracer(1.5)
    prize.collisions(player1)
    prize.collisions(player2)
    dead()
    player1.movement()
    player2.movement()
    prize.mp()
    update()
    z_moves()
    if player1.status != "true":
      turt.color("purple")
      turt.write("Purple is the WINNER", align="center", font=("Arial", 25, "normal"))
      break
    elif player2.status != "true":
      turt.color("maroon")
      turt.write("Maroon is the WINNER", align="center", font=("Arial", 25, "normal"))
      
      break
### Game Loop ###
game()
