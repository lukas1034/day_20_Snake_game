from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        # range z zmiennymi start, stop i step
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)
