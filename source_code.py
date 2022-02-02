# imports libraries needed later on in the program for condtructing dataframes and making graphs and plots
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# imports a file containing the data 
df1 = pd.read_csv('Incidence_count.csv', encoding = "ISO-8859-1")

#This drops columns that are empty, as the are not of any use
df1 = df1.dropna(axis=1,how='any')

# This drops another column that we don't need
del df1['Gaul_Code']

# This removes the index column and is replaced by the next one
df1.set_index('Name', inplace=True)

#  pivots the table so the rows become columns and columns become rows
df = df1.transpose()

# this resets the index and stores the values in a column called 'year'
df.reset_index()
df['year'] = df.index

# converts year to numerical
df['year'] = pd.to_numeric(df['year'])

# The actual graph is drawn. we can do any country by replacing 'Africa' in its name
sns.lmplot(x='year',y='Africa',data=df,fit_reg=True)
plt.show()

# define variables to go on the axes later
feature_cols = ['Africa']
x = df[feature_cols]
y = df[['year']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
linreg = LinearRegression()
linreg.fit(x_train, y_train)
zip(feature_cols, linreg.coef_)
y_pred = linreg.predict(x_test)
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
plt.show()
x = df['year']
y = df['Nigeria']

# Define the slope and intercepts, which will be used to draw the regression line 
slope, intercept = np.polyfit(x, y, 1)
# design the regression line, with a 4-degree polynomial as compared to the 1-degree polynomial I used before
z = np.polyfit(x, y, 4)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

# make the plot with the regression line
plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
feature_cols = ['Nigeria']
x = df[feature_cols]
y = df[['year']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
linreg = LinearRegression()
linreg.fit(x_train, y_train)
zip(feature_cols, linreg.coef_)
y_pred = linreg.predict(x_test)
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
plt.show()
