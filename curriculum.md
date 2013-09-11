Curriculum
==========

Vision: Create better digital citizens

Units


Details

Python IDEs:
- IDLE (terrible)
- Wing IDE
- Geanie

http://pythongamebook.wordpress.com/2011/11/30/idle-vs-geany/


MIT 6.00
========

Day 1
=====
Day 1 notes 
fixed and stored-program computers

Goals: prepare you for a little programming experience before college
confident in ability to write small to medium
how to map problems to computational frameworks: solving problems w/computer

Help you become skillful to make the computer do what you want, quickly.

First problem is just getting Python installed on your computer
Open book and open note on pro

You won't be memorizing stuff. Some muscle-memory should go to
shortcuts. This is more about how well you can solve problems.

Collaborate with anyone on problem sets, but not on quizzes.
Too collaborative means you won't do well on quizzes.

No textbook. Plenty of Python books. No handouts.

Programming is a lot of fun!

What is computation?
--------------------
Two kinds of knowledge:
- declarative: statements of fact
  y is the square root of x if y * y = x

- imperative: tells you how to solve a problem
  cookbook receipe

### Recipe for finding square root
From Heron of Alexandria

Assume you want the square root of a number `n`

1. Start with a guess g
2. if g * g is close enough to n, stop
3. otherwise, create a new guess g-new = (g-old + x / g-old) / 2
4. go back to step 2


	n = 25
	g = 3
	3 * 3 = 9						# not close enough
	g = (3 + 25/3) / 2 = 5.66	# new guess
	5.667 * 5.667 = 32			# 
	g = (5.667 * 25/5.667) / 2 = 5.0392
	g = (5.0392 * 25/5.0392) / 2 = 5.000000

This is an `algorithm` that we learn to translate into a `program` for a
computer. Essential features in a program:

- It stopped, or converged. (shampoo) Occasionally they don't stop.
- instructions (operators and operands)
- Flow of control (go back to step 2, start over)

You could build circuits to solve these: fixed program computers
1941 computer by Sperry solved system of linear equations 
Alan Turing built a dedicated machine to solve Engima machines

Big break through: stored program computers
The instructions are the same as data. No distinction between the two.

You could easily change the program. And programs could build programs.
Interpreter can execute any legal set of instructions

This became a 'von Neumann architecture'.


                 +------------------+
                 |    MEMORY        |
                 +------------------+
                   +   ^        + ^
                   |   |        | |
                   v   +        v +
             +------------+   +----------+
             | CONTROL    |+-->  A L U   |
             |            |   |accumulator
             | UNIT       <--+|          |
             +------------+   +-^------+-+
                                |      |
                         +------++    +v------+
                         |input  |    |output |
                         +-------+    +-------+

Computers have a very small set of instructions.
Like a chef with a small set of ingredients.

Alan Turing showed there are 6 primative instructions, 
each operating on 1 bit of information.

Read, write, L, R, N,  HALT
http://aturingmachine.com

Python is a teaching tool. Not the best language: no such thing. Easily transferable
skills. It has:

1. syntax				
   which sequence of characters and symbols are  
   x = 3 + 4 *OK* x = 3 4 *NOT OK*  

   Formally specified in BNF:  
   http://inst.eecs.berkeley.edu/~cs164/fa11/python-grammar.html

2. static semantics
   which well-formed strings have a meaning

3. semantics

You're program might:
- crash
- might never stop (Max's primes, Sean's loop) / infinite loop
- run to completion but produce the wrong answer
  example: radiation machine, mars probe error

Big error, the 1999 $125M Mars orbiter. After 286-day journey, probe
fired to push itself into orbit. Got too close, about 100km too close.
We used pound-seconds instead of newton-seconds.

Flight system software onboard used SI units so expected newton-seconds for thrust.
Ground-based software sent Imperial measures in pound-force. 

### Why Python?
Much easier than Java
More 'correct' than JavaScript
Popular in the science and engineering
Easier to debug (interpreted vs. compiler)

Interpreted:
	source code -> checker -> interpreter -> output
Compiled
	source -> compiler -> object code (hardware) -> interpreter ->
	output




Day 2
-----
IDLE: Integraded Development Environment (IDE)
	  May be named after Eric Idle from Monty Python (lookup)

- auto-indentation
- syntax coloring
- shell (REPL)
- debugger

### Objects

Objects: everything in python is an object.
Each **object** has a **type**.
Built in function `type` determines what kind.
Two types of `type`: scalar (atomic) and non-scalar.

	3			# int	
	type(3)
	3.2			# float(ing) point - not the same as Real numbers
	type(3.2)
	3 / 4
	True		# Boolean values (look up George Boole)
	False
	type(True)
	True and False	# Perform Boolean operations on them
	None		# special value when you don't know the value

Strings of characters

	'a'
	type('s')		# <type 'str'> (a string of length 1)
	'abc'			# next two are the same
	"abc"
	type(123)		# an int
	type('123')		# a string

Can only get so far with literals. So we need Expressions. An
**expression** is a sequence of operands and operators.

	3 + 2			# 5
	3 / 2			# 1	(basically a floor operation in Py ver < 3.0)
	3.0 / 2.0		# 1.5

Other operators: +

	'a' + 'b'		# 'ab'

This is operator overloading:
Plus means string concatenation or addition, depending on types
Overloaded operators have a meaning that depends upon types of operands.

	3 3				# syntax error (two operands in a row)
	'a' + 3			# Static type error, which are good things!

Static errors catches errors that might suprise the programmer.

	'a' + '3'		# this is ok
	'a' + str(3)	# type conversion...
	int('3')		# works
	int('3x')		# fails
	int(2.1)		# truncates decimal part ... is this a good idea?
		
Usually you'll use a text editor to type something in, and `python` to
run them, in the shell.

A Program is a sequence of commands.
Program == Script. The same thing in Python.

### print
Using the `print` command. Very important.

### assignment
binds a name to an object

	x = 3
	x = x * x
	print x

### input
Getting data from the user

	raw_input('enter a number')			# returns a string
	float(raw_input('enter a number'))	# returns a float

### Complexity Theory
These are called "straight line programs". They're dead boring. You
can't do anything interesting with these.

### Conditional statements
if else





	

