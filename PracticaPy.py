import pandas as pd

# 1. Cargar el archivo 'netflix_title.csv'
netflix_data = pd.read_csv('C:\\Users\\18498\\Desktop\\Homeworks\\netflix_titles.csv')
""""
# 2. Visualizar los primeros 10 registros del conjunto de datos
print("Primeros 10 registros del conjunto de datos:")
print(netflix_data.head(10))
# 3. Visualizar los últimos 15 registros del conjunto de datos

print("\nÚltimos 15 registros del conjunto de datos:")
print(netflix_data.tail(15))


# 4. Generar los estadísticos básicos
print("\nEstadísticos básicos del conjunto de datos:")
print(netflix_data.describe())



# 5. Completar todos los datos vacíos (na) con ceros (0)
netflix_data.fillna(0, inplace=True)

"""

# 6. Generar un gráfico de tipo barras que compare películas vs series desde el 2010 hasta el 2021
import matplotlib.pyplot as plt

# Filtrar los datos por películas y series
movies = netflix_data[(netflix_data['type'] == 'Movie') & (netflix_data['release_year'] >= 2010) & (netflix_data['release_year'] <= 2021)]
series = netflix_data[(netflix_data['type'] == 'TV Show') & (netflix_data['release_year'] >= 2010) & (netflix_data['release_year'] <= 2021)]

# Contar el número de películas y series por año
movies_by_year = movies['release_year'].value_counts().sort_index()
series_by_year = series['release_year'].value_counts().sort_index()

# Generar el gráfico de barras
plt.figure(figsize=(10, 6))
bar_width = 0.35  # Ancho de las barras

plt.bar(movies_by_year.index - bar_width/2, movies_by_year.values, bar_width, color='blue', label='Películas')
plt.bar(series_by_year.index + bar_width/2, series_by_year.values, bar_width, color='red', label='Series')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.title('Comparación de Películas vs Series (2010-2021)')
plt.legend()
plt.show()

