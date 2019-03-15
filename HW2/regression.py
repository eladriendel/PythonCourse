import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import math

def getRegressionResults(xList, yList):
    # Least Squares Method
    x = np.array(xList)
    y = np.array(yList)
    n = np.size(x)
    xBar = np.mean(x)
    yBar = np.mean(y)
    SSxy = np.sum(y*x) - n*yBar*xBar
    SSxx = np.sum(x*x) - n*xBar*xBar
    beta = SSxy/SSxx
    alpha = yBar - beta*xBar
    yEstimate = alpha + beta*x
    stdErrorSquared = np.sum(np.square(yEstimate - y)) / ((n-2)*np.sum(np.square(x - xBar)))
    standardError = math.sqrt(stdErrorSquared)
    lowerBound = beta - 1.96*standardError
    upperBound = beta + 1.96*standardError
    return (alpha, beta, standardError, lowerBound, upperBound)

def plotRegressionGraph(xList, yList, alpha, beta):
    x = np.array(xList)
    y = np.array(yList)
    pyplot.scatter(x, y, color = "b", marker = "o", s = 30)
    yEstimate = alpha + beta*x
    pyplot.plot(x, yEstimate, color = "r")
    pyplot.xlabel('GDP Per Capita (Current US$)')
    pyplot.ylabel('Urban population (% of total)')
    pyplot.show()
