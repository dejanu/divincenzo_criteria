#!/usr/bin/env python

from qiskit_aer import AerSimulator

simulator = AerSimulator()

# return the available simulation devices
print (simulator.available_devices())

# Return the available simulation methods
print(simulator.available_methods())