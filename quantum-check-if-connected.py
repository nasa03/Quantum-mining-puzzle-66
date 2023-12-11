from qiskit import IBMQ

# Load IBM Quantum account
IBMQ.load_account()

# Check if you are connected
provider = IBMQ.get_provider()
print("Connected to IBM Quantum:", provider)
