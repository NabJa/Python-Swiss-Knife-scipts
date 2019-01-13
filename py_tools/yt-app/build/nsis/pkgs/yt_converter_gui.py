from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import re
import os
from pytube import YouTube


def downloadYouTube(url, out):
    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(out):
        os.makedirs(out)
    yt.download(out)


def check_yt_link(url):
    if re.search("http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", url):
        return True
    else:
        return False


def print_link():
    if check_yt_link(E1.get()):
        link = E1.get()

        path = filedialog.askdirectory(title='Please select a directory')

        try:
            downloadYouTube(link, path)
            messagebox.showinfo("Success!", "Successfully downloaded to " + path)
            top.destroy()
        except pytube.exceptions.RegexMatchError:
            messagebox.showwarning("Invalid link", "YouTube link not found!")
    else:
        messagebox.showwarning("WARNING", "Give me a valid YouTube link")


top = Tk(className=" YouTube converter")

L1 = Label(top, text="YouTube Link:")
L1.grid(row=0, column=0)

E1 = Entry(top, width=75)
E1.grid(row=0, column=1)

B1 = Button(top, text="Download", command=print_link)
B1.grid(row=0, column=2)

top.mainloop()
