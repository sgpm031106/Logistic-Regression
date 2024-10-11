import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de resenias de "Straight Outta Compton"
url = 'https://www.rottentomatoes.com/m/straight_outta_compton/reviews'

# Realizar la peticion HTTP
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Intentar extraer reseñas utilizando un selector diferente
    review_table = soup.find('div', class_='review_table')

    # Guardar en una lista de las reseñas extraídas
    extracted_reviews = []
    reviews = review_table.find_all('p', class_='review-text')  #Inspeccionar la pagina de rotten tomatoes y verificar en que area especifica se encuentran las reseñas
    for review in reviews:
        review_text = review.text.strip()
        # Eliminar el texto específico que aparece por default al extraer y guardar las reseñas
        review_text = review_text.replace('[Full review in Spanish]', '')
        extracted_reviews.append(review_text)

    # Crear un DataFrame con las reseñas
    df = pd.DataFrame(extracted_reviews, columns=['review'])

    # Guardar las reseñas en un archivo CSV
    df.to_csv('straight_outta_compton_reviews.csv', index=False)

    print("Reseñas guardadas en 'straight_outta_compton_reviews.csv'.")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
