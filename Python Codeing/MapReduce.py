import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def storematrixvalue(self, matrixname, value):
        self.intermediate.setdefault(matrixname, [])
        self.intermediate[matrixname].append(value)

    def display(self, value):
        self.result.append(value) 

    def multiplication(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for matrixname in self.intermediate:
            reducer(matrixname, self.intermediate[matrixname])

        jenc = json.JSONEncoder()
        for item in self.result:
            print jenc.encode(item)
