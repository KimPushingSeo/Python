#TDMA Method

#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#time step=0.01, space step=0.1
#total length=1m, total time=200s
total_length = 1
total_time = 200
dx = 0.01
dt = 0.1

#range of x and t
x = np.arange(0,total_length+dx,dx)
t = np.arange(0,total_time+dt,dt)

#temperature matrix along one-dimensional line over time
n = len(x)
m = len(t)
T = np.zeros((n,m))

#number of time steps to display, exclude t=0
nt_display = 3

#initial condition
T[:,0] = 300

#boundary condition
T[-1,:] = 300
T[0,:] = 400

#heat conductivity (assumption)
k = 200

#thermal diffusivity alpha
#Al density = 2700 kg/m**3
#Al specific heat = 900 J/g*K
alpha = k/(2700*900)

#costant lambda
lam = alpha*dt/(dx**2)

#define tridiagonal matrix A and columns vector B
A = np.diag([1+2*lam]*(n-2),0) + np.diag([-1*lam]*(n-3),-1) + np.diag([-1*lam]*(n-3),1)

#columns vertor B = (initial condition) + lambda*(next time step boundary condition)
#each time the value of j changes, the value of B are updated accordingly
for j in range(1,m):
    B = T[1:-1,j-1].copy() #assign to B calculated value, not just value of T
    B[0] = B[0] + lam* T[0,j]
    B[-1] = B[-1] + lam* T[-1,j] #each time the value of j changes, the values of B are updated accordingly
    U = np.linalg.solve(A,B)
    T[1:-1,j] = U
    
#setting ploted time value
display_j = np.arange(m/nt_display,m,m/nt_display)
display_j = np.append(display_j,[0,m-1])
display_j = display_j.astype(int)
display_j = np.sort(display_j)
    
#plot only 10 state from 0sec to 200sec at intervals of 25sec
for j in display_j:
    plt.plot(x,T[:, j], label = f't={j*dt}s')

#setting plot
plt.xlabel('Position [m]')
plt.ylabel('Temperature [K]')
plt.title('1D Heat Equation TDMA Method')
plt.legend(loc='upper right')





            