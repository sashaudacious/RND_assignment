# R&D / AI Assignment: Parametric Curve Fitting

This repository contains the solution for the Research and Development / AI assignment. The goal of this assignment is to find the unknown parameters ($\theta$, $M$, $X$) of a given parametric equation to best fit a target dataset.

---

## 🚀 How to Run Locally

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

* Python 3.7 or newer.
* The `xy_data.csv` file must be in the same root folder as the Python script.

### 2. Dependencies

The project requires the following Python libraries:
* `pandas`
* `numpy`
* `scipy`

You can install them all using `pip`:
```bash
pip install pandas numpy scipy
````

### 3\. Run the Script

Once the dependencies are installed, you can run the solution from your terminal:

```bash
python solve.py
```

*(Note: If `solve.py` is not the name of your script, replace it with the correct filename, e.g., `python main.py`)*

The script will execute the optimization process and print the final, optimal parameters to your console.

-----

## 🎯 Final Answer

Based on the optimization, the best-fit values for the unknown parameters are:

  * **$\theta$ (theta) in degrees:** `28.14097063118018`
  * **$\theta$ (theta) in radians:** `0.491152592221121`
  * **$M$:** `0.021249625918205495`
  * **$X$:** `54.90719550926761`

-----

## 🧠 Methodology & Step-by-Step Explanation

### Methodology

This problem is a **parameter estimation** (or curve-fitting) task. The core methodology is to use a numerical optimization algorithm to find the set of parameters ($\theta$, $M$, $X$) that **minimizes the error** between the curve produced by the equations and the target data.

The assessment criteria specified the error metric to be the **L1 Distance** (or Manhattan distance). Therefore, the optimization strategy is to minimize this L1 loss. The `scipy.optimize.differential_evolution` algorithm was chosen for this task due to its effectiveness in global optimization problems with defined bounds.

### Step-by-Step Explanation

1.  **Step 1: Data Preparation**

      * The target data was loaded from the `xy_data.csv` file using the `pandas` library.
      * The `x` and `y` columns were extracted into `numpy` arrays, which serve as our `x_target` and `y_target` values.
      * The problem states the parameter $t$ ranges from 6 to 60. A corresponding `t_samples` array of 1,500 points (to match the 1,500 data points) was created using `numpy.linspace(6, 60, 1500)`. This ensures each $(x, y)$ pair is correctly mapped to a $t$ value.

2.  **Step 2: Defining the Loss Function**

      * A Python function, `calculate_loss`, was defined to quantify the error for any given set of parameters.
      * This function takes an array `[theta_rad, M, X]` as input.
      * **Important:** It converts $\theta$ from degrees to radians, as required by all `numpy` trigonometric functions.
      * It calculates the `x_pred` and `y_pred` values for all $t$ samples using the given parametric equations.
      * It then computes the L1 distance between the predicted and target points, as per the formula:
        $$L(\theta, M, X) = \sum_{i} \left( |x_{\text{pred}, i} - x_{\text{target}, i}| + |y_{\text{pred}, i} - y_{\text{target}, i}| \right)$$
      * This function returns the total loss $L$ as a single number.

3.  **Step 3: Optimization**

      * The `scipy.optimize.differential_evolution` function was used to find the minimum of our `calculate_loss` function.
      * This function was given the specific **bounds** for each variable as defined in the assignment:
          * `theta (radians)`: `(0, 0.8727)` (which is $0^\circ$ to $50^\circ$)
          * `M`: `(-0.05, 0.05)`
          * `X`: `(0, 100)`
      * `differential_evolution` works by intelligently testing many combinations of parameters within these bounds, iteratively "evolving" the population of solutions towards the set that produces the lowest L1 loss.

4.  **Step 4: Execution & Results**

      * Running the script executes this optimization.
      * After the algorithm converges, it returns the `result` object.
      * The final parameters (`result.x`) and the final loss (`result.fun`) are extracted and printed to the console. The values in the "Final Answer" section are the direct output of this process.

<!-- end list -->

```
```
