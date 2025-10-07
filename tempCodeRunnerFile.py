
df = pd.DataFrame.from_records(dataframe)
joblib.dump(df,"embeddings.joblib")
