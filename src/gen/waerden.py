#!/usr/bin/python3

# Usage: python3 waerden.py j k n
#
# Generates the Waerden clauses described in Knuth 7.2.2.2 (10). These are
# satisfiable exactly when n < W(j,k), for the function W(j,k). Knuth lists the
# known non-trivial values of W(j,k) like W(3,3) = 9 and W(3,4) = 18.
#
# These Waerden clauses with parameters j, k, and n encode the following
# problem: Can a binary sequence of length n be created that contains no j
# equally spaced zeros and no k equally spaced ones? "equally spaced" here just
# means that there's some i and j > 0 such that x_i, x_{i+j}, x_{i+2*j}, ... are
# all equal, for example 111 is an equally spaced sequence of ones with j=1 or
# 10101 is an equally spaced sequence of ones with j=2. `waerden.py 3 3 8` is
# satisfiable, for example, because 00110011 is a sequence of length 8 that has
# no 3 equally spaced zeros and no 3 equally spaced ones.

import io
import math
import sys

def waerden(j, k, n):
    buffer = io.StringIO()
    n_clauses = 0
    for sign, clause_len in (('', j), ('-', k)):
        for jump in range(1, int(math.ceil(n / (clause_len - 1)))):
            for start in range(1,n - (clause_len - 1) * jump + 1):
                for x in range(clause_len):
                    buffer.write("{0}{1} ".format(sign, start + x*jump))
                buffer.write('0\n')
                n_clauses += 1
    return 'p cnf {0} {1}\n'.format(n, n_clauses) + buffer.getvalue()

if __name__ == '__main__':
    try:
        assert(len(sys.argv) == 4)
        j, k, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except:
        print('Usage: "waerden.py j k n" for integer j, k, n')
        sys.exit(-1)
    print("c Generated by waerden.py {0} {1} {2}".format(j,k,n))
    print("c Generator source: github.com/aaw/sat/gen/waerden.py")
    print(waerden(j, k, n))
