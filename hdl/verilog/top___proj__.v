// Timescale declaration necessary for simulation.
`timescale 1ns/1ns

module top__proj__ (
    // Port declarations
    // input|inout|output p_i|io|o_NAME,
  );

  // Submodule instantiation
  // submodule_name
    // parameters
    // # (
      // .g_PARAM(VALUE)
    //)
    // i_submodule_name (
      // .p_i|io|o_SUB_NAME(signal|port),
    // );

  // Wave dump
  initial begin
    $dumpfile("waves__proj__.vcd");
    // $dumpvars(<level>, <module>);
    // level: 0 >> all, 1 >> top only, 2 >> up to 1 level down
    $dumpvars(0, top__proj__);
  end

endmodule

