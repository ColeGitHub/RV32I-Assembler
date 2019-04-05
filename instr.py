import instr_types

class Instruction:

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
            "zero": "x0",
            "ra": "x1",
            "sp": "x2",
            "gp": "x3",
            "tp": "x4",
            "t0": "x5",
            "t1": "x6",
            "t2": "x7",
            "s0": "x8",
            "s1": "x9",
            "a0": "x10",
            "a1": "x11",
            "a2": "x12",
            "a3": "x13",
            "a4": "x14",
            "a5": "x15",
            "a6": "x16",
            "a7": "x17",
            "s2": "x18",
            "s3": "x19",
            "s4": "x20",
            "s5": "x21",
            "s6": "x22",
            "s7": "x23",
            "s8": "x24",
            "s9": "x25",
            "s10": "x26",
            "s11": "x27",
            "t3": "x28",
            "t4": "x29",
            "t5": "x30",
            "t6": "x31"
            }


    def convert(instr):
        tokens = instr.lstrip().split(None, 1)
        tokens[1] = tokens[1].replace(" ", "").split(",")

        # Convert instruction to opcode
        opcode = instructions[tokens[0]]


