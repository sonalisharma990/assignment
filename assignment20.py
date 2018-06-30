#Q1
import pandas as pd
data={'Name':['sonali','lovisha','jasleen'],'Age':[19,20,21],'mail_id':['sonas45@gmail.com','lovig6@gmail.com','jassk87@gmail.com'],'phone_no':[3458907256,6789064369,9964457899]}
df=pd.DataFrame(data,index=[1,2,3])
print(df)



#Q2
import pandas as pd
d=pd.read_csv("test8.csv")
df=pd.DataFrame(d)
#1.
print(df.head(5))

#2.
print(df.head(10))

#3.
print(df.axes)
print(df.T)

#4.
print(df.tail(5))


#5.
print(df['MinTemp'].head)
print(df['MinTemp'].dtypes)
print(df['MinTemp'].shape)

