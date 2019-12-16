#cython: boundscheck=False, wraparound=False, nonecheck=False
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def compute(initial_input, int iterations, int r1, int r2, reps=False):
    cdef int[:] input = initial_input.copy()
    cdef int r, i, op_int
    cdef Py_ssize_t s, start, z,x,y
    cdef Py_ssize_t first=1, second=2, third=3,

    if reps:
        input[first] = r1
        input[second]= r2

    for i in range(iterations):
        start = i * 4
        op_int = input[start]
        if op_int == 99:
            return input
        # op = get_operator(op_int)
        x = input[start + first]
        y = input[start + second]
        z = input[start + third]

        c = input[x]
        d = input[y]
        if op_int ==1:
            input[z] = c + d
        elif op_int == 2:
            input[z] = c * d

    return input

# print(compute([1, 0, 0, 0, 99]))
# print(compute([2, 3, 0, 3, 99]))
# print(compute([2, 4, 4, 5, 99, 0]))
# print(compute([1, 1, 1, 4, 99, 5, 6, 0, 99]))

# a = time.time()
# array = compute(input, replacements)
# print('Part 1', array[0])


# a = time.time()
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)

def iterate(input):
    cdef int X = 100
    cdef int Y = 100
    cdef int x, y
    cdef int target = 19690720
    cdef Py_ssize_t zero = 0
    cdef int iterations = 42

    for x in range(X):
        for y in range(Y):
            array = compute(input,iterations, x,y, True)
            if array[zero] == target:
                # print('Part 2', x, y, 100 * x + y)
                # print(time.time() - a)
                return

# iterate(input)
