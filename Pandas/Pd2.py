#Data Frames
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
print(df.loc[["one"]])
print(df.loc[["one","two"]])
df["age"]=18
df=pd.DataFrame(data,columns=["name", "sport", "gender", "score", "age"], index=["one","two","three","four","five","six","seven"])
values=[18,19,20,18,17,17,18]
df["age"]=values
print(df)
df["pass"]=df.score>=70
print(df)
del df["pass"]
print(df)
scores={"Math":{"A":85,"B":90,"C":95}, "Physics":{"A":90,"B":80,"C":75}}
scores_df=pd.DataFrame(scores)
print(scores_df)
print(scores_df.T)
scores_df.index.name="name"
scores_df.columns.name="lesson"
print(scores_df)
print(scores_df.values)
scores_index=scores_df.index
# scores_index[1]="Jack"
print(scores_index)

# Indexing & Selection & Filtering
letters=pd.Series(np.arange(5), index=["a","b","c","d","e"])
print(letters)
print(letters["c"])
print(letters[2])
print(letters[0:3])
print(letters[["a","c"]])
print(letters[[0,2]])
print(letters[letters<2])
print(letters["a":"c"])
letters["b":"c"]=5
print(letters)
