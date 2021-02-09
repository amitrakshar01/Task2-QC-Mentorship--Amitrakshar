%matplotlib inline
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from iqx import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()
import qiskit as qk
q=qk.QuantumRegister(2)
c=qk.ClassicalRegister(2)
circuit=qk.QuantumCircuit(q,c)
circuit.h(q[0])
circuit.id(q[0]) #for Z gate the code: circuit.z(q[0])
circuit.cx(q[0],q[1])
circuit.measure(q,c)
print(circuit) # to see the circuit
#Assigning  a bit flip error using a 3 qubit quantum sytem

qreg_q =qk.QuantumRegister(3)
creg_c = qk.ClassicalRegister(3)
circuit = qk.QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.x(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
circuit.ccx(qreg_q[2], qreg_q[1], qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
print(circuit) # to see the cicuit with the bit flip error gate

