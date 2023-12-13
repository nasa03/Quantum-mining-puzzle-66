# Quantum-mining-puzzle-66
Currently setup to run on the IBM Quantum simulator 32 qubits simulation or use quantum-run-kyoto.py for<br>
Actual connection to IBM Quantum Kyoto, Japan super computer<br>
Same basic code to connect to live resources with some adjustments that may be needed<br>
Setup to match the first 4 characters of the Hash160<br>
Working on more selective 10 character version<br>
go to https://quantum.ibm.com/ and get an account so you can be assigned your personal API<br> 
Add your API code to quantum_login-step1.py<Br>
pip3 install qiskit<br>
pip3 install qiskit_ibm_provider<br>
pip3 install qiskit-ibm-runtime
https://github.com/Qiskit/qiskit-ibm-provider<br>
https://github.com/Qiskit/qiskit-ibm-runtime<br>
If you go live you only get 10 minutes free after that IBM charges $1.60 US per minute<br>
Simulator has no time limit but really just tests the software for errors<br>
Since there is no real way to verify the software is completing the desired task on actual super computer<br>
If you decide to pay for time to IBM you are doing this at your own risk and I as the developer am not responsible<br>
for any loss(es) you may incur. <bR>
When you connect to the actual super computer ex. ibm_kyoto you will be put in queue then the resource will run your code<br> 
for 2 to 5 seconds then back in queue over and over so it could take hours for your 10 minutes to be used, this is mostly new to me.<br>
so if you have questions best to contact IBM Quantum or Qiskit support.<br>
Some resources may need timing adjustments depending where you live due to network and the super computer you connect to.<br>
ibm_brisbane and ibm_osaka would not connect properly for me.<br>
