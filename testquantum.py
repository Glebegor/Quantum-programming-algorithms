import qiskit
import qiskit_ibm_runtime
import qiskit_aer
import numpy as np
import random as rand



version = qiskit.__version__
print("The version of Qiskit is -", version)

# Quantum circuit
quantumReg = qiskit.QuantumRegister(5)
# Classical circuit
classicalReg = qiskit.ClassicalRegister(5)

# composed circuit of the q-reg and c-reg
circuit = qiskit.QuantumCircuit(quantumReg, classicalReg)

# Setup image folder
imageFolder = "./Images/"

circuit.h(quantumReg[0])
circuit.h(quantumReg[3])
circuit.h(quantumReg[4])

circuit.measure(quantumReg, classicalReg)

print(":)")

circuit.draw(output='mpl', filename=imageFolder + 'test.png')

# execute the circuit 1024 times
job = qiskit_aer.AerSimulator(method='automatic').run(circuit,shots=1024)
# get the result
counts = job.result().get_counts(circuit)
print(counts)








# Projecting Quantum class
class CommandsStack:
    def __init__(self):
        self.stack = list()

class Quantum:
    def __init__(self, cStack, qbCount, imgFolder):
        self.qiskitVersion = qiskit.__version__
        self.imagesPath = imgFolder # Folder to Images

        self.commandsStack = cStack # Stack of the commands
        self.qubitsCount = qbCount # count of the qubits

        # Registers
        self.regQ = qiskit.QuantumRegister(self.qubitsCount) # Quantum
        self.regC = qiskit.ClassicalRegister(self.qubitsCount) # Classic

        self.circuit = qiskit.QuantumCircuit(self.regQ, self.regC) # Circuit


