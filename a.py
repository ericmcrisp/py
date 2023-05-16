# lists of natrual numbers
import numpy as np

a_range = np.linspace(1, 1000, 1)
b_range = np.linspace(1, 999, 1)
c_range = np.linspace(1, 998, 1)

for k in range(len(c_range)):
    for j in range(len(b_range)):
        for i in range(len(a_range)):
            a_temp = a_range[i]
            b_temp = b_range[j]
            c_temp = c_range[k]
            if a_temp > b_temp and b_temp > c_temp:
                asq = pow(a_temp, 2)
                bsq = pow(b_temp, 2)
                csq = pow(c_temp, 2)
                if sum(asq, bsq) == csq:
                    a = a_temp
                    b = b_temp
                    c = c_temp
                    print(a,b,c)
