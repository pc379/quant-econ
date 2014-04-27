from __future__ import division
from random import uniform, normalvariate
from math import sqrt
from pylab import plot, show, legend

#Exercise 1
def factorial(n):
	answer=1
	for i in range(n):
			answer=answer*i+1
	return answer

#print factorial(2)

#Exercise 2
def binomial_rv(n,p):
	count=0
	i=1
	while i<=n:
		U=uniform(0,1)
		if U<p:
			count=count+1
		i=i+1
	return count

#print binomial_rv(2,.9)

#Exercise 3
def ApproxPi(n):
	count=0
	for i in range(n):
		x=uniform(-1,1)
		y=uniform(-1,1)
		if sqrt((x)**2+(y)**2)<1:
			count=count+1
	return 4*count/n

#print ApproxPi(1000000)

#Exercise 4
def coinToss():
	tricount=0
	count=0
	for i in range(10):
		toss=uniform(0,1)
		if toss<.5:
			count=count+1
		else: count=0
		if count==3:
			tricount=tricount+1
	if tricount>0:
		return 'won a dollar!'
	else: return 'won nothing'

#print coinToss()

#Exercise 5 & 6
def timeSeries():
	T=200
	As=[0, .8, .98]
	for a in As:
		xes=[0]
		for t in range(T):
			e=normalvariate(0,1)
			x1=xes[t]*a+e
			xes.append(x1)
		plot(xes, label="alpha="+str(a))
	legend()
	show()

#timeSeries()






