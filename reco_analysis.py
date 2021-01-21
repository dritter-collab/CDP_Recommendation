import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Einlesen der Recommendation Übersicht
df = pd.read_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/reco_overview.csv', sep=',')
print(list(df))

# Filtern nach Recommendation und tatsächlicher Bestellung
reco = df[df.event =='store']
reco_order = df[df.event =='order']

# Zähle Anzahl der Recommendation und Bestellungen
number_of_reco = reco.shape[0]
number_of_reco_order = reco_order.shape[0]

# Zähle Distinct die Anzahl der unterschiedlichen E-mails für die Recommmendation und die Bestellung
number_of_unique_reco = reco['hashedEmail'].unique().shape[0]
number_of_unique_reco_order = reco_order['hashedEmail'].unique().shape[0]

# Zähle das Häufigste Produkt in der Recommendation an 1. Stelle
reco1 = pd.DataFrame(reco, columns = ['p0'])
reco1 = reco1.rename(columns={'p0': 'Reco1'})
reco1 = reco1.value_counts().rename_axis('products_reco1').reset_index(name='counts')
print(reco1)

# Zähle das Häufigste Produkt in der Recommendation an 2. Stelle
reco2 = pd.DataFrame(reco, columns = ['p1'])
reco2 = reco2.rename(columns={'p1': 'Reco2'})
reco2 = reco2.value_counts().rename_axis('products_reco2').reset_index(name='counts')
print(reco2)

# Zähle das Häufigste Produkt in der Recommendation an 3. Stelle
reco3 = pd.DataFrame(reco, columns = ['p2'])
reco3 = reco3.rename(columns={'p2': 'Reco3'})
reco3 = reco3.value_counts().rename_axis('products_reco3').reset_index(name='counts')
print(reco3)

# Zähle das Häufigste Produkt in der Recommendation an 4. Stelle
reco4 = pd.DataFrame(reco, columns = ['p3'])
reco4 = reco4.rename(columns={'p3': 'Reco4'})
reco4 = reco4.value_counts().rename_axis('products_reco4').reset_index(name='counts')
print(reco4)

# Zähle das Häufigste Produkt in der Recommendation an 5. Stelle
reco5 = pd.DataFrame(reco, columns = ['p4'])
reco5 = reco5.rename(columns={'p4': 'Reco5'})
reco5 = reco5.value_counts().rename_axis('products_reco5').reset_index(name='counts')
print(reco5)

# Zähle das Häufigste Produkt in der Recommendation an 6. Stelle
reco6 = pd.DataFrame(reco, columns = ['p5'])
reco6 = reco6.rename(columns={'p5': 'Reco6'})
reco6 = reco6.value_counts().rename_axis('products_reco6').reset_index(name='counts')
print(reco6)

# Zähle das Häufigste Produkt in der Recommendation an 7. Stelle
reco7 = pd.DataFrame(reco, columns = ['p6'])
reco7 = reco7.rename(columns={'p6': 'Reco7'})
reco7 = reco7.value_counts().rename_axis('products_reco7').reset_index(name='counts')
print(reco7)

# Zähle das Häufigste Produkt in der Recommendation an 8. Stelle
reco8 = pd.DataFrame(reco, columns = ['p7'])
reco8 = reco8.rename(columns={'p7': 'Reco8'})
reco8 = reco8.value_counts().rename_axis('products_reco8').reset_index(name='counts')
print(reco8)

# Zähle das Häufigste Produkt in der Recommendation an 9. Stelle
reco9 = pd.DataFrame(reco, columns = ['p8'])
reco9 = reco9.rename(columns={'p8': 'Reco9'})
reco9 = reco9.value_counts().rename_axis('products_reco9').reset_index(name='counts')
print(reco9)

# Zähle das Häufigste Produkt in der Recommendation an 10. Stelle
reco10 = pd.DataFrame(reco, columns = ['p9'])
reco10 = reco10.rename(columns={'p9': 'Reco10'})
reco10 = reco10.value_counts().rename_axis('products_reco10').reset_index(name='counts')
print(reco10)

# Zähle das Häufigste Produkt in der Recommendation an 11. Stelle
reco11 = pd.DataFrame(reco, columns = ['p10'])
reco11 = reco11.rename(columns={'p10': 'Reco11'})
reco11 = reco11.value_counts().rename_axis('products_reco11').reset_index(name='counts')
print(reco11)

# Zähle das Häufigste Produkt in der Recommendation an 12. Stelle
reco12 = pd.DataFrame(reco, columns = ['p11'])
reco12 = reco12.rename(columns={'p11': 'Reco12'})
reco12 = reco12.value_counts().rename_axis('products_reco12').reset_index(name='counts')
print(reco12)

# Zähle das Häufigste Produkt in der Recommendation an 13. Stelle
reco13 = pd.DataFrame(reco, columns = ['p12'])
reco13 = reco13.rename(columns={'p12': 'Reco13'})
reco13 = reco13.value_counts().rename_axis('products_reco13').reset_index(name='counts')
print(reco13)

# Zähle das Häufigste Produkt in der Recommendation an 14. Stelle
reco14 = pd.DataFrame(reco, columns = ['p13'])
reco14 = reco14.rename(columns={'p13': 'Reco14'})
reco14 = reco14.value_counts().rename_axis('products_reco14').reset_index(name='counts')
print(reco14)


