from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
import numpy as np
import sys

# Load the training data into lists
f = open("train_data.txt")
f1=open("train_label.txt")
data =  np.loadtxt(fname = f, delimiter = ',')
data1 = np.loadtxt(fname=f1,delimiter=',')
X = data[:,0:]  # select columns 1 through end
y = data1[0:]

# Load the test data into list
f3=open("test_data.txt")
test = np.loadtxt(fname = f3, delimiter = ',')
T = test[0:]

# Split the data for cross validation
X_train, X_test, y_train, y_test=cross_validation.train_test_split(X,y,test_size=0.25,random_state=0)

# Build the model
clf = LogisticRegression(penalty="l2", C=10, solver="lbfgs", fit_intercept=1, class_weight="balanced", dual=0, max_iter=500).fit(X,y)

# Print the accuracy of the model
print 'Accuracy: ', clf.score(X_test,y_test)*100

# Print the predicted  labels of the test data into a file
sys.stdout=open("test_label_LR.txt", "w")

# Predict the labels of the test data
a=clf.predict(T)
for elem in a:
    print int(elem)