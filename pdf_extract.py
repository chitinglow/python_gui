import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.geometry("300x450")
root.resizable(0,0)
root.title("Text Extractor From PDF")
root.iconbitmap("robot icon.ico")

# Add the App Logo
App_logo = Image.open("pdf logo.png")
logo = ImageTk.PhotoImage(App_logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.pack(padx=10, pady=10)

# Creating Text Label
text_label = tk.Label(root,text="Text Extractor From PDF", font=("courier New", 15, "bold"), fg="green")
text_label.pack(padx=10,pady=10)


root.mainloop()