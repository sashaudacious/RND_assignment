import pandas as pd
import numpy as np
from scipy.optimize import differential_evolution

# --- 1. Load and Prepare Data ---
df = pd.read_csv('xy_data.csv')

# The CSV has 1500 points. Creating a uniform 't' array from the problem's range [6, 60].
num_points = len(df)
t_samples = np.linspace(6, 60, num_points)

# Obtaining target x and y values from the DataFrame
x_target = df['x'].values
y_target = df['y'].values

# --- 2. Define the Loss Function (L1 Distance) ---

# Parameters [theta_rad, M, X] and returns the total L1 loss.
def calculate_loss(params):
    theta_rad, M, X = params
    t = t_samples
    
    # Calculating predicted x and y using the parametric equations
    cos_theta = np.cos(theta_rad)
    sin_theta = np.sin(theta_rad)
    exp_Mt = np.exp(M * t)
    sin_03t = np.sin(0.3 * t)
    x_pred = (t * cos_theta) - (exp_Mt * sin_03t * sin_theta) + X
    y_pred = (42 + t * sin_theta) + (exp_Mt * sin_03t * cos_theta)
    # Calculating total L1 loss
    loss = np.sum(np.abs(x_pred - x_target) + np.abs(y_pred - y_target))
    
    return loss

# --- 3. Define Parameter Bounds ---

# Bounds: [ (min_theta_rad, max_theta_rad), (min_M, max_M), (min_X, max_X) ]
min_theta_rad = 0.0
max_theta_rad = 50.0 * (np.pi / 180.0)

min_M = -0.05
max_M = 0.05

min_X = 0.0
max_X = 100.0

bounds = [(min_theta_rad, max_theta_rad), (min_M, max_M), (min_X, max_X)]

print("Starting optimization... This may take a moment.")

# --- 4. Run the Optimization ---

# Using differential_evolution for its robustness in global optimization.
result = differential_evolution(
    calculate_loss,
    bounds,
    seed=42,      # For reproducible results
    polish=True,  # Refines the solution at the end
    disp=True     # Shows convergence updates
)

# --- 5. Print The Final Results ---

print("\n--- Optimization Complete ---")
if result.success:
    print("Optimization was successful.")
    best_params = result.x
    min_loss = result.fun

    print(f"\nMinimum L1 Loss found: {min_loss}")

    # Separating the optimal parameters
    theta_rad_opt = best_params[0]
    M_opt = best_params[1]
    X_opt = best_params[2]

    # Converting optimal theta back to degrees for clarity
    theta_deg_opt = theta_rad_opt * (180.0 / np.pi)

    print("\n--- Optimal Parameters Found ---")
    print(f"  theta (degrees): {theta_deg_opt}")
    print(f"  theta (radians): {theta_rad_opt}")
    print(f"  M:               {M_opt}")
    print(f"  X:               {X_opt}")

else:
    print(f"Optimization was not successful: {result.message}")