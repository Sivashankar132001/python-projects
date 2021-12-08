from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 


Foldre_Nmae = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="please choose folder",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)


        if(choice == choices[0])

root = Tk()
root.title("YTD Downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

# link label
ytdlabel = Label(root,text="Enter the url",font=("jost",15))
ytdlabel.grid()

#entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()


ytdError = Label(root,text="Error msg",fg="red",font=("jost",10))
ytdError.grid()


savelabel = Label(root,text="save the video file",font=("jost",15,"bold"))
savelabel.grid()

saveEntry = Button(root,width=10, bg="red",fg="white",text="choose Path")
saveEntry.grid()

locationError = Label(root,text="Error msg",fg="red",font=("jost",10))
locationError.grid()

ytdQuality = Label(root,text="select quality",font=("jost",15))
ytdQuality.grid()


choice = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choice)
ytdchoices.grid()


downloadbtn = Button(root, text="Download",width=10,bg="red",fg="white")
downloadbtn.grid()


developerlabel = Label(root,text="Dream Developers",font =("jost",15))
developerlabel.grid()


root.mainloop()
