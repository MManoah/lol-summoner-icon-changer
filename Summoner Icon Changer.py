import os
from os.path import isfile, join
from tkinter import *
from tkinter import messagebox
import psutil
from PIL import Image, ImageTk
from json import dumps
from lcu_driver import Connector

Window_Width = 650
Window_Height = 475
connector = Connector()
global SummonerIcon


# Makes a request to set the proper icon by the icon code
def set_icon_button(entry):
    global SummonerIcon
    SummonerIcon = entry

    async def set_icon():
        response = await connector.request('put', '/lol-summoner/v1/current-summoner/icon',
                                           data=dumps({'profileIconId': SummonerIcon}))
        if response.status == 201:
            messagebox.showinfo("Status", "SUCCESS!")
        else:
            messagebox.showerror("Error", "THERE WAS AN ERROR")
        await connector.stop_ws()

    @connector.event
    async def connect():
        await set_icon()

    connector.start()


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title('Summoner Icon Changer - Manoah')
        master.iconbitmap('Background and Icon/Icon.ico')
        canvas = Canvas(master, height=Window_Height, width=Window_Width)
        canvas.pack()

        img = Image.open("Background and Icon/Background.jpg")
        img = img.resize((864, 486), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(img)
        background = Label(master, image=background_image)
        background.image = background_image
        background.place(relwidth=1, relheight=1)
        path = 'Summoner Icon Pictures'  # Summoner Icon Pictures folder
        image_list = [f for f in os.listdir(path) if isfile(join(path, f))]  # Creates a list of the pictures
        relx = 0.05
        rely = 0.05
        for i in range(len(image_list)):
            icon_button = image_list[i]
            icon_button = int(icon_button[:-4])
            placement("{path}/{x}".format(path=path, x=image_list[i]), background, icon_button, relx, rely)
            if (i + 1) % 5 == 0:  # 5 is the number of columns
                relx = 0.05
            else:
                relx += 0.20
            if (i + 1) % 5 == 0:  # When 5 icons have been placed move to the next row
                rely += 0.15


# Places icons on the label called background
def placement(path, background, icon_button, x, y):
    image = Image.open(path)
    image = image.resize((50, 50), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    button = Button(background, image=image, borderwidth=0, highlightthickness=0,
                    command=lambda: set_icon_button(icon_button))
    button.image = image
    button.place(relx=x, rely=y)


# Checks if the league client is open and logged in
def ProcessExists():
    for p in psutil.process_iter():
        try:
            if p.name() == 'LeagueClient.exe':
                return True
        except psutil.Error:
            return False


if __name__ == '__main__':
    if ProcessExists():
        root = Tk()
        root.resizable(0, 0)
        application = MainWindow(root)
        root.mainloop()
    else:
        messagebox.showerror("Error", "PLEASE LOGIN TO LEAGUE OF LEGENDS")
        exit(0)
