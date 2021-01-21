from avro.datafile import DataFileReader
from avro.io import DatumReader
import os
import pandas as pd

fileDirProfiles = r"/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/Customer Profiles"
fileDirJourneys = r"/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/Customer Journeys"
fileExt = ".avro"
df = pd.DataFrame()

result = [_ for _ in os.listdir(fileDirProfiles) if _.endswith(fileExt)]
result = sorted(result)
print(result)
counter = 0

for file in result:
    folder = fileDirProfiles + "/" + file
    reader = DataFileReader(open(folder, "rb"), DatumReader())
    for user in reader:
        print(counter)
        df = df.append(user, ignore_index=True)
        counter = counter + 1
reader.close()

df.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/test.csv')
df.to_json('/Users/davidritter/Documents/userwerk/CDP_Recommendation/test.json')