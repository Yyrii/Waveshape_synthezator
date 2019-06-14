from tkinter import ttk


class ChannelScale(ttk.Scale):
    def __init__(self,parent,orient,initial_pos,beg_of_scale,end_of_scale):
        super().__init__(parent)
        self.pos=initial_pos
        self.pack()
        self.set(initial_pos)
        self.configure(orient=orient)
        self.configure(takefocus="")
        self.configure(from_=beg_of_scale, to=end_of_scale)
        self.configure(command=self.update_pos)

    def set_position(self, position):
            self.pos = position

    def get_position(self):
            return self.pos

    def update_pos(self, val):
            self.set_position(val)