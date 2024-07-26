import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Arithmatic Operations
s1=pd.Series(np.arange(4),
             index=["a","c","d","e"])
s2=pd.Series(np.arange(5),
             index=["a","c","e","f","g"])
print(s1)
print(s2)
print(s1+s2)
st1=pd.DataFrame(
    np.arange(6).reshape(2,3),
    columns=list("ABC"),
    index=["Tim","Tom"])
st2=pd.DataFrame(
    np.arange(9).reshape(3,3),
    columns=list("ACD"),
    index=["Tim","Kate","Tom"])
print(st1)
print(st2)
print(st1+st2)
st1.add(st2,fill_value=0)
print(1/st1)
print(st1*3)
print(st1.mul(3))
print(st2)
s=st2.iloc[1]
print(s)
print(st2-s)
s2=st2["A"]
print(s2)
st2.sub(s2,axis="index")
st=pd.DataFrame(np.random.randn(4,3), columns=list("ABC"), index=["Kim","Susan","Tim","Tom"])
print(st)
print(np.abs(st))
f=lambda x:x.max()-x.min()
print(st.apply(f))
print(st.apply(f,axis=1))
def f(x):
    return x**2
print(st.apply(f))

#Statistics
st=pd.DataFrame([[2.4,np.nan],[6.3,-5.4], [np.nan,np.nan],[0.75,-1.3]], index=["a","b","c","d"],
    columns=["one","two"])
print(st)
print(st.sum())
print(st.sum(axis=1))
print(st.mean(axis=1))
print(st.mean(axis=1,skipna=False))
print(st.idxmax())
print(st.idxmin())
print(st.cumsum())
print(st.describe())

s=pd.Series(["b","b","b","b","c",
             "c","a","a","a"])
print(s)
print(s.unique())
print(s.value_counts())
x=s.isin(["b","c"])
print(x)
print(s[x])

#Data visulaization:
# plt.style.use("fivethirtyeight")
# data=pd.Series(np.random.randn(1000).cumsum())
# data.plot()
# plt.show()

# st1 = pd.DataFrame(np.random.randn(100, 4),columns=list('ABCD'))
# st1 = st1.cumsum()
# st1.plot()
# plt.show()

# st2=pd.DataFrame(np.random.rand(7,3), columns=list("ABC"))
# st2.plot.bar()
# plt.show()

# st2=pd.DataFrame(np.random.rand(7,3), columns=list("ABC"))
# st2.plot.bar(stacked=True)
# plt.show()

# st2=pd.DataFrame(np.random.rand(7,3), columns=list("ABC"))
# st2.plot.barh(stacked=True)
# plt.show()

#Reading & writing data
st2=pd.read_table("Student.txt", sep=",")
print(st2)
st2=pd.read_table("Student.txt", sep=",")
print(st2)
st=pd.read_table("Student.txt",sep=",",header=None)
print(st)
st=pd.read_table("Student.txt", sep=",", header=None, names=["Name","Wieght","Gender"])
print(st)
st=pd.read_table("Student.txt", sep=",", header=None, names=["Name","Wieght","Gender"], index_col="Name")
print(st)
st2=pd.read_table("Student2.txt", sep=",")
print(st2)
st2=pd.read_table("Student2.txt", sep=",", index_col=["Name","Wieght"])
print(st2)
st3=pd.read_table("Student3.txt", sep=",",  skiprows=[0,2])
print(st3)
st3=pd.read_table("Student3.txt", sep=",", skiprows=[0,2],usecols=[0,1])
print(st3)
st3=pd.read_table("Student3.txt", sep=",", skiprows=[0,2],usecols=[0,1], nrows=3)
print(st3)
st=pd.read_csv("Student3.txt",sep="\t")
print(st)
