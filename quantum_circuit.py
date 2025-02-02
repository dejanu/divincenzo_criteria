#!/usr/bin/env python
from qiskit import QuantumCircuit, transpile
from qiskit_aer.aerprovider import AerSimulator

# Create a Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put the qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit on the qasm simulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
sim_result = simulator.run(compiled_circuit).result()
counts = sim_result.get_counts()

print(qc)
print("Measurement results:", counts)
