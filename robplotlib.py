import math

class Board:
    def __init__(self, size, seperator):
        self.SIZE = size
        self.OFFSET = int((self.SIZE-1)/2)
        self.points = []
        self.lines = []
        self.scale = 1
        self.seperator = seperator
       
        self.clear()
   
    def clear(self):
        self.board = [[" " for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if x == self.OFFSET and y == self.OFFSET:
                    self.board[y][x] = "+"
                elif x == self.OFFSET and y % 2 == 0:
                    self.board[y][x] = "|"
                elif y == self.OFFSET and x % 2 == 0:
                    self.board[y][x] = "-"
   
    def show(self):
        print()
        for line, char in self.lines:
            self._line(line, char)
       
        for cord, char in self.points:
            if -self.OFFSET*self.scale <= cord[0] <= self.OFFSET*self.scale and -self.OFFSET*self.scale <= cord[1] <= self.OFFSET*self.scale:
                self._point(cord, char)
       
        for i in range(len(self.board)-1, -1, -1):
            print("[" + self.seperator.join(self.board[i]) + "]")
       
        self.clear()
   
    def point(self, cord, char):
        if [cord, char] not in self.points:
            self.points.append([cord, char])
   
    def _point(self, cord, char):
        self.board[round(cord[1]/self.scale+self.OFFSET)][round(cord[0]/self.scale+self.OFFSET)] = char
       
    def zoom(self, scale):
        self.scale = scale
   
    def segment(self, a, b, char):
        point1 = a
        point2 = b
        line = Line(point1, point2)
       
        m = line.m
        b = line.b
       
        if m == Math.UNDEFINED:
            ymin = min(point1[1], point2[1])
            ymax = max(point1[1], point2[1])
           
            for i in range(ymin, ymax+1):
                self.point([point1[0], i], char)
           
            return
       
        if m == 0:
            xmin = min(point1[0], point2[0])
            xmax = max(point1[0], point2[0])
           
            for i in range(xmin, xmax+1):
                self.point([i, point1[1]], char)
           
            return
       
        if point1[0] > point2[0]:
            temp = point1
            point1 = point2
            point2 = temp
       
        for x in range(-self.OFFSET, self.OFFSET + 1):
            for y in range(-self.OFFSET, self.OFFSET + 1):
                if round(y) == round(m*x + b) and point1[0] < x < point2[0]:
                    self.point([x, y], char)
       
        if point1[1] > point2[1]:
            temp = point1
            point1 = point2
            point2 = temp
       
        for x in range(-self.OFFSET, self.OFFSET + 1):
            for y in range(-self.OFFSET, self.OFFSET + 1):
                if round(x) == round((y-b)/m) and point1[1] < y < point2[1]:
                    self.point([x, y], char)
   
    def line(self, a, b, c = None):
        if c is not None:
            self.lines.append([Line(a, b), c])
       
        else:
            self.lines.append([a, b])
   
    def _line(self, line, char):
        m = line.m
        b = line.b
        a = line.a
       
        if m == Math.UNDEFINED:
            for i in range(-self.OFFSET, self.OFFSET+1):
                self.point([a, i*self.scale], char)
           
            return
       
        for x in range(-self.OFFSET, self.OFFSET+1):
            self.point([x*self.scale, line.get_y(x*self.scale)], char)
       
        for y in range(-self.OFFSET, self.OFFSET+1):
            if m != 0:
                self.point([line.get_x(y*self.scale), y*self.scale], char)
           

class Math:
    ALL_REAL_NUMBERS = True
    NO_SOLUTIONS = False
    UNDEFINED = None
    
    def sin(angle):
        return math.sin(math.radians(angle))

    def cos(angle):
        return math.cos(math.radians(angle))

    def tan(angle):
        return math.tan(math.radians(angle))
   
    def asin(x):
        return math.degrees(math.asin(x))
   
    def acos(x):
        return math.degrees(math.acos(x))
   
    def atan(x):
        return math.degrees(math.atan(x))

    def ymxb(p1, p2):
        if not isinstance(p2, list):
            m = p2

        else:
            if p1[0] == p2[0]:
                return [Math.UNDEFINED, p1[0]]
           
            m = (p2[1]-p1[1])/(p2[0]-p1[0])
       
        b = p1[1]-m*p1[0]

        return [m, b]

    def cord(coord):
        return [coord[1]*Math.cos(coord[0]), coord[1]*Math.sin(coord[0])]

    def dist(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def intersect(line1, line2):
        if line1.m == line2.m and line1.b == line2.b and line1.a == line2.a:
            return Math.ALL_REAL_NUMBERS
        
        if line1.m == line2.m:
            return Math.NO_SOLUTIONS
       
        if line1.m is Math.UNDEFINED:
            x = line1.a
            y = x * line2.m + line2.b
           
            return [x, y]
       
        if line2.m is Math.UNEDFINED:
            x = line2.a
            y = x * line1.m + line1.b
           
            return [x, y]
       
        x = (line2.b-line1.b)/(line1.m-line2.m)
        y = line1.m * x + line1.b
       
        return [x, y]

class Line:
    def __init__(self, *args):
        if isinstance(args[0], list):
            line = Math.ymxb(*args)
       
        else:
            line = args

        self.m = line[0]

        if self.m == 0:
            if line[1] == 0:
                self.b = 0
                self.a = 0
           
            else:
                self.b = line[1]
                self.a = None
           
        elif self.m is not Math.UNDEFINED:
            self.b = line[1]
            self.a = -self.b / self.m
       
        else:
            if line[1] == 0:
                self.b = 0
                self.a = 0
            else:
                self.b = None
                self.a = line[1]
       
    def __getitem__(self, key):
        return self.get_y(key)
   
    def get_y(self, x):
        if self.m == Math.UNDEFINED:
            if x == self.a:
                return Math.ALL_REAL_NUMBERS
            else:
                return Math.NO_SOLUTIONS
       
        return self.m * x + self.b
   
    def get_x(self, y):
        if self.m == 0:
            if y == self.b:
                return Math.ALL_REAL_NUMBERS
            else:
                return Math.NO_SOLUTIONS
       
        if self.m == Math.UNDEFINED:
            return self.a
       
        return (y - self.b) / self.m
   
    def has_point(self, point):
        x = point[0]
        y = point[1]

        if self.m is Math.UNDEFINED:
            return round(x) == round(self.a)
       
        else:
            return round(y) == round(self.m * x + self.b)

class Color:
    BLACK = "\033[30m\u25A0\033[0m"
    RED = "\033[31m\u25A0\033[0m"
    GREEN = "\033[32m\u25A0\033[0m"
    YELLOW = "\033[33m\u25A0\033[0m"
    BLUE = "\033[34m\u25A0\033[0m"
    PURPLE = "\033[35m\u25A0\033[0m"
    CYAN = "\033[36m\u25A0\033[0m"
    GRAY = "\033[37m\u25A0\033[0m"
