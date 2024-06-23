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
class GatesStack:
    def __init__(self):
        self.stack = list()

class Quantum:
    def __init__(self, gStack, qbCount, imgFolder):
        self.qiskitVersion = qiskit.__version__
        self.imagesPath = imgFolder # Folder to Images

        self.gatesStack = gStack # Stack of the gates
        self.qubitsCount = qbCount # count of the qubits

        # Registers
        self.regQ = qiskit.QuantumRegister(self.qubitsCount, "QuantumRegister") # Quantum
        self.regC = qiskit.ClassicalRegister(self.qubitsCount, "ClassicRegister") # Classic

        self.circuit = qiskit.QuantumCircuit(self.regQ, self.regC) # Circuit

        self.gates = ["h", "x", "z", "ry", "cx", "cu3", "ccx"]

    def saveImage(self):
        pass

    def loggCircuit(self):
        pass

    def isInCircuit(self, qubitIdList):
        for qubitId in qubitIdList:
            if not (qubitId > 0 and qubitId < self.qubitsCount):
                return False
        return True

    # Using of the gates
    def useGate(self, gateElement):
        gate = gateElement[0]

        if (gate == "h"):
            if len(gateElement) != 2:
                print("Gate h has 1 parametr")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("h", 1,)
        elif (gate == "x"):
            if len(gateElement) != 2:
                print("Gate x has 1 parametr")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("x", 1,)
        elif (gate == "z"):
            if len(gateElement) != 2:
                print("Gate z has 1 parametr")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("z", 1,)
        elif (gate == "ry"):
            if len(gateElement) != 3:
                print("Gate ry has 2 parametr")
                return

            self.isInCircuit(gate[1:2])
            self.circuit.ry(2*gateElement[2], self.regQ[gateElement[1]]) # ("ry", 1, 45)
        elif (gate == "cx"):
            if len(gateElement) != 2:
                print("Gate cx has 2 parametr")
                return

            self.isInCircuit(gate[1:])
            self.circuit.cx(self.regQ[gateElement[1]], self.regQ[gateElement[2]]) # ("cx", 1, 2)
        elif (gate == "cu3"):
            if len(gateElement) != 4:
                print("Gate cu3 has 3 parametr")
                return

            self.isInCircuit(gate[1:3])
            self.circuit.cu3(self.regQ[gateElement[3]], 0, 0, self.regQ[gateElement[1]], self.regQ[gateElement[2]]) # ("cu3", 1, 2, 45)
        elif (gate == "ccx"):
            if len(gateElement) != 4:
                print("Gate ccx has 3 parametr")
                return

            self.isInCircuit(gate[1:])
            self.circuit.ccx(self.regQ[gateElement[1]], self.regQ[gateElement[2]], self.regQ[gateElement[3]]) # ("ccx", 1, 2, 3)
        else:
            print("Doesn't found gate: " + gate)
            return None
        return gate

    def run(self):
        for el in self.gatesStack:
            result = self.useGate(el)
            if result == None:
                return
            else:
                print("Operator - " + result + " - used.")

stackOfGates = [["h", 1],["r", 2],["h", 3],["h", 4]]
quantum = Quantum(stackOfGates, 10, "./Images")

quantum.run()