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

        # JAL instruction
        return 0


    def u_type(self, opcode, op, tokens):
        # LUI, AUIPC instructions

        return 0


    def b_type(self, opcode, op, tokens):
        # Branch instructions
        branch_dict = self.branch_dict
        return 0


    def i_type(self, opcode, op, tokens):
        # Immediate instructions
        load_dict = self.load_dict
        arith_i_dict = self.arith_imm_dict
        return 0


    def s_type(self, opcode, op, tokens):
        # Store instructions
        store_dict = self.store_dict
        return 0


    def r_type(self, opcode, op, tokens):
        # Register instructions
        arith_dict = self.arith_dict

        funct3 = arith_dict[op] << 12

        if op != "sub" and op != "sra":
            funct7 = 0
        else:
            funct7 = 1 << 30

        rd = tokens[0] << 7
        rs1 = tokens[1] << 15
        rs2 = tokens[2] << 20

        instr = 0 & opcode & rd & funct3 & rs1 & rs2 & funct7

        return instr


    def f_type(self, opcode, op, tokens):
        # Fence instructions
        fence_dict = self.fence_dict
        return 0


    def c_type(self, opcode, op, tokens):
        # CSRR instructions
        csrr_dict = self.csrr_dict
        return 0
