TOPLEVEL_LANG=vhdl

SIM?=ghdl
SIM_ARGS?="--waves=waves___proj__.ghw"

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top-level source
VHDL_SOURCES=$(PWD)/../../../hdl/vhdl/top___proj__.vhd
# Submodule sources
VHDL_SOURCES+=$(PWD)/../../../hdl/vhdl/dff.vhd
TOPLEVEL=top___proj__

MODULE=test___proj__

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
