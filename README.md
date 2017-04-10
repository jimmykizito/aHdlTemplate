HDL Project Template
====================

Version 1.0

A template for test-driven (using cocotb) HDL development in both VHDL and Verilog.

Directory structure:
.
├── build
│   ├── verilog
│   └── vhdl
├── doc
├── hdl
│   ├── verilog
│   └── vhdl
├── include
│   ├── verilog
│   └── vhdl
├── lib
│   ├── verilog
│   └── vhdl
├── proj
│   ├── verilog
│   │   ├── libero
│   │   └── xise
│   └── vhdl
│       ├── libero
│       └── xise
├── README.md
├── sw
├── test
│   ├── verilog
│   └── vhdl
└── tools

Initialisation
--------------
- git clone <url> <local_dir>
- run tools/init_py <proj name> -d <local_dir>
- git init
- git remote add origin <url>
- git add .. commit ..
- git push -u origin --all
- Replace this README with something project relevant

Usage
-----
- cd test/<verilog|vhdl>
- make clean
- make test
- gtkwave [sim_build/]waves_tut_sync_logic.vcd

Dependencies
------------
- icarus
- ghdl
- gtkwave

