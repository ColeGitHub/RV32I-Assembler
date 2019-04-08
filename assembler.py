#!/usr/bin/env python3

import itypes

class Assembler:

    instructions = {
            "lui": [0b0110111, "u"],
            "auipc": [0b0010111, "u"],
            "jal": [0b1101111, "j"],
            "jalr": [0b1100111, "i"],
            "beq": [0b1100011, "b"],
            "bne": [0b1100011, "b"],
            "blt": [0b1100011, "b"],
            "bge": [0b1100011, "b"],
            "bltu": [0b1100011, "b"],
            "bgeu": [0b1100011, "b"],
            "lb": [0x0000011, "i"],
            "lh": [0x0000011, "i"],
            "lw": [0x0000011, "i"],
            "lbu": [0x0000011, "i"],
            "lhu": [0x0000011, "i"],
            "sb": [0b0100011, "s"],
            "sh": [0b0100011, "s"],
            "sw": [0b0100011, "s"],
            "addi": [0b0010011,"i"],
            "slti": [0b0010011,"i"],
            "sltiu": [0b0010011,"i"],
            "xori": [0b0010011,"i"],
            "ori": [0b0010011,"i"],
            "andi": [0b0010011,"i"],
            "slli": [0b0010011,"i"],
            "srli": [0b0010011,"i"],
            "srai": [0b0010011,"i"],
            "add": [0b0110011, "r"],
            "sub": [0b0110011, "r"],
            "slt": [0b0110011, "r"],
            "sltu": [0b0110011, "r"],
            "xor": [0b0110011, "r"],
            "or": [0b0110011, "r"],
            "and": [0b0110011, "r"],
            "sll": [0b0110011, "r"],
            "srl": [0b0110011, "r"],
            "sra": [0b0110011, "r"],
            "fence": [0b0001111, "f"],
            "fence.i": [0b0001111, "f"],
            "ecall": [0b01110011, "c"],
            "ebreak": [0b01110011, "c"],
            "csrrw": [0b01110011, "c"],
            "csrrs": [0b01110011, "c"],
            "csrrc": [0b01110011, "c"],
            "csrrwi": [0b01110011, "c"],
            "csrrsi": [0b01110011, "c"],
            "csrrci": [0b01110011, "c"]
            }

    registers = {
            "zero": 0,
            "ra": 1,
            "sp": 2,
            "gp": 3,
            "tp": 4,
            "t0": 5,
            "t1": 6,
            "t2": 7,
            "s0": 8,
            "s1": 9,
            "a0": 10,
            "a1": 11,
            "a2": 12,
            "a3": 13,
            "a4": 14,
            "a5": 15,
            "a6": 16,
            "a7": 17,
            "s2": 18,
            "s3": 19,
            "s4": 20,
            "s5": 21,
            "s6": 22,
            "s7": 23,
            "s8": 24,
            "s9": 25,
            "s10": 26,
            "s11": 27,
            "t3": 28,
            "t4": 29,
            "t5": 30,
            "t6": 31
            }

    types = itypes.ITypes()

    def convert(self, instr):
        types = self.types
        registers = self.registers
        instructions = self.instructions

        tokens = instr.lstrip().split(None, 1)
        tokens[1] = tokens[1].replace(" ", "").split(",")

        tokens_temp = []
        for token in tokens[1]:

            if token in registers:
                tokens_temp.append(registers[token])
            elif token[0] == "x":
                if len(token) == 2:
                    tokens_temp.append(int(token[1]))
                else:
                    tokens_temp.append( (int(token[1]) * 10) + int(token[2]) )
            else:
                print("Illegal register token")

        tokens[1] = tokens_temp

        # Convert instruction to opcode
        op = tokens[0]
        opcode, instr_type = instructions[tokens[0]]
        args = tokens[1]

        if instr_type == "j":
            return types.j_type(opcode, op, args)
        elif instr_type == "u":
            return types.u_type(opcode, op, args)
        elif instr_type == "b":
            return types.b_type(opcode, op, args)
        elif instr_type == "i":
            return types.i_type(opcode, op, args)
        elif instr_type == "s":
            return types.s_type(opcode, op, args)
        elif instr_type == "r":
            return types.r_type(opcode, op, args)
        elif instr_type == "f":
            return types.f_type(opcode, op, args)
        elif instr_type == "c":
            return types.c_type(opcode, op, args)


