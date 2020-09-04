import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv('parkinsons.data')

#print(df.head())
#print(df.info())
#print(df.describe())
print(df['status'].value_counts())

X = df.drop(['name','status'], axis = 1)
Y = df['status']
s = MinMaxScaler((-1,1))
cols = X.columns
cols = list(cols)
X = s.fit_transform(X)
X = pd.DataFrame(X)
i = list(X.columns)
name = dict(zip(i,cols))
X = X.rename(columns=name)

print(X.shape)
print(Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.15, random_state = 7)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


model = XGBClassifier()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print(accuracy_score(Y_test, Y_pred)*100)
print(confusion_matrix(Y_test,Y_pred))


