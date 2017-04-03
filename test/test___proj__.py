import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure, TestSuccess

@cocotb.test()
def test___proj__(dut):
    """
    <Test description>
    """
    dut._log.info("Test beginning.")

    dut._log.info("Test ending.")

