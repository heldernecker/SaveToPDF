import tkinter
import subprocess, sys
import pdfkit

def gen_pdf():
	"""Generate PDF file from a website"""
	url = ent_url.get()
	file_name = ent_file_name.get()
	if not file_name.endswith(".pdf"):
		file_name = file_name + ".pdf"
	pdfkit.from_url(url, file_name)
	opener = "open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, file_name])
	clear_labels()

def get_clipboard_data():
	"""Get data from clipboard to insert in the URL field"""
	p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
	retcode = p.wait()
	data = p.stdout.read()
	return data

def clear_labels():
	ent_url.delete(0, 'end')
	ent_file_name.delete(0, 'end')

window = tkinter.Tk()
window.title("PDF Generator")

# URL field
form_entry = tkinter.Frame(master=window)
lbl_url = tkinter.Label(master=form_entry, text="Page URL:", width=10)
ent_url = tkinter.Entry(master=form_entry, width=45)
ent_url.insert(0, get_clipboard_data())

lbl_url.grid(row=0, column=0, sticky="w")
ent_url.grid(row=0, column=1, sticky="w")

# File name field
form_file_name = tkinter.Frame(master=window)
lbl_file_name = tkinter.Label(master=form_file_name, text="File Name:", width=10)
ent_file_name = tkinter.Entry(master=form_file_name, width=30)

lbl_file_name.grid(row=0, column=0, sticky="w")
ent_file_name.grid(row=0, column=1, sticky="w")

btn_gen_pdf = tkinter.Button(
	master=form_file_name,
	text="Generate PDF",
	command=gen_pdf
)

btn_gen_pdf.grid(row=0, column=2, sticky="w", padx=(10, 0))
btn_gen_pdf.config(width=10)

# Set URL field on first row. Set file name field on second row
form_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")
form_file_name.grid(row=1, column=0, padx=10, pady=(0, 10), stick="w")


window.mainloop()