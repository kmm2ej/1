import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge

@cocotb.test()
async def test_bit_shift(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.r.value = 1  # Using 'r' to match Verilog reset signal
    await ClockCycles(dut.clk, 10)
    dut.r.value = 0

    previous_value = 0b00000000
    for i in range(1, 256):  # Test through multiple shift cycles
        await RisingEdge(dut.clk)
        current_value = int(dut.out.value)
        expected_value = ((previous_value & 0x7f) << 1) | (~(previous_value >> 7) & 0x01)
        assert current_value == expected_value, f"Failed at cycle {i}: {current_value:08b} != {expected_value:08b}"
        previous_value = current_value
        dut._log.info(f"Cycle {i}: out={current_value:08b}")
