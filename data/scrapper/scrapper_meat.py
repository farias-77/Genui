import requests
from bs4 import BeautifulSoup

def fetch_and_format_meat_data(url):
    response = requests.get(url)

    product_list = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        products = soup.find_all('a', class_='info-product')
        
        for product in products:
            name = product.find('div', class_='product-name').text.strip().lower().replace(" ", "_")
            price = product.find('div', class_='product-price').text.strip()
            product_list.append((name, price))
    else:
        print("Falha na requisição HTTP. Status code:", response.status_code)
    
    return product_list


if __name__ == "__main__":
    url = "https://www.extracarne.com.br/carnes-bovinas"

    products_data = fetch_and_format_meat_data(url)

    for product in products_data:
        print(f"Produto: {product[0]}, Preço: {product[1]}")
