import sys


class CPU:

    def __init__(self):
        self.ram = [None] * 256
        self.reg = [None] * 8
        self.pc = 0
        self.commands = {}
        self.commands[0b10000010] = self.handle_LDI
        self.commands[0b01000111] = self.handle_PRN
        self.commands[0b00000001] = self.handle_HLT
        self.commands[0b10100111] = self.handle_CMP
        self.commands[0b01010100] = self.handle_JMP
        self.commands[0b01010101] = self.handle_JEQ
        self.commands[0b01010110] = self.handle_JNE
        self.FL = 0b00000000

    def load(self):
        """Load a program into memory."""

        address = 0

        filename = 'sctest.ls8'

        file = open(filename, 'r')
        program = []

        for line in file:
            if not line[0] == '#' and not len(line.strip()) == 0:
                program.append(int(line.strip()[:8], 2))

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self):
        pass

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def handle_HLT(self):
        sys.exit()

    def handle_LDI(self):
        reg_address = self.ram[self.pc + 1]
        value = self.ram[self.pc + 2]
        self.reg[reg_address] = value

    def handle_PRN(self):
        reg_address = self.ram[self.pc + 1]
        print(self.reg[reg_address])

    def handle_CMP(self):
        reg_address_a = self.ram[self.pc + 1]
        reg_address_b = self.ram[self.pc + 2]
        self.alu('CMP', reg_address_a, reg_address_b)

    def handle_JMP(self):
        reg_address = self.ram[self.pc + 1]
        self.pc = self.reg[reg_address]

    def handle_JEQ(self):
        # Runs JUMP if equal flag is up
        eq = self.FL & 0b00000001
        if eq == 1:
            self.handle_JMP()
        else:
            self.pc += 2

    def handle_JNE(self):

        eq = self.FL & 0b00000001
        if not eq:
            self.handle_JMP()
        else:
            self.pc += 2

    def run(self):
        self.reg[7] = 0xF4

        while True:
            
            mem = self.ram[self.pc]
            increment = ((mem & 0b11000000) >> 6) + 1
            jumping = ((mem & 0b00010000) >> 4)

            if mem in self.commands:
                self.commands[mem]()
            else:
                print(f'Intruction {mem} unknown')
                break

                if not jumping:
                    self.pc += increment
