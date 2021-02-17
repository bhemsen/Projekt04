from tkinter import *
from tkinter import ttk

def doStuff():
    for thing in range(100):
	    Button(f1, text=f'Button {thing} Yo!').pack()


root = Tk()
root.title('Learn To Code at Codemy.com')
root.geometry("500x400")

myNotebook = ttk.Notebook(root)
myNotebook.pack()

frame1 = ttk.Frame(myNotebook, width=800, height=600)
frame2 = ttk.Frame(myNotebook, width=800, height=600)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

myNotebook.add(frame1, text= 'Subnets')
myNotebook.add(frame2, text='Convert')

# Create A Main Frame

horizontalPane = ttk.Panedwindow(frame1, orient=HORIZONTAL)
horizontalPane.pack(fill=BOTH, expand=True)

f1 = ttk.Labelframe(horizontalPane, text='Input', width=100, height=100)
f2 = ttk.Labelframe(horizontalPane, text='Input', width=100, height=100)
ttk.Button(f2, text='btn', command=doStuff).grid(column=0, row=0, sticky=E)
horizontalPane.add(f1)
horizontalPane.add(f2)

main_frame = Frame(f1)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# for thing in range(100):
# 	Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)

my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)


root.mainloop()
