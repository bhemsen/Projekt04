from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from netaddr import * 
from functools import partial
from IPConverter.Converter import Converter
from inputhandler.Inputhandler import Inputhandler
from Outputhandler.Outputhandler import Outputhandler
from Networks.Network import Network
from _MySQL.Database import Database
import os.path



class IPMaster9000:

    def __init__(self, root):

        self.converter = Converter()
        self.inputhandler = Inputhandler()
        self.outputhandler = Outputhandler()
        # self.db = Database('localhost','webadmin','password','projekt04')


        root.title("IPMaster9000")
        root.geometry('1200x400')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # mainframe.pack(fill=BOTH, expand=True)

        myNotebook = ttk.Notebook(root)
        myNotebook.pack(fill=BOTH, expand=True)

        frame1 = ttk.Frame(myNotebook, width=800, height=600)
        frame2 = ttk.Frame(myNotebook, width=800, height=600)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        myNotebook.add(frame1, text= 'Subnets')
        myNotebook.add(frame2, text='Convert')
# -----------------------------------------------------------------------------------------------------------------------------------
        # Frame 1: Calculating Subnets
# -----------------------------------------------------------------------------------------------------------------------------------
        # creating panels
        self.horizontalPane = ttk.Panedwindow(frame1, orient=HORIZONTAL)
        self.horizontalPane.pack(fill=BOTH, expand=True)
        self.f1 = ttk.Labelframe(self.horizontalPane, text='Input', width=100, height=100)


#-------------------------------------------PanedWindow2-----------------------------------------------------------------------------        
        self.f2parent = ttk.Labelframe(self.horizontalPane, text='Abteilung', width=400, height=300)

        
        # Create A Canvas
        my_canvas = Canvas(self.f2parent,bd=0, highlightthickness=0, relief='ridge')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.f2parent, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        self.f2 = Frame(my_canvas, border=0, pady=2, padx=2)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=self.f2, anchor="nw")



        #-------------------------------------------PanedWindow3-------------------

        self.f3parent = ttk.Labelframe(self.horizontalPane, text='IP-Zuordnung', width=400, height=300)

        
        # Create A Canvas
        my_canvas2 = Canvas(self.f3parent,bd=0, highlightthickness=0, relief='ridge')
        my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar2 = ttk.Scrollbar(self.f3parent, orient=VERTICAL, command=my_canvas2.yview)
        my_scrollbar2.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
        my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion = my_canvas2.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        self.f3 = Frame(my_canvas2)

        # Add that New frame To a Window In The Canvas
        my_canvas2.create_window((0,0), window=self.f3, anchor="nw")


        self.horizontalPane.add(self.f1)
        self.horizontalPane.add(self.f2parent)
        self.horizontalPane.add(self.f3parent)

        # Setting the Variables#
        self.inputNetwork = StringVar()
        self.inputSubnetmask = StringVar()
        self.inputHostCount = StringVar()


        # Setting up the Inputfields
        ttk.Label(self.f1, text='Eingabe IPv4-Netzadresse: ').grid(column=0, row=0, sticky=W)
        ttk.Entry(self.f1, textvariable=self.inputNetwork).grid(column=1, row=0, sticky=EW)

        ttk.Label(self.f1, text='Eingabe der Subnetzmaske: ').grid(column=0, row=1, sticky=W)
        ttk.Entry(self.f1, textvariable=self.inputSubnetmask).grid(column=1, row=1, sticky=EW)

        ttk.Label(self.f1, text='Anzahl der benötigten Hosts: ').grid(column=0, row=2, sticky=W)
        ttk.Entry(self.f1, textvariable=self.inputHostCount).grid(column=1, row=2, sticky=EW)


        ttk.Button(self.f1, text='berechnen', command=self.createSubnet).grid(column=1, row=3, sticky=NSEW)

# ----------------------------------------------------------------------------------------------------------------------------
        # 2. Frame Converter: 
# ----------------------------------------------------------------------------------------------------------------------------
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

        # Subnetzmaske
        self.snm = StringVar()
        self.outputSuffix = StringVar()
        self.outputSnm_binär = StringVar()
        snm_entry = ttk.Entry(frame2, textvariable=self.snm)
        snm_entry.grid(column=1, row=9, sticky=NSEW)
        
        # Display Labels and Buttons
        ttk.Label(frame2, text='Eingabe IPv4: ').grid(column=0, row=1, sticky=W)
        ttk.Button(frame2, text='umwandeln', command=self.convertIPv4ToIPv6).grid(column=2, row=1, sticky=NSEW)

        Entry(frame2, textvariable=self.outputIPv4_binär, state='readonly', borderwidth=0, width=128).grid(column=1, row=2, sticky=EW)
        ttk.Label(frame2, text='IPv4-binär: ').grid(column=0, row=2, sticky=W)

        Entry(frame2, textvariable=self.outputIPv6, state='readonly', borderwidth=0, width=128).grid(column=1, row=3, sticky=EW)
        ttk.Label(frame2, text='IPv6-Adresse: ').grid(column=0, row=3, sticky=W)
        
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
        
        ttk.Label(frame2, text='Eingabe Subnetzmaske: ').grid(column=0, row=9, sticky=W)
        ttk.Button(frame2, text='umwandeln', command=self.convertSubnetzmaske).grid(column=2, row=9, sticky=NSEW)
        
        Entry(frame2, textvariable=self.outputSnm_binär, state='readonly', borderwidth=0, width=140).grid(column=1, row=10, sticky=EW)
        ttk.Label(frame2, text='Subnetzmaske-binär: ').grid(column=0, row=10, sticky=W)
        
        Entry(frame2, textvariable=self.outputSuffix, state='readonly', borderwidth=0, width=140).grid(column=1, row=11, sticky=EW)
        ttk.Label(frame2, text='Suffix: ').grid(column=0, row=11, sticky=W)



        # for child in frame1.winfo_children(): 
        #     child.grid_configure(padx=8, pady=8)

        for child in frame2.winfo_children(): 
            child.grid_configure(padx=2, pady=2)

        
        # root.bind("<Return>", self.calculate)

