import tkinter
import subprocess, sys
import pdfkit

def gen_pdf():
	"""Generate PDF file from a website"""
	url = ent_url.get()
	pdfkit.from_url(url, "last_page.pdf")
	opener = "open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, "last_page.pdf"])

window = tkinter.Tk()
window.title("PDF Generator")

form_entry = tkinter.Frame(master=window)
ent_url = tkinter.Entry(master=form_entry, width=50)
lbl_url = tkinter.Label(master=form_entry, text="Page URL:", padx=10)

lbl_url.grid(row=0, column=0, sticky="w")
ent_url.grid(row=0, column=1, sticky="w")

btn_gen_pdf = tkinter.Button(
	master=window,
	text="Generate PDF",
	command=gen_pdf
)

form_entry.grid(row=0, column=0, padx=10)
btn_gen_pdf.grid(row=0, column=1, pady=10, padx=10)

window.mainloop()