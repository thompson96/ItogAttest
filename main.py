from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import os
from dotenv import load_dotenv

url = 'https://api.coingecko.com/api/v3/simple/price'

load_dotenv()
api_key = os.getenv('COINGECKO_API_KEY')

cryptocurrencies = {
    'bitcoin': 'Биткоин',
    'ethereum': 'Эфириум',
    'tether': 'Тезер',
    'binancecoin': 'BNB',
    'ripple': 'XRP',
    'solana': 'Солана',
    'tron': 'Трон',
    'figure-heloc': 'Figure Heloc',
    'staked-ether': 'Lido Staked Ether',
}


def update_crypto_label(event):
    code = crypto_combobox.get()
    name = cryptocurrencies[code]
    crypto_label.config(text=name)


def get_crypto_rate():
    crypto_id = crypto_combobox.get()
    params = {
        'ids': crypto_id,
        'vs_currencies': 'usd'
    }
    headers = {
        'x-cg-demo-api-key': api_key
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    rate = data[crypto_id]['usd']
    print(rate)


root = Tk()
root.title('Курс криптовалют к USD')
root.geometry('360x180')

Label(root, text='Выберите криптовалюту').pack(pady=10)
crypto_combobox = ttk.Combobox(
    root,
    values=list(cryptocurrencies.keys()),
    state='readonly'
)
crypto_combobox.current(0)
crypto_combobox.pack(pady=5)
crypto_combobox.bind('<<ComboboxSelected>>', update_crypto_label)

crypto_label = ttk.Label(root, text=cryptocurrencies['bitcoin'])
crypto_label.pack()

Button(
    root,
    text='Получить курс к USD',
    command=get_crypto_rate
).pack(pady=10)

root.mainloop()