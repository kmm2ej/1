/*
 * tt_um_factory_test.v
 *
 * Test user module
 *
 * Author: Sylvain Munaut <tnt@246tNt.com>
 */

`default_nettype none

module tt_um_factory_test (clk, r, out);

parameter size=7;
input clk;
input r;
output [0:size]out;

reg [0:size]out;

always @ (posedge clk or posedge r)
	begin
		if (r) 
			out= 8'b0000_0000;
		else
			out={~out[size],out[0:size-1]};   
	end

endmodule




