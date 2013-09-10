Curriculum
==========

Vision: Create better digital citizens

Units


Details


MIT 6.00
Day 1 notes 
fixed and stored-program computers

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



	

