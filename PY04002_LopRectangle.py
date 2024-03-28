
class Rectangle:
    def __init__(self, width, height, color):
        self.height = height
        self.width = width
        self.color = color
    def out(self):
        if self.width <= 0 or self.height <= 0: return 'INVALID'
        p = (self.width+ self.height)*2
        s = (self.width * self.height)
        return f'{p} {s} {self.color.capitalize()}'
    
l = input().split()
x = Rectangle(int(l[0]), int(l[1]), l[2])
print(x.out())

"""
10 2 RED
0 1 Rre
1 2 red
"""
