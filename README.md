#

This module is a matplotlib-inspired library for micropython.

THIS IS **NOT** A PORT OF MATPLOTLIB
In fact, I have never even used matplotlib and I don't know how to.
This library uses its own graphing system that is completely unnafiliated with matplotlib.

THE DOCS:

class Board:
	this is the class used to display points and lines using the shell.


	def __init__(self, size, seperator):
		initializes the class
		
		size: determines the total width of the board. ie. size = 11:
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[-| |-| |-|+|-| |-| |-]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		size = 21:
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[-| |-| |-| |-| |-| |+| |-| |-| |-| |-| |-]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		[ | | | | | | | | | | | | | | | | | | | | ]
		[ | | | | | | | | | ||| | | | | | | | | | ]
		
		seperator: determines the seperator in between all of the cells. ie. seperator = "|"
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[-| |-| |-|+|-| |-| |-]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		[ | | | | | | | | | | ]
		[ | | | | ||| | | | | ]
		seperator = " "
		[          |          ]
		[                     ]
		[          |          ]
		[                     ]
		[          |          ]
		[-   -   - + -   -   -]
		[          |          ]
		[                     ]
		[          |          ]
		[                     ]
		[          |          ]

	
	def clear(self):
		clear the board. this runs when you initialize the board

	
	def show(self):
		display the current board using the current zoom

	def point(self, cord, char):
		add a point to the board. when you call this, it does not print the screen. to actually view the point, you must call show().
	
		cord: a two-item list (cannot be a tuple) that contains the x and y value. ie. x = 5 and y = 2 would be [5, 2].
		
		char: the character used to display the point. This can be any normal keyboard character, or it can be one of the constants in the Color class.


	def zoom(self, scale):
		zooms in or out of the board. when you call this, it does not print the screen. to actually view the updated zoom, you must call show().
	
		scale: the scale of the zoom. 1 is normal, greater is more zoomed in and less is more zoomed out. CANNOT BE NEGATIVE OR ZERO.


	def segment(self, a, b, char):
		draws a segment on the board. when you call this, it does not print the screen. to actually view the segment, you must call show().
	
		a: the first point of the segment in the format mentioned above.
		b: the second point of the segment in the format mentioned above.
		char: the character used to display the point. This can be any normal keyboard character, or it can be one of the constants in the Color class.


	def line(self, a, b, c = None):
		draws a segment on the line. when you call this, it does not print the screen. to actually view the line, you must call show().
	
		there are multiple ways to use this function. you can either use a as the line and b as the char, or you can use a and b as params for the line and c as the char. if you want to use the first way, look below to the Line class. The second way is identical but instead of saying board.line(Line(1, 1), Color.BLUE), you can just say board.line(1, 1, Color.BLUE).



class Math:
	this class has some features for interacting with lines and angles.


	these are self explanitory:
	ALL_REAL_NUMBERS = True
    NO_SOLUTIONS = False
    UNDEFINED = None

	def sin(angle):
		this is like normal python sin but it uses degrees instead of radians


	def cos(angle):
		this is like normal python cos but it uses degrees instead of radians


	def tan(angle):
		this is like normal python tan but it uses degrees instead of radians


	def asin(x):
		this is like normal python asin but it uses degrees instead of radians


	def acos(x):
		this is like normal python acos but it uses degrees instead of radians

	def atan(x):
		this is like normal python atan but it uses degrees instead of radians

	def ymxb(p1, p2):
		takes in a point and a slope or two points and returns a list pair of [slope, y intercept]. If the slope is undefined, it will return [Math.UNDEFINED, x intercept].

		if you are giving this function a point and a slope, than p1 is the point and p2 is the slope.
		if you are giving this function two points, than p1 is the first point and p2 is the second.


	def cord(coord):
		takes in a [angle, distance] list pair and returns a coordinate pair.


	def dist(p1, p2):
		returns the distance between p1 and p2


	def intersect(line1, line2):
		returns at which point line1 and line2 intersect. If they do not intersect, it returns Math.NO_SOLUTIONS. If they are the same line, it returns Math.ALL_READ_NUMBERS.

		both line1 and line2 must be of the Line type, defined below.


class Line:
	the format of a line used in the module.

	def __init__(self, *args):
		there are multiple ways to use this function. You can either pass in a slope and y intercept (if the slope is undefined, pass in an x intercept), you can pass in a point and a slope, (like used in Math.ymxb shown previously), or you can pass in two points.

	self.m: the slope of the line
	self.b: the y intercept of the line. None if it does not hit the y-axis.
	self.a: the x intercept of the line. None if it does not hit the x-axis.

	def __getitem__(self, key):
		equivalent to self.get_y shown below.

	def get_y(self, x):
		takes in an x value and returns the y

	def get_x(self, y):
		takes in a y value and returns the x

	def has_point(self, point):
		takes in a point and return a boolean if it is on the line or not.


class Color:
	this is really just a bunch of unicode squares with ANSI colors


#
	currently, defined colors are BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, and GRAY
