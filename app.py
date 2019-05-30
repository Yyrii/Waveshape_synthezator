from interface.widgets import MasterPage
import tkinter as tk
from ttkthemes import ThemedTk

if __name__ == '__main__':
    root = ThemedTk(theme="clearlooks")
    # root.geometry('300x300')

    a = MasterPage(root)
    root.mainloop()