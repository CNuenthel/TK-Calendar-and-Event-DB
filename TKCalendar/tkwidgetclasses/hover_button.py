from tkinter import Button


class HoverButton(Button):
    """
    Creates a Tkinter button with hover highlighting

        @:param master: Root window in which button will be created
        @:param **kw: Standard keyword arguments to the Tkinter button

    """
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.default_background = None
        self.active_bg = "#D9F1FF"
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """ Sets default bg and changes bg to active color on mouse entry to widget """
        self.default_background = self["background"]
        if self.default_background != "#808080":  # Here we use #808080 as a standard "inactive" color
            self["background"] = self.active_bg

    def on_leave(self, e):
        """ Returns default bg on mouse exit of widget """
        self["background"] = self.default_background

