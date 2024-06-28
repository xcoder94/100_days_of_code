from tkinter import Tk, Button, Label, Canvas, filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter.simpledialog import askstring


class ImageViewerApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Image Viewer")
        self.window.geometry("500x500")

        self.open_button = Button(self.window, text="Open Image", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=20, pady=20)

        self.image_label = Label(self.window)
        self.image_label.grid(row=0, column=1, padx=20, pady=20)

        self.selected_file_path = None
        self.watermark_text = None

    def open_file(self):
        self.selected_file_path = filedialog.askopenfilename(
            filetypes=[('Image files', '*.jpg, *.png'), ('All files', '*.*')]
        )
        if self.selected_file_path:
            self.display_image(self.selected_file_path)

    def display_image(self, file_path):
        original_image = Image.open(file_path)
        resized_img = original_image.resize((200, 200), Image.LANCZOS)
        tk_resized_img = ImageTk.PhotoImage(resized_img)

        # Display the image in the label
        self.image_label.config(image=tk_resized_img)
        self.image_label.image = tk_resized_img  # Keep a reference to the image
        if file_path:
            ask_watermark = askstring('Watermark text', 'Type text')
            self.watermark_text = ask_watermark
            self.add_watermark(self.watermark_text, file_path)

    def add_watermark(self, text, file_path):
        im = Image.open(file_path)
        width, height = im.size
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('arial.ttf', 18)
        # Calculate text size
        bbox = draw.textbbox((0, 0), text, font=font)
        textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font, fill='#000')
        im.show()

        # Save watermarked image
        im.save('watermarked.png')


# Main program
if __name__ == "__main__":
    root = Tk()
    app = ImageViewerApp(root)
    root.mainloop()
