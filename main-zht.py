from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import get_char
import count_char
import global_var
import ttc_get
import ntpath
import pyglet
#drag and drop
import sys
first_time = True

#load ui font
pyglet.font.add_file('GenYoGothicTW-R.ttf')
pyglet.font.add_file('cjk-char-bold.ttf')
#start window
main = Tk()
#set title
# main.title("字型計數軟體")
main.title("Z01 FontElf-逐浪字體精靈v1.0 逐浪字形檔出品 http://f.ziti163.com 字形檔授權與訂制熱線：0791-86161900、13177777714")  # 程序名称
#window size
main.geometry('')
#prepare font
title_font=("cjk-char-bold", 16, "underline")
text_font=("GenYoGothic TW R", 14)
text_sum_font=("cjk-char-bold", 14)
#add frame
frame = Frame(main)
frame.pack(padx=(25,40), pady=(0,30))
#set module language
current_lang="zht"


#text label + button
input_lbl = Label(frame, text="選擇字型檔：　　　", font=text_font)
input_lbl.grid(column=0, row=0, sticky=E)
btn = Button(frame, text ='打開', font=text_font, command = lambda:open_file(None) ) #just send None as no drag and drop file
btn.grid(column=0, row=0, sticky=E)

#show file name
font_name = StringVar(main)
font_name_lbl = Label(frame, textvariable=font_name, justify="left", font=text_font)
font_name_lbl.grid(column=2, row=0, sticky=W, columnspan=3)
font_name.set("無")

font_txt_lbl = Label(frame, text="字型檔：", justify="right", font=text_font)
font_txt_lbl.grid(column=1, row=0, sticky=E, padx=(5,0))


#section 1: chinese encoding
#prepare listing for string var
cjk_lbl={}
cjk_empty={}
cjk_count={}
cjk_var={}

cjk_fan_start=2
cjk_enc_lbl = Label(frame, text="正體（繁體）中文編碼", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_fan_start, sticky=W, padx=5)
#loop label for cjk fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_fan_list_zht.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_fan_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_fan_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_fan_start+1, sticky=W)
    cjk_jian_fan_start=cjk_fan_start+i+1

cjk_jian_fan_start+=2
cjk_enc_lbl = Label(frame, text="簡體/正體（繁體）中文編碼", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_jian_fan_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk jian-fan
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_fan_list_zht.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_fan_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_fan_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_fan_start+1, sticky=W, padx=(0,16))
    cjk_jian_start=cjk_jian_fan_start+i+1

cjk_jian_start+=2
cjk_enc_lbl = Label(frame, text="簡體中文編碼", font=title_font, anchor="w")
cjk_enc_lbl.grid(column=0, row=cjk_jian_start-1, rowspan=2, sticky="SW", padx=5)
#loop label for cjk jian
for i, (cjk_enc, cjk_enc_name) in enumerate(global_var.cjk_jian_list_zht.items()):
    cjk_var[cjk_enc] = StringVar(main)
    cjk_lbl[cjk_enc] = Label(frame, text=cjk_enc_name+"：", justify="left", font=text_font).grid(column=0, row=i+cjk_jian_start+1, sticky=W)
    cjk_empty[cjk_enc] = Label(frame, textvariable=cjk_var[cjk_enc], justify="left", font=text_font).grid(column=1, row=i+cjk_jian_start+1)
    cjk_count[cjk_enc] = Label(frame, text="/"+str(global_var.cjk_count[cjk_enc]), justify="left", font=text_font).grid(column=2, row=i+cjk_jian_start+1, sticky=W)
    last_row = i+cjk_jian_start+1


#section 2: unicode section
unicode_lbl = Label(frame, text="統一碼區段", font=title_font)
unicode_lbl.grid(column=3, row=2, sticky=W, padx=5)
unicode_lbl={}
unicode_empty={}
unicode_count={}
unicode_var={}
unicode_last_tag=0
#listing with unicode area
for i, (unicode_enc, unicode_enc_name) in enumerate(global_var.unicode_list_zht.items()):
    unicode_row=i+3
    unicode_var[unicode_enc] = StringVar(main)
    #only bold total
    if unicode_enc == "total":
        unicode_text_font = text_sum_font
    else:
        unicode_text_font = text_font
    unicode_lbl[unicode_enc] = Label(frame, text=unicode_enc_name+"：", justify="left", font=unicode_text_font).grid(column=3, row=unicode_row, sticky=W, pady=2)
    unicode_empty[unicode_enc] = Label(frame, textvariable=unicode_var[unicode_enc], justify="left", font=unicode_text_font).grid(column=4, row=unicode_row)
    unicode_count[unicode_enc] = Label(frame, text="/"+str(global_var.unicode_count[unicode_enc]), justify="left", font=unicode_text_font).grid(column=5, row=unicode_row, sticky=W)

