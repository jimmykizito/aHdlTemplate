TOPLEVEL_LANG = verilog

SIM?=icarus

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top level source
VERILOG_SOURCES=$(PWD)/../../hdl/verilog/top__proj__.v
# Submodule sources
#VERILOG_SOURCES+=$(PWD)/../../hdl/verilog/<submodule>.v
TOPLEVEL=top__proj__

MODULE=test__proj__

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

