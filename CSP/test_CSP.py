# Author : Daniel Carstensen
# Date : 11/12/2022
# File name : test_CSP.py
# Class : COSC76
# Purpose : test MapColoringCSP and CircuitCSP for various inputs

from MapColoringCSP import MapColoringCSP
from CircuitCSP import CircuitCSP
import time


text = open('australia.txt')
australia = text.read()
text.close()

text = open('us.txt')
us = text.read()
text.close()

text = open('map_1.txt')
map_1 = text.read()
text.close()

text = open('map_2.txt')
map_2 = text.read()
text.close()

text = open('map_3.txt')
map_3 = text.read()
text.close()

text = open('circuit.txt')
circuit = text.read()
text.close()

# maps: australia, us, map_1, map_2, map_3
# use CSP with various configurations of heuristics

# australia
start = time.time()
test = MapColoringCSP(australia, 'adj_list', ['r', 'g', 'b'], False, False, False)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)

# us
start = time.time()
test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], False, False, True)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], False, True, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], True, False, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], True, True, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)


# map 1
start = time.time()
test = MapColoringCSP(map_1, 'node_edge_list', ['r', 'g', 'b', 'd'], False, False, True)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)

# map 2
start = time.time()
test = MapColoringCSP(map_2, 'node_edge_list', ['r', 'g', 'b', 'd'], False, False, True)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)

# map 3
start = time.time()
test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], False, False, True)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], False, True, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], True, False, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)

start = time.time()
test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], True, True, True)
test.translate_solution()
# print(test.translate_solution())
print(time.time() - start)


# circuit
start = time.time()
test = CircuitCSP(circuit, 'dimensions', (10, 3), True, True, True)
print(test.translate_solution())
test.print_solution()
print(time.time() - start)
