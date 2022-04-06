from tkinter.ttk import Combobox, Style
from tkinter import Tk, Toplevel


class NumberOnlyCombobox(Combobox):
    """
    Creates a TTK Combobox that accepts only numbers

    ...
    Parameters
    ----------
    master: Tk or Toplevel
        Root window in which button will be created
    base_value: str or int
        Original value set for combobox
    max_length : int = None
        max length a selection or manual input can be if specified
    **kw: dict
        Standard keyword arguments to the TTkinter combobox

    """

    def __init__(self, master: Tk or Toplevel, base_value: str or int, max_length: int = None, **kw):
        """ Constructs a Tkinter Entry """
        super().__init__(master=master, **kw)
        self.style = Style()
        self.style.theme_use("clam")
        self.max_length = max_length
        self.base_value = base_value

        self.bind("<FocusOut>", self._check_value)

    def set_style(self, fbg: str, bg: str):
        self.style.configure("TCombobox", fieldbackground=fbg, background=bg)

    def _check_value(self, e):
        """ Verifies integer value input and max length if filled """
        try:
            int(self.get())
        except ValueError:
            self.set(self.base_value)

        if self.max_length:
            if len(self.get()) > self.max_length:
                self.set(self.base_value)


