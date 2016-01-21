# Luke Reed
# ex18.py
# 01/21/2016
# Names, Variables, Code, Functions

# this one is like your scripts with argv
# make a function using 'def' to define it
# '*args' is like the argv parameter except for functions
def print_two(*args):	# define function name and arguments and finish with ':'
	# make sure all lines within the function are indented
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

# now we call each of these functions
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()