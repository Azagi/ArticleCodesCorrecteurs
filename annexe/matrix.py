import math
import random
from tkinter import Frame, Label

import hamming


def calculate_parity(data: list[int]) -> list[int]:
    b = hamming.required_parity_bits(len(data))
    bits = [0] + [1 << i for i in range(b - 1)]
    for i in range(len(data)):
        for b in bits:
            if b == 0 or b & i != 0:
                data[b] ^= data[i]
    return data


class Matrix:
    cases = []
    current = 0
    bits = [1, 2, 4, 8]
    parity_bits = [None, None, None, None]

    def __init__(self, frame: Frame) -> None:
        """Crée une matrice de Hamming de taille 4x4"""
        self.frame = frame
        self.data = calculate_parity([random.choice([0, 1]) for _ in range(16)])
        n = random.randint(1, len(self.data) - 1)
        self.data[n] ^= 1
        for i in range(len(self.data)):
            self.cases.append(
                Label(
                    frame, text=self.data[i],
                    width=0, height=0, padx=15, pady=15,
                    border=1.0, relief="solid",
                    font=("Courier", 20),
                    fg="orange" if i in self.bits else "black",
                    bg="#06A3D4"
                ))
        self.cases[0].configure(fg="black")
        self.cases[0].configure(bg="white")
        self.__update()

    def __update_current_parity_bit(self):
        if self.current < len(self.bits):
            self.cases[self.bits[self.current]].configure(fg="black")
            self.cases[self.bits[self.current]].configure(bg="orange")

    def __update_cases(self):
        for (i, case) in enumerate(self.cases):
            for (bit, correct) in zip(self.bits, self.parity_bits):
                if correct is None:
                    continue
                elif correct and i & bit != 0:
                    case.configure(bg="white")
                elif not correct and i & bit == 0:
                    case.configure(bg="white")
                if i == bit:
                    case.configure(fg="green" if correct else "red")

    def __update(self):
        self.__update_cases()
        self.__update_current_parity_bit()

    def set_parity_bit(self, is_correct: bool) -> None:
        """Définit si le bit actuel est correct ou non"""
        if self.current < len(self.bits):
            self.parity_bits[self.current] = is_correct
            current_bit = self.bits[self.current]
            if is_correct:
                self.cases[current_bit].configure(fg="green")
            else:
                self.cases[current_bit].configure(fg="red")
            self.cases[current_bit].configure(bg="#06A3D4")
            self.current += 1
        self.__update()

    def __reset(self):
        for (i, case) in enumerate(self.cases):
            case.configure(bg="#06A3D4")
            case.configure(fg="orange" if i in self.bits else "black")

    def undo(self):
        """Annule la dernière action"""
        if self.current > 0:
            if self.current < len(self.bits):
                self.cases[self.bits[self.current]].configure(fg="black")
                self.cases[self.bits[self.current]].configure(bg="#06A3D4")
            self.current -= 1
            self.parity_bits[self.current] = None
            self.__reset()
            self.__update()

    def pack(self, side):
        for i in range(len(self.cases)):
            row = math.floor(i // 4)
            column = i % 4
            self.cases[i].grid(row=row, column=column)
        self.frame.pack(side=side, expand=True)

    def check(self) -> bool:
        """Vérifie si le joueur a bien trouvé l'erreur"""
        error = 0
        for i in range(len(self.parity_bits)):
            if self.parity_bits[i] is None:
                raise Exception("Not all parity bits have been checked")
            if not self.parity_bits[i]:
                error |= self.bits[i]
        return error == hamming.find_error(self.data)
