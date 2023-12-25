from pytube import YouTube
import tkinter as tk
import customtkinter
from tkinter import filedialog

def download_video():
  try:
    ytlink = link.get()
    ytobject = YouTube(ytlink, on_progress_callback=on_prog)
    streams = ytobject.streams.filter(progressive=True, file_extension="mp4")
    highest_res_stream = streams.get_highest_resolution()
    title.configure(text=ytobject.title, text_color="white")

    save_path = filedialog.askdirectory()
    if save_path:
      finishLabel.configure(text="")
      finishLabel.configure(text=f"Selected Folder: {save_path}", text_color="white")
      highest_res_stream.download(output_path=save_path)
      finishLabel.configure(text="Video Downloaded Successfully!", text_color="white") 
      
  except Exception:
    title.configure(text="YT Video Downloader")
    finishLabel.configure(text="Invalid URL", text_color="red")

def on_prog(stream, chunk, bytes_rem):
  total_size = stream.filesize
  bytes_downloaded = total_size-bytes_rem
  percentage_of_completion = bytes_downloaded / total_size * 100
  per = str(int(percentage_of_completion))
  progNum.configure(text=per + "%")
  progNum.update()
  progBar.set(float(percentage_of_completion / 100))
  
  
# system settings
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("Anthracite.json")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YT Downloader")

# adding ui elements
title = customtkinter.CTkLabel(app, text="YT Video Downloader", font=("Montserrat", 15))
title.pack(padx=10, pady=10)

# link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, placeholder_text='Enter URL', width=350, height=40, textvariable=url_var)
link.pack()

# finish label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# prog bar
progNum = customtkinter.CTkLabel(app, text="0%")
progNum.pack()

progBar = customtkinter.CTkProgressBar(app, width=400)
progBar.set(0)
progBar.pack(padx=10, pady=10)

root = tk.Tk()
root.withdraw()

# download button
download = customtkinter.CTkButton(app, text="Download", command= download_video, corner_radius=5, fg_color="#1f538d")
download.pack(padx=0, pady=10)

# run app
app.mainloop() 