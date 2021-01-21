from avro.datafile import DataFileReader
from avro.io import DatumReader
from pathlib import Path
import os
import pandas as pd

fileDirProfiles = r"/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/Customer Profiles"
fileDirJourneys = r"/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/Customer Journeys"
fileExt = r".avro"
df = pd.DataFrame()
fileList = []
counter = 0

for root, dirs, files in os.walk(fileDirJourneys):  # root = Path, dirs = folders, files = files
    for file in Path(str(root)).iterdir():
        string = str(file)
        if string.endswith(".avro"):
            fileList.append(string)
fileList = sorted(fileList)
print(fileList)

for files in fileList:
    reader = DataFileReader(open(files, "rb"), DatumReader())
    for user in reader:
        df = df.append(user, ignore_index=True)
        counter = counter + 1
        print(counter)
reader.close()

df.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/test.csv')
df.to_json('/Users/davidritter/Documents/userwerk/CDP_Recommendation/test.json')