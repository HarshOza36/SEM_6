import numpy as np
from itertools import product
from functools import reduce
debug_print = print
class McCullochPitt:
    def __init__(self, dataset, target_row_val, name_of_gate):
        self.dataset = dataset
        self.target_row_val = target_row_val
        self.X = [row[:-1] for row in dataset]
        self.Y = [row[-1] for row in dataset]
        self.m = len(self.X[0])
        self.n = len(self.dataset)
        self.function = Gates.get_gate(name_of_gate)
        self.weights = None 
        self.threshold = None 
    @staticmethod
    def get_threshold(op, target):
        return min([i for i in zip(op, target) if i[1] == 1], key=lambda x: x[1])[0]
    @staticmethod
    def apply_threshold(row, threshold):
        return [0 if ele < threshold else 1 for ele in row]
    def train(self, combs=(-1, 0, 1)):
        possible_weights = product(combs, repeat=self.m)
        for weights in map(np.array, possible_weights):
            debug_print('Checking for weights {}'.format(weights))
            op = [sum(weights * row) for row in self.X]
            threshold = McCullochPitt.get_threshold(op, target=self.Y)
            neuron_op = McCullochPitt.apply_threshold(op, threshold)
            if neuron_op == self.Y:
                self.weights = weights
                self.threshold = threshold
                break
        if self.weights is None:
            raise ValueError("Couldn't train model")
        else:
            debug_print('Training successful!! ')
class DataSet:
    def __new__(cls, name_of_gate, repeat, ip_values):
        return cls.get_dataset(Gates.get_gate(name_of_gate), repeat, ip_values)
    @staticmethod
    def get_dataset(function, repeat, ip_values):
        return [list(row) + [function(row)] for row in product(ip_values, repeat=repeat)]
class Gates:
    @staticmethod
    def _and(l):
        return reduce(lambda x, y: x * y, l)
    @staticmethod
    def _or(l):
        if len(l) != 2:
            raise NotImplementedError("number of element should be 2")
        return l[0] or l[1]
    @staticmethod
    def nand(l):
        if len(l) != 2:
            raise NotImplementedError("number of element should be 2")
        return int(not Gates._and(l))
    @staticmethod
    def and_not(l):
         if len(l) != 2:
            raise NotImplementedError("number of element should be 2")
         return int(l[0] and not l[1])
    @staticmethod
    def nor(l):
        if len(l) != 2:
            raise NotImplementedError("number of element should be 2")
        return int(not Gates._or(l))
    @staticmethod
    def get_gate(name_of_gate):
        function_gate_mapping = {
        "AND": Gates._and,
        "OR": Gates._or,
        "NAND": Gates.nand,
        "NOR": Gates.nor,
        "AND_NOT": Gates.and_not
        }
        return function_gate_mapping.get(name_of_gate.upper())
for gate in ("and", 'or', 'nand', 'nor', 'and_not'):
    try:
        print('\nTrying to train model for {} gate:'.format(gate.upper()))
        dataset = DataSet(gate, 2, [0, 1])
        model = McCullochPitt(dataset=dataset, target_row_val=1, name_of_gate='naNd')
        model.train()
        print('Trained weights:', model.weights, model.threshold)
    except ValueError:
         print("Couldn't train the model for the gate.")
"""
Trying to train model for AND gate:
Checking for weights [-1 -1]
Checking for weights [-1 0]
Checking for weights [-1 1]
Checking for weights [ 0 -1]
Checking for weights [0 0]
Checking for weights [0 1]
Checking for weights [ 1 -1]
Checking for weights [1 0]
Checking for weights [1 1]
Training successful!!
Trained weights: [1 1] 2
Trying to train model for OR gate:
Checking for weights [-1 -1]
Checking for weights [-1 0]
Checking for weights [-1 1]
Checking for weights [ 0 -1]
Checking for weights [0 0]
Checking for weights [0 1]
Checking for weights [ 1 -1]
Checking for weights [1 0]
Checking for weights [1 1]
Training successful!!
Trained weights: [1 1] 1
Trying to train model for NAND gate:
Checking for weights [-1 -1]
Checking for weights [-1 0]
Checking for weights [-1 1]
Checking for weights [ 0 -1]
Checking for weights [0 0]
Checking for weights [0 1]
Checking for weights [ 1 -1]
Checking for weights [1 0]
Checking for weights [1 1]
Couldn't train the model for the gate.
Trying to train model for NOR gate:
Checking for weights [-1 -1]
Training successful!!
Trained weights: [-1 -1] 0
Trying to train model for AND_NOT gate:
Checking for weights [-1 -1]
Checking for weights [-1 0]
Checking for weights [-1 1]
Checking for weights [ 0 -1]
Checking for weights [0 0]
Checking for weights [0 1]
Checking for weights [ 1 -1]
Training successful!!
Trained weights: [ 1 -1] 1
"""
