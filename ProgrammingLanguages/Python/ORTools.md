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

Here's a typical optimization problem. Suppose that a shipping company delivers packages to its customers using a fleet of trucks. Every day, the company must assign packages to trucks, and then choose a route for each truck to deliver its packages. Each possible assignment of packages and routes has a cost, based on the total travel distance for the trucks, and possibly other factors as well. The problem is to choose the assignments of packages and routes that has the least cost.

Like all optimization problems, this problem has the following elements:

- **The objective**—the quantity you want to optimize. In the example above, the objective is to minimize cost. To set up an optimization problem, you need to define a function that calculates the value of the objective for any possible solution. This is called the objective function. In the preceding example, the objective function would calculate the total cost of any assignment of packages and routes.

- **An optimal solution** is one for which the value of the objective function is the best. ("Best" can be either a maximum or a minimum.)

- **The constraints**—restrictions on the set of possible solutions, based on the specific requirements of the problem. For example, if the shipping company can't assign packages above a given weight to trucks, this would impose a constraint on the solutions.

- **A feasible solution** is one that satisfies all the given constraints for the problem, without necessarily being optimal.

The first step in solving an optimization problem is identifying the objective and constraints.