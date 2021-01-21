import pandas as pd

df = pd.read_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/bearbeitete_regionale_zeitungen.csv', sep=';')
df = df[df.isregional ==True]
df['number of PostalCodes'] = 0

for i in df.index:
    counter = 0
    string = df["postalCodes"][i]
    counter = string.count(",")
    df['number of PostalCodes'][i] = counter + 1

df.to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/regional_newspaper_blackList.csv")
blacklist = df
whitelist = pd.read_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/ProductCatalog_Jan_2021.csv")

whitelist['isInBlacklist'] = whitelist['hashedAbstractProductId'].isin(blacklist['hashedAbstractProductId'])
whitelist = whitelist[whitelist.isInBlacklist == False]
whitelist.to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/regional_newspaper_whitelist.csv")
whitelist = whitelist['hashedAbstractProductId'].unique()
print(whitelist)
pd.DataFrame(whitelist).to_csv("/Users/davidritter/Documents/userwerk/CDP_Recommendation/1. Meeting/whitelist.csv")