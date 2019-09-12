import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Soal 2.3
# Connect to MySqL DB
dbku = mysql.connector.connect(
  host="localhost",
  user="shendy",
  passwd="password",
  database="world"
)

# Read DB
df = pd.read_sql('select country.Name, country.GNP from country where country.Region = "Southeast Asia" order by Name asc', con = dbku)
# print(df)
plt.style.use('seaborn')

# Customs Colors
warna = ['lightblue', 'orange', 'green', 'red', 'purple', 'saddlebrown', 'pink', 'grey', 'olive', 'cyan', 'blue']
plt.figure('Figure 3: Pendapatan Bruton Nasional ASEAN', figsize=(16, 9))

# Bar Chart
plt.bar(df.Name, df.GNP, color=warna)
plt.title('Pendapatan Bruton Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product(US$)')
plt.xticks(rotation = 45)

for x, y in enumerate(df.GNP):
    plt.text(x-.3, y, str(y))
plt.show()
