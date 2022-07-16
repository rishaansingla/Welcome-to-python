from tkinter import *
def get_gst():
    a=int(netprice_t.get())
    b=int(originalcost_t.get())
    display.insert(0,f'GST rate ={((a-b)*100)/b}')

c=Tk()
c.title("GST rate calculator")
c.geometry('400x300')
c.config(bg='#0f4b6e')

netprice_t=Entry(c)
originalcost_t=Entry(c)

netprice_lbl=Label(c,text='Net Price',bg='#0f4b6e',fg='white')
originalcost_lbl=Label(c,text='Original Cost',bg='#0f4b6e',fg='white')

netprice_lbl.pack()
netprice_t.pack()
originalcost_lbl.pack()
originalcost_t.pack()

bt=Button(c,text="Get GST Rate",relief='solid',command=get_gst)
bt.pack(pady=10)

display=Entry(c,width=38,font=('Arial',14))
display.pack(pady=5)
c.mainloop()
