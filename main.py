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

root.mainloop()