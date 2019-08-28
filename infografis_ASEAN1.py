import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Soal 2.2
# Connect to MySQL
dbku = mysql.connector.connect(
  host="localhost",
  user="shendy",
  passwd="2991Iluj92",
  database="world"
)
# Read DB
df = pd.read_sql('select country.Name,country.Population from country where country.Region="Southeast Asia" order by Name asc',con=dbku)
# print(df)

plt.figure('Figure 2: Persentase Penduduk ASEAN ', figsize=(16, 9))

# Pie Chart
plt.pie(df.Population, labels=df.Name, autopct='%.1f%%', textprops={'color':'black'})
plt.title('Persentase Penduduk ASEAN')
plt.show()