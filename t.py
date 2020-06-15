import pandas as pd
import numpy as np

head=["id","date_time","flag","option"]

temporal_dataset = pd.read_csv("temporal_activity.csv",header=None)
temporal_dataset.columns=head
temporal_dataset["date_time"]=pd.to_datetime(temporal_dataset["date_time"])

compressed_set = temporal_dataset.groupby(['id'])['flag'].apply(lambda x: "%s" % ''.join(x)).reset_index()

print(compressed_set)


temporal_dataset = pd.read_csv("noofdays.csv")

print(temporal_dataset)


final = pd.merge(compressed_set,temporal_dataset,on="id",how="outer")

print(final)