#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *
from ula_modules import *
import sys

sys.path.insert(0, "../1-comb/")
from comb_modules import bin2hex


@block
def toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5):
    sw = [SW(i) for i in range(10)]
    key = [KEY(i) for i in range(10)]
    ledr_s = [Signal(bool()) for i in range(10)]
    ledr_bin = ConcatSignal(*reversed(ledr_s))

    # --=======================================--
    # INSTANCE
    # --=======================================--
    ic1 = adder(sw[0:4], sw[6:10], ledr_s[0:4], ledr_s[9])
    ic2 = bin2hex(HEX0, ledr_bin)

    @always_comb
    def comb():
        for i in range(len(ledr_s)):
            LEDR[i].next = ledr_s[i]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
top = toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5)
top.convert(hdl="verilog")
