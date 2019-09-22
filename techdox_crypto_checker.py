from tkinter import *
import requests
from tkinter import scrolledtext
import requests
from tkinter.ttk import *

#Functions -------
def coincost():
    r = requests.get(f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={combo.get()}&tsyms={combo1.get()}&api_key={apitxt.get()}')
    text = (r.text)
    return text

def clicked():
    lbl.configure(text=coincost())
    lbl2.configure(text="Above is the Price for " + combo.get())


#Title Bar 
window = Tk()
window.title("Techdox Crypto Price Checker")

#Label for coin price
lbl = Label(window, text="")
lbl.grid(column=0, row=2)


# Window Sizing
window.geometry('350x200')
 
#Coin Combo Box
combo = Combobox(window)
combo['values']= ("XRP","BTC","LTC", "XLM" )
combo.current(0) #set the selected item
combo.grid(column=0, row=0)

#Curreny Combo Box
combo1 = Combobox(window)
combo1['values']= ("USD","NZD")
combo1.current(0) #set the selected item
combo1.grid(column=2, row=0)

#Main Button
btn = Button(window, text="Click Me To See Price", command=clicked) 
btn.grid(column=1, row=2)

#Label shows 
lbl2 = Label(window, text="Current Selected")
lbl2.grid(column=1, row=3)

apitxt = Entry(window,width=10)
apitxt.grid(column=1, row=1)


window.mainloop()
