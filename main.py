import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def upload_image():
    global img_path, img_name
    img_path = filedialog.askopenfilename()
    img_name = img_path.split('/')[-1]
    tk.Label(window, text=img_name).grid(row=4, column=1)


def ask_directory():
    directory = filedialog.askdirectory()


def add_watermark():
    img = Image.open(img_path)
    font_size = int(font_entry.get())
    img_to_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial', font_size)
    img_to_draw.text((0, 0), text_entry.get(), font=font)
    img.show()
    img.save(f'C:/Users/hp/Downloads/watermarker/{img_name}')
    tk.Label(window, text='Image Saved').grid(row=6, column=1)

# C:\Users\hp\Downloads
window = tk.Tk()
window.title('Watermarker')
window.geometry('500x300+800+200')


text_label = tk.Label(window, text='Watermark: ')
text_label.grid(row=1, column=0)
text_entry = tk.Entry(window, width=50)
text_entry.insert(0, 'watermark')
text_entry.grid(row=1, column=1)

fontsize_label = tk.Label(window, text='Font Size(px): ')
fontsize_label.grid(row=2, column=0)
font_entry = tk.Entry(window, width=50)
font_entry.insert(0, '65')
font_entry.grid(row=2, column=1)

destination_label = tk.Label(window, text='Destination: ')
destination_label.grid(row=3, column=0)
destination_entry = tk.Entry(window, width=50)
destination_entry.insert(0, 'C:/Users/hp/Downloads/watermarker/')
destination_entry.grid(row=3, column=1)

upload_img_btn = tk.Button(window, text='Upload Image', command=upload_image, padx=21)
upload_img_btn.grid(row=4, column=1)


done_btn = tk.Button(text='Add Watermark', command=add_watermark, padx=17)
done_btn.grid(row=5, column=1)

window.mainloop()
