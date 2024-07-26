import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DataFrame Indexing
country=pd.DataFrame(np.arange(16).reshape(4,4), index=["London","Paris","Berlin","Istanbul"],
    columns=["one","two","three","four"])
print(country)
print(country["two"])
print(country[["one","two"]])
print(country[:3])
print(country[country["four"]>5])
country[country<5]=0
print(country)

#Selecting using iloc & loc
print(country.iloc[1])
print(country.iloc[1,[1,2,3]])
print(country.iloc[[1,3],[1,2,3]])
print(country.loc["Paris",["one","two"]])
print(country.loc[:"Paris","four"])
continents=pd.Series(np.arange(5),
                   index=["a","b","c",
                          "d","e"])
print(continents)
print(continents[-1])

#Usefull methods
s=pd.Series([1,2,3,4], index=["a","b","c","d"])
print(s)
s["a"]
s2=s.reindex(["b","d","a","c","e"])
print(s2)
s3=pd.Series(["blue","yellow","purple"],
             index=[0,2,4])
print(s3)
s3.reindex(range(6),method="ffill")
st=pd.DataFrame(np.arange(9).reshape(3,3),
                index=["a","c","d"],
                columns=["Tim","Tom","Kate"])
print(st)
st2=st.reindex(["d","c","b","a"])
print(st2)
names=["Kate","Tim","Tom"]
st.reindex(columns=names)
st.loc[["c","d","a"]]
s=pd.Series(np.arange(5.),
            index=["a","b","c","d","e"])
print(s)
new_s=s.drop("b")
print(new_s)
s.drop(["c","d"])
data=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=["Kate","Tim",
                         "Tom","Alex"],
                  columns=list("ABCD"))
print(data)
data.drop(["Kate","Tim"])
data.drop("A",axis=1)
data.drop("Kate",axis=0)
print(data)
data.mean(axis="index")
data.mean(axis="columns")
