# Computational Physics
Projects done in university in computational physics module. The instructions are detailed below: (they get progressively harder!)

<b>Exercise 1.2</b>   
Type in the program above, save it as a Python file (text file with a .py extension), run it and check that it works. (The button with the green triangle runs the current Python file, or else you can type run filename.py in the IPython command line.) 

---

<b>Exercise 1.3</b>   
Write a Python program to:
add, subtract, multiply and divide the two complex numbers 2+3i and 3-7i,
subtract 2 from -3+4i
divide 7 by 2
(put comments in your code). 

---

<b>Exercise 1.4</b>  
Use a for-loop to go through the list L=[5,7,18,9,0,1,3,7,7,2] and find the largest item and its index, i.e. for this list you should print “the largest value is 18, item number 3 in the list”. 

---

<b>Exercise 1.5</b>  
Generate an array, called x, of 100 evenly spaced values between 0 and 2𝜋 inclusive (you can use np.pi for 𝜋). Generate an array, called y, whose elements are the sine of the x array (i.e. y[i] = sin(x[i]) etc.).

---

<b>Exercise 1.6</b>  
Plot the function 𝑓(𝑥) = sin(𝑥) between 𝑥 = 0 and 𝑥 = 2𝜋.

---

<b>Exercise 1.7</b>  
Type in and run the following code: 

---

<b>Exercise 1.8</b>  
Plot the function 𝑓(𝑥) = sin(𝑥) between 𝑥 = 0 and 𝑥 = 2𝜋 with a green dashed line. Label your axes, add gridlines and a legend. Your axes should extend only as far as the plotted data.

---

<b>Exercise 1.9</b>  
Type in and run the following code:

---

<b>Problem 1.1</b>  
Write a program to plot the trajectory of a projectile thrown from the surface of the Earth.
The user should be allowed to specify the initial velocity, launch angle and time interval

---

<b>Exercise 2.2</b>  
Write a program to calculate the derivative of a function (defined in the program) at a point using the 3-point derivative.
Use it to calculate 

$$
\frac{d(\sin x)}{dx} \text{ at } x = \frac{\pi}{4} \, (\text{use } h = 0.01)
$$


What is the analytical answer?

---

<b>Exercise 2.3</b>  
Write a program to calculate the derivative of a function (defined in the program) at a point using the 5-point derivative.
Use it to calculate 

$$
\frac{d(\sin x)}{dx} \text{ at } x = \frac{\pi}{4} \, (\text{use } h = 0.01)
$$

---

<b>Exercise 2.4</b>  
Write a program to plot both a function and its derivative (calculated using either the 3-or 5-point formula) over a specified range (you can use sin(𝑥) as an example and define therange in the program). 

---

<b>Problem 2.1</b>  
Plot sin(𝑥) and 𝑑(sin(𝑥))/d𝑥 in the range [0,4𝜋].
Plot the error in the 3 point and 5 point derivative of sin(𝑥). (You can find the error because you know what the analytical answer is.)
Add some random noise to sin(𝑥) and repeat using the 3- and 5-point method.
Which method is more sensitive to noise? 


---

<b>Exercise 3.1</b>  
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

<b>Exercise 3.2</b>  
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

<b>Exercise 3.3</b>  
Extend the exercises above to plot 𝑓(𝑥) for all 𝑥 in range 𝑥<sub>0</sub> − 𝑥<sub>4</sub>. 

---

<b>Exercise 3.4</b>  
Spline interpolations, which fit piecewise polynomials that have a smooth slope
everywhere, are often preferable to local or global interpolation. Polynomials of order 3 or
more can be used; cubic splines are the most widely used. The SciPy package in Python has
methods that can be used for spline interpolation. In a two-step process
interpolate.splrep(xarray,yarray) returns a tuple (let’s call it tck) that
contains the spline coefficients and then interpolate.splev(xval,tck) uses this
interpolation to find the value corresponding to xval.
Use cubic spline interpolation to estimate 𝑓(𝑥) in [0, 1.4] if the function is known at the
following points  

$$
  𝑥 = [ 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]  
$$

$$
𝑓(𝑥) = [ 0.5, 2.0, 4.0, 6.0, 4.0, 4.0, 5.2, 0]
$$

Plot your interpolation on [0,1.4]. Indicate on your plot 𝑓(𝑥) for 𝑥 = 0.3, 0.5, 0.9. 

---

<b>Exercise 3.5</b>  
Compare cubic spline and global interpolation for the data points in 3.4 above. 

---

<b>Exercse 4.1</b>  
Write a program to integrate a function using the Trapezoidal rule. Comment your code.

--- 

<b>Exercse 4.2</b>  
What does your program give for ∫ sin(x) dx from 0 to π when 10 steps are used?
- What is the analytical answer?
- What is the error for 10, 20 and 100 steps?


---

<b>Exercse 4.3</b>  
Write a program to integrate a function using Simpson's rule.
Comment your code. 

---

<b>Exercse 4.4</b>  
What is the error in the integral 

∫ from 0 to π [sin(x) dx]

