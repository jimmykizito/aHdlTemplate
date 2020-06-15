TOPLEVEL_LANG = verilog

SIM ?= icarus

PWD = $(shell pwd)
COCOTB ?= /usr/local/src/cocotb.git
export PYTHONPATH := $(PWD)/../:$(PYTHONPATH)

# Top level source
VERILOG_SOURCES = $(PWD)/../../../hdl/verilog/top___proj__.v
# Submodule sources
VERILOG_SOURCES += $(PWD)/../../../hdl/verilog/dff.v
TOPLEVEL = top___proj__

MODULE = test___proj__

include $(shell cocotb-config --makefiles)/Makefile.sim
