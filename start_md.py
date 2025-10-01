from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout

# Load the Amber prmtop and inpcrd files
prmtop = AmberPrmtopFile('complex_su_hmass.prmtop')
inpcrd = AmberInpcrdFile('complex_su.crd')

# Create the system
system = prmtop.createSystem(nonbondedMethod=PME,
                             nonbondedCutoff=1*nanometer,
                             constraints=HBonds)

# Define the integrator with 4 fs time step
integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 4*femtoseconds)

# Create the simulation object
simulation = Simulation(prmtop.topology, system, integrator)
simulation.context.setPositions(inpcrd.positions)

# Minimize energy
simulation.minimizeEnergy(maxIterations=5000)

# Gradual heating from 0 K to 300 K in 50 K increments
for temp in range(0, 301, 50):
    integrator.setTemperature(temp*kelvin)
    simulation.step(5000)

# Set temperature to 300 K for production run
integrator.setTemperature(300*kelvin)

# Add reporters
simulation.reporters.append(NetCDFReporter('output.nc', 25000))  # 0.1 ns = 25000 steps with 4 fs
simulation.reporters.append(StateDataReporter(stdout, 25000, step=True,
                                              potentialEnergy=True, temperature=True))

# Run production simulation (500 ns = 125,000,000 steps with 4 fs)
simulation.step(125000000)
