# This is a sample for logistic optimization in python. I took this from the R
# version located in my CodeSamples folder as well as information here:
# https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html

import numpy as np
import pandas as pd
from plotnine import *
from scipy.optimize import minimize
# import matplotlib.pyplot as plt

data = pd.read_csv('../R/logitPracticeData.csv')
data.head()
data['label'] = data['label'].astype('category')
# %matplotlib inline
# figure
# Creating theme for APA in ggplot


# See for plot themes
# http://plotnine.readthedocs.io/en/stable/generated/plotnine.themes.theme.html

# Does full apa only thing that is not implemented is that transparant legend box
apatheme = theme(panel_grid_major=element_blank(),
                 panel_grid_minor=element_blank(),
                 panel_border=element_blank(),
                 panel_background=element_rect(fill="None"),
                 axis_line=element_line(),
                 text=element_text(family='sans'),
                 plot_title=element_text(hjust=0.5),
                 legend_key=element_rect(fill="None", colour="None", size=0.25),
                 legend_box_background=element_rect(fill="None", linetype="None"),
                 plot_background=element_rect(fill="None", colour='None'))

p = ggplot(data, aes(x='score-1', y='score-2', color='label')) + \
    geom_point() + apatheme

print(p)

data['label'] = data['label'].astype('int64')

# plt.plot(data['score-1'], data['score-2'],'o', 'color', data['label'])
# plt.show()

X = data.iloc[:, 0:-1].as_matrix()
X = np.c_[np.ones(100), X]
Y = data['label']


def sigmoid(z):
    '''
    Calculates the Sigmoid value based on the input parameters, with defaults
    for SVf = 1, SFl = 0, and gamma = 1

.. math::
    \sum_{i=1}^{\\infty} x_{i}

    '''
    # 1/(1 + np.exp(gamma*(SVf - SVl)))
    return 1 / (1 + np.exp(-z))


def logitCost(theta):
    '''
    Vectorized Cost function for logistic regression
    Obtained from here:
            http://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html
    '''
    m = Y.shape[0]
    g = sigmoid(np.dot(X, theta))
    j = (1 / m) * sum((-Y * np.log(g)) - ((1 - Y) * np.log(1 - g)))
    # cost = 1./len(y) *(-np.dot(np.log(h),(y))-np.dot(np.log(1-h),(1-y)))
    return j


x0 = np.zeros(X.shape[1])
res = minimize(logitCost, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True, 'maxiter': 10000})
print(res.x)