for 10, 20, and 100 steps (using Simpson's rule)?  
Compare with the corresponding results using the Trapezoidal rule.

---
<b>Exercise 4.5</b>
Calculate (using either the trapezoidal or Simpson’s method)

∫₀¹ eˣ dx  [0 and 1 are the limits of the integral]

∫₀.₁¹⁰ ᵡ³ / (eˣ - 1) dx [0.1 and 10 are the limits of the integral]

---

<b>Exercise 4.6</b>  
A very accurate integration method, known as **Gaussian quadrature**, allows us to vary the separation of the points xᵢ at which the function is evaluated. Gaussian quadrature is especially useful when only a small number of sample points can be used. 

Use `scipy.integrate.quadrature()` to integrate the function:
**f(x) = x⁴ - 2x + 1**
between **x = 0** and **x = 2**.

(Use online resources to find information on Python commands.)

---

<b>Problem 4.1</b><br>
Calculate the magnetic field produced by a current in a straight wire 

<div align="center">
  <img width="500" src="https://github.com/HardeepKaur21/Computational_Physics/blob/main/image.png?raw=true" alt="Description">
</div>
<br>
Write a program to calculate (& plot) the magnitude of the magnetic field over a range of
distances from a straight wire of length 2𝐿.

---

<b>Exercise 5.1</b>  
Write a program to plot and find the roots of the equation given by

$$ 
f(x) = x^4 - 19x^3 + 117x^2 - 261x + 162 = 0 
$$

between user-specified limits. The accuracy can be defined within
the program. Use the half-interval search method. (𝑓(𝑥) should be defined in a separate
function)

---

<b>Exercise 5.2</b>  
Write a program that uses the bisection method to find a root of an equation in a userspecified interval. Test the program using the equation

$$
x^4 - 19x^3 + 117x^2 - 261x + 162 = 0
$$

---

<b>Exercise 5.3</b>  
Write a program to graph the function:

$$ f(x) = \sin(x) + 4x^2 - 13x - 5 $$

in the interval $[-5,5]$. Use Newton’s Method to find a root of $f(x) = 0$. Use \( x = 1 \) and \( x = 4 \) as starting values.

---
<b>Exercise 5.4</b>  
Graph the function 

$$
f(x) = \sin(x) + 4x^2 - 13x - 5
$$

in the interval $[-5,5]$. 
Use the Secant Method to find a root of $f(x) = 0$. Use $x = 1, 4$ as starting values.

---
<b>Exercise 5.5</b>  
Use `scipy.optimize.fsolve()` to find the roots of the equation

$$
x^4 - 19x^3 + 117x^2 - 261x + 162 = 0.
$$

(Use online resources to find information on Python commands.)

---
<b>Problem 5.1</b>

Ferromagnetism arises when a collection of electron spins conspire so that all of their magnetic moments point in the same direction giving a total moment that is macroscopic insize. The spins interact with each other in 
such a way that parallel spins are favoured in a ferromagnet. The interaction is largest for nearest neighbours 
(𝑧) and falls off rapidly after that.

<div align="center">
  <img width="500" alt="P5.1 image" src="https://github.com/user-attachments/assets/4edb8591-ce66-4497-a956-7100890624c8" />
</div>



---
<b>Exercise 6.1</b>  
### Euler Method Approximation

Use the **Euler method** to solve the following first-order differential equation over the interval \([0,1]\), with the given initial condition:

$$
\frac{dy}{dx} = x + y, \quad y(0) = 1
$$

Plot a graph of your numerical solution and overlay it with the analytical solution:

$$
y = 2e^x - x - 1
$$

---
<b>Exercise 6.2</b>  
Write a program to solve the differential equation:

$$
\frac{d^2 y}{dt^2} + \frac{k}{m} y = 0
$$

numerically using **Euler's method** over the interval [0 ≤ t ≤ 20].

Take:

- k/m = 1
- Initial conditions:
  <br>
  <br>
  <img src="https://latex.codecogs.com/png.image?\dpi{120}&space;\color{White}{y(0)=0,\quad\frac{dy}{dt}(0)=1}" alt="Initial Conditions" width="120"/>


Plot a graph of y(t) as a function of t.

---
<b>Exercise 6.3</b>  
Solve the differential equation for a simple pendulum:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l} \sin(\theta)
$$

numerically using Euler's method. Plot both:
  - θ(t)
  - dθ/dt(t)  
on the same plot (choose your own initial values). Also plot the phase-space diagram (dθ/dt vs θ). Now repeat the same simulation using the **Euler-Cromer method**.
Explain the difference in behavior between the two methods.

---
<b>Exercise 6.4</b>  
Use `scipy.integrate.odeint()` to solve the ODE in Exercise 6.1. Use on-line
resources for help.

---
<b>Problem 6.1</b>
Add damping (retarding force proportional to velocity) to your pendulum model of 6.3.
Solve using the Euler-Cromer method and plot a phase space diagram. What happens if you
start with a large initial (angular) velocity?

---
<b>Exercise 7.1</b>  
Write a program to solve the differential equation:

$$
\frac{dy}{dx} = x + y
$$

on [0,1] using the RK2 and RK4 methods. Take

$$
y(0) = 1
$$

Compare your numerical results with the analytical solution:

$$
y(x) = 2e^x - x - 1
$$

---
<b>Exercise 7.2</b>  
Use the Runge–Kutta 4 method to obtain solutions to the differential equation:

$$
\frac{dy}{dt} = g \-\ \frac{k}{m} y
$$

in the interval $0 <= t <= 10$, with

- m = 1kg
- g = 9.81 $m/s^2$
- k = 2

The initial conditions are

$y(0) = 2\ \mathrm{m},\frac{dy}{dt} = 10\ \mathrm{m/s}$
