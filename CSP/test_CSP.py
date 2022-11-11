# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : test_CSP.py
# Class : COSC76
# Purpose :

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

# start = time.time()
# test = MapColoringCSP(australia, 'adj_list', ['r', 'g', 'b'], False, False, False)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(australia, 'adj_list', ['r', 'g', 'b'], True, True, False)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)

# start = time.time()
# test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], False, False, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], False, True, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], True, False, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(us, 'adj_list', ['r', 'g', 'b', 'd'], True, True, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)

# start = time.time()
# test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], False, False, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], False, True, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], True, False, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)
#
# start = time.time()
# test = MapColoringCSP(map_3, 'node_edge_list', ['r', 'g', 'b', 'd'], True, True, True)
# test.translate_solution()
# # print(test.translate_solution())
# print(time.time() - start)

start = time.time()
test = CircuitCSP(circuit, 'dimensions', (3, 10), True, True, True)
test.translate_solution()
print(test.translate_solution())
print(time.time() - start)