# Zähle das Häufigste Produkt in der Recommendation an 15. Stelle
reco15 = pd.DataFrame(reco, columns = ['p14'])
reco15 = reco15.rename(columns={'p14': 'Reco15'})
reco15 = reco15.value_counts().rename_axis('products_reco15').reset_index(name='counts')
print(reco15)

# Erstellen eines DataFrames mit allen absoluten Häufigkeiten der Produkte
products = pd.concat([reco1['products_reco1'], reco2['products_reco2'], reco3['products_reco3'], reco4['products_reco4'], reco5['products_reco5'], reco6['products_reco6'], reco7['products_reco7'], reco8['products_reco8'], reco9['products_reco9'], reco10['products_reco10'], reco11['products_reco11'], reco12['products_reco12'], reco13['products_reco13'], reco14['products_reco14'], reco15['products_reco15']], axis=0)
freq = pd.DataFrame({'products':list(products)})
freq = freq.drop_duplicates()
freq = freq.reset_index()
freq = freq.drop(['index'], axis=1)
freq = freq.join(reco1, lsuffix='products', rsuffix='products_reco1')
freq = freq.drop(['products_reco1'], axis=1)
freq = freq.rename(columns={'counts': 'Reco1'})
freq = freq.set_index('products').join(reco2.set_index('products_reco2'))
freq = freq.rename(columns={'counts': 'Reco2'})
freq = freq.join(reco3.set_index('products_reco3'))
freq = freq.rename(columns={'counts': 'Reco3'})
freq = freq.join(reco4.set_index('products_reco4'))
freq = freq.rename(columns={'counts': 'Reco4'})
freq = freq.join(reco5.set_index('products_reco5'))
freq = freq.rename(columns={'counts': 'Reco5'})
freq = freq.join(reco6.set_index('products_reco6'))
freq = freq.rename(columns={'counts': 'Reco6'})
freq = freq.join(reco7.set_index('products_reco7'))
freq = freq.rename(columns={'counts': 'Reco7'})
freq = freq.join(reco8.set_index('products_reco8'))
freq = freq.rename(columns={'counts': 'Reco8'})
freq = freq.join(reco9.set_index('products_reco9'))
freq = freq.rename(columns={'counts': 'Reco9'})
freq = freq.join(reco10.set_index('products_reco10'))
freq = freq.rename(columns={'counts': 'Reco10'})
freq = freq.join(reco11.set_index('products_reco11'))
freq = freq.rename(columns={'counts': 'Reco11'})
freq = freq.join(reco12.set_index('products_reco12'))
freq = freq.rename(columns={'counts': 'Reco12'})
freq = freq.join(reco13.set_index('products_reco13'))
freq = freq.rename(columns={'counts': 'Reco13'})
freq = freq.join(reco14.set_index('products_reco14'))
freq = freq.rename(columns={'counts': 'Reco14'})
freq = freq.join(reco15.set_index('products_reco15'))
freq = freq.rename(columns={'counts': 'Reco15'})
freq = freq.fillna(0)
freq = freq.astype(int)
freq['top'] = freq['Reco1']
freq['top2'] = freq['Reco1'] + freq['Reco2']
freq['top3'] = freq['Reco1'] + freq['Reco2'] + freq['Reco3']
freq['top4'] = freq['Reco1'] + freq['Reco2'] + freq['Reco3'] + freq['Reco4']
freq['top5'] = freq['Reco1'] + freq['Reco2'] + freq['Reco3'] + freq['Reco4'] + freq['Reco5']
freq['top10'] = freq['Reco1'] + freq['Reco2'] + freq['Reco3'] + freq['Reco4'] + freq['Reco5'] + freq['Reco6'] + freq['Reco7'] + freq['Reco8'] + freq['Reco9'] + freq['Reco10']
freq['total'] = freq['Reco1'] + freq['Reco2'] + freq['Reco3'] + freq['Reco4'] + freq['Reco5'] + freq['Reco6'] + freq['Reco7'] + freq['Reco8'] + freq['Reco9'] + freq['Reco10'] + freq['Reco11'] + freq['Reco12'] + freq['Reco13'] + freq['Reco14'] + freq['Reco15']
freq = freq.sort_values(by=['total'], ascending=False)
print(freq)

# Produkte die Immer Empfohlen werden
always_reco = freq.dropna()
print(always_reco)

print(freq)
print(len(reco))

rel_freq = (freq/len(reco)) * 100
print(rel_freq)

freq.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/reco_freq.csv')
rel_freq.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/reco_rel_freq.csv')



# Zähle das Häufigsten bestellten Produkt in der Recommendation an 1. Stelle
ordere_product = pd.DataFrame(reco_order, columns = ['orderedProduct'])
ordere_product = ordere_product.value_counts().rename_axis('products_reco1').reset_index(name='counts')

ordere_product= ordere_product.reset_index()
ordere_product = ordere_product.drop(['index'], axis=1)
ordere_product= ordere_product.rename(columns={'products_reco1': 'orderedProduct'})
print(ordere_product)
print(len(reco_order))

rel_freq_ordere_product = ordere_product
rel_freq_ordere_product['counts'] = (rel_freq_ordere_product['counts']/len(reco_order)) * 100
print(rel_freq_ordere_product)

ordere_product.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/ordere_product.csv')
rel_freq_ordere_product.to_csv('/Users/davidritter/Documents/userwerk/CDP_Recommendation/rel_freq_ordere_product.csv')