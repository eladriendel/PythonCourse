import wbdata
import datetime
import pandas as pd

# SP.URB.TOTL.IN.ZS	            Urban population as percentage of total population
# NY.GDP.PCAP.CD                GDP per capita in USD

def getData():
    data_date = datetime.datetime(2010, 1, 1)
    x = wbdata.get_data("NY.GDP.PCAP.CD", data_date = data_date, pandas = True)
    y = wbdata.get_data("SP.URB.TOTL.IN.ZS", data_date = data_date, pandas = True)
    data = pd.concat([x, y], axis = 1)
    data = data.dropna(axis=0, how='any')
    data.columns = ["gdp", "urbanPop"]
    x = data["gdp"].tolist()
    y = data["urbanPop"].tolist()
    return (x, y)

import regression
import getData
import numpy as np

(xList, yList) = getData.getData()

# Scale GDP data to achieve better results
xArray = np.array(xList)
xMin = np.amin(xArray)
xMax = np.amax(xArray)
xScaled = (xArray - xMin) / (xMax - xMin)
x = xScaled.tolist()

# Convert percent values to decimals
yArray = np.array(yList)
yNormalized = yArray / 100
y = yNormalized.tolist()

(alpha, beta, standardError, lowerBound, upperBound) = regression.getRegressionResults(x, y)
print("With given format of Y = alpha + beta*X")
print("Alpha value is: " + str(alpha))
print("Beta value is: " + str(beta))
print("Standard error is: " + str(standardError))
print("95% Confidence interval for beta: " + str(lowerBound) + " - " + str(upperBound))
regression.plotRegressionGraph(x, y, alpha, beta)

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
