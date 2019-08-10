import visa
import wx
from main_window import MainWindow

class HP3478A:

    self.address = 'GPIB::20::INSTR'

    def __init__(self):
        rm = visa.ResourceManager()
        self.instrument = rm.open_resource(self.address)

    def measure_voltage(self):
        return self.instrument.query("")


app = wx.App()
gpib_dev = HP3478A()
frame = MainWindow(None, gpib_dev)
frame.Show()
app.MainLoop()
