import pandas as pd 
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle
#To find diameter of the asteroid
"""Attributes to determine the diameter of an asteroid are
 absolute magnitude H and an assumed geometric albedo, 
 speed of the asteroid"""
df = pd.read_csv('nasa.csv')
drop_col = ['Neo Reference ID', 'Name','Est Dia in M(min)', 'Est Dia in M(max)',
       'Est Dia in Miles(min)', 'Est Dia in Miles(max)',
       'Est Dia in Feet(min)', 'Est Dia in Feet(max)', 'Close Approach Date',
       'Epoch Date Close Approach','Relative Velocity km per sec','Miles per hour',
       'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)',
       'Miss Dist.(kilometers)', 'Miss Dist.(miles)', 'Orbiting Body',
       'Orbit ID', 'Orbit Determination Date', 'Orbit Uncertainity',
       'Minimum Orbit Intersection', 'Jupiter Tisserand Invariant',
       'Epoch Osculation', 'Eccentricity', 'Semi Major Axis', 'Inclination',
       'Asc Node Longitude', 'Orbital Period', 'Perihelion Distance',
       'Perihelion Arg', 'Aphelion Dist', 'Perihelion Time', 'Mean Anomaly',
       'Mean Motion', 'Equinox', 'Hazardous']

df.drop(drop_col, axis = 1, inplace = True)

df['diameter'] = df.iloc[:, 1:3].sum(axis = 1)
df.drop(['Est Dia in KM(min)', 'Est Dia in KM(max)'], axis = 1, inplace = True)
x = df.drop('diameter', 1)
y = df['diameter']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
with open('asteroid_model.pkl', 'wb') as f:
  pickle.dump(model, f)

predict = model.predict(x_test)
predict1 = model.predict([[20.33, 23423]])
print(predict1)