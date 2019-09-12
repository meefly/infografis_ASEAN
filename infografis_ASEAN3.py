import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Soal 2.4
# Connect to MySQL
dbku = mysql.connector.connect(
  host="localhost",
  user="shendy",
  passwd="password",
  database="world"
)
# Read DB
df = pd.read_sql('select country.Name, country.SurfaceArea from country where country.Region = "Southeast Asia" order by Name asc',con=dbku)
# print(df)

plt.figure('Figure 4: Persentase Luas Daratan ASEAN', figsize=(16, 9))

# Pie Chart
plt.pie(df.SurfaceArea, labels=df.Name, autopct='%.1f%%', textprops={'color':'black'})
plt.title('Persentase Luas Daratan ASEAN')
plt.show()
