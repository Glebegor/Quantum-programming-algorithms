import numpy as np
import random as rand

import qiskit as qk
import qiskit_ibm_runtime as qk_runtime
import qiskit_aer as qk_aer

'''
Created by Hlib Arseniuk 2024.
Application for Quantum Computing.
Hello world.
Qubits: 2 
'''

def saveImage(circuit, name):
    circuit.draw(output='mpl', filename=name)

def runSimulator() -> None:
    pass
def runIBM() -> None:
    pass

def main() -> None:
    run = int(input("Choose simulator: 1. IBM or 2. Aer"))




    if run == 1:
        runIBM()
    elif run == 2:
        runSimulator()
    else:
        print("Choose 1 or 2.")


if __name__=="__main__":
    main()
