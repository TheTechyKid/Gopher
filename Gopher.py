import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImageViewer():
    def __init__(self, url):
        self.root = tk.Tk()
        self.root.title("Gopher")

        self.image_url = url
        self.down_size = 2

        self.response = requests.get(self.image_url)
        self.image_data = BytesIO(self.response.content)
        self.image_pil = Image.open(self.image_data)
        self.newSize = self.calculate_new_size(self.image_pil.size, self.down_size)

        # Resize Image
        self.image_resized = self.image_pil.resize(self.newSize, Image.Resampling.LANCZOS)

        # Display Image
        self.image_tk = ImageTk.PhotoImage(self.image_resized)
        self.oldsizelb = tk.Label(text=f"Old_Size: width {self.image_pil.size[0]}, height {self.image_pil.size[1]}")
        self.newsizelb = tk.Label(text=f"New_Size: width {self.newSize[0]}, height {self.newSize[1]}")
        self.image_label = tk.Label(self.root, image=self.image_tk)
        
        print(self.image_pil.size[0], self.image_pil.size[1])
        print(self.newSize[0], self.newSize[1])
        self.image_label.pack()
        self.oldsizelb.pack()
        self.newsizelb.pack()
        
        self.root.mainloop()

    def calculate_new_size(self, original_size, down):
        width, height = original_size
        if width >= 1000 or height >= 1000:
            return (round(width / down), round(height / down))
        elif width <= 300 or height <= 300:
            return (round(width + 50), round(height + 50))
        else:
            return (round(width / down), round(height / down))

if __name__ == "__main__":
    url = input("Enter: ").replace("https:////", " https://")
    mainApp = ImageViewer
    mainApp(url)