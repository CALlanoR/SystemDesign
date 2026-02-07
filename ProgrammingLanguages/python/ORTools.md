# OR-Tools
OR-Tools is open source software for combinatorial optimization, which seeks to find the best solution to a problem out of a very large set of possible solutions. Here are some examples of problems that OR-Tools solves:

- **Vehicle routing**: Find optimal routes for vehicle fleets that pick up and deliver packages given constraints (e.g., "this truck can't hold more than 20,000 pounds" or "all deliveries must be made within a two-hour window").
- **Scheduling**: Find the optimal schedule for a complex set of tasks, some of which need to be performed before others, on a fixed set of machines, or other resources.
- **Bin packing**: Pack as many objects of various sizes as possible into a fixed number of bins with maximum capacities.

In most cases, problems like these have a vast number of possible solutions—too many for a computer to search them all. To overcome this, OR-Tools uses state-of-the-art algorithms to narrow down the search set, in order to find an optimal (or close to optimal) solution.

OR-Tools includes solvers for:

- **Constraint Programming**: A set of techniques for finding feasible solutions to a problem expressed as constraints (e.g., a room can't be used for two events simultaneously, or the distance to the crops must be less than the length of the hose, or no more than five TV shows can be recorded at once).
- **Linear and Mixed-Integer Programming**: The Glop linear optimizer finds the optimal value of a linear objective function, given a set of linear inequalities as constraints (e.g., assigning people to jobs, or finding the best allocation of a set of resources while minimizing cost). Glop and the mixed-integer programming software SCIP are also available via the Google Apps Script Optimization Service.
- **Vehicle Routing**: A specialized library for identifying best vehicle routes given constraints.
- **Graph Algorithms**: Code for finding shortest paths in graphs, min-cost flows, max flows, and linear sum assignments.

## Get Started with OR-Tools for Python
### What is an optimization problem?

The goal of optimization is to find the best solution to a problem out of a large set of possible solutions. (Sometimes you'll be satisfied with finding any feasible solution; OR-Tools can do that as well.)