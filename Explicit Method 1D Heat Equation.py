#Explicit Method

#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#space step dx=0.01m, time step dt=0.1s
dx = 0.01
dt = 0.1

#range of x and t
total_time = 200
total_length = 1
x = np.arange (0,total_length+dx,dx)
t = np.arange (0,total_time+dt,dt)

#define temperature matrix T along the scale of space,time step
n = len(x)
m = len(t)
T = np.zeros((n,m))

#initial condition
T[:,0] = 300

#boundary condition
T[0,:] = 400
T[-1,:] = 300

#number of time steps to display, exclude t=0
nt_display = 8

#thermal conductivity (assumption)
k= 200

#thermal diffusivity alpha
#Al density = 2700 kg/m**3
#Al specific heat = 900 J/gK
alpha = k/(2700*900)

#constant lambda
lam = alpha*dt/(dx**2)

#calculate T ,exclude initial and boundary condition
for j in range(1,m):
    for i in range(1,n-1):
        T[i,j] = lam*T[i-1,j-1]+(1-2*lam)*T[i,j-1]+lam*T[i+1,j-1]

#setting ploted time value
display_j = np.arange(m/nt_display,m,m/nt_display)
display_j = np.append(display_j,[0,m-1])
display_j = display_j.astype(int)
display_j = np.sort(display_j)

#i is just sequence number of space step rather than actual space value
#plot x and T
#plot just 10 state from 0sec to 200sec at intervals of 25sec
for j in display_j:
    rounded_time = round(j*dt,1)
    plt.plot(x, T[:, j], label = f't={j*dt}s')

#setting plot
plt.xlabel('Position [m]')
plt.ylabel('Temperature [K]')
plt.title('1D Heat Equation Explicit Method')
plt.legend(loc ='upper right')
