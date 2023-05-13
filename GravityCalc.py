import csv
import pandas as pd
df = pd.read_csv("data.csv")
rows = []
with open("data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_name = planet_data[0]
  planet_mass = planet_data[2]
  planet_mass = float(planet_mass) * 1.989e+30
  planet_radius = planet_data[3]
  planet_radius = float(planet_radius)* 6.957e+8


        
planet_gravity = [] 
for index, name in enumerate(planet_name): 
         gravity = (float(planet_mass[index])*5.972e+24) / (float(planet_radius[index])*float(planet_radius[index])*6371000*6371000) * 6.674e-11
         planet_gravity.append(gravity) 

df['Gravity'] = planet_gravity
import plotly.express as px
fig = px.bar(x = planet_name, y = planet_mass)
fig.show()
fig = px.scatter(x=planet_radius, y=planet_mass, size=planet_gravity, hover_data=[planet_name]) 
fig.show()