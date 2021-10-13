from tkinter import *
import tkinter.messagebox
import qrcode
import json
import time
import os

# generate qr code


def generate():
    text = entry.get("1.0", END)
    # replace spaces and newline
    if checkedsp.get():
        text = text.replace(" ", "")
    if checkednl.get():
        text = text.replace("\n", "")
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "qrcode_%s.png" % timestr
    img.save(filename)
    answer = tkinter.messagebox.askyesno(
        title="qr code is saved!", message="qr-code is saved under:\n%s\%s\nopen file?" % (os.getcwd(), filename))
    if answer:
        os.system(filename)

# validate if the json string spits out any errors


def validate():
    jsonData = entry.get("1.0", END)
    try:
        json.loads(jsonData)
    except ValueError as err:
        tkinter.messagebox.showerror(
            title="error", message="this is not valid json \n %s \n %s" % (err, jsonData))
        return False
    answer = tkinter.messagebox.askyesno(
        title="success", message="JSON seems to be valid.\n Create QR Code?")
    if answer:
        generate()
        return True
    else:
        return False


# build gui
win = Tk()
win.title("generate QR Code from text")
win.resizable(0, 0)

checkednl = BooleanVar(value=True)
checkedsp = BooleanVar(value=True)

# build widgets
entry = Text(win, width=50, height=10, wrap=WORD)
button = Button(win, text="Validate JSON", width=20)
button2 = Button(win, text="Generate QR", width=20)
checkboxnl = Checkbutton(win, text="remove newline",
                         variable=checkednl, offvalue=False, onvalue=True)
checkboxsp = Checkbutton(win, text="remove spaces",
                         variable=checkedsp, offvalue=False, onvalue=True)
l2 = Label(win, text="Converted text:")

# layout
entry.grid(row=2, column=0, columnspan=2, pady=5, padx=5)
button.grid(row=3, column=1, columnspan=2, pady=5, padx=5)
button2.grid(row=4, column=1, columnspan=2, pady=5, padx=5)
checkboxnl.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky="w")
checkboxsp.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky="w")

# buttons
button.configure(command=validate)
button2.configure(command=generate)

# exec
win.mainloop()
