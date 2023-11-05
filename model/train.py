from os import PathLike
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(pathlib.Path('data/weatherHistory.csv'))

df = df.rename(columns={
    'Wind Speed (km/h)': 'WindSpeed',
    'Wind Bearing (degrees)':'WindBearing',
    'Visibility (km)':'Visibility',
    'Pressure (millibars)': 'Pressure'
})

df = df.drop(["Formatted Date","Summary","Precip Type","Loud Cover","Daily Summary","Apparent Temperature (C)"],axis=1)

y = df.pop('Temperature (C)')
X = df

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)
print ('Training model.. ')
clf = RandomForestRegressor(n_estimators =25,
                            max_depth=6,
                            random_state=0)
clf.fit(X_train, y_train)
print ('Saving model..')

dump(clf, pathlib.Path('model/weatherHistory-v1.joblib'))
