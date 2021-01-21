import pandas as pd
import numpy as np
import json

pd.read_json("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/ProductCatalog_Jan_2021.json").to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/ProductCatalog_Jan_2021.csv")

df = pd.read_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/ProductCatalog_Jan_2021.csv', sep=',')
df = df[df.category =='newspaper']
df.to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/newspaper.csv")
df["isregional"] = ""
df["postalCodes"] = ""
df["country"] = ""
print(list(df))

for i in df.index:
    string = df["attributes"][i]
    index_left = string.find("countryRestrictions")
    string = string[index_left:]
    index_left = string.find("countryCode")
    countryCode = string[index_left+14:]
    index_right = countryCode.find("\"")
    countryCode = countryCode[:index_right]
    index_left = string.find("postCodes")
    postalCodeRestriction = string[index_left:]
    index_left = postalCodeRestriction.find("[")
    postalCodeRestriction = postalCodeRestriction[index_left+2:]
    index_right = postalCodeRestriction.find("]")
    postalCodeRestriction = postalCodeRestriction[:index_right-1]
    df["country"][i] = countryCode
    df["postalCodes"][i] = postalCodeRestriction
    postalCodeRestriction = postalCodeRestriction.strip()
    if(len(postalCodeRestriction) > 0):
        df["isregional"][i] = True
    else:
        df["isregional"][i] = False

df = df[df.isregional ==True]
df = df[df.country != "CH"]
df = df[df.country != "AT"]
df.to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/regional_newspaper.csv")