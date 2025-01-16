#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ensure Qiskit is installed:
# pip install qiskit

from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply CNOT gate to entangle the first qubit with the second qubit
qc.cx(0, 1)

# Measure both qubits and store results in classical bits
qc.measure([0, 1], [0, 1])

# Print the circuit diagram
print(qc)