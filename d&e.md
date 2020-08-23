# Definitions & Examples

## Logical Operators

### AND

$A ∧ B$ is true if and only if $A$ is true and $B$ is true.

### OR

$A ∨ B$ is true if $A$ is true, or if $B$ is true, or if both $A$ and $B$ are true.

## Unit Clause

> A unit clause is a clause which has exactly one literal which is still unassigned, and the other literals are all assigned to false.

The importance of this clause is that if all the current assignment is valid, you can determine what is the value of the variable which is in the unassigned literal - because the literal must be true.

**For Example**
___

If we have the formula

$(x_1 ∨ x_2 ∨ x_3) ∧ (\bar{x_1} ∨ \bar{x_4} ∨ x_5) ∧ (\bar{x_1} ∨ x_4)$

And we have already assigned 

$x_1 = true,\ x_4 = true$

Then $(\bar{x_1} ∨ \bar{x_4} ∨ x_5)$ is a *unit clause*, because you must assign $x_5 = true$ in order to satisfy this clause in its current partial assignment.
