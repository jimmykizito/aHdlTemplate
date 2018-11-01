`default_nettype none
`timescale 1ns/1ns

/*!
 * Module description.
 */
module top___proj__
  // #(
    // parameter _PARAM = DEFAULT_VALUE,
  // )
  (
    // Port declarations
    // input|inout|output i|io|o_port_name,
  );

  // Submodule instantiation
  // submodule_name
    // parameters
    // #(
      // ._PARAM(VALUE),
    //)
    // u_submodule_name (
      // .i|io|o_port_name(signal|port),
    // );

  // Wave dump
  initial begin
    $dumpfile("waves___proj__.vcd");
    // $dumpvars(<level>, <module>);
    // level: 0 >> all, 1 >> top only, 2 >> up to 1 level down
    $dumpvars(0, top___proj__);
  end

endmodule
