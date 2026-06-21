from tkinter import *
from tkinter import filedialog, messagebox
from pytubefix import YouTube
import os


# Download function
def download_video():

    url = url_entry.get()

    if url == "":
        messagebox.showerror("Error", "Please enter YouTube URL")
        return

    try:

        folder = filedialog.askdirectory()

        if folder:

            yt = YouTube(url)

            video = yt.streams.get_highest_resolution()

            video.download(folder)

            messagebox.showinfo(
                "Completed",
                "Video Downloaded Successfully"
            )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# Window
window = Tk()

window.title("YouTube Video Downloader")

window.geometry("500x300")

window.config(bg="#222222")


title = Label(
    window,
    text="YouTube Video Downloader",
    font=("Arial",18,"bold"),
    bg="#222222",
    fg="white"
)

title.pack(pady=20)


label = Label(
    window,
    text="Enter YouTube URL",
    bg="#222222",
    fg="white",
    font=("Arial",12)
)

label.pack()


url_entry = Entry(
    window,
    width=50
)

url_entry.pack(pady=10)


button = Button(
    window,
    text="Download Video",
    command=download_video,
    bg="green",
    fg="white",
    font=("Arial",12)
)

button.pack(pady=20)


window.mainloop()