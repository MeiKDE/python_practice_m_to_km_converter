from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
window.minsize(width=350, height=250)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=1)


kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=2, row=1)


def miles_to_km():
    miles = float(miles_input.get())
    miles_input.config(text=miles)
    # convert m to km
    m_to_km = round(miles * 1.60934, 2)
    # display on label
    kilometer_result_label.config(text=m_to_km)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
