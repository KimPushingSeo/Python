#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#define common parameters

#time step=0.01, position step=0.1
#total length=1m, total time=200s
total_length = 1
total_time = 200
dx = 0.01
dt = 0.1

#range of x and t
x = np.arange(0,total_length+dx,dx)
t = np.arange(0,total_time+dt,dt)

#heat conductivity (assumption)
k = 200

#thermal diffusivity alpha
#Al density = 2700 kg/m**3
#Al specific heat = 900 J/g*K
alpha = k/(2700*900)

#costant lambda
lam = alpha*dt/(dx**2)

#temperature matrix along one-dimensional line over time
#tdma method = TT, explicit method = ET
n = len(x)
m = len(t)
TT = np.zeros((n,m))
ET = np.zeros((n,m))

#initial condition
TT[:,0] = ET[:,0] = 300

#boundary condition
TT[0,:] = ET[0,:] = 400
TT[-1,:] = ET[-1,:] = 300

#number of time steps to display
nt_display = 8
#number of dotss for TDMA Method to display per unit time
nd_display = 15


############################################################################################################################

#define tridiagonal matrix A
A = np.diag([1+2*lam]*(n-2),0) + np.diag([-1*lam]*(n-3),-1) + np.diag([-1*lam]*(n-3),1)

#define column vector B
#columns vertor B = (initial condition) + lambda*(next time step boundary condition)
#each time the value of j changes, the value of B are updated accordingly
#calculate TT
for j in range(1,m):
    B = TT[1:-1,j-1].copy() #assign to B calculated value, not just value of TT
    B[0] = B[0] + lam* TT[0,j]
    B[-1] = B[-1] + lam* TT[-1,j] #each time the value of j changes, the values of B are updated accordingly
    U = np.linalg.solve(A,B)
    TT[1:-1,j] = U
    
#calculate ET ,exclude initial and boundary condition
for j in range(1,m):
    for i in range(1,n-1):
        ET[i,j] = lam*ET[i-1,j-1]+(1-2*lam)*ET[i,j-1]+lam*ET[i+1,j-1]
    
############################################################################################################################    
    
#overlap TDMA method and Explicit method

#setting ploted time value
display_j = np.arange(m/nt_display,m,m/nt_display)
display_j = np.append(display_j,[0,m-1])
display_j = display_j.astype(int)
display_j = np.sort(display_j)

#setting ploted position value
display_i = np.arange(n/nd_display,n,n/nd_display)
display_i = np.append(display_i,[0,n-1])
display_i = display_i.astype(int)
display_i = np.sort(display_i)

#plot TDMA method for black dot
for i in display_i:
    for j in display_j:
        dot_TT = TT[i,j]
        plt.scatter(i*dx, dot_TT, s=3, marker='o', facecolor='black', zorder=2, label='TDMA Method' if i== 0 and j==0 else'')

#plot Explicit method for line
for j in display_j:
    color = plt.cm.rainbow(1-(j/m))
    rounded_time = round(j*dt,1)
    plt.plot(x, ET[:, j], color=color, label=f't={rounded_time}s',zorder=1)

#setting plot
plt.xlabel('Position [m]')
plt.ylabel('Temperature [K]')
plt.title ('Overlaping TDMA and Explicit Method')
plt.legend(loc ='upper right')
plt.show()


