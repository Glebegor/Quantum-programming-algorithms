import numpy as np
import random as rand
import dotenv
import os
import matplotlib.pyplot as plt

import qiskit as qk
from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2, EstimatorV2
from qiskit import transpile
import qiskit_aer as qk_aer
from qiskit.circuit.library import MCXGate, ZGate, CCZGate
from qiskit.circuit.library.standard_gates import HGate, XGate, CXGate, CCXGate

'''
Created by Hlib Arseniuk (Glebegor) 2024.
Application for Quantum Computing.
(y ^ x) && (i && j) problem.
Qubits: 6
'''


def saveImage(circuit: qk.circuit.QuantumCircuit, name: str) -> None:
    '''
    Save image of circuit.
    '''
    circuit.draw(output='mpl', filename=name)

def runSimulator(circuit: qk.circuit.QuantumCircuit, shorts_count: int) -> None:
    '''
    Run simulator.
    '''
    job = qk_aer.AerSimulator(method='automatic').run(circuit, shots=shorts_count)
    counts = job.result().get_counts(circuit)
    print(counts)

    plt.figure(figsize=(10, 6))
    plt.bar(counts.keys(), counts.values())
    plt.show()


def runIBM(circuit: qk.circuit.QuantumCircuit, shots_count: int) -> None:
    '''
    Run IBM backend.
    '''

    # Save IBM account
    QiskitRuntimeService.save_account(
        channel="ibm_quantum",
        name=os.getenv("IBM_NAME"),
        token=os.getenv("IBM_TOKEN"),
        set_as_default=True,
        overwrite=True
    )

    service = QiskitRuntimeService()

    # Connect to the least busy backend
    backends = service.backends(
        filters=lambda x: x.configuration().n_qubits >= circuit.num_qubits
                          and not x.configuration().simulator
                          and x.status().operational
    )

    if not backends:
        print("No suitable backends found.")
        return

    print("Backends: ", [backend.name for backend in backends])

    backend_busy = min(backends, key=lambda x: x.status().pending_jobs)
    print("The least busy backend is:", backend_busy.name)

    # Transpile the circuit to match the backend's constraints
    transpiled_circuit = transpile(circuit, backend=backend_busy)

    # Create a session for the execution
    with Session(service=service, backend=backend_busy.name) as session:
        sampler = SamplerV2(session=session)
        job = sampler.run([transpiled_circuit], shots=shots_count)

        print("Job ID:", job.job_id())
        result = job.result()
        print("Job status:", job.status())
        print("Job result:", result)

def algorithm(qb_count: int) -> qk.QuantumCircuit:
    reg_quantum = qk.QuantumRegister(qb_count, "q_reg")
    reg_classic = qk.ClassicalRegister(qb_count, "c_reg")

    circuit = qk.QuantumCircuit(reg_quantum, reg_classic)

    circuit.h([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4], reg_quantum[5]])

    circuit.mcx([reg_quantum[0], reg_quantum[1]], reg_quantum[2])

    circuit.cx(reg_quantum[5], reg_quantum[4])

    # CCZ garte
    circuit.h(reg_quantum[3])
    circuit.mcx([reg_quantum[2], reg_quantum[4]], reg_quantum[3])
    circuit.h(reg_quantum[3])

    circuit.mcx([reg_quantum[0], reg_quantum[1]], reg_quantum[2])
    circuit.cx(reg_quantum[5], reg_quantum[4])

    # RESET
    circuit.barrier()

    # circuit.mcx([reg_quantum[0], reg_quantum[1]], reg_quantum[2])
    # circuit.ccx(reg_quantum[0], reg_quantum[1], reg_quantum[2])
    # circuit.ccx(reg_quantum[1], reg_quantum[0], reg_quantum[2])
    #
    # circuit.cx(reg_quantum[5], reg_quantum[4])
    circuit.barrier()

    # RESET END

    circuit.h([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4], reg_quantum[5]])

    circuit.x([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4], reg_quantum[5]])

    circuit.h(reg_quantum[5])
    circuit.mcx([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4]], reg_quantum[5])
    circuit.h(reg_quantum[5])

    circuit.x([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4], reg_quantum[5]])

    circuit.h([reg_quantum[0], reg_quantum[1], reg_quantum[3], reg_quantum[4], reg_quantum[5]])

    circuit.measure(reg_quantum, reg_classic)

    return circuit

def main() -> None:
    dotenv.load_dotenv()

    run = int(input("Choose simulator: 1. IBM or 2. Aer: \n"))
    shorts_count = int(input("Shorts count: \n"))

    circuit = algorithm(6)
    saveImage(circuit, "circuit")

    if run == 1:
        runIBM(circuit, shorts_count)
    elif run == 2:
        runSimulator(circuit, shorts_count)
    else:
        print("Choose 1 or 2.")

if __name__=="__main__":
    main()
