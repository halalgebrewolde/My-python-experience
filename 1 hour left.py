class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point=Point(10,20)
# we can change x by adding
#point.x=Point(11) which would make it print 11
print(point.x)