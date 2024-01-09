import requests
from bs4 import BeautifulSoup


def get_bbc_headlines():
    url = "https://www.bbc.com/news"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

        if headlines:
            print("BBC News Headlines:")
            for index, headline in enumerate(headlines, start=1):
                print(f"{index}. {headline.text.strip()}")
        else:
            print("No headlines found on the BBC News website.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_bbc_headlines()