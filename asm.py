#!/usr/bin/env python3

import assembler

def main():
    asm = assembler.Assembler()

    instr_list = [
            "add a0, a1, a2",
            "sub a0, a1, a2",
            "sll a0, a1, a2",
            "slt a0, a1, a2",
            "sltu a0, a1, a2",
            "xor a0, a1, a2",
            "srl a0, a1, a2",
            "sra a0, a1, a2",
            "or a0, a1, a2",
            "and a0, a1, a2" ]

    for instr in instr_list:
        print(instr)
        print(asm.convert(instr))


if __name__ == "__main__":
    main()
