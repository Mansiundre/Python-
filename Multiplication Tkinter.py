from tkinter import * def show_table():

num = int(entry.get())

str1=' Table of ' + str(num) + '\n----------------- \n'

for i in range(1,11):

str1 = str1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

output_label.configure(text = str1, justify=LEFT)

main_window = Tk() main_window.title("Multiplication Table")

message_label = Label(text= ' Enter a number to \n display its Table ' , font=( ' Verdana ' , 12))

output_label = Label(font=( ' Verdana ' , 12)) entry = Entry(font=( ' Verdana ' , 12), width=6)

