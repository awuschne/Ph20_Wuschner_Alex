
# coding: utf-8

# In[245]:

import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import math


# In[246]:

# Helper function

def plot_data(x_data, y_data, title, x_label, y_label):
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# In[247]:

# Part 1:
# Problem 1:
# Function to give next position and next velocity of the spring mass.

def spring_motion_next(x_i, v_i, h):
    x_next = x_i + h * v_i
    v_next = v_i - h * x_i
    return (x_next, v_next)


# In[248]:

# Problem 1:
h = 0.5
times = np.arange(0, 30+h, h)
x_values = np.zeros(times.size)
v_values = np.zeros(times.size)

x_values[0] = 1
v_values[0] = 0

curr_index = 0
for time in times[:-1]:
    next_state = spring_motion_next(x_values[curr_index], v_values[curr_index], h)
    x_values[curr_index + 1] = next_state[0]
    v_values[curr_index + 1] = next_state[1]
    curr_index += 1
    
explicit_x = x_values
explicit_v = v_values


# In[249]:

# Problem 1:
plot_data(times, x_values, "X(t)", "Time", "X")
plt.savefig('1.png')

# In[250]:

# Problem 1:
plot_data(times, v_values, "V(t)", "Time", "V")
plt.savefig('2.png')

# In[251]:

# Problem 2:
real_x = np.zeros(times.size)
real_v = np.zeros(times.size)

curr_index = 0
for time in times:
    real_x[curr_index] = math.cos(time)
    real_v[curr_index] = math.sin(time)
    curr_index += 1
global_errors_x = real_x - x_values
global_errors_v = real_v - v_values


# In[252]:

# Problem 2:
plot_data(times, global_errors_x, "Global Position Errors Over Time", "Time", "Global Error")
plt.savefig('3.png')

# In[253]:

# Problem 2:
plot_data(times, global_errors_v, "Global Velocity Errors Over Time", "Time", "Global Error")
plt.savefig('4.png')

# In[254]:

# Problem 3:
h = 0.1
h_values = [h, h/2, h/4, h/8, h/16]
max_truncation_error = []

for value in h_values:
    times = np.arange(0, 30+value, value)
    x_values = np.zeros(times.size)
    v_values = np.zeros(times.size)
    real_x = np.zeros(times.size)

    x_values[0] = 1
    v_values[0] = 0

    curr_index = 0
    for time in times[:-1]:
        real_x[curr_index] = math.cos(time)
        next_state = spring_motion_next(x_values[curr_index], v_values[curr_index], value)
        x_values[curr_index + 1] = next_state[0]
        v_values[curr_index + 1] = next_state[1]
        curr_index += 1
    global_error = real_x - x_values
    np.absolute(global_error)
    max_truncation_error.append(np.amax(global_error))


# In[255]:

# Problem 3:
plot_data(h_values, max_truncation_error, "Max Error vs. h", "h", "Max Truncation Error")
plt.savefig('5.png')

# In[256]:

# Problem 4:
h = 0.5
times = np.arange(0, 30+h, h)
x_values = np.zeros(times.size)
v_values = np.zeros(times.size)

x_values[0] = 1
v_values[0] = 0

curr_index = 0
for time in times[:-1]:
    next_state = spring_motion_next(x_values[curr_index], v_values[curr_index], h)
    x_values[curr_index + 1] = next_state[0]
    v_values[curr_index + 1] = next_state[1]
    curr_index += 1
energy_values = x_values**2 + v_values**2
plot_data(times, energy_values, "Normalized Total Energy", "Time","Energy")
plt.savefig('6.png')

# In[257]:

# Problem 5:
def spring_motion_next_implicit(x_i, v_i, h):
    x_next = x_i/(1+h**2) + (h * v_i)/(1+h**2)
    v_next = (-h * x_i)/(1+h**2) + v_i/(1+h**2)
    return (x_next, v_next)


# In[258]:

# Problem 5:
# Global Error

