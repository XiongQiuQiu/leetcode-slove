import numpy as np
import matplotlib as plt
fur_x = []
fur_y = []
for i in range(1,300):
    f = i/100.0
    ex = round(1/f,2)
    lo = 100
    range_l = int(lo*ex)
    print range_l
    t_l = [i/100.0 for i in range(10000)]
    print len(t_l)
    gx = [np.cos(t) for t in t_l]
    intensity=[np.cos(10*t)+1.1 for t in t_l]
    # circle = [np.e**(2*np.pi*a*t*f) for t in t_l]
    # c = [np.complex(np.cos(2*np.pi*t*f),np.sin(2*np.pi*t*f)).imag for t in t_l]
    c = [-2*np.pi*t*f for t in t_l]
    l = [intensity[i] for i in range(10000)]
    angle = [i/(2*np.pi)*360 for i in c]
    x_l = [li*np.cos(ci) for ci,li in zip(c,l)]
    y_l = [li*np.sin(ci) for ci,li in zip(c,l)]
    fur_x.append(np.mean(x_l))
    fur_y.append(np.mean(y_l))
f_l = [i/100.0 for i in range(1,300)]
right = [x for x in fur_x]
plt.subplot()
plt.plot(f_l, right)
plt.show()