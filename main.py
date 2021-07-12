from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context  #helps to solve ssl certification error

#------------ BACK-END STARTS HERE ------------

#file path fuction
file_path=""
def openlocation():
    global file_path
    file_path=filedialog.askdirectory()
    if (len(file_path)>1):
        path_error.config(text=file_path,fg="green")
    else:
        path_error.config(text="Please Choose Valid Path",fg="red")

#download Video
def download():
    choice=select_choice.get()
    url=entry_url.get()
    if (len(url)>1):
        url_error.config(text="")
        video=YouTube(url)
        title.config(text="Title\n"+video.title,font=("josh",18,"bold"))
        thumbnail.config(text="Thumbnail URL\n"+video.thumbnail_url,font=("josh",18,"bold"))
        option=""
        if (choice==choices[0]):
            option=video.streams.filter(progressive=True).first()
        elif (choice == choices[1]):
            option = video.streams.filter(progressive=True,file_extension="mp4").last()
        elif (choice==choices[2]):
            option=video.streams.filter(only_audio=True).first()
        else:
            url_error.config(text="Paste A Link Again!!",fg="red")

        option.download(file_path)
        url_error.config(text="Download Completed!!",fg="green")
    else:
        url_error.config(text="Please Enter A Valid URL",fg="red")

#------------ BACK-END ENDS HERE ------------




#------------ FRONT-END STARTS HERE ------------

project=Tk() #assigning the project
project.title("YouTube Plus")  # name of the project
project.geometry("500x700") #size of gui
project.columnconfigure(0,weight=1) #index,weight. helps to set text in center

#main label
main_label=Label(project,text="Enter URL Of The Video Here ", font=("jost",25,"bold"),pady=30)
main_label.grid()

#entry box
entry_url=Entry(project,width=40,textvariable=StringVar)
entry_url.grid()

#error message
url_error=Label(project,text="",font=("josh",20))
url_error.grid()

#location message
location_label=Label(project,text="Save The File Here",width=30,font=("josh",25, "bold"),pady="40")
location_label.grid()

#save button
save_button=Button(project,text="Choose Path",fg="green",width=15,font=("josh",20),command=openlocation)
save_button.grid()

#path error
path_error=Label(project,text="Please Select A Valid Path",font=("josh",15))
path_error.grid()

#resolution
qualty=Label(project,text="Please Select The Quality",width=30,font=("josh",25,"bold"),pady="40")
qualty.grid()

#choicebox
choices=["720p","144p","Only Audio"]
select_choice =ttk.Combobox(project,values=choices,width=20,height=220,font=("josh",15))
select_choice.grid()

#download button
download_button=Button(project,text="Download",width=15,font=("josh",30,"bold"),pady=10,fg="green",command=download)
download_button.grid()

#additonal details
title=Label(project,text="",font=("josh",20),pady=10)
title.grid()

thumbnail=Label(project,text="",font=("josh",20))
thumbnail.grid()

#developer name
developer_name=Label(project,text="Developed by Shashank Naik",font=("josh",18),pady="55",)
developer_name.grid()




#------------ FRONT-END ENDS HERE ------------

project.mainloop() # helps to call the whole program