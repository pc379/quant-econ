from __future__ import division
# 1
def inProduct(x_vals, y_vals):
	return sum(x*y for x,y in zip(x_vals,y_vals))
x=(1,2,3,4)
y=(3,4,5,6)
#print inProduct(x,y)

#print sum(x%2==0 for x in range(100))

pairs=((2,5),(4,2),(9,8),(12,10))
#print sum (x%2==0 and y%2==0 for x,y in pairs)

#2
def p(x, coeff):
	return sum (a*(x**index) for index, a in enumerate(coeff))
	 
#print p(2, [3,4,5,6])

#3
def numCap(x):
	return sum (c1==c2 for c1,c2 in zip(x, x.upper()))

#print numCap('adCDef')

#4
def subSet(seq_a, seq_b):

	for a in seq_a:
		if a not in seq_b:
			return False
	return True

#print subSet('abcdedf','abcdefhgh')

#5
def linapprox(f, a, b, n, x):
	interval=b-a
	step=interval/n
	point=a
	while point<=x:
		point=point+step
	x2,x1=point, point-step
	return f(x1)+(x-x1)*(f(x2)-f(x1))/(x2-x1)



