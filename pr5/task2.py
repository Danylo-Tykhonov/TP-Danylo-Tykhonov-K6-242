import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
    print("Не вдалося отримати курс валют")
    return None

def convert():
    supported = ["EUR", "USD", "PLN"]
    currency = input("Введіть валюту (EUR, USD, PLN): ").upper()

    if currency not in supported:
        print("Ця валюта не підтримується")
        return

    try:
        amount = float(input(f"Введіть кількість {currency}: "))
    except ValueError:
        print("Невірне число")
        return

    rate = get_exchange_rate(currency)
    if rate:
        uah = amount * rate
        print(f"{amount} {currency} = {uah:.2f} UAH за курсом {rate:.2f}")

if __name__ == "__main__":
    convert()
