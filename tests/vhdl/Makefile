TOPLEVEL_LANG=vhdl

SIM?=ghdl
SIM_ARGS?="--vcd=waves___proj__.vcd"

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top-level source
VHDL_SOURCES=$(PWD)/../../hdl/vhdl/top___proj__.vhd
# Submodule sources
#VHDL_SOURCES+=$(PWD)/../../hdl/vhdl/<submodule>.vhd
TOPLEVEL=top___proj__

MODULE=test___proj__

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

