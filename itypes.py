#!/usr/bin/env python3

class ITypes:

    branch_dict = {
            "beq": 0,
            "bne": 1,
            "blt": 4,
            "bge": 5,
            "bltu": 6,
            "bgeu": 7
            }

    load_dict = {
            "lb": 0,
            "lh": 1,
            "lw": 2,
            "lbu": 4,
            "lhu": 5
            }

    store_dict = {
            "sb": 0,
            "sh": 1,
            "sw": 2
            }

    arith_imm_dict = {
            "addi": 0,
            "slti": 2,
            "sltiu": 3,
            "xori": 4,
            "ori": 6,
            "andi": 7,
            "slli": 1,
            "srli": 5,
            "srai": 5
            }

    arith_dict = {
            "add": 0,
            "sub": 0,
            "slt": 2,
            "sltu": 3,
            "xor": 4,
            "or": 6,
            "and": 7,
            "sll": 1,
            "srl": 5,
            "sra": 5
            }

    fence_dict = {
            "fence": 0,
            "fence.i": 1
            }

    csrr_dict = {
            "csrrw": 1,
            "csrrs": 2,
            "csrrc": 3,
            "csrrwi": 5,
            "csrrsi": 6,
            "csrrci": 7
            }

    def j_type(self, opcode, op, tokens):
        # JAL, JALR instructions
        rd = tokens[0] << 7

        if op == "jalr":
            if tokens[2] > 2047 or tokens[2] < -2048:
                return 0

            rs1 = tokens[1] << 15
            imm = (tokens[2] & 0xFFF) << 20
            return 0 | opcode | rd | rs1 | imm

        if tokens[1] > 524287 or tokens[1] < -524288:
            return 0

        imm = tokens[1]
        imm20 = ((imm >> 19) & 1) << 31
        imm10to1 = (imm & 0x3FF) << 21
        imm11 = ((imm >> 10) & 0x1) << 20
        imm19to12 = ((imm >> 11) & 0xFF) << 12
        return 0 | opcode | rd | imm19to12 | imm11 | imm10to1 | imm20


    def u_type(self, opcode, op, tokens):
        # LUI, AUIPC instructions
        if tokens[1] > 1048575 or tokens[1] < -1048576:
            return 0

        rd = tokens[0] << 7
        imm = tokens[1] << 12
        return 0 | opcode | rd | imm


    def b_type(self, opcode, op, tokens):
        # Branch instructions
        if tokens[2] > 511 or tokens[2] < -512:
            return 0

        funct3 = self.branch_dict[op] << 12
        rs1 = tokens[0] << 15
        rs2 = tokens[1] << 20
        imm = tokens[2]
        imm12 = (imm >> 11) << 31
        imm11 = ((imm >> 10) & 0x1) << 7
        imm10to5 = ((imm >> 4) & 0x3F) << 25
        imm4to1 = (imm & 0xF) << 8

        instr = 0 | opcode | imm11 | imm4to1 | funct3 | rs1 | rs2 | imm10to5 | imm12
        return instr


    def i_type(self, opcode, op, tokens):
        # Arith-Immediate instructions
        if tokens[2] > 511 or tokens[2] < -512:
            return 0

        funct3 = self.arith_imm_dict[op] << 12

        if op != "srai":
            funct7 = 0
        else:
            funct7 = 1 << 30

        rd = tokens[0] << 7
        rs1 = tokens[1] << 15
        imm = tokens[2] << 20
        instr = 0 | opcode | rd | funct3 | rs1 | imm

        if op in ["slli", "srli", "srai"]:
            instr = instr | funct7

        return instr


    def l_type(self, opcode, op, tokens):
        # Load instruction
        funct3 = self.load_dict[op] << 12

        rd = tokens[0] << 7
        rs1 = tokens[1] << 15
        imm = tokens[2] << 20
        instr = 0 | opcode | rd | funct3 | rs1 | imm

        return instr


    def s_type(self, opcode, op, tokens):
        # Store instructions
        funct3 = self.store_dict[op] << 12
        rs1 = tokens[0] << 15
        rs2 = tokens[1] << 20
        imm11to5 = (tokens[2] >> 5) << 25
        imm4to0 = (tokens[2] & 0x1F) << 7

        instr = 0 | opcode | imm4to0 | funct3 | rs1 | rs2 | imm11to5

        return instr


    def r_type(self, opcode, op, tokens):
        # Register instructions
        funct3 = self.arith_dict[op] << 12

        if op != "sub" and op != "sra":
            funct7 = 0
        else:
            funct7 = 1 << 30

        rd = tokens[0] << 7
        rs1 = tokens[1] << 15
        rs2 = tokens[2] << 20

        instr = 0 | opcode | rd | funct3 | rs1 | rs2 | funct7

        return instr


    def f_type(self, opcode, op, tokens):
        # Fence instructions
        fence_dict = self.fence_dict
        return 0


    def c_type(self, opcode, op, tokens):
        # CSRR instructions
        csrr_dict = self.csrr_dict
        return 0
