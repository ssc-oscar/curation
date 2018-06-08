from pandas import DataFrame
df = DataFrame.from_csv("results_data.csv", sep=",")

print(df.values)