from qiskit_ibm_provider import IBMQProvider

# Replace 'YOUR_API_TOKEN' with your actual API token
api_token = 'YOUR_API_TOKEN'

# Save IBM Quantum account
provider = IBMQProvider()
provider.save_account(api_token, overwrite=True)

# Load IBM Quantum account
provider.load_account()


