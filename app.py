from tkinter import *
from client import *

from PIL import ImageTk, Image

window = Tk()

window.title("Zapzap")

window.geometry('690x610')

frame_comunication = LabelFrame(window, text="Enviar/Receber Mensagem", padx=15, pady=15)
frame_comunication.grid(column=0, row=0)

lbl_ori = Label(frame_comunication, text="username:")
lbl_ori.grid(column=0, row=0)
txt_ori = Entry(frame_comunication,width=10)
txt_ori.grid(column=1, row=0)

lbl_dest = Label(frame_comunication, text="Destino:")
lbl_dest.grid(column=3, row=0)
txt_dest = Entry(frame_comunication,width=10)
txt_dest.grid(column=4, row=0)

lbl_msg = Label(frame_comunication, text="Mensagem:")
lbl_msg.grid(column=0, row=2)
txt_msg = Entry(frame_comunication,width=20)
txt_msg.grid(column=1, row=2)


frame_message = LabelFrame(window, text="Mensagem", padx=15, pady=15)
frame_message.grid(column=0, row=1)

width_size = 40
height_size = 5

lbl_encoded = Label(frame_message, text="Codificada:")
lbl_encoded.grid(column=0, row=0) 
text_encoded = Text(frame_message,width=width_size, height=height_size)
text_encoded.insert(END,"Codificada")
text_encoded.grid(column=0, row=1)

lbl_bits = Label(frame_message, text="Bits:")
lbl_bits.grid(column=0, row=2) 
text_bits = Text(frame_message,width=width_size, height=height_size)
text_bits.insert(END,"Bits")
text_bits.grid(column=0, row=3)

lbl_crypt = Label(frame_message, text="Criptografada:")
lbl_crypt.grid(column=0, row=4) 
text_crypt = Text(frame_message,width=width_size, height=height_size)
text_crypt.insert(END,"Criptografia")
text_crypt.grid(column=0, row=5)

lbl_img = Label(frame_message, text="Grafico:")
lbl_img.grid(column=0, row=6) 


graphic_img = Image.open('grafico.png')

h = graphic_img.height
w = graphic_img.width
limit_h = 650
p = w/limit_h
w = limit_h
h = int(h/p) 
print(w,h, p)
graphic_img = ImageTk.PhotoImage(graphic_img.resize((w,h)))

pnl_graphic = Label(frame_message, image=graphic_img)
pnl_graphic.grid(column=0, row=7)


def click_enviar():
    text_encoded.delete(1.0, END)
    text_bits.delete(1.0, END)
    text_crypt.delete(1.0, END)

    print('Enviando...')
    username_ori = txt_ori.get()
    username_dest = txt_dest.get()
    message = txt_msg.get()

    print(username_ori, username_dest, message)
    res_encode = encode(message)
    print(res_encode)

    res_send = send(username_ori, username_dest, res_encode['encoded'])
    print(res_send)

    encoded = list(map(int, res_encode['encoded'].strip('][').split(', ')))
    graph(encoded)
    
    text_encoded.insert(INSERT, res_encode['encoded'])
    text_bits.insert(INSERT, res_encode['binary'])
    text_crypt.insert(INSERT, res_encode['encrypted'])

    graphic_img = Image.open('grafico.png')
    h = graphic_img.height
    w = graphic_img.width
    limit_h = 650
    p = w/limit_h
    w = limit_h
    h = int(h/p) 
    print(w,h, p)
    graphic_img = ImageTk.PhotoImage(graphic_img.resize((w,h)))

    pnl_graphic.configure(image=graphic_img)
    pnl_graphic.image = graphic_img

    print('Enviado')

def click_receber():
    text_encoded.delete(1.0, END)
    text_bits.delete(1.0, END)
    text_crypt.delete(1.0, END)
    txt_msg.delete(0,"end")
    print('Recebendo...')
    username = txt_ori.get()
    print(username)

    res_listen = listen(username)
    print(res_listen)
    if not res_listen:
        return

    res_msg = decode(res_listen['message'])
    print(res_msg)

    txt_msg.insert(0, res_msg['message'])

    encoded = list(map(int, res_msg['encoded'].strip('][').split(', ')))
    graph(encoded)

    text_encoded.insert(INSERT, res_msg['encoded'])
    text_bits.insert(INSERT, res_msg['binary'])
    text_crypt.insert(INSERT, res_msg['encrypted'])
    
    graphic_img = Image.open('grafico.png')
    h = graphic_img.height
    w = graphic_img.width
    limit_h = 650
    p = w/limit_h
    w = limit_h
    h = int(h/p) 
    print(w,h, p)
    graphic_img = ImageTk.PhotoImage(graphic_img.resize((w,h)))

    pnl_graphic.configure(image=graphic_img)
    pnl_graphic.image = graphic_img

    print('Recebido')

btn_enviar = Button(frame_comunication, text="Enviar", command=click_enviar)
btn_enviar.grid(column=5, row=2)

btn_enviar = Button(frame_comunication, text="Receber", command=click_receber)
btn_enviar.grid(column=6, row=2)

window.mainloop()   