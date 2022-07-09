#!/usr/bin/env python
import numpy as np
import pandas as pd
from scipy.stats import pearsonr


def rcorr(df):
    coeffmat = np.zeros((df.shape[1], df.shape[1]))
    pvalmat = np.zeros((df.shape[1], df.shape[1]))

    for i in range(df.shape[1]):
        for j in range(df.shape[1]):
            corrtest = pearsonr(df[df.columns[i]], df[df.columns[j]])
            coeffmat[i, j] = corrtest[0]
            pvalmat[i, j] = corrtest[1]

    dfcoeff = pd.DataFrame(coeffmat, columns=df.columns, index=df.columns)
    dfpvals = pd.DataFrame(pvalmat, columns=df.columns, index=df.columns)

    return(dfcoeff, dfpvals)
