# Ideas

## General Program Plan

1. Read input of DIMACS file
2. Determine number of clauses, vars and literals. Extend their respective vectors to match.
3. (Optional) Propagate all clauses and simplify the problem.
4. Begin `solve()` function
5. Assign values to each variable until we hit a conflict.
6. `Backtrack()` to the previous assignment and force the opposite assignment.
7. If assignment results in true, return SAT.
8. If not, `backtrack()` further and force opposite assignment.
9. Repeat steps 6, 7 and 8 until a satisfying assignment has been found.
10. If no satisfying assignment has been found, the problem is deemed unsatisfiable.

## Ideas from other implementations.

* If time allows, possibility of two watches literals may be implemented.
