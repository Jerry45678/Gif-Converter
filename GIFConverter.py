import sys
from tkinter import StringVar, filedialog, messagebox
from tkinter.filedialog import askdirectory
import os
import imageio

##依照版本匯入Tkinter
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#圖片檔列表 內容會是路徑文字
filez = []

#匯入按鈕功能
def open_file():
    #叫出開檔案視窗
    files = filedialog.askopenfilenames(parent=root,filetypes = (("png files","*.png"),("all files","*.*")))
    #把開啟的圖片路徑匯入上面那個列表
    for file in files:
        filez.append(file)
        Textbox.insert(tk.END, os.path.basename(str(file)))

def delete_all():
    Textbox.delete(0,tk.END)
    filez = []

def select_path():
    #叫出選路徑視窗
    file_path = filedialog.askdirectory()
    #Listbox1是路徑按鈕前面那一個文字輸入區塊 先把顯示的文字刪掉 避免像是選錯位子在按第二次按鈕 所以先把內容清空
    Listbox1.delete(0,tk.END)
    #加入新路徑
    Listbox1.insert(1, str(file_path))

def converter():
    if(filez == [] or Entry1.get() == ""):
        tk.messagebox.showinfo(title="警告", message="找不到檔案或未輸入名稱")
        return
    #輪迴次數 0是無限次 但選單內我用文字無限不是數字0 所以要先把無限兩字換成0
    if(TCombobox1.get() == "無限"): Loop = 0
    else: Loop = TCombobox1.get()
    #把檔案轉乘GIF
    images = []
    for item in filez:
        images.append(imageio.imread(item))
    ##輸出 duration=間隔 loop=輪迴次數 Loop是50行那邊給的值
    imageio.mimsave(Entry1.get() + '.gif', images, 'GIF',duration = Spinbox1.get(), loop = Loop)
    ##把檔案移動到指定目錄 如果老師問為什麼不直接匯出到目標就好 因為我不會
    if(Listbox1.get(0) != ""):
        #原位
        src = str.replace(os.path.abspath(os.getcwd()),"/","\\") + "\\" + Entry1.get() + '.gif'
        #目的
        des = str.replace(Listbox1.get(0),"/","\\") + "\\"  + Entry1.get() + '.gif'
        #傳送
        os.rename(src,des)
    tk.messagebox.showinfo(title="通知", message="成功輸出檔案")


root = tk.Tk()


#介面 我直接用PAGE製作在複製過來
root.geometry("312x253")
root.resizable(0, 0)
root.title("GIF轉換器")
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")

