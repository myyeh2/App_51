#  App51.py 

import numpy as np 
import matplotlib.pyplot as plt 

#t 
t = [      
        0.00000,          
        0.97000,          
        1.94000,          
        2.91000,          
        3.88000,         
        4.85000,         
        5.82000,         
        0.50681,         
        1.47681,          
        2.44681,          
        3.41681,          
        4.38681,         
        5.35681,         
        0.04363,          
        1.01363,          
        1.98363,          
        2.95363,          
        3.92363,                
] 
#y
y = [   
        6.00000,
        4.88204,
        4.67382,
        6.55952,
        8.92336,
       10.62240,
       12.13236,
        0.25346,
        5.29941,
        2.42056,
        7.42709,
       12.47838,
       12.28274,
        1.34090,
        1.74577,
        7.41427,
        9.50797,
       10.15999,
  ]
plt.figure(figsize = (8, 4)) 
plt.subplots_adjust(bottom = 0.2, left=0.2) 

plt.plot(t, y, 'r-', label = r'$y$', lw = 3) 
 

plt.xlabel(r'$Time(sec)$').set_fontsize(16) 
plt.ylabel(r'$Amplitude$').set_fontsize(16)  
plt.title(r'$Time*Amplitude$').set_fontsize(16) 

plt.grid(axis='both') 
plt.legend(loc='best') 

plt.show() 
