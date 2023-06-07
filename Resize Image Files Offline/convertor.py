import  tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import Button
from PIL import Image
import os
from tkinter import ttk
import webbrowser



class convertor(tk.Tk):
    
 def browse(self):
      self.entry5.delete(0,1000)
      self.file_name=filedialog.askopenfilename(title="Select Photo",initialdir=f"{self.home_directory}",filetypes = (('PNG files', '*.png'),('JPG files', '*.jpg'),('ICO files', '*.ico'),
                                                                                                                      ('Webp files', '*.webp'),('GIF files', '*.gif')),)
      self.entry5.insert(0,self.file_name)
      
             

     
 def convert_file(self):
    # convert files with pixel #
  try:
    if  self.entry2.get()!="" and self.entry1.get()!="":
     if self.entry5.get()=="":
         messagebox.showerror("Convert Manager","Browse Photo File...")
     elif self.entry6.get()=="":
         messagebox.showerror("Convert Manager","Enter File Name...")
     elif self.compobox.get()=="PNG"  or self.compobox.get()=="Webp" or self.compobox.get()=="GIF":
         img=Image.open(self.file_name)
         img = img.resize((int(self.entry1.get()),int(self.entry2.get())))
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
     elif self.compobox.get()=="jpg":
         img=Image.open(self.file_name)
         img=img.convert('RGB')
         img = img.resize((int(self.entry1.get()),int(self.entry2.get())))
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
     elif self.compobox.get()=="ICO":
         image = Image.open(self.file_name)
         icon_sizes = [(int(self.entry1.get()),int(self.entry2.get()))]
         fileoutpath = f'{self.home_directory}\\Desktop\\{self.entry6.get()}.ico'
         image.save(fileoutpath,format="ICO",sizes=icon_sizes, quality=90)
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
          # convert files with pixel #
     
          ##                        ##
         
          # convert files with percenteage #
    elif  self.entry3.get()!="" and self.entry4.get()!="":
        Width=int(self.entry3.get())
        height=int(self.entry4.get())
        max_r=19
        calc1=(int(float(Width)) / int(max_r)) * 100
        calc2=(int(float(height)) / int(max_r)) * 100
        if self.entry5.get()=="":
         messagebox.showerror("Convert Manager","Browse Photo File...")
        elif self.entry6.get()=="":
         messagebox.showerror("Convert Manager","Enter File Name...")
        elif self.compobox.get()=="PNG"  or self.compobox.get()=="Webp" or self.compobox.get()=="GIF":
         img=Image.open(self.file_name)
         img = img.resize((int(calc1),int(calc2)))
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
        elif self.compobox.get()=="jpg":
         img=Image.open(self.file_name)
         img=img.convert('RGB')
         img = img.resize((int(calc1),int(calc2)))
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
        elif self.compobox.get()=="ICO":
         image = Image.open(self.file_name)
         icon_sizes = [(int(calc1),int(calc2))]
         fileoutpath = f'{self.home_directory}\\Desktop\\{self.entry6.get()}.ico'
         image.save(fileoutpath,format="ICO",sizes=icon_sizes, quality=90)
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
             # convert files with percenteage # 
        
             ###                              ###
        
             # where you want to convert image without chnange diminsions pixels # 
    elif  self.entry2.get()=="" and self.entry1.get()=="":
     if self.entry5.get()=="":
         messagebox.showerror("Convert Manager","Browse Photo File...")
     elif self.entry6.get()=="":
         messagebox.showerror("Convert Manager","Enter File Name...")
     elif self.compobox.get()=="PNG"  or self.compobox.get()=="Webp" or self.compobox.get()=="GIF":
         img=Image.open(self.entry5.get())
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
     elif self.compobox.get()=="jpg":
         img=Image.open(self.entry5.get())
         img=img.convert('RGB')
         img.save(f"{self.home_directory}\\Desktop\\{self.entry6.get()}.{self.compobox.get()}")
         messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
         self.entry5.delete(0,1000)
         self.entry6.delete(0,1000)
     elif self.compobox.get()=="ICO":
         if self.entry1.get()=="" and self.entry2.get()=="":
          image = Image.open(self.entry5.get())
          fileoutpath = f'{self.home_directory}\\Desktop\\{self.entry6.get()}.ico'
          image.save(fileoutpath,format="ICO",sizes=[(256,256)], quality=100)
          messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
          self.entry5.delete(0,1000)
          self.entry6.delete(0,1000)
         else:
          image = Image.open(self.file_name)
          icon_sizes = [(int(self.entry1.get()),int(self.entry2.get()))]
          fileoutpath = f'{self.home_directory}\\Desktop\\{self.entry6.get()}.ico'
          image.save(fileoutpath,format="ICO",sizes=icon_sizes,quality=90)
          messagebox.showinfo("Successfully Converted","File Has Been Dowloaded On Your Desktop....")
          self.entry5.delete(0,1000)
          self.entry6.delete(0,1000)
                                                          
  except:
      messagebox.showerror("Image Converter","Errors:\n1)Enter Valid Numbers\n2)Enter Valid File Location")
 #contact with me functions #  
 def git_hub(self):
     webbrowser.open("https://github.com/KILLER-RAMADAN")
 def gmail(self):
     webbrowser.open("https://mail.proton.me/u/0/inbox")
 def linkinen(self):
     webbrowser.open("https://www.linkedin.com/in/ahmed-ramadan-9b5a32221/")
       
 # contact with me functions # 
 
 
 
 # get informations #
 def get_pix_info(self):
     messagebox.showinfo("Image Converter","You can resize your image\nby entering a specific resolution in pixels by what you want to downscale your image")
 def get_per_info(self):
     messagebox.showinfo("Image Converter","You can resize your image\nby entering a specific percentage by what you want to downscale your image")
 def get_format(self):
     messagebox.showinfo("Image Converter","Select your target format")
 # get informations #
 
 def __init__(self):
    
        
    super().__init__()
     
    self.home_directory = os.path.expanduser( '~' )
    self.geometry("700x500+450+200")
    self.title("Image Converter")
    
     
    self.attributes("-topmost",True)
     
    self.resizable(0,0)
    
    self.iconbitmap("images//convert.ico")
    
    self.info=tk.PhotoImage(file="images//info.png")
    
    self.setting=tk.PhotoImage(file="images//setting.png")
    
    self.file=tk.PhotoImage(file="images//file.png")
    
    self.git=tk.PhotoImage(file="images//github.png")
    
    self.lenkid=tk.PhotoImage(file="images//linkedin.png")
    
    self.gmai=tk.PhotoImage(file="images//gmail.png")
    
    self.label1=tk.Label(text="Resize image by Pixel:",font=("arial,20,bold"))
    self.label1.place(x=5,y=5)
    
    self.label2=tk.Label(text="Width:",font=("arial,20,bold"))
    self.label2.place(x=5,y=40)
    
    self.label3=tk.Label(text="Height:",font=("arial,20,bold"))
    self.label3.place(x=200,y=40)
    
    self.entry1=tk.Entry(text="",width=10,font=("arial",15,"bold"),relief="solid")
    self.entry1.place(x=5,y=70)
    
    self.label1=tk.Label(text="Px",width=0,font=("arial,20,bold"),relief="solid")
    self.label1.place(x=120,y=70)
    
    
    
    self.entry2=tk.Entry(text="",width=10,font=("arial",15,"bold"),relief="solid")
    self.entry2.place(x=200,y=70)
    
    self.label2=tk.Label(text="Px",width=0,font=("arial,20,bold"),relief="solid")
    self.label2.place(x=315,y=70)
    
    
    self.label4=tk.Button(image=self.info,bd=0,command=self.get_pix_info)
    self.label4.place(x=205,y=5)
    
    self.fram1=tk.Frame(bg="#f8f8f8",width=700,height=5)
    self.fram1.place(x=0,y=110)
    
    
    self.label5=tk.Label(text="Resize image by Percentage:",font=("arial,20,bold"))
    self.label5.place(x=5,y=115)
    
    
    self.label6=tk.Button(image=self.info,bd=0,command=self.get_per_info)
    self.label6.place(x=265,y=115)
    
    self.label7=tk.Label(text="Width:",font=("arial,20,bold"))
    self.label7.place(x=5,y=150)
    
    
    self.label8=tk.Label(text="Height:",font=("arial,20,bold"))
    self.label8.place(x=200,y=150)
    
    
    
    
    self.entry3=tk.Entry(self,text="",width=10,font=("arial",15,"bold"),relief="solid")
    self.entry3.place(x=5,y=180)
    
    self.label9=tk.Label(text=" %",width=0,font=("arial,20,bold"),relief="solid")
    self.label9.place(x=120,y=180)
    
    
    self.entry4=tk.Entry(self,text="",width=10,font=("arial",15,"bold"),relief="solid")
    self.entry4.place(x=200,y=180)
    
    self.label10=tk.Label(text=" %",width=0,font=("arial,20,bold"),relief="solid")
    self.label10.place(x=315,y=180)
    
    
    self.fram2=tk.Frame(bg="#f8f8f8",width=700,height=40)
    self.fram2.place(x=0,y=230)
    
    self.label11=tk.Label(text="Optional Settings:",bg="#f8f8f8",font=("arial,20,bold"))
    self.label11.place(x=5,y=235)
    
    self.label12=tk.Label(image=self.setting,bd=0,bg="#f8f8f8")
    self.label12.place(x=165,y=235)
    
    self.label13=tk.Label(text="Target Format:",font=("arial,20,bold"))
    self.label13.place(x=5,y=285)
    
    self.label14=tk.Button(image=self.info,bd=0,command=self.get_format)
    self.label14.place(x=140,y=285)
    
    self.compobox=Combobox(self,values=["PNG","Webp","jpg","ICO","GIF"],width=10,font=("arial,29,bold"))
    self.compobox.place(x=5,y=320)
    self.compobox.set("PNG")
    
    self.fram3=tk.Frame(bg="#f8f8f8",width=700,height=40)
    self.fram3.place(x=0,y=360)
    
    
    self.label15=tk.Label(text="File Location:",bg="#f8f8f8",font=("arial,20,bold"))
    self.label15.place(x=5,y=365)
    
    self.label16=tk.Label(image=self.file,bd=0,bg="#f8f8f8")
    self.label16.place(x=130,y=365)
    
    
    self.label17=tk.Label(text="Browse File:",font=("arial,20,bold"))
    self.label17.place(x=5,y=410)
    
    self.label18=tk.Label(text="Rename File:",font=("arial,20,bold"))
    self.label18.place(x=5,y=455)
    
    self.entry5=tk.Entry(self,width=25,font=("arial",20,"bold"),relief="solid")
    self.entry5.place(x=130,y=410)
    
    
    self.entry6=tk.Entry(self,width=25,font=("arial",20,"bold"),relief="solid")
    self.entry6.place(x=130,y=455)
    

      
    
    style=Style()

    style.configure("TButton",font=('calibri',20,'bold'),borderwidth="4")
    style.map("TButton",foreground=[('active','!disabled','green')],
    background=[('active','black')])
    
    self.browse_button=ttk.Button(text="Browse",command=self.browse)
    self.browse_button.place(x=510,y=406)
    
    self.convert_button=ttk.Button(text="START",command=self.convert_file)
    self.convert_button.place(x=510,y=452)
    
    # comtact with me  #
    self.github_button=ttk.Button(text="",image=self.git,command=self.git_hub)
    self.github_button.place(x=640,y=5)
    
    self.linkid_button=ttk.Button(text="",image=self.lenkid,command=self.linkinen)
    self.linkid_button.place(x=580,y=5)
    
    self.gmail_button=ttk.Button(text="",image=self.gmai,command=self.gmail)
    self.gmail_button.place(x=520,y=5)

    # comtact with me  #
    
app=convertor()
app.mainloop()