Button1 = tk.Button(root, command=converter)
Button1.place(relx=0.032, rely=0.751, height=54, width=298)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(cursor="fleur")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''轉換''')

Labelframe1 = tk.LabelFrame(root)
Labelframe1.place(relx=0.038, rely=0.0, relheight=0.593
                , relwidth=0.494)
Labelframe1.configure(relief='groove')
Labelframe1.configure(foreground="black")
Labelframe1.configure(labelanchor="n")
Labelframe1.configure(text='''圖片檔案''')
Labelframe1.configure(background="#d9d9d9")
Labelframe1.configure(highlightbackground="#d9d9d9")
Labelframe1.configure(highlightcolor="black")

Textbox = tk.Listbox(Labelframe1)
Textbox.place(relx=0.065, rely=0.127, relheight=0.633, relwidth=0.877
                , bordermode='ignore')

Import = tk.Button(Labelframe1, command=open_file)
Import.place(relx=0.13, rely=0.8, height=24, width=48
                , bordermode='ignore')
Import.configure(activebackground="#ececec")
Import.configure(activeforeground="#000000")
Import.configure(background="#d9d9d9")
Import.configure(disabledforeground="#a3a3a3")
Import.configure(foreground="#000000")
Import.configure(highlightbackground="#d9d9d9")
Import.configure(highlightcolor="black")
Import.configure(pady="0")
Import.configure(text='''匯入''')

Clear = tk.Button(Labelframe1, command=delete_all)
Clear.place(relx=0.584, rely=0.8, height=24, width=48
                , bordermode='ignore')
Clear.configure(activebackground="#ececec")
Clear.configure(activeforeground="#000000")
Clear.configure(background="#d9d9d9")
Clear.configure(disabledforeground="#a3a3a3")
Clear.configure(foreground="#000000")
Clear.configure(highlightbackground="#d9d9d9")
Clear.configure(highlightcolor="black")
Clear.configure(pady="0")
Clear.configure(text='''清空''')

Labelframe2 = tk.LabelFrame(root)
Labelframe2.place(relx=0.564, rely=0.0, relheight=0.605
                , relwidth=0.423)
Labelframe2.configure(relief='groove')
Labelframe2.configure(foreground="black")
Labelframe2.configure(labelanchor="n")
Labelframe2.configure(text='''設定''')
Labelframe2.configure(background="#d9d9d9")
Labelframe2.configure(highlightbackground="#d9d9d9")
Labelframe2.configure(highlightcolor="black")

Label1 = tk.Label(Labelframe2)
Label1.place(relx=0.076, rely=0.719, height=20, width=26
                , bordermode='ignore')
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="black")
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(justify='left')
Label1.configure(text='''檔名:''')

Spinbox1 = tk.Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1.place(relx=0.303, rely=0.196, relheight=0.124
                , relwidth=0.568, bordermode='ignore')
Spinbox1.configure(activebackground="#f9f9f9")
Spinbox1.configure(background="white")
Spinbox1.configure(buttonbackground="#d9d9d9")
Spinbox1.configure(disabledforeground="#a3a3a3")
Spinbox1.configure(font="TkDefaultFont")
Spinbox1.configure(foreground="black")
Spinbox1.configure(highlightbackground="black")
Spinbox1.configure(highlightcolor="black")
Spinbox1.configure(insertbackground="black")
Spinbox1.configure(justify='right')
Spinbox1.configure(selectbackground="blue")
Spinbox1.configure(selectforeground="white")

TCombobox1 = ttk.Combobox(Labelframe2)
TCombobox1.place(relx=0.303, rely=0.451, relheight=0.137
                , relwidth=0.553, bordermode='ignore')
value_list = ['無限','1','3','5','8','10',]
TCombobox1.configure(values=value_list)
TCombobox1.configure(justify='right')
TCombobox1.configure(takefocus="")
TCombobox1.current(0)

Entry1 = tk.Entry(Labelframe2)
Entry1.place(relx=0.303, rely=0.719, height=17, relwidth=0.561
                , bordermode='ignore')
Entry1.configure(background="white")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#000000")
Entry1.configure(insertbackground="black")

Label2 = tk.Label(root)
Label2.place(relx=0.577, rely=0.13, height=31, width=34)
Label2.configure(activebackground="#f9f9f9")
Label2.configure(activeforeground="black")
Label2.configure(background="#d9d9d9")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")
Label2.configure(highlightbackground="#d9d9d9")
Label2.configure(highlightcolor="black")
Label2.configure(text='''間隔:''')

Label4 = tk.Label(root)
Label4.place(relx=0.577, rely=0.277, height=30, width=34)
Label4.configure(activebackground="#f9f9f9")
Label4.configure(activeforeground="black")
Label4.configure(background="#d9d9d9")
Label4.configure(disabledforeground="#a3a3a3")
Label4.configure(foreground="#000000")
Label4.configure(highlightbackground="#d9d9d9")
Label4.configure(highlightcolor="black")
Label4.configure(text='''循環:''')

Listbox1 = tk.Listbox(root)
Listbox1.place(relx=0.064, rely=0.632, relheight=0.079
                , relwidth=0.718)
Listbox1.configure(background="white")
Listbox1.configure(disabledforeground="#a3a3a3")
Listbox1.configure(font="TkFixedFont")
Listbox1.configure(foreground="#000000")

Button2 = tk.Button(root, command=select_path)
Button2.place(relx=0.801, rely=0.632, height=24, width=48)
Button2.configure(activebackground="#ececec")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''路徑''')

root.mainloop()