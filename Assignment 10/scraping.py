import requests
from bs4 import BeautifulSoup

url = input("Enter product URL: ")
target_price = float(input("Enter your target price: "))

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h1")
        price_tag = soup.find("p", class_="price_color")

        if title_tag and price_tag:
            title = title_tag.text.strip()
            price_text = price_tag.text.strip()

            # Remove currency symbol safely
            price_clean = ""
            for ch in price_text:
                if ch.isdigit() or ch == ".":
                    price_clean += ch

            price = float(price_clean)

            print("\nProduct Title:", title)
            print("Current Price:", price)

            if price < target_price:
                print("Price is below your target price!")
            elif price == target_price:
                print("Price is equal to your target price.")
            else:
                print("Price is above your target price.")

        else:
            print("Could not find title or price on page.")

    else:
        print("Could not access website.")

except Exception as e:
    print("An error occurred:", e)