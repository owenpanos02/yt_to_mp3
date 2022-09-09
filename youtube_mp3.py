from pytube import YouTube
import os
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Youtube to MP3")
root.iconbitmap('icon.ico')



title_image = ImageTk.PhotoImage(Image.open("youtube_mp3_title_image.png"))

canvas1 = tk.Canvas(root, width=600, height= 800)
canvas1.pack()

title_image_label = tk.Label(root, image = title_image)
canvas1.create_window(300, 200, window= title_image_label)

entry1 = tk.Entry (root)
canvas1.create_window(300, 400, window=entry1)

def downloadVid():

    yt_url = str(entry1.get())
    yt = YouTube(yt_url)

    video = yt.streams.filter(only_audio=True).first()

    path = "Videos"

    out_file = video.download(output_path=path)

    base, ext = os.path.splitext(out_file)

    new_file = base + '.mp3'

    os.rename(out_file, new_file)

    print(f"\n{yt.title}\nhas downloaded succesfully...")

button = tk.Button(root, text='Download File', command=downloadVid)
canvas1.create_window(300, 445, window = button)
root.mainloop()