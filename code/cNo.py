class cNo:
    # *******************************************************
    def __init__(self, dado=0.0):
        self.__dado = dado
        self.__filhoDir = None
        self.__filhoEsq = None

    # *******************************************************
    def getDado(self):
        return self.__dado

    # *******************************************************
    def setDado(self, valor):
        self.__dado = valor

    # *******************************************************
    def getFilhoDir(self):
        return self.__filhoDir

    def setFilhoDir(self, filhoDir):
        self.__filhoDir = filhoDir

    # *******************************************************
    def getFilhoEsq(self):
        return self.__filhoEsq

    def setFilhoEsq(self, filhoEsc):
        self.__filhoEsq = filhoEsc

    # *******************************************************
    def __str__(self):
        outStr =  f'+================================================+\n'
        outStr += f'|             {id(self):16x}                   |\n'
        outStr += f'+===================++========++=================\n'
        outStr += f'| {id(self.__filhoEsq):16x} | {self.__dado} | {id(self.__filhoDir):16x} |\n'
        outStr += f'+===================++========++=================\n'
        return outStr