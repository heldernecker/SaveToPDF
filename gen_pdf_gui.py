import tkinter
import subprocess, sys
import pdfkit

def gen_pdf():
	"""Generate PDF file from a website"""
	url = ent_url.get()
	file_name = ent_file_name.get()
	pdfkit.from_url(url, file_name)
	opener = "open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, file_name])

window = tkinter.Tk()
window.title("PDF Generator")

# URL field
form_entry = tkinter.Frame(master=window)
lbl_url = tkinter.Label(master=form_entry, text="Page URL:", padx=10)
ent_url = tkinter.Entry(master=form_entry, width=45)

lbl_url.grid(row=0, column=0, sticky="w")
ent_url.grid(row=0, column=1, sticky="w")

# File name field
form_file_name = tkinter.Frame(master=window)
lbl_file_name = tkinter.Label(master=form_file_name, text="File Name:", padx=10)
ent_file_name = tkinter.Entry(master=form_file_name, width=30)

lbl_file_name.grid(row=0, column=0, sticky="w")
ent_file_name.grid(row=0, column=1, sticky="w")

btn_gen_pdf = tkinter.Button(
	master=form_file_name,
	text="Generate PDF",
	command=gen_pdf
)

btn_gen_pdf.grid(row=0, column=2, pady=10, padx=10, sticky="e")

form_entry.grid(row=0, column=0, padx=10)
form_file_name.grid(row=1, column=0, padx=10)


window.mainloop()