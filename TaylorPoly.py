# CST-307: Principles of Modeling 
# WF1100A Dr. Citro
# Dayana Gonzalez Cruz
# Numerical Computations with Taylor Polynomials: Project 6: Lorenz_Adjusted.py
# 11/29/2023

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

step_size = 0.05
num_steps = 1000

# Initialize lists to hold data points
P1a = np.empty(num_steps + 1)
P1b = np.empty(num_steps + 1)
P2 = np.empty(num_steps + 1)

# Define Part 1: (a) Taylor polynomial
def Part1a():
	x = 0
	for i in range(num_steps):
		y = 1 - x - (1/3)*pow(x,3)-(1/12)*pow(x,4)
		P1a[i] = y
		x += step_size
	x_values = np.linspace(0, (num_steps-1)*step_size, num_steps+1)
	plt.plot(x_values, P1a, label='y(x) = 1 - x - (1/3)x^3 -(1/12)x^4 ')
	
	# Mark particular point y at x = 3.5
	x = 3.5
	y = 1 - x - (1/3)*pow(x,3)-(1/12)*pow(x,4)
	print('y(3.5) = ', y)
	plt.scatter(x,y, color='pink', label = 'y(3.5) = -29.2969')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title('Taylor Series Solution to Part 1 (a)')
	plt.legend()
	plt.show()

# Define Part 1: (b) Taylor polynomial 
def Part1b():
	x = 3
	for i in range(num_steps):
		y = 6 + (x-3)-(11/2)*pow((x-3),2)
		P1b[i] = y
		x += step_size
	x_values = np.linspace(0, (num_steps-1)*step_size, num_steps+1)
	plt.plot(x_values,P1b, label = 'y(x) = 6 + (x-3)-(11/2)(x-3)^2 ')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.title('Taylor Series Solution to Part 1 (b)')
	plt.show()

# Define Part 2: Recursive formula for power series solution

def Part2():
	a0 = 1
	i = 0
	n = 0
	for i in range(num_steps):
		a_n =  -a0 / (4 * (n+1) * (n+2))
		P2[i] = a_n
		i += 1
		n += 1
	plt.plot(P2, label = 'a_(n+2) = -a0 / (4(n+1)(n+2)')
	plt.xlabel('n')
	plt.ylabel('an+2')
	plt.title('Power Series Solution to Part 2')
	plt.legend()
	plt.show()

# Define Part 3: Computer Performance Model
def performanceModel(C,t,a,b):
	P = C[0]
	M = C[1]
	dC_dt = a * P - b * M
	return [dC_dt,0]
def Part3():
	# Intialize dummy data 
	a = 0.1 # Processor speed scaling factor
	b = 0.05 # Memory capacity scaling factor
	P0 = 2.0 # Initial processor speed
	M0 = 500 # Initial memory capacity
	initial_values = [P0,M0]
	# Time intervals
	t = np.linspace(0,10,100)
	P3 = odeint(performanceModel,initial_values, t, args=(a, b))
	P_t = P3[:, 0]
	M_t = P3[:,1]
	
	# Label and Display
	plt.plot(t,P_t, label = 'Processor Speed (P)')
	plt.plot(t, M_t, label = 'Memory Capacity (M)')
	plt.xlabel('Time')
	plt.ylabel('Values')
	plt.title('Computer Performance over Time: dC/dt = aP - bM')
	plt.legend()
	plt.show()
# Call all functions to calculate and display
Part1a()
Part1b()
Part2()
Part3()
		