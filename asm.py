#!/usr/bin/env python3

import assembler

def main():
    asm = assembler.Assembler()

    r_list = [
            "add x10, x11, x12",
            "sub x10, x11, x12",
            "sll x10, x11, x12",
            "slt x10, x11, x12",
            "sltu x10, x11, x12",
            "xor x10, x11, x12",
            "srl x10, x11, x12",
            "sra x10, x11, x12",
            "or x10, x11, x12",
            "and x10, x11, x12" ]

    j_list = [
            "jal ra, 524287",
            "jal ra, 339064",
            "jal ra, -524288",
            "jal ra, -524289",
            "jalr ra, a0, 2047",
            "jalr ra, a0, 2048",
            "jalr ra, a0, -2048",
            "jalr ra, a0, -2049"
            ]

    b_list = [
            "beq a0, a1, 4",
            "bne a0, a1, 4",
            "blt a0, a1, 4",
            "bge a0, a1, 4",
            "bltu a0, a1, 4",
            "bgeu a0, a1, 4"
            ]

    l_list = [
            "lb a0, a1, 4",
            "lh a0, a1, 4",
            "lw a0, a1, 4",
            "lbu a0, a1, 4",
            "lhu a0, a1, 4"
            ]

    s_list = [
            "sb a0, a1, 2201",
            "sh a0, a1, 2201",
            "sw a0, a1, 2201"
            ]

    i_list = [
            "addi x10, x11, 29",
            "slli x10, x11, 29",
            "slti x10, x11, 29",
            "sltiu x10, x11, 29",
            "xori x10, x11, 29",
            "srli x10, x11, 29",
            "srai x10, x11, 29",
            "ori x10, x11, 29",
            "andi x10, x11, 29" ]

    for instr in instr_list:
        print(instr)
        print(hex(asm.convert(instr) & 0xFFFFFFFF))


if __name__ == "__main__":
    main()
