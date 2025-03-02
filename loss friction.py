#imports
import math


# Given data for part (b)
tau_w = 200  # Wall shear stress (Pa)
rho = 900  # Density (kg/m^3)
D_pipe = 0.1  # Pipe diameter (m)
nu = 1.2e-6  # Kinematic viscosity (m^2/s)

# Step 1: Calculate lambda h* V^2
lambda_V_squared = (8 * tau_w) / rho

# Step 2: For laminar flow (lambda = 64 / Re), solve for velocity
# V = sqrt((lambda_V_squared * D) / (64 * nu))
V_laminar = math.sqrt((lambda_V_squared * D_pipe) / (64 * nu))

# Step 3: Calculate flow rate (Q = A * V)
A_pipe = math.pi * (D_pipe / 2) ** 2  # Cross-sectional area of pipe (m^2)
Q_laminar = A_pipe * V_laminar  # Flow rate for laminar flow (m^3/s)

# Step 4: Convert to liters per second
Q_laminar_liters = Q_laminar * 1000  # Convert m^3/s to L/s

# Results
print = V_laminar, Q_laminar_liters
