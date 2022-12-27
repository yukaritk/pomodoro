from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(200, 200)
window.config(padx=10, pady=50)

my_label = Label(text="is equal to")
my_label.grid(row=1, column=0)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="Km")
km.grid(row=1, column=2)

def button_clicked():
    num_miles = int(input.get())
    num_km = int(num_miles * 1.61)
    result = Label(text=num_km)
    result.grid(row=1, column=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


input = Entry(width=10)
input.grid(row=0, column=1)



window.mainloop()