from qiskit import IBMQ

# Load IBM Quantum account
IBMQ.load_account()
provider = IBMQ.get_provider()

# Print the available backends
available_backends = provider.backends()
print("Available Backends:")
for backend in available_backends:
    print(backend.name())
