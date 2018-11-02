HDL Project Template
====================

Version 1.1

A template for test-driven HDL development in both VHDL and Verilog.

Directory structure - many are still unused and may be removed in later
releases:
```
<root_dir>
|-- build
|-- docs
|-- hdl                     # HDL source files
    |-- verilog
    |-- vhdl
|-- include
|-- lib
|-- proj
|-- README.md
|-- sw
|-- tests                   # Test source files
    |-- cocotb
        |-- __proj__        # Python module for Cocotb tests
        |-- verilog
        |-- vhdl
|-- tools
```

Initialisation
--------------
This will replace the template text `__proj__` throughout the project with the
`project_name` (lower case with spaces replaced by underscores) and rename the
`<root_dir>` to `aProjectName` (camel case with 'a' prepended).

```
git clone <template_repo> <root_dir>
cd <root_dir>
run tools/init_py <"proj name in quotes"> [-d <root_dir>]
git init
git remote add origin <project_repo>
git add ...
git commit ...
git push -u origin --all
```

Replace this README with something project relevant.

Usage
-----
Once the project has been initialised, it should be possible to run the DFF
(D-type flip-flop) test using [Cocotb](https://cocotb.readthedocs.io).

```
cd test/cocotb/<verilog|vhdl>
make clean
make
gtkwave [sim_build/]waves_tut_sync_logic.[vcd/ghw]
```

Dependencies
------------
- icarus
- ghdl
- gtkwave
- rename
