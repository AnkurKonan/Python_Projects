import pandas as pd
print(pd.__version__)

Name=pd.Series([1,"Ankur",3.5,"Hey"])
print(Name)
print(Name[0])
print(Name.values)

Name2=pd.Series([1,"Ankur",3.5,"Hey"],index=["a","b","c","d"])
print(Name2)
print(Name2["b"])
print(Name2.index)

score={"Jane":90, "Tony":80,"Elon":85,"Rahul":75,"Rohit":95}
names=pd.Series(score)
print(names)

print(names["Rohit"])
print(names[names>=85])
names["Rahul"]=60
print(names)
names[names<=80]=83
print(names)
print("Can" in names)
print(names/10)
print(names**2)
print(names.isnull())

#Series
soliders=pd.read_csv("Data.csv")
print(soliders.head())
print(soliders.dtypes)
print(soliders.Genre.describe())
print(soliders.Genre.value_counts())
print(soliders.Genre.value_counts(normalize=True))
print(type(soliders.Genre.value_counts()))
print(soliders.Genre.value_counts().head())
print(soliders.Genre.unique())
print(soliders.Genre.nunique())
print(pd.crosstab(soliders.Genre, soliders.Year))
print(soliders.Global_Sales.describe())
print(soliders.Global_Sales.mean())
print(soliders.Global_Sales.value_counts())
# print(soliders.Year.plot(kind="hist"))
print(soliders.Genre.value_counts())
# print(soliders.Genre.value_counts().plot(kind="bar"))

#Data frames
data={"name":["Tony","Rahul","Rohit","Ankur","Arzoo","Aamya","Gurnoor"],
      "score":[90,80,85,75,95,60,65],
      "sport":["Wrestling","Football","Skiing","Swimming","Tennis",
               "Karete","Surfing"],
      "sex":["M","M","M","M","F","F","F"]}
df=pd.DataFrame(data)
print(df)
df=pd.DataFrame(data,columns=["name","sport","sex","score"])
print(df)
print(df.head())
print(df.tail())
print(df.tail(3))
print(df.head(2))
df=pd.DataFrame(data, columns=["name", "sport", "gender", "score", "age"])
print(df)
df=pd.DataFrame(data, columns=["name", "sport", "gender", "score", "age"],
                index=["one","two","three","four","five","six","seven"])
print(df)
print(df["sport"])
my_columns=["name","sport"]
print(df[my_columns])
print(df.sport)
df.loc[["one"]]
df.loc[["one","two"]]
df["age"]=18
df=pd.DataFrame(data,columns=["name", "sport", "gender", "score", "age"],
                index=["one","two","three","four","five","six","seven"])
values=[18,19,20,18,17,17,18]
df["age"]=values
df
df["pass"]=df.score>=70
df
del df["pass"]
df
scores={"Math":{"A":85,"B":90,"C":95}, "Physics":{"A":90,"B":80,"C":75}}
scores_df=pd.DataFrame(scores)
scores_df
scores_df.T
scores_df.index.name="name"
scores_df.columns.name="lesson"
scores_df
scores_df.values
scores_index=scores_df.index
scores_index[1]="Jack"
scores_index


