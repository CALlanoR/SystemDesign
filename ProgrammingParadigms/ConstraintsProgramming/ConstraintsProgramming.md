# The CP-SAT Primer - Using and Understanding Google OR-Tools' CP-SAT Solver

## The basics of constraint programming (CP)
Similarly to the declarative example mentioned above, with CP we describe the desired result to a problem. This description is called a model. The main components of a model are variables and constraints. Variables represent what we are looking for, and each variable has an associated domain which is the set of values that this variable is allowed to take. Constraints describe relationships between variables.

## The three fundamental pillars are:
- **Variables**: The unknowns that the program must decide.
    - Example: Cell A1 in Sudoku.
- **Domains**: The possible values that a variable can take.
    - Example: Numbers from 1 to 9.
    - Key: In CP, the solver "prunes" (reduces) the domain. If it discovers that A1 cannot be 9, it removes it from the list of possibilities.
- **Constraints**: Rules that limit what values variables can take in relation to others.
    - Example: Value(A1) != Value(A2).
- **Solver**: The solver does not try all combinations by brute force (that would take millions of years). It uses:
    - **Propagation**: If A=1 and the rule is A < B, then B cannot be 1. The solver "propagates" this information throughout the system.
    - **Intelligent backtracking**: It tries one path; if it breaks a rule, it backtracks and tries another.

Example:
```python
# Our first problem has no deeper meaning, except for showing the basic workflow of creating the variables (x and y), adding the constraint x+y<=30 on them, setting the objective function (maximize 30x+50y), and obtaining a solution:

from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Variables
x = model.new_int_var(0, 100, "x")
y = model.new_int_var(0, 100, "y")

# Constraints
model.add(x + y <= 30)

# Objective
model.maximize(30 * x + 50 * y)

# Solve
solver = cp_model.CpSolver()
status_code = solver.solve(model)
status_name = solver.status_name()

# Print the solver status and the optimal solution.
print(f"{status_name} ({status_code})")
```

## The solver can return five different statuses:
Status	Code	Description
- **UNKNOWN**: 0, The solver has not run for long enough.
- **MODEL_INVALID**: 1, The model is invalid. You will rarely see that status.
- **FEASIBLE**: 2, The model has a feasible, but not necessarily optimal, solution. If your model does not have an objective, every feasible model will return OPTIMAL, which may be counterintuitive.
- **INFEASIBLE**: 3, The model has no feasible solution. This means that your constraints are too restrictive.
- **OPTIMAL**: 4, The model has an optimal solution. If your model does not have an objective, OPTIMAL is returned instead of FEASIBLE.
