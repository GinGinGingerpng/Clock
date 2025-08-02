import datetime, locale ,tkinter
class digitalClock:
    def __init__(self,root:tkinter.Tk):
        root.title("時計")
        root.geometry('480x120')
        self.canvas =tkinter.Canvas(root,bg="#B9EAFF")
        self.canvas.pack(expand=True,fill=tkinter.BOTH)
        self.afterId = None
        locale.setlocale(locale.LC_TIME,'ja_JP')
        root.bind('<Configure>',self.configured)

    def configured(self,event):
        self.update()
    
    def update(self):
        if self.afterId != None:
            root.after_cancel(self.afterId)
        self.canvas.delete('all')
        self.img=tkinter.PhotoImage(file=".\kumo.png",width=152, height=86)
        self.img2=tkinter.PhotoImage(file="./taiyo.png",width=100, height=71)
        self.canvas.create_image(100,100,image=self.img)
        self.canvas.create_image(400,60,image=self.img)
        self.canvas.create_image(100,30,image=self.img2)
        self.canvas.create_text(
            self.canvas.winfo_width() //2,
            self.canvas.winfo_height() //2,
            text=datetime.datetime.now().strftime(
                '%Y年%m月%d日(%a) %H:%M:%S'
            ),
            font=("HG丸ｺﾞｼｯｸM-PRO",20),
            fill= "#225bcd"
        )
        self.afterId=root.after(100,self.update)
root=tkinter.Tk()
digitalClock(root)
root.mainloop()
    