h = 0.5
times = np.arange(0, 30+h, h)
x_values = np.zeros(times.size)
v_values = np.zeros(times.size)
real_x = np.zeros(times.size)
real_v = np.zeros(times.size)

x_values[0] = 1
v_values[0] = 0

curr_index = 0
for time in times[:-1]:
    next_state = spring_motion_next_implicit(x_values[curr_index], v_values[curr_index], h)
    x_values[curr_index + 1] = next_state[0]
    v_values[curr_index + 1] = next_state[1]
    real_x[curr_index] = math.cos(time)
    real_v[curr_index] = math.sin(time)
    curr_index += 1

global_errors_x = real_x - x_values
global_errors_v = real_v - v_values

implicit_x = x_values
implicit_v = v_values


# In[259]:

# Problem 5:
plot_data(times, global_errors_x, "Global Position Errors Over Time", "Time", "Global Error")
plt.savefig('7.png')

# In[260]:

# Problem 5:
plot_data(times, global_errors_v, "Global Velocity Errors Over Time", "Time", "Global Error")
plt.savefig('8.png')

# In[261]:

# Problem 5:
energy_values = x_values**2 + v_values**2
plot_data(times, energy_values, "Normalized Total Energy", "Time","Energy")
plt.savefig('9.png')

# In[271]:

# Part 2:
# Problem 1:
h = 0.2
times = np.arange(0, 30+h, h)
explicit_x = np.zeros(times.size)
explicit_v = np.zeros(times.size)
implicit_x = np.zeros(times.size)
implicit_v = np.zeros(times.size)

explicit_x[0] = 1
explicit_v[0] = 0
implicit_x[0] = 1
implicit_v[0] = 0

curr_index = 0
for time in times[:-1]:
    next_state_ex = spring_motion_next(explicit_x[curr_index], explicit_v[curr_index], h)
    next_state_im = spring_motion_next_implicit(implicit_x[curr_index], implicit_v[curr_index], h)
    explicit_x[curr_index + 1] = next_state_ex[0]
    explicit_v[curr_index + 1] = next_state_ex[1]
    implicit_x[curr_index + 1] = next_state_im[0]
    implicit_v[curr_index + 1] = next_state_im[1]
    curr_index += 1


# In[272]:

# Problem 1:
plt.plot(explicit_x, explicit_v)
plt.title("Phase Space for Explicit Euler")
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.plot(real_x, real_v)
plt.show()
plt.savefig('10.png')

# In[273]:

# Problem 1:
plt.plot(implicit_x, implicit_v)
plt.title("Phase Space for Implicit Euler")
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.plot(real_x, real_v)
plt.show()
plt.savefig('11.png')

# In[265]:

# Problem 2:
def spring_motion_next_symplectic(x_i, v_i, h):
    x_next = x_i + h * v_i
    v_next = v_i - h * x_next
    return (x_next, v_next)


# In[274]:

# Problem 2:
h = .2
times = np.arange(0, 30+h, h)
symplectic_x = np.zeros(times.size)
symplectic_v = np.zeros(times.size)

symplectic_x[0] = 1
symplectic_v[0] = 0

curr_index = 0
for time in times[:-1]:
    next_state = spring_motion_next_symplectic(symplectic_x[curr_index], symplectic_v[curr_index], h)
    symplectic_x[curr_index + 1] = next_state[0]
    symplectic_v[curr_index + 1] = next_state[1]
    curr_index += 1
    
plt.plot(symplectic_x, symplectic_v, label="Symplectic Method")
plt.title("Phase Space for Implicit Euler")
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.plot(real_x, real_v, label="Analytical Solution")
plt.legend(loc=8,bbox_to_anchor=(1.3, 0.5))
plt.axis('equal')
plt.show()
plt.savefig('12.png')

# In[275]:

# Problem 3:
energy_values = symplectic_x**2 + symplectic_v**2
plot_data(times, energy_values, "Normalized Total Energy", "Time","Energy")
plt.savefig('13.png')

# In[ ]:



