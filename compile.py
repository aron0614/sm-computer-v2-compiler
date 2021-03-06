import os
import logging

from importlib_metadata import version

class command:
    asm_command : str
    actuall_command : int
    
    hasVariables : bool
    variables : int
    varTypes : list
    def __init__(self, ams_command, cmd, variables=None, types=None):
        self.asm_command = ams_command
        self.actuall_command = cmd
        self.hasVariables = False
        self.variables = 0
        self.varTypes = []
        if variables != None:
            self.hasVariables = True
            self.variables = variables
            self.varTypes = types
            
        
class compiler:
    PROGRAM_MEMORY_SIZE = 128
    USE_MEMORY_FOR_CODE_STORAGE = False
    
    CMP_errors = []
    
    DEFAULT_COMPILER_SETTINGS = {
        "commentKey": "&&",
        "compilerVersion":"latest",
        
    }
    
    compilerSettings = {
        "commentKey": "&&",
        "compilerVersion":"latest",
        
    }
    
    commandLibary = {}
    compilerCommmands = {}

    def __init__(self, settings=None):
        pass
    
    def addCommand(self, commandToAdd):
        cmdData = {"cmd": commandToAdd.actuall_command, "requiresVars": commandToAdd.hasVariables, "variableCount": commandToAdd.variables, "varTypes": commandToAdd.varTypes}
        self.commandLibary[commandToAdd.asm_command] = cmdData
        
    def removeCommand(self, commandName):
        if commandName in self.commandLibary:
            del self.commandLibary[commandName]
    
    def compile(self, path, whereTo):
        version = self.compilerSettings["compilerVersion"]
        with open(path) as file:
            self._scan(file, version)
    
    def _scan(self, file, version):
        lineNum = 0
        
        for line in file.readlines():
            lineNum += 1
            
            lineSegments = line.split()
            print(lineSegments)
            
            if lineSegments[0] != self.compilerSettings["commentKey"] and lineSegments[0] in self.commandLibary:
                pass
            
                        
            


def main():
    STA = command("STA", 1, 1, ["int"])
    STB = command("STB", 2, 1, ["int"])
    STC = command("STC", 3, 1, ["int"])
    STD = command("STD", 4, 1, ["int"])
    STE = command("STE", 5, 1, ["int"])

    STX = command("STX", 6, 1, ["int"])
    STY = command("STY", 7, 1, ["int"])

    STM = command("STM", 8, 1, ["any"])

    comp = compiler()

    comp.addCommand(STA)
    comp.addCommand(STB)
    comp.addCommand(STC)
    comp.addCommand(STD)
    comp.addCommand(STE)

    comp.addCommand(STX)
    comp.addCommand(STY)

    comp.addCommand(STM)
    
    #print(comp.commandLibary)
    
    comp.compile("smltest.asm", "compile.smc")

if __name__ == "__main__":
    main()