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








# Proecting Quantum class

class QuantumService:
    def __init__(self, cStk, qbC):
        self.commandsStack = cStk # Stack of the commands
        self.qubitsCount = qbC

        # Registers
        self.regQ = qiskit.QuantumRegister(qbC) # Quantum
        self.regC = qiskit.ClassicalRegister(qbC) # Classic


