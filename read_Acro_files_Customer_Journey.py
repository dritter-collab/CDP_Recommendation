from avro.datafile import DataFileReader
from avro.io import DatumReader
from pathlib import Path
import os
import pandas as pd
import json
import avro.schema
import copy

fileDirJourneys = r"/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/Customer Journeys"
fileExt = r".avro"
df = pd.DataFrame()
fileList = []
counter = 0

# Auslesen aller Avro-Daten in diesem Ordner
for root, dirs, files in os.walk(fileDirJourneys):  # root = Path, dirs = folders, files = files
    for file in Path(str(root)).iterdir():
        string = str(file)
        if string.endswith(".avro"):
            fileList.append(string)

# Liste sortieren
fileList = sorted(fileList)

# Durch jedes File gehen und diese von Avro in ein Textfile schreiben
for files in fileList:
    with open(files, 'rb') as f:
        targetfile = "/Users/davidritter/Documents/userwerk/CDP_Recommendation/Avro-Files/transformed Avro-Files/Customer Journey/Journey_" + str(counter)
        if os.path.exists(targetfile) == False:
            reader = DataFileReader(f, DatumReader())
            metadata = copy.deepcopy(reader.meta)
            schema_from_file = json.loads(metadata['avro.schema'])
            users = [user for user in reader]
            with open(targetfile, "w") as write_file:
                users = str(users)
                json.dump(users, write_file)
                print(counter)
            reader.close()
        counter = counter + 1