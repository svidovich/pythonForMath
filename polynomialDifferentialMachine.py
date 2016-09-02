#!/usr/bin/python

from sympy import *
print "Welcome to polynomial differentiator. v0.0.1.\n"
print "Please enter your polynomial with the following syntax.\n"
print "To multiply two terms: m*x"
print "For exponents: u**2, u**3,...,u**n.\n"
print "Acceptable variables for use are x, y, and z."
print "This machine is NOT capable of partial differentiation."

#Allows us to use the letters x, y and z symbolically in algebraic expressions
x,y,z = symbols('x,y,z')
if __name__=='__main__':
	exp = input('Enter your polynomial: ')
	try:
		exp = sympify(exp)
	except SympifyError:
		print('Invalid input.')
	else:
		d = Derivative(exp, x)

solution = d.doit()
print "Your polynomial's derivative with respect to x is {}".format(solution)
