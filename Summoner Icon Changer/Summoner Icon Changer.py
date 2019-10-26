from tkinter import *
from PIL import Image, ImageTk
from json import dumps
from lcu_driver import Connector
Window_Width = 650
Window_Height = 650
connector = Connector()
global SummonerIcon

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title('Summoner Icon Editor - Manoah [Developmental]')
        master.iconbitmap('Icon.ico')

        self.canvas = Canvas(master, height=Window_Height, width=Window_Width)
        self.canvas.pack()

        img = Image.open("Background.jpg")
        img = img.resize((2030, 1184), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(img)
        self.background = Label(master, image=background_image)
        self.background.image = background_image
        self.background.place(relwidth=1, relheight=1)

        self.button = Button(self.background, text="Set Summoner Icon", fg='#e6e6ff', font=50, bg='#00001a', command=lambda: self.set_icon_button(self.entry.get()))
        self.button.place(relx=0.3, rely=0.93, relwidth=0.42, relheight=0.065)

        self.entry = Entry(self.background, font=50)
        self.entry.place(relx=0.255, rely=0.89, relwidth=0.5, relheight=0.03)

        img2 = Image.open("icon-reference.png")
        img2 = img2.resize((317, 567), Image.ANTIALIAS)
        icon_reference = ImageTk.PhotoImage(img2)
        self.iconimage = Label(self.background, image=icon_reference)
        self.iconimage.image = icon_reference
        self.iconimage.place(relx=0.26, rely=0)

        self.statuslabel = Label(self.background, fg='#e6e6ff', bg='#00001a', text='Not Connected')
        self.statuslabel.place(relx=0.15, rely=0.974, relwidth=0.125, relheight=0.020)

        self.instruction = Button(self.background, text="Click Here" + "\n" + "For Instructions", fg='#e6e6ff', bg='#00001a', command=lambda: self.instructions())
        self.instruction.place(relx=0.03, rely=0.83, relwidth=0.2, relheight=0.1)

    def instructions(self):
        self.instruction_window = Toplevel(self.master)
        self.app = Tutorial(self.instruction_window)

    def set_icon_button(self, entry):
        global SummonerIcon
        SummonerIcon = entry

        async def set_icon():
            icon = await connector.request('put', '/lol-summoner/v1/current-summoner/icon',
                                           data=dumps({'profileIconId': SummonerIcon}))
            if icon.status == 201:
                await connector.stop_ws()
            else:
                self.statuslabel['text'] = 'Error'
                await connector.stop_ws()

        @connector.event
        async def connect():
            self.statuslabel['text'] = 'Success'
            summoner = await connector.request('get', '/lol-summoner/v1/current-summoner')
            data = await summoner.json()
            await login(None, None, data)

        @connector.ws_events(['/lol-summoner/v1/current-summoner'], event_types=['Update'])
        async def login(typ, uri, data):
            await set_icon()
        connector.listen()
        connector.start()


class Tutorial:
    def __init__(self, master):
        self.master = master
        master.title('Instructions')
        master.iconbitmap('Icon.ico')
        master.resizable(0, 0)
        instructions_canvas = Canvas(master, height=650, width=650)
        instructions_canvas.pack()
        img2 = Image.open("Instruction Background.jpg")
        img2 = img2.resize((1400, 660), Image.ANTIALIAS)
        instructions_bg = ImageTk.PhotoImage(img2)
        instructions_background = Label(master, image=instructions_bg)
        instructions_background.image = instructions_bg
        instructions_background.place(relwidth=1, relheight=1)
        text = Text(instructions_background, fg='#e6e6ff', bg='#00001a', borderwidth=2, relief="groove")
        text.place(relx=0.025, rely=0.27, relwidth=0.95, relheight=0.7)
        text.insert('end', 'YOUR LEAGUE CLIENT MUST BE OPENED AND LOGGED IN FOR THIS TO WORK!!')
        text.insert('end', '\n\n' + '1. Type in the number of the summoner icon you want into the white text box '
                                    'above the "Set Summoner Icon" button' + '\n\n' + '2. Click Set Summoner Icon' 
                                    ' and if it worked the status should changed to' + '\n' + '"success"')
        text.insert('end', '\n' + '----------------------------------------------------------------------------')
        text.insert('end', '\n\n\n' + 'If status still says not connected: ')
        text.insert('end', '\n\n' + '1. You must have a 64 bit OS or it will not work, to check this type in' + '\n'
                    + '"About your PC" in the start menu and it will be under "Device specfications" next to "System type"')
        text.insert('end', '\n\n' + '2. Check the Folder the application is in, there must be a' + '\n'
                    + '"libcrypto-1_1-x64.dll" and a "libssl-1_1-x64.dll" file in there')
        text.insert('end', '\n\n' + 'Still not working, install OpenSSL: https://slproweb.com/products.html '
                    '(Highlight text, CTRL+C to copy, CTRL+V to paste) ')
        text.insert('end', '\n\n' + 'These two issues will be fixed sometime in the future')


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    application = MainWindow(root)
    root.mainloop()