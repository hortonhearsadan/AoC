import time

import numpy as np

TESTSTRING = '''12345678'''
TESTSTRING2 = '''80871224585914546619083218645595'''
TESTSTRING3 = '''19617804207202209144916044189917'''
TESTSTRING4 = '''69317163492948606335995924319873'''
TESTSTRING5 = '''03036732577212944063491565474664'''
TESTSTRING6 = '''02935109699940807407585447034323'''
TESTSTRING7 = '''03081770884921959731165446850517'''
STRING = '''59766299734185935790261115703620877190381824215209853207763194576128635631359682876612079355215350473577604721555728904226669021629637829323357312523389374096761677612847270499668370808171197765497511969240451494864028712045794776711862275853405465401181390418728996646794501739600928008413106803610665694684578514524327181348469613507611935604098625200707607292339397162640547668982092343405011530889030486280541249694798815457170337648425355693137656149891119757374882957464941514691345812606515925579852852837849497598111512841599959586200247265784368476772959711497363250758706490540128635133116613480058848821257395084976935351858829607105310340'''


def get_matrix(base_pattern, input_length):
    matrix = np.zeros((input_length, input_length), dtype=int)
    for i in range(input_length):
        pattern = np.repeat(base_pattern, i + 1)
        while len(pattern) < input_length + 1:
            pattern = np.append(pattern, pattern)

        matrix[i] = pattern[1:input_length + 1]
    return matrix


def run1():
    string = STRING
    input_signal = np.array(list(string), dtype=int)
    base_pattern = np.array([0, 1, 0, -1], dtype=int)
    input_length = len(input_signal)
    base_pattern_matrix = get_matrix(base_pattern, input_length)
    for i in range(100):
        output_signal = base_pattern_matrix.dot(input_signal)
        input_signal = np.remainder(np.absolute(output_signal), 10)
    return ''.join(str(x) for x in input_signal[:8])


def run2():
    string = STRING
    offset = int(string[:7])
    input_signal = np.fromstring(string, dtype=np.int8) - 48  # weird fromstring behaviour so I minus 48 from each entry
    input_signal = np.tile(input_signal, 10000)
    reduced_input = input_signal[offset:][::-1]  # flip the array to work backwards
    for i in range(100):
        new_input = np.cumsum(reduced_input)  # a phase is the cumulative sum of the previous phase
        reduced_input = np.remainder(new_input, 10)  # full array mod
    return ''.join(str(x) for x in reduced_input[::-1][:8])  # did have np.absolute here but it wasnt required


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
