# Computational Physics
Projects done in university in computational physics module. The instructions are detailed below:

Exercise 1.2 
Type in the program above (don’t worry yet about the details), save it as a Python file (text file with a .py extension), run it and check that it works. (The button with the green triangle runs the current Python file, or else you can type run filename.py in the IPython command line.) 

---

Exercise 1.3 
Write a Python program to:
add, subtract, multiply and divide the two complex numbers 2+3i and 3-7i,
subtract 2 from -3+4i
divide 7 by 2
(put comments in your code). 

---

Exercise 1.4 
Use a for-loop to go through the list L=[5,7,18,9,0,1,3,7,7,2] and find the largest item and its index, i.e. for this list you should print “the largest value is 18, item number 3 in the list”. 

---

Exercise 1.5 
Generate an array, called x, of 100 evenly spaced values between 0 and 2𝜋 inclusive (you can use np.pi for 𝜋). Generate an array, called y, whose elements are the sine of the x array (i.e. y[i] = sin(x[i]) etc.).

---

Exercise 1.7 
Type in and run the following code: 

---

Exercise 1.8 
Plot the function 𝑓(𝑥) = sin(𝑥) between 𝑥 = 0 and 𝑥 = 2𝜋 with a green dashed line. Label your axes, add gridlines and a legend. Your axes should extend only as far as the plotted data.

---

Exercise 1.9 
Type in and run the following code:

---

Problem P1.1
Write a program to plot the trajectory of a projectile thrown from the surface of the Earth.
The user should be allowed to specify the initial velocity, launch angle and time interval

---

Exercise 2.2 
Write a program to calculate the derivative of a function (defined in the program) at a point using the 3-point derivative.
Use it to calculate 

$$
\frac{d(\sin x)}{dx} \text{ at } x = \frac{\pi}{4} \, (\text{use } h = 0.01)
$$


What is the analytical answer?

---

Exercise 2.3
Write a program to calculate the derivative of a function (defined in the program) at a point using the 5-point derivative.
Use it to calculate 

$$
\frac{d(\sin x)}{dx} \text{ at } x = \frac{\pi}{4} \, (\text{use } h = 0.01)
$$

---

2.4 Write a program to plot both a function and its derivative (calculated using either the 3-or 5-point formula) over a specified range (you can use sin(𝑥) as an example and define therange in the program). 

---

Problem P2.1 Plot sin(𝑥) and 𝑑(sin(𝑥))/d𝑥 in the range [0,4𝜋].
Plot the error in the 3 point and 5 point derivative of sin(𝑥). (You can find the error because you know what the analytical answer is.)
Add some random noise to sin(𝑥) and repeat using the 3- and 5-point method.
Which method is more sensitive to noise? 


---

Exercise 3.1
| x   | f(x) |
|-----|------|
| 0.0 | 0.5  |
| 0.2 | 2.0  |
| 0.4 | 4.0  |
| 0.6 | 6.0  |
| 0.8 | 4.0  |

Write a program to estimate f(x) on any point in [0,0.8] using all the data points given (global
interpolation). Plot the points given and your values for f(0.3), f(0.5) & f(0.75). 

---

Exercise 3.2
The function f(x) is known at the following points

| x   | f(x) |
|-----|------|
| 0.0 | 0.0  |
| 1.0 | 1.0  |
| 2.0 | 1.0  |
| 2.5 | 4.0  |
| 3.0 | 3.0  |

Write a program to estimate a value for f(x) at any point in the interval [0,3] using (local)
linear interpolation. Plot the data points given along with the values you calculate for f(0.5)
& f(2.25). 

---

Exercise 3.3 
Extend the exercises above to plot 𝑓(𝑥) for all 𝑥 in range 𝑥<sub>0</sub> − 𝑥<sub>4</sub>. 

---

Exercise 3.4 
Spline interpolations, which fit piecewise polynomials that have a smooth slope
everywhere, are often preferable to local or global interpolation. Polynomials of order 3 or
more can be used; cubic splines are the most widely used. The SciPy package in Python has
methods that can be used for spline interpolation. In a two-step process
interpolate.splrep(xarray,yarray) returns a tuple (let’s call it tck) that
contains the spline coefficients and then interpolate.splev(xval,tck) uses this
interpolation to find the value corresponding to xval.
Use cubic spline interpolation to estimate 𝑓(𝑥) in [0, 1.4] if the function is known at the
following points
              𝑥 = [ 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
              𝑓(𝑥) = [ 0.5, 2.0, 4.0, 6.0, 4.0, 4.0, 5.2, 0]
Plot your interpolation on [0,1.4]. Indicate on your plot 𝑓(𝑥) for 𝑥 = 0.3, 0.5, 0.9. 

---


