from tkinter import *
from tkinter import ttk
from IPConverter.Converter import Converter
from inputhandler.Inputhandler import Inputhandler

class FeetToMeters:

    def __init__(self, root):

        self.converter = Converter()
        self.inputhandler = Inputhandler()

        root.title("Feet to Meters")
        # root.geometry('800x600')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # mainframe.pack(fill=BOTH, expand=True)

        myNotebook = ttk.Notebook(root)
        myNotebook.pack()

        frame1 = ttk.Frame(myNotebook, width=800, height=600)
        frame2 = ttk.Frame(myNotebook, width=800, height=600)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        myNotebook.add(frame1, text= 'Subnets')
        myNotebook.add(frame2, text='Convert')


        self.feet = StringVar()
        feet_entry = ttk.Entry(frame1, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(frame1, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(frame1, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(frame1, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(frame1, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(frame1, text="meters").grid(column=3, row=2, sticky=W)



        # 2. Frame Converter: 

        # Setting the variables
        # V4
        self.inputIPv4 = StringVar()
        self.outputIPv4_binär = StringVar()
        self.outputIPv6 = StringVar()
        self.outputIPv6_binär = StringVar()
        inputIPv4_entry = ttk.Entry(frame2, textvariable=self.inputIPv4)
        inputIPv4_entry.grid(column=1, row=1, sticky=NSEW)

        # V6
        self.inputIPv6 = StringVar()
        self.outputIPv4 = StringVar()
        self.outputIPv4_binär2 = StringVar()
        self.outputIPv6_binär2 = StringVar()
        inputIPv6_entry = ttk.Entry(frame2, textvariable=self.inputIPv6)
        inputIPv6_entry.grid(column=1, row=5, sticky=NSEW)
        
        # Display Labels and Buttons
        ttk.Label(frame2, text='Eingabe IPv4: ').grid(column=0, row=1, sticky=W)
        ttk.Button(frame2, text='umwandeln', command=self.convertIPv4ToIPv6).grid(column=2, row=1, sticky=NSEW)

        Entry(frame2, textvariable=self.outputIPv4_binär, state='readonly', borderwidth=0, width=128).grid(column=1, row=2, sticky=EW)
        ttk.Label(frame2, text='IPv4-binär: ').grid(column=0, row=2, sticky=W)

        Entry(frame2, textvariable=self.outputIPv6, state='readonly', borderwidth=0, width=128).grid(column=1, row=3, sticky=EW)
        ttk.Label(frame2, text='IPv6-Adresse: ').grid(column=0, row=3, sticky=E)
        
        Entry(frame2, textvariable=self.outputIPv6_binär, state='readonly', borderwidth=0, width=140).grid(column=1, row=4, sticky=EW)
        ttk.Label(frame2, text='IPv6-binär: ').grid(column=0, row=4, sticky=W)
        
        ttk.Label(frame2, text='Eingabe IPv6: ').grid(column=0, row=5, sticky=W)
        ttk.Button(frame2, text='umwandeln', command=self.convertIPv6ToIPv4).grid(column=2, row=5, sticky=NSEW)

        Entry(frame2, textvariable=self.outputIPv6_binär2, state='readonly', borderwidth=0, width=128).grid(column=1, row=6, sticky=EW)
        ttk.Label(frame2, text='IPv6-binär: ').grid(column=0, row=6, sticky=W)

        Entry(frame2, textvariable=self.outputIPv4, state='readonly', borderwidth=0, width=128).grid(column=1, row=7, sticky=EW)
        ttk.Label(frame2, text='IPv4-Adresse: ').grid(column=0, row=7, sticky=W)

        Entry(frame2, textvariable=self.outputIPv4_binär2, state='readonly', borderwidth=0, width=140).grid(column=1, row=8, sticky=EW)
        ttk.Label(frame2, text='IPv4-binär: ').grid(column=0, row=8, sticky=W)

        




        for child in frame2.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

    def convertIPv4ToIPv6(self, *args):
        try:
            value = str(self.inputIPv4.get())
            ip = self.inputhandler.handleIPv4(value)
            convertedIP = self.converter.convertIPv4inIPv6(ip)

            self.outputIPv4_binär.set(self.converter.convertV4ToBinary(ip))
            self.outputIPv6.set(convertedIP)
            self.outputIPv6_binär.set(self.converter.convertV6ToBinary(convertedIP))
        except ValueError:
            self.outputIPv6.set('xxx')

    def convertIPv6ToIPv4(self, *args):
        try:
            value = str(self.inputIPv6.get())
            ip = self.inputhandler.handleIPv6(value)
            convertedIP = self.converter.convertIPv6inIPv4(ip)

            self.outputIPv6_binär2.set(self.converter.convertV6ToBinary(ip))
            self.outputIPv4.set(convertedIP)
            self.outputIPv4_binär2.set(self.converter.convertV4ToBinary(convertedIP))
        except ValueError:
            self.outputIPv6.set('xxx')



root = Tk()
FeetToMeters(root)
root.mainloop()