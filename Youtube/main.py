from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('700x300')
root.resizable(0, 0)
root.title("Youtube Downloader")

Label(root, text='Copie o link do video do Youtube',
      font='arial 15 bold').pack()

# colocar o link
link = StringVar()

Label(root, text='Cole o link aqui:', font='arial 15 bold').place(x=270, y=60)
Entry(root, width=80, textvariable=link).place(x=32, y=90)

# function para baixar video


def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=270, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='white',
       padx=2, command=Downloader).place(x=280, y=150)

root.mainloop()