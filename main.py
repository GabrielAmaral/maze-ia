import turtle, math, time, random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Rat 'n Cheese - The Game")
wn.setup(700,700)
wn.tracer(0)

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create Rat
class Rat(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = rat.xcor()
        move_to_y = rat.ycor() + 24

        #Check if has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            path.append(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = rat.xcor()
        move_to_y = rat.ycor() - 24

        #Check if has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            path.append(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = rat.xcor() - 24
        move_to_y = rat.ycor() 

        #Check if has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            path.append(move_to_x, move_to_y)

    def collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt( (a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False 

    def go_right(self):
        move_to_x = rat.xcor() + 24
        move_to_y = rat.ycor()

        #Check if has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            path.append(move_to_x, move_to_y)

    #def move(self):

#Create Cheese
class Cheese(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
               
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create Levels List
levels = [""]

#Create wall coordinate list
walls = []

#Create path coordinate list
path = []

#Create Cheese coordinate list
cheeses = []

#Define Levels
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XQ XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXX   XXXXX",
    "X       XX  XXX       XXX",
    "X       XX  XXX   P   XXX",
    "XXXXXX  XX  XXX       XXX",
    "XXXXXX  XX  XXXXX   XXXXX",
    "XXXXXX  XX    XXX   XXXXX",
    "X  XXX        XXX   XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add level to maze list
levels.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
                       
            #Check if it is a P (rat)
            if character == "P":
                rat.goto(screen_x, screen_y)

            #Check if it is a Q (cheese)
            if character == "Q":
                cheeses.append(Cheese(screen_x, screen_y))

#Create class 
pen = Pen()
rat = Rat()

#Setup the level
setup_maze(levels[1])


#Keyboard Binding
turtle.listen()
turtle.onkey(rat.go_left,"Left")
turtle.onkey(rat.go_right,"Right")
turtle.onkey(rat.go_up,"Up")
turtle.onkey(rat.go_down,"Down")



#Main Game Loop
while True:
    for cheese in cheeses:
        if rat.collision(cheese):
            turtle.color('red')
            style = ('Courier', 30, 'italic')
            turtle.write('YOU WIN!', font=style, align='center')
            turtle.hideturtle()
            cheese.destroy()        
            cheeses.remove(cheese)
            time.sleep(1)
    wn.update()