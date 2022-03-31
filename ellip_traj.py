import numpy as np
import matplotlib.pyplot as plt

def h(w,t,t_mid):
    delta_t = t - t_mid
    return 2.0*np.pi/(1.0 + np.exp(-delta_t/w))


def t9(dt,dn,t9_0,b_a,t,t_mid,w):
    return t9_0 - dt*np.cos(h(w,t,t_mid))/2.0 - b_a*dn*np.sin(h(w,t,t_mid))/2.0

def nn(dt,dn,nn_0,b_a,t,t_mid,w):
    return nn_0 + dn*np.cos(h(w,t,t_mid))/2.0 + b_a*dt*np.sin(h(w,t,t_mid))/2.0

'''
def t9(t9_0,a,b,t,t_mid,w,phi):
    return t9_0 - a*np.cos(h(w,t,t_mid))*np.cos(phi) - b*np.sin(h(w,t,t_mid))*np.sin(phi)

def nn(nn_0,a,b,t,t_mid,w,phi):
    return nn_0 - a*np.cos(h(w,t,t_mid))*np.sin(phi) + b*np.sin(h(w,t,t_mid))*np.cos(phi)
'''
#specify min and max for t_9, n_n, and eccentricity (e) of ellipse
#since we need a semi-ellipse on a log-lin scale, the choice for
#n_n should be the exponents to the base 10

t9_max = 0.210
t9_min = 0.1
t9_int = 0.135

nn_max_log = 6
nn_min_log = 3
nn_int_log = 2.8

phi = np.pi/4.0
#w smoothens or sharpens the transition for h(t)
w = 1e+11

#####################################################
#code parameters calculated from specified parameters

#central coordinates
t9_0 = (t9_int + t9_min)/2.0
nn_0 = (nn_int_log + nn_min_log)/2.0

#mirror image coordinates of the max w.r.t ellipse center
t9_mir = t9_int + t9_min - t9_max
nn_mir = nn_int_log + nn_min_log - nn_max_log

#difference to calculate trig due to inclination
dn = nn_max_log - nn_mir
dt = t9_max - t9_mir

#Ellipse properties
a = np.sqrt(np.power(t9_max - t9_0,2) + np.power(nn_max_log - nn_0,2))
b = 0.5*np.sqrt(np.power(nn_int_log - nn_min_log,2) + np.power(t9_int - t9_min ,2))
b_a = b/a

time = np.linspace(0,3.1536e+12,10000)
t_mid = (3.1536e+12)/2.0

#####################################################
#calculate arrays for ellipse########################

t_9 = t9(dt,dn,t9_0,b_a,time,t_mid,w)
n_n = 10**nn(dt,dn,nn_0,b_a,time,t_mid,w)

'''
t_9 = t9(t9_0,a,b,time,t_mid,w,phi)
n_n = nn(nn_0,a,b,time,t_mid,w,phi)
'''
####################################################
#plotting###########################################


plt.figure(figsize =[19.20,10.80])
plt.rc('text', usetex=True)
plt.rc('font', family = 'serif')
plt.rcParams['font.size']=24

plt.plot(t_9,n_n)
t9 = np.array([t9_mir,t9_0,t9_max,t9_min,t9_int])
n = np.array([nn_mir,nn_0,nn_max_log,nn_min_log,nn_int_log])
plt.scatter(t9,10**n,color = 'black')
plt.yscale('log')
'''
plt.figure(figsize = [19.20,10.80])
plt.rc('text',usetex = True)
plt.rc('font', family = 'serif')
plt.rcParams['font.size'] = 24

plt.plot(time,h(w,time,t_mid))


plt.figure()

plt.yscale('log')
'''
plt.show()
