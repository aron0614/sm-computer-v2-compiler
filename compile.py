import os
import logging

class command:
    asm_command : str
    actuall_command : int
    
    hasVariables : bool
    variables : int
    def __init__(self, ams_command, cmd, variables=None):
        self.asm_command = ams_command
        self.actuall_command = cmd
        self.hasVariables = False
        if variables != None:
            self.hasVariables = True
            self.variables = variables
            
class compilerCommand:
    pass
        
class compiler:
    PROGRAM_MEMORY_SIZE = 128
    USE_MEMORY_FOR_CODE_STORAGE = False
    
    commandLibary = {}
    compilerCommmands = {}

    def __init__(self, settings=None):
        pass
    
    def addCommand(self, commandToAdd):
        pass
    
    def addCompilerCommand(self, compilerCommandToAdd):
        pass
    
    def removeCommand(self, commandName):
        pass
    
    def removeCompilerCommand(self, compilerCommandName):
        pass
    
    def compile(self, path, version=1):
        pass


if __name__ == "__main__":
    pass