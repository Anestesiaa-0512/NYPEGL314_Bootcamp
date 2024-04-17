import tkinter as tk  # importing tkinter and shortening name to tk
import osc_client

def Function1():
    print(" This is function1")

def Function2():
    print(" This is function2")

def Function3():
    print(" This is function3")

def VolumeUp():
    print(" This is volumeUp")

def VolumeDown():
    print(" This is volumeDown")

def Volume_Change(x):
    global var
    if x == 1:
        if var == 50:
            print(" You have reached the maximum volume")
            var = var
        else:
            var = var + 1 
    else: 
        if var == 0:
            print(" You have reached the minimum volume")
            var = var
            var = var
        else:
            var = var -1
        
    print(var)

def OSC():
    osc_client.OSC_Message()

main = tk.Tk() 
var = 0 



title = tk.Label(main, text="NYPOSC DEMO CLASS", font="20")
title.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(main, text="Function1", font="20", command=Function1)

button2 = tk.Button(main, text="Function2", font="20", command=Function2)

button3 = tk.Button(main, text="Function3", font="20", command=Function3)

volumeUp = tk.Button(main, text="Volume Up", font="20", command=lambda m=1:Volume_Change(m))

volumeDown = tk.Button(main,text="Volume Down", font="20", command=lambda m=0:Volume_Change(m))

osc = tk.Button(main, text="OSC" ,font="20", command= OSC)

#Button Placements
button1.grid(row=1,column=0)
button2.grid(row=1, column=1)
button3.grid(row=1,column=2)
volumeUp.grid(row=2,column=0)
volumeDown.grid(row=2,column=2)
osc.grid(row=3, column=1)
main.mainloop()