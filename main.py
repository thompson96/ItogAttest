from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


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

root.mainloop()