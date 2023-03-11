import io
import tkinter
from urllib.request import urlopen
from PIL import ImageTk, Image
from tkinter import Tk, ttk, messagebox
import pypokedex


def poke_load(query):
    try:
        pokemon = pypokedex.get(name=query)
        # poke name
        poke_name.config(text=f"{pokemon.name.capitalize()}", relief="flat", anchor="center", font="Fixedsys 20", fg="black")

        # poke type
        if len(pokemon.types) == 1:
            poke_type.config(text=f"{pokemon.types[0].capitalize()}", relief="flat", anchor="center", font="Ivy 10 bold", fg="black")
        else:
            poke_type.config(text=f"{pokemon.types[0].capitalize()}, {pokemon.types[1].capitalize()}", relief="flat", anchor="center", font="Ivy 10 bold", fg="black")

        # poke id
        poke_id.config(text=f"#{pokemon.dex}", relief="flat", anchor="center", font="Ivy 10 bold", fg="black")

        # poke ability
        if len(pokemon.abilities) == 1:
            poke_ability.config(text=f"{pokemon.abilities[0].name.capitalize()}", bg="#CBC3E3", font="Fixedsys 14", relief="flat", anchor="center", justify="left")
        elif len(pokemon.abilities) == 2:
            poke_ability.config(text=f"{pokemon.abilities[0].name.capitalize()}\n{pokemon.abilities[1].name.capitalize()}", bg="#CBC3E3", font="Fixedsys 14", relief="flat", anchor="center",
                                justify="left")
        else:
            poke_ability.config(text=f"{pokemon.abilities[0].name.capitalize()}\n{pokemon.abilities[1].name.capitalize()}\n{pokemon.abilities[2].name.capitalize()}", bg="#CBC3E3", font="Fixedsys 14",
                                relief="flat", anchor="center", justify="left")

        # render pokemon image
        raw = urlopen(pokemon.sprites.front["default"]).read()
        img = Image.open(io.BytesIO(raw)).resize((238, 238))
        img = ImageTk.PhotoImage(img)
        poke_img.config(image=img)
        poke_img.image = img

        # poke stats
        poke_hp.config(text=f"HP: {pokemon.base_stats.hp}", relief="flat", anchor="center", font="Fixedsys 14", fg="black", bg="#CBC3E3")
        poke_height.config(text=f"Height: {pokemon.height}", relief="flat", anchor="center", font="Fixedsys 14", fg="black")
        poke_weight.config(text=f"Weight: {pokemon.weight}", relief="flat", anchor="center", font="Fixedsys 14", fg="black")
        poke_atk.config(text=f"Attack: {pokemon.base_stats.attack}", relief="flat", anchor="center", font="Fixedsys 14", fg="black")

        # clear search field
        poke_search.delete("1.0", "end")
    except Exception as er:
        messagebox.showerror("Error", str(er))
        poke_search.delete("1.0", "end")


def poke_next(now):
    now = int(now.replace("#", ""))
    poke_load(str(now + 1))


def poke_prv(now):
    now = int(now.replace("#", ""))
    poke_load(str(now - 1))


screen = Tk()
screen.title("Pokedex")
screen.geometry("550x440")
screen.configure(bg="#CBC3E3")
screen.iconphoto(False, tkinter.PhotoImage(file="icon.png"))

ttk.Separator(screen, orient="horizontal").grid(row=0, columnspan=1, ipadx=272)
style = ttk.Style(screen)
style.theme_use("clam")

# frame
frame = tkinter.Frame(screen, width=550, height=290, relief="flat", bg="#CBC3E3")
frame.grid(row=1, column=0)

# poke name
poke_name = tkinter.Label(frame, bg="#CBC3E3")
poke_name.place(x=12, y=15)

# poke type
poke_type = tkinter.Label(frame, bg="#CBC3E3")
poke_type.place(x=12, y=50)

# poke id
poke_id = tkinter.Label(frame, bg="#CBC3E3")
poke_id.place(x=12, y=75)

# poke abilities
poke_title = tkinter.Label(frame, text="Abilities", bg="#CBC3E3", font="Fixedsys 20", relief="flat", anchor="center", fg="black")
poke_title.place(x=370, y=15)
poke_ability = tkinter.Label(frame, bg="#CBC3E3")
poke_ability.place(x=370, y=50)

# poke stats
poke_stats = tkinter.Label(screen, text=f"Stats", relief="flat", anchor="center", font="Fixedsys 20", fg="black", bg="#CBC3E3")
poke_stats.place(x=15, y=310)
poke_hp = tkinter.Label(screen, bg="#CBC3E3")
poke_hp.place(x=15, y=350)
poke_height = tkinter.Label(screen, bg="#CBC3E3")
poke_height.place(x=15, y=369)
poke_weight = tkinter.Label(screen, bg="#CBC3E3")
poke_weight.place(x=15, y=389)
poke_atk = tkinter.Label(screen, bg="#CBC3E3")
poke_atk.place(x=15, y=407)

# poke img
poke_img = tkinter.Label(frame, bg="#CBC3E3")
poke_img.place(x=120, y=40)
poke_img.lower()

# search pokémon
poke_search = tkinter.Text(screen, font="Fixedsys 14", fg="black", border=2, width=15, height=1)
poke_search.place(x=300, y=320)
poke_btn = tkinter.Button(screen, text="Search", font="Fixedsys 14", fg="black", height=1, command=lambda: poke_load(poke_search.get(1.0, "end-1c")))
poke_btn.place(x=450, y=317.5)
poke_nxt = tkinter.Button(screen, text="Next", font="Fixedsys 14", fg="black", height=1, command=lambda: poke_next(poke_id.cget("text")))
poke_prev = tkinter.Button(screen, text="Prev", font="Fixedsys 14", fg="black", height=1, command=lambda: poke_prv(poke_id.cget("text")))
poke_prev.place(x=300, y=350)
poke_nxt.place(x=370, y=350)

screen.mainloop()
