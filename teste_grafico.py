from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('AMI graphic')
root.geometry("800x600")

test_msg = [0, 1, -1, 0, 0, 1, -1, 0, 0, 1, -1, 1, 0, -1, 0, 1, 0, -1, 1, -1, 0, 1, 0, 0, 0, -1, 1, 0, 0, -1, 1, 0, 0, -1, 1, -1, 0, 1, 0, -1]

def graph(data):
    data.insert(len(data),0)
    y = data
    x = np.arange(len(data))
    print(len(data)/2)

    fig = plt.figure(figsize=(10,2),dpi=150)

    ax = fig.add_subplot()

    ax.plot(x, y, drawstyle="steps-post", linewidth=2.0)

    ax.set_yticks([-1,0,1])
    ax.set_yticklabels(['-V',0,'+V'])
    ax.set_title('Forma da onda - AMI')

    x_major_ticks = np.arange(-1, len(data)+1, 5)
    x_minor_ticks = np.arange(-1, len(data)+1, 1)

    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, minor=True)

    ax.grid(which='major', axis='x', linestyle='--')
    ax.grid(which='minor', axis='x', linestyle='--')
    ax.grid(which='major', axis='y', linestyle='-', alpha=0.7)
    
    plt.show()


button = Button(root, text="Mostrar Gráfico", command= lambda: graph(test_msg))
button.pack()

root.mainloop()