
instructions = {
        "lui": [0x37, "u"],
        "auipc": [0x17, "u"],
        "jal": [0x6F, "j"],
        "jalr": [0x67, "i"],
        "beq": [0x63, "b"],
        "bne": [0x63, "b"],
        "blt": [0x63, "b"],
        "bge": [0x63, "b"],
        "bltu": [0x63, "b"],
        "bgeu": [0x63, "b"],
        "lb": [0x3, "i"],
        "lh": [0x3, "i"],
        "lw": [0x3, "i"],
        "lbu": [0x3, "i"],
        "lhu": [0x3, "i"],
        "sb": [0x23, "s"],
        "sh": [0x23, "s"],
        "sw": [0x23, "s"],
        "addi": [0x13,"i"],
        "slti": [0x13,"i"],
        "sltiu": [0x13,"i"],
        "xori": [0x13,"i"],
        "ori": [0x13,"i"],
        "andi": [0x13,"i"],
        "slli": [0x13,"i"],
        "srli": [0x13,"i"],
        "srai": [0x13,"i"],
        "add": [0x33, "r"],
        "slt": [0x33, "r"],
        "sltu": [0x33, "r"],
        "xor": [0x33, "r"],
        "or": [0x33, "r"],
        "and": [0x33, "r"],
        "sll": [0x33, "r"],
        "srl": [0x33, "r"],
        "sra": [0x33, "r"],
        "fence": [0xf, "f"],
        "fence.i": [0xf, "f"],
        "ecall": [0x73, "c"],
        "ebreak": [0x73, "c"],
        "csrrw": [0x73, "c"],
        "csrrs": [0x73, "c"],
        "csrrc": [0x73, "c"],
        "csrrwi": [0x73, "c"],
        "csrrsi": [0x73, "c"],
        "csrrci": [0x73, "c"]
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


