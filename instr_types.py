
class Instr_Type:

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
            "andi": 7
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
            "and": 7
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

    def j_type(self,  ):
        # JAL instruction
        opcode = 0b110111


    def u_type():
        # LUI, AUIPC instructions

    def b_type():
        # Branch instructions

    def i_type():
        # Immediate instructions

    def s_type():
        # Store instructions

    def r_type():
        # Register instructions

    def f_type():
        # Fence instructions

    def c_type():
        # CSRR instructions
