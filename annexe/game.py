from tkinter import *

from matrix import Matrix


def check_if_correct(m: Matrix, label: Label) -> None:
    """Vérifie si le joueur à trouver l'erreur et affiche un message."""
    try:
        ok = m.check()
    except Exception:
        label['text'] = "Vous devez marquer tous les bits de parité."
        label['fg'] = "red"
        return
    if ok:
        label['text'] = "Correcte"
        label['fg'] = 'green'
    else:
        label['text'] = "Incorrecte"
        label['fg'] = 'red'


def set_parity_bit(m: Matrix, is_correct: bool, label: Label) -> None:
    m.set_parity_bit(is_correct)
    label['text'] = ""
    label['fg'] = 'black'


def undo(m: Matrix, label: Label) -> None:
    m.undo()
    label['text'] = ""
    label['fg'] = 'black'


if __name__ == '__main__':
    window = Tk()
    window.title("Find the error")
    window.geometry('500x500')
    window.wm_resizable(width=False, height=False)

    m = Matrix(frame=Frame(window))
    m.pack(LEFT)

    right = Frame(window)

    Label(
        right,
        text="Vous devez marquer tous les bits de parité comme correct ou incorrect, quand vous avez fini, "
             "cliquez sur le bouton confirmer",
        wraplength=250,
        justify=LEFT,
    ).pack(side=TOP)

    result = Label(right, text="", font=("Courier", 12), wraplength=250, justify=LEFT)
    result.pack(side=TOP)

    frame = Frame(right)
    Button(
        frame,
        text="Correcte",
        command=lambda: set_parity_bit(m, True, result)
    ).pack(side=LEFT)
    Button(
        frame,
        text="Incorrecte",
        command=lambda: set_parity_bit(m, False, result)
    ).pack(side=RIGHT)
    frame.pack(side=TOP)

    Button(
        right,
        text="Annuler",
        command=lambda: undo(m, result)
    ).pack(side=LEFT)
    Button(
        right,
        text="Confirm",
        command=lambda: check_if_correct(m, result)
    ).pack(side=RIGHT)
    right.pack(side=RIGHT, expand=True)

    window.mainloop()
