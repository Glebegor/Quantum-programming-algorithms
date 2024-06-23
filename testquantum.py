import time

import qiskit
import qiskit_ibm_runtime
import qiskit_aer
import numpy as np
import random as rand
import os


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


# execute the circuit 1024 times
job = qiskit_aer.AerSimulator(method='automatic').run(circuit,shots=1024)
# get the result
counts = job.result().get_counts(circuit)
print(counts)








# Projecting Quantum class

class Quantum:
    def __init__(self, gStack, qbCount):
        self.qiskitVersion = qiskit.__version__
        self.imagesPath = "./Images" # Folder to Images
        self.loggerPath = "./Logger" # Folder to Loggs

        self.gatesStack = gStack # Stack of the gates
        self.qubitsCount = qbCount # count of the qubits

        # Registers
        self.regQ = qiskit.QuantumRegister(self.qubitsCount, "QRegister") # Quantum
        self.regC = qiskit.ClassicalRegister(self.qubitsCount, "CRegister") # Classic

        self.circuit = qiskit.QuantumCircuit(self.regQ, self.regC) # Circuit

        self.gates = ["h", "x", "z", "ry", "cx", "cu3", "ccx"]
    def findId(self):
        return time.ctime().replace(" ", "_").replace(":", "-")
    def saveImage(self, name):
        self.circuit.draw(output='mpl', filename=self.imagesPath + "/" + name)

    def loggCircuit(self, name):
        with os.open(path=self.loggerPath + "/" + name + ".txt", flags=777) as openedFile:
            for el in stackOfGates:
                newRow = ""
                for row in stackOfGates:
                    newRow += str(row)
                openedFile.write(newRow)

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
                print("Gate h has 1 param.")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("h", 1,)
        elif (gate == "x"):
            if len(gateElement) != 2:
                print("Gate x has 1 param.")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("x", 1,)
        elif (gate == "z"):
            if len(gateElement) != 2:
                print("Gate z has 1 param.")
                return

            self.isInCircuit(gate[1:])
            self.circuit.h(self.regQ[gateElement[1]]) # ("z", 1,)
        elif (gate == "ry"):
            if len(gateElement) != 3:
                print("Gate ry has 2 params.")
                return

            self.isInCircuit(gate[1:2])
            self.circuit.ry(2*gateElement[2], self.regQ[gateElement[1]]) # ("ry", 1, 45)
        elif (gate == "cx"):
            if len(gateElement) != 2:
                print("Gate cx has 2 params.")
                return

            self.isInCircuit(gate[1:])
            self.circuit.cx(self.regQ[gateElement[1]], self.regQ[gateElement[2]]) # ("cx", 1, 2)
        elif (gate == "cu3"):
            if len(gateElement) != 4:
                print("Gate cu3 has 3 params.")
                return

            self.isInCircuit(gate[1:3])
            self.circuit.cu3(self.regQ[gateElement[3]], 0, 0, self.regQ[gateElement[1]], self.regQ[gateElement[2]]) # ("cu3", 1, 2, 45)
        elif (gate == "ccx"):
            if len(gateElement) != 4:
                print("Gate ccx has 3 params.")
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
        self.build()
    def build(self):
        self.circuit.measure(self.regQ, self.regC)
        print("Circuit was measured.")

        idOfJob = self.findId()
        print("Created job: " + idOfJob)

        self.saveImage(idOfJob)
        self.loggCircuit(idOfJob)


stackOfGates = [["h", 1],["h", 2],["h", 3],["h", 4]]
quantum = Quantum(stackOfGates, 10)

quantum.run()