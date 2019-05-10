import pandas as pd

tt = pd.read_csv('immSurvey.csv')

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

from sklearn.feature_extraction.text import CountVectorizer

# Word Frequency as Extracted Feature (Same as in-class)
vec = CountVectorizer()
X = vec.fit_transform(sample)

# Down weighting frequent words; TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer()
X = vec.fit_transform(sample)

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas, random_state=1)

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

# Compute posterior predictive mean and covariance
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

# Test correlation between test and mus
import numpy as np
print(np.corrcoef(ytest, mu_s))

# Include bigrams
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

X = bigram_vectorizer.fit_transform(sample)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas, random_state=1)

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

print(np.corrcoef(ytest, mu_s))
#Correlation was 0.68 and When bigrams are used, correlation became 0.61
