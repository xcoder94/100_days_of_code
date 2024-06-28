from tkinter import *
from tkinter import filedialog
# import tkinter.messagebox as msgbox
from PIL import Image, ImageTk

# Window settings
window = Tk()
window.title('Watermark GUI layout')
window.geometry('900x600')
window.config(padx=5, pady=5, bg='skyblue')
window.resizable(True, True)


# Canvas settings for showing image everywhere
def show_canvas(path):
    original_image = Image.open(path)
    resized_img = original_image.resize((200, 200))
    # Convert resized image to a format Tkinter can use
    tk_resized_img = ImageTk.PhotoImage(resized_img)
    return tk_resized_img


tk_image = show_canvas('watermark.png')
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=tk_image)
canvas.grid(row=0, column=0)


# Upload file
def file_path():
    selected_file_path = filedialog.askopenfilename(title='Select a photo', filetypes=[('Image files', '*.jpg, *.png'), ('All files', '*.*')])


main_label = Label(text='Welcome to auto watermarker app.\nplease choose file')
main_label.grid(row=0, column=1, columnspan=1, padx=15)
import_button = Button(text='choose file', command=file_path)
import_button.grid(row=1, column=1, columnspan=1, padx=15,)

window.mainloop()
