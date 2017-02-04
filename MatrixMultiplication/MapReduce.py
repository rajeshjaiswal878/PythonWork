import json

"""
Title:Matrix multiplication in the Simple Python MapReduce Framework
Dated:4th feb 2017
Name: XYZ
"""

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    '''
    This function will generate both matrix internally before multiplication
    '''

    def storematrixvalue(self, matrixname, value):
        self.intermediate.setdefault(matrixname, [])
        self.intermediate[matrixname].append(value)

    '''
        This function will display resultant matrix after multiplication
    '''

    def display(self, value):
        self.result.append(value)

    '''
    This function will read value line by line from data file for actual multiplication
    '''

    def multiplication(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for matrixname in self.intermediate:
            reducer(matrixname, self.intermediate[matrixname])

        jenc = json.JSONEncoder()
        for item in self.result:
            print jenc.encode(item)
