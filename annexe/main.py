from tkinter import *

from hamming import *


def encode(text: str, label: Label) -> str:
    """Convert a text into a Hamming code and return it as a string."""
    label['text'] = ""
    code = text_to_hamming(text)
    return ''.join([str(i) for i in code])


def decode(code: str, label: Label) -> str:
    label['text'] = ""
    data = []
    code = code.replace(' ', '').replace('\n', '')
    for c in code:
        if c == '0':
            data.append(0)
        elif c == '1':
            data.append(1)
        else:
            label['text'] = "Invalid input"
            return ""
    try:
        return hamming_code_to_text(data)
    except UnicodeDecodeError:
        label['text'] = "Invalid input"
        return ""


if __name__ == '__main__':
    window = Tk()
    window.title("Hamming (en|de)coder")
    window.geometry('500x500')
    window.wm_resizable(width=False, height=False)

    main = Frame(window)
    left = Frame(main)
    right = Frame(main)
    bottom = Frame(window)

    left_text_area = Text(left, height=10, width=30)
    right_text_area = Text(right, height=10, width=30)

    message = Label(bottom, text="")
    encode_button = Button(
        bottom, text="Encode",
        command=lambda: right_text_area.replace(
            index1=1.0, index2=END,
            chars=encode(left_text_area.get(1.0, END), message)
        )
    )
    decode_button = Button(
        bottom, text="Decode",
        command=lambda: left_text_area.replace(
            index1=1.0, index2=END,
            chars=decode(right_text_area.get(1.0, END), message)
        )
    )

    main.pack(side=TOP, fill=BOTH, expand=True)
    left.pack(side=LEFT, fill=BOTH, expand=True)
    right.pack(side=RIGHT, fill=BOTH, expand=True)
    bottom.pack(side=BOTTOM, fill=BOTH)

    left_text_area.pack(side=TOP, fill=BOTH, expand=True)
    right_text_area.pack(side=TOP, fill=BOTH, expand=True)

    encode_button.pack(side=LEFT, fill=BOTH, expand=True)
    message.pack(side=LEFT, fill=BOTH, expand=True)
    decode_button.pack(side=RIGHT, fill=BOTH, expand=True)

    window.mainloop()