# ------------------------------------------------------------------------------------------------------------------------------
    # Frame 1 funktions
# ------------------------------------------------------------------------------------------------------------------------------
    def createSubnet(self):
        try:
            networkAdress = str(self.inputNetwork.get())
            subnetmask = str(self.inputSubnetmask.get())
            hostcount = str(self.inputHostCount.get())

            userInput = self.inputhandler.handleNewNetwork(networkAdress, subnetmask, hostcount)
            
            ipNetwork = self.converter.convertToNetwork(userInput)
            networks = Network().createSubnets(userInput, ipNetwork)
            
            self.displaySubnets(networks)
        

        except ValueError:
            pass


    def displaySubnets(self, networks):
        try:
            for widget in self.f2.winfo_children():
                widget.destroy()
            self.f2.pack_forget()

            # for every created network connect IP to PC
            keys = networks.keys()
            self.data = {}
            self.inputAbteilungen = {}
            i = 0
            for key in keys:
                self.data[i] = StringVar()
                self.inputAbteilungen[i] = ttk.Entry(self.f2, textvariable=self.data[i])
                self.inputAbteilungen[i].grid(column=2, row=i, sticky=EW)
            
                ttk.Label(self.f2, text=key).grid(column=0, row=i, sticky=W, padx=3, pady=3)
                ttk.Label(self.f2, text='Abteilung: ').grid(column=1, row=i, sticky=W)
                ttk.Button(self.f2, text='Go', command=partial(self.displayIPAssignment, self.inputAbteilungen[i], key, networks[key])).grid(column=3, row=i, sticky=NSEW)

                i = i+1
                
        except:
            pass


    def displayIPAssignment(self, varName, network, listOfIPs):
        for widget in self.f3.winfo_children():
            widget.destroy()
        self.f3.pack_forget()
        self.value = varName.get()
        ip = IPNetwork(network)
        self.data['name'] = 'Abteilung_'+self.value
        self.data['content'] = '#\n# IP-Adresszuordung für das Netz '+ self.value+'\n#\n# IP-Adresse     PC\n\n' +str(ip.network) + '    Netzadresse\n' + str(ip.broadcast) + '   Broadcastadresse\n'+str(ip.netmask)+ '    Subnetsmaske\n\n'
        self.ipAssignment = {}
        self.pcs = {}

        if(os.path.exists(self.data['name'])):
            overwrite = messagebox.askyesno(message='Are you sure you want to overwrite the file??',icon='question', title='Overwrite File')
            if(overwrite):
                self.outputhandler.overwriteToFile(self.data)
            else:
                self.data['name']= filedialog.asksaveasfilename()
                self.outputhandler.writeToFile(self.data)

        else:
            self.outputhandler.writeToFile(self.data)

        
        ttk.Label(self.f3, text=ip.network).grid(column=0, row=0, sticky=W)
        ttk.Label(self.f3, text='Netzwerkadresse').grid(column=1, row=0, sticky=W, padx=5)

        ttk.Label(self.f3, text=ip.broadcast).grid(column=0, row=1, sticky=W)
        ttk.Label(self.f3, text='Broadcastadresse').grid(column=1, row=1, sticky=W, padx=5)

        ttk.Label(self.f3, text=ip.netmask).grid(column=0, row=2, sticky=W)
        ttk.Label(self.f3, text='Subnetzmaske').grid(column=1, row=2, sticky=W, padx=5)


        for i in range(1,len(listOfIPs)-1):
            ip = str(listOfIPs[i])
            self.ipAssignment[i] = StringVar()

            self.pcs[ip] = ttk.Entry(self.f3, textvariable=self.ipAssignment[i])
            self.pcs[ip].grid(column=1, row=(i+3), sticky=EW, padx=5)

            ttk.Label(self.f3, text=ip).grid(column=0, row=(i+3), sticky=W)

        ttk.Button(self.f3, text='speichern', command=partial(self.saveIPs, self.pcs)).grid(column=2, row=1, sticky=NSEW)


    def saveIPs(self, assignments):
        k = assignments.keys()
        # validation
        l = []
        for x in k:
            if(assignments[x].get() != ''):
                if(assignments[x].get() in l):
                    messagebox.showinfo(message='Überprüfe deine Eingabe!\nJedem PC kann nur eine IP zugeordnet werden')
                    return
                
            l.append(assignments[x].get())
        
        for x in k:
            self.data['content'] = x +"    "+ assignments[x].get()+'\n'
            self.outputhandler.appendToFile(self.data)
            assignments[x].delete(0, 'end')
        

                         
# --------------------------------------------------------------------------------------------------------------------------------
    # Frame 2 funktions
# --------------------------------------------------------------------------------------------------------------------------------
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

    def convertSubnetzmaske(self, *args):
        try:
            value = str(self.snm.get())
            netmask = self.inputhandler.handleNetmask(value)
            binär = self.converter.convertSubnetmaskToBinary(netmask)
            suffix = self.converter.convertNetmaskInSuffix(netmask)

            self.outputSnm_binär.set(binär)
            self.outputSuffix.set(suffix)
        except ValueError:
            self.outputIPv6.set('xxx')


# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

