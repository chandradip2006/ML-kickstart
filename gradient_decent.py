import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gradient_decent(x , y):
    m_curr=b_curr=0
    n=len(x)
    itr=10000
    learning=0.0831

    for i in range(itr):
        y_predicted=m_curr*x+b_curr
        cost=(1/n)*sum((y-y_predicted)**2)
        print(f"m:{m_curr} b:{b_curr} cost:{cost} itr:{i}")
        m_dec=(-1)*(2/n)*sum(x*(y-y_predicted))
        b_dec=(-1)*(2/n)*sum(y-y_predicted)

        m_curr=m_curr-learning*m_dec
        b_curr=b_curr-learning*b_dec


        


x=np.array([1 , 2 , 3 , 4 , 5])
y=np.array([5 , 7 , 9 , 11 , 13])

gradient_decent(x , y)