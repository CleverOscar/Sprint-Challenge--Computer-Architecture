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

    def load(self):
        address = 0

        filename = 'sctest.sctest.ls8'

        file = open(filename, 'r')
        program = []

        for line in file:
            if not line[0] == '#' and not len(line.strip()) == 0:
                program.append(int(line.strip()[:8], 2))

        for instructoin in program:
            self.ram[address] = instructoin
            address += 1

    def alu():
        pass

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def run():
        