#use last row
notice_oldname = Label(frame, text="逐浪字库出品，基于CJK-character-count开源项目。", justify="right", font=text_font).grid(column=3, row=last_row, sticky=E, columnspan=3)


# 增加按钮
import webbrowser  # 导入浏览器

def openLink1():
     url = 'http://f.ziti163.com'
     webbrowser.open(url = url, new = 0)

def openLink2():
     url = 'http://www.ziti163.com'
     webbrowser.open(url = url, new = 1)

btn = Button(frame, text ='♛逐浪字库官网-可免费下载千套字库', font=text_font, command = openLink1,background='red',fg='#ffffff' ) #just send None as no drag and drop file
btn.grid(column=3, row=0, sticky=W)

 
btn = Button(frame, text ='♛字体网-业界知识门户', font=text_font, command = openLink2,background='red',fg='#ffffff' ) #just send None as no drag and drop file
btn.grid(column=4, row=0, sticky=W)


#open file react function
def open_file(filename_arg):
    #check if file is dragged onto here
    if filename_arg:
        #set filename to font
        filename = filename_arg
    else:
        #get file with open file dialog
        filename = fd.askopenfilename(initialdir = 'shell:Desktop', title="選擇字型文件",
                                    filetypes = [("所有支援的字型格式","*.ttf *.otf *.woff *.woff2 *.otc *.ttc"),
                                                ("單獨字型文件","*.ttf *.otf *.woff *.woff2"),
                                                ("TrueType 字型","*.ttf"),
                                                ("OpenType 字型","*.otf"),
                                                ("網頁開放字型 (WOFF)","*.woff *.woff2"),
                                                ("OpenType 合集字型","*.otc *.ttc"),
                                                ("全部文件","*.*")
                                                ]
                                    )
    #test if the file is a valid font file
    is_a_font = False
    if (filename.lower().endswith((".otf",".ttf",".woff",".woff2",".otc",".ttc"))):
        # external module: get_char
        is_a_font = get_char.is_font(filename)
    
    #default value for non-TTCollection
    font_id = -1
    #for TTCollections, get which font to check
    if is_a_font and (filename.lower().endswith((".otc",".ttc"))):
        #get which font to use, if no choose will return None - external module: ttc_get
        font_id = ttc_get.TTC_popup(main, filename, lang=current_lang).show()
        #if user not select
        if font_id is None:
            filename = "" #trigger as no font selected
            is_a_font = False #prevent font to process

    if is_a_font:
        #show filename
        font_name.set(path_leaf(filename))
        #reset 0
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(0)
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(0)
        #get character list in font - external module: get_char
        char_list = get_char.font_import(filename, font_id, lang=current_lang)
        #get list count - external module: count_char
        output = count_char.count_char(char_list, main, lang=current_lang)
        cjk_char_count = output[0]
        unicode_char_count = output[1]
        #update list count
        for cjk_enc in global_var.cjk_list:
            cjk_var[cjk_enc].set(cjk_char_count[cjk_enc])
        for unicode_enc in global_var.unicode_list:
            unicode_var[unicode_enc].set(unicode_char_count[unicode_enc])
    elif filename == '' or filename is None:
        #no file selected, fd.askopenfilename() will return empty string
        font_name.set("無")
        messagebox.showwarning(title="無選擇", message="沒有選擇字體。")
    elif not is_a_font:
        #not a font, change filename back to null n give error message
        font_name.set("無")
        messagebox.showwarning(title="非字型", message="這不是一個標準字型檔。")
    else:
        #unknown error
        font_name.set("無")
        messagebox.showwarning(title="錯誤", message="出現問題，請重試。")
    #reset to finish counting first time
    first_time = False



#get filename only
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#add icon
main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file='appicon.png'))

#if dragged file onto exe, received file path as parameter 1 and directly start counting, icon loaded alrdy by this
if first_time:
    try:
        font_arg = sys.argv[1]
        if font_arg.lower().endswith((".otf",".ttf",".woff",".woff2",".otc",".ttc")):
            open_file(font_arg)
    except: 
        pass

#UI stay appear
main.mainloop()
