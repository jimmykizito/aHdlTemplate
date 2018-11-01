import cocotb

from __proj__.__proj___drv import __Proj__Driver
from __proj__.__proj___mdl import __Proj__Model
from __proj__.__proj___mon import __Proj__MonitorIn, __Proj__MonitorOut
from __proj__.__proj___sb import __Proj__ScoreBoard

class __Proj__Testbench:
    """
    Houses cocotb test components.

    - Monitor captures simulation input and output.
    - Model uses captured input to produce expected output from Python model of
    DUT.
    - Scoreboard compares captured output from simulation to expected output
    model.
    """

    def __init__(self, dut, **kwargs):
        self.dut = dut
        #self.attr = kwargs.get("name of arg")

        self.exp_out = []
        self._mdl = __Proj__Model(self.dut, exp_out=self.exp_out)

        self._mon_in = __Proj__MonitorIn(self.dut, "dff_in",
                                        callback=self._mdl.callback)

        self._mon_out = __Proj__MonitorOut(self.dut, "dff_out")

        self.sb = __Proj__ScoreBoard(self.dut)
        self.sb.add_interface(self._mon_out, self.exp_out)

        self.drv = __Proj__Driver(self.dut)
