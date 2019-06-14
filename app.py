from interface.widgets import MasterPage
from ttkthemes import ThemedTk

if __name__ == '__main__':
    root = ThemedTk(theme="radiance")
    root.geometry("1200x700")
    # root.resizable(0, 0)
    MasterPage(root)
    root.mainloop()