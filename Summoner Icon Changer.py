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

        blank_img = Image.open("Summoner Icon Pictures/Blank_Icon.jpg")
        blank_img = blank_img.resize((50, 50), Image.ANTIALIAS)
        blank_img = ImageTk.PhotoImage(blank_img)
        blank_button = Button(background, image=blank_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(29))
        blank_button.image = blank_img
        blank_button.place(relx=0.05, rely=0.05)

        alistar_img = Image.open("Summoner Icon Pictures/alistar_icon.jpg")
        alistar_img = alistar_img.resize((50, 50), Image.ANTIALIAS)
        alistar_img = ImageTk.PhotoImage(alistar_img)
        alistar_button = Button(background, image=alistar_img, borderwidth=0, command=lambda: set_icon_button(59))
        alistar_button.image = alistar_img
        alistar_button.place(relx=0.25, rely=0.05)

        gangplank_img = Image.open("Summoner Icon Pictures/gangplank_icon.jpg")
        gangplank_img = gangplank_img.resize((50, 50), Image.ANTIALIAS)
        gangplank_img = ImageTk.PhotoImage(gangplank_img)
        gangplank_button = Button(background, image=gangplank_img, borderwidth=0,
                                  command=lambda: set_icon_button(69))
        gangplank_button.image = gangplank_img
        gangplank_button.place(relx=0.45, rely=0.05)

        kayle_img = Image.open("Summoner Icon Pictures/kayle_icon.jpg")
        kayle_img = kayle_img.resize((50, 50), Image.ANTIALIAS)
        kayle_img = ImageTk.PhotoImage(kayle_img)
        kayle_button = Button(background, image=kayle_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(50))
        kayle_button.image = kayle_img
        kayle_button.place(relx=0.65, rely=0.05)

        eve_img = Image.open("Summoner Icon Pictures/eve_icon.jpg")
        eve_img = eve_img.resize((50, 50), Image.ANTIALIAS)
        eve_img = ImageTk.PhotoImage(eve_img)
        eve_button = Button(background, image=eve_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(60))
        eve_button.image = eve_img
        eve_button.place(relx=0.85, rely=0.05)

        ezreal_img = Image.open("Summoner Icon Pictures/ezreal_icon.jpg")
        ezreal_img = ezreal_img.resize((50, 50), Image.ANTIALIAS)
        ezreal_img = ImageTk.PhotoImage(ezreal_img)
        ezreal_button = Button(background, image=ezreal_img, borderwidth=0, highlightthickness=0,
                               command=lambda: set_icon_button(70))
        ezreal_button.image = ezreal_img
        ezreal_button.place(relx=0.05, rely=0.20)

        morg_img = Image.open("Summoner Icon Pictures/morgana_icon.jpg")
        morg_img = morg_img.resize((50, 50), Image.ANTIALIAS)
        morg_img = ImageTk.PhotoImage(morg_img)
        morg_button = Button(background, image=morg_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(51))
        morg_button.image = morg_img
        morg_button.place(relx=0.25, rely=0.20)

        tf_img = Image.open("Summoner Icon Pictures/tf_icon.jpg")
        tf_img = tf_img.resize((50, 50), Image.ANTIALIAS)
        tf_img = ImageTk.PhotoImage(tf_img)
        tf_button = Button(background, image=tf_img, borderwidth=0, highlightthickness=0,
                           command=lambda: set_icon_button(61))
        tf_button.image = tf_img
        tf_button.place(relx=0.45, rely=0.20)

        cait_img = Image.open("Summoner Icon Pictures/caitlyn_icon.jpg")
        cait_img = cait_img.resize((50, 50), Image.ANTIALIAS)
        cait_img = ImageTk.PhotoImage(cait_img)
        cait_button = Button(background, image=cait_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(71))
        cait_button.image = cait_img
        cait_button.place(relx=0.65, rely=0.20)

        idk_img = Image.open("Summoner Icon Pictures/idk_icon.jpg")
        idk_img = idk_img.resize((50, 50), Image.ANTIALIAS)
        idk_img = ImageTk.PhotoImage(idk_img)
        idk_button = Button(background, image=idk_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(52))
        idk_button.image = idk_img
        idk_button.place(relx=0.85, rely=0.20)

        akali_img = Image.open("Summoner Icon Pictures/akali_icon.jpg")
        akali_img = akali_img.resize((50, 50), Image.ANTIALIAS)
        akali_img = ImageTk.PhotoImage(akali_img)
        akali_button = Button(background, image=akali_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(62))
        akali_button.image = akali_img
        akali_button.place(relx=0.05, rely=0.35)

        nasus_img = Image.open("Summoner Icon Pictures/nasus_icon.jpg")
        nasus_img = nasus_img.resize((50, 50), Image.ANTIALIAS)
        nasus_img = ImageTk.PhotoImage(nasus_img)
        nasus_button = Button(background, image=nasus_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(72))
        nasus_button.image = nasus_img
        nasus_button.place(relx=0.25, rely=0.35)

        vlad_img = Image.open("Summoner Icon Pictures/vlad_icon.jpg")
        vlad_img = vlad_img.resize((50, 50), Image.ANTIALIAS)
        vlad_img = ImageTk.PhotoImage(vlad_img)
        vlad_button = Button(background, image=vlad_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(53))
        vlad_button.image = vlad_img
        vlad_button.place(relx=0.45, rely=0.35)

        shen_img = Image.open("Summoner Icon Pictures/shen_icon.jpg")
        shen_img = shen_img.resize((50, 50), Image.ANTIALIAS)
        shen_img = ImageTk.PhotoImage(shen_img)
        shen_button = Button(background, image=shen_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(63))
        shen_button.image = shen_img
        shen_button.place(relx=0.65, rely=0.35)

        olaf_img = Image.open("Summoner Icon Pictures/olaf_icon.jpg")
        olaf_img = olaf_img.resize((50, 50), Image.ANTIALIAS)
        olaf_img = ImageTk.PhotoImage(olaf_img)
        olaf_button = Button(background, image=olaf_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(73))
        olaf_button.image = olaf_img
        olaf_button.place(relx=0.85, rely=0.35)

        sona_img = Image.open("Summoner Icon Pictures/sona_icon.jpg")
        sona_img = sona_img.resize((50, 50), Image.ANTIALIAS)
        sona_img = ImageTk.PhotoImage(sona_img)
        sona_button = Button(background, image=sona_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(54))
        sona_button.image = sona_img
        sona_button.place(relx=0.05, rely=0.50)

        xin_img = Image.open("Summoner Icon Pictures/xin_icon.jpg")
        xin_img = xin_img.resize((50, 50), Image.ANTIALIAS)
        xin_img = ImageTk.PhotoImage(xin_img)
        xin_button = Button(background, image=xin_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(64))
        xin_button.image = xin_img
        xin_button.place(relx=0.25, rely=0.50)

        leblanc_img = Image.open("Summoner Icon Pictures/leblanc_icon.jpg")
        leblanc_img = leblanc_img.resize((50, 50), Image.ANTIALIAS)
        leblanc_img = ImageTk.PhotoImage(leblanc_img)
        leblanc_button = Button(background, image=leblanc_img, borderwidth=0, highlightthickness=0,
                                command=lambda: set_icon_button(74))
        leblanc_button.image = leblanc_img
        leblanc_button.place(relx=0.45, rely=0.50)

        lux_img = Image.open("Summoner Icon Pictures/lux_icon.jpg")
        lux_img = lux_img.resize((50, 50), Image.ANTIALIAS)
        lux_img = ImageTk.PhotoImage(lux_img)
        lux_button = Button(background, image=lux_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(55))
        lux_button.image = lux_img
        lux_button.place(relx=0.65, rely=0.50)

        kat_img = Image.open("Summoner Icon Pictures/kat_icon.jpg")
        kat_img = kat_img.resize((50, 50), Image.ANTIALIAS)
        kat_img = ImageTk.PhotoImage(kat_img)
        kat_button = Button(background, image=kat_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(65))
        kat_button.image = kat_img
        kat_button.place(relx=0.85, rely=0.50)

        rat_img = Image.open("Summoner Icon Pictures/rat_icon.jpg")
        rat_img = rat_img.resize((50, 50), Image.ANTIALIAS)
        rat_img = ImageTk.PhotoImage(rat_img)
        rat_button = Button(background, image=rat_img, borderwidth=0, highlightthickness=0,
                            command=lambda: set_icon_button(76))
        rat_button.image = rat_img
        rat_button.place(relx=0.05, rely=0.65)

        trynd_img = Image.open("Summoner Icon Pictures/trynd_icon.jpg")
        trynd_img = trynd_img.resize((50, 50), Image.ANTIALIAS)
        trynd_img = ImageTk.PhotoImage(trynd_img)
        trynd_button = Button(background, image=trynd_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(56))
        trynd_button.image = trynd_img
        trynd_button.place(relx=0.25, rely=0.65)

        bush_img = Image.open("Summoner Icon Pictures/bush_icon.jpg")
        bush_img = bush_img.resize((50, 50), Image.ANTIALIAS)
        bush_img = ImageTk.PhotoImage(bush_img)
        bush_button = Button(background, image=bush_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(66))
        bush_button.image = bush_img
        bush_button.place(relx=0.45, rely=0.65)

        mf_img = Image.open("Summoner Icon Pictures/mf_icon.jpg")
        mf_img = mf_img.resize((50, 50), Image.ANTIALIAS)
        mf_img = ImageTk.PhotoImage(mf_img)
        mf_button = Button(background, image=mf_img, borderwidth=0, highlightthickness=0,
                           command=lambda: set_icon_button(77))
        mf_button.image = mf_img
        mf_button.place(relx=0.65, rely=0.65)

        rammus_img = Image.open("Summoner Icon Pictures/rammus_icon.jpg")
        rammus_img = rammus_img.resize((50, 50), Image.ANTIALIAS)
        rammus_img = ImageTk.PhotoImage(rammus_img)
        rammus_button = Button(background, image=rammus_img, borderwidth=0, highlightthickness=0,
                               command=lambda: set_icon_button(57))
        rammus_button.image = rammus_img
        rammus_button.place(relx=0.85, rely=0.65)

        lux2_img = Image.open("Summoner Icon Pictures/lux2_icon.jpg")
        lux2_img = lux2_img.resize((50, 50), Image.ANTIALIAS)
        lux2_img = ImageTk.PhotoImage(lux2_img)
        lux2_button = Button(background, image=lux2_img, borderwidth=0, highlightthickness=0,
                             command=lambda: set_icon_button(67))
        lux2_button.image = lux2_img
        lux2_button.place(relx=0.05, rely=0.80)

        renekton_img = Image.open("Summoner Icon Pictures/renekton_icon.jpg")
        renekton_img = renekton_img.resize((50, 50), Image.ANTIALIAS)
        renekton_img = ImageTk.PhotoImage(renekton_img)
        renekton_button = Button(background, image=renekton_img, borderwidth=0, highlightthickness=0,
                                 command=lambda: set_icon_button(78))
        renekton_button.image = renekton_img
        renekton_button.place(relx=0.25, rely=0.80)

        yi_img = Image.open("Summoner Icon Pictures/yi_icon.jpg")
        yi_img = yi_img.resize((50, 50), Image.ANTIALIAS)
        yi_img = ImageTk.PhotoImage(yi_img)
        yi_button = Button(background, image=yi_img, borderwidth=0, highlightthickness=0,
                           command=lambda: set_icon_button(58))
        yi_button.image = yi_img
        yi_button.place(relx=0.45, rely=0.80)

        vayne_img = Image.open("Summoner Icon Pictures/vayne_icon.jpg")
        vayne_img = vayne_img.resize((50, 50), Image.ANTIALIAS)
        vayne_img = ImageTk.PhotoImage(vayne_img)
        vayne_button = Button(background, image=vayne_img, borderwidth=0, highlightthickness=0,
                              command=lambda: set_icon_button(68))
        vayne_button.image = vayne_img
        vayne_button.place(relx=0.65, rely=0.80)

        w_img = Image.open("Summoner Icon Pictures/w_icon.jpg")
        w_img = w_img.resize((50, 50), Image.ANTIALIAS)
        w_img = ImageTk.PhotoImage(w_img)
        w_button = Button(background, image=w_img, borderwidth=0, highlightthickness=0,
                               command=lambda: set_icon_button(75))
        w_button.image = w_img
        w_button.place(relx=0.85, rely=0.80)


def process_exists():
    for p in psutil.process_iter():
        try:
            if p.name() == 'LeagueClient.exe':
                return True
        except psutil.Error:
            return False


if __name__ == '__main__':
    if process_exists():
        root = Tk()
        root.resizable(0, 0)
        application = MainWindow(root)
        root.mainloop()
    else:
        messagebox.showerror("Error", "PLEASE LOGIN TO LEAGUE OF LEGENDS")
        exit(0)
