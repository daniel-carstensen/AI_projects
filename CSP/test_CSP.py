# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : test_CSP.py
# Class : COSC76
# Purpose :

from MapColoringCSP import MapColoringCSP
import time


adj_tests = []
node_edge_tests = []

# text = open('australia.txt')
# australia = text.read()
# adj_tests.append(australia)
# text.close()

text = open('us.txt')
us = text.read()
adj_tests.append(us)
text.close()

# text = open('map_1.txt')
# map_1 = text.read()
# node_edge_tests.append(map_1)
# text.close()
#
# text = open('map_2.txt')
# map_2 = text.read()
# node_edge_tests.append(map_2)
# text.close()

text = open('map_3.txt')
map_3 = text.read()
node_edge_tests.append(map_3)
text.close()

for test_input in adj_tests:
    start = time.time()
    test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], False, False, True)
    # print(test.translate_solution())
    print(time.time() - start)

for test_input in adj_tests:
    start = time.time()
    test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], False, True, True)
    # print(test.translate_solution())
    print(time.time() - start)

for test_input in adj_tests:
    start = time.time()
    test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], True, True, True)
    # print(test.translate_solution())
    print(time.time() - start)

# for test_input in node_edge_tests:
#     start = time.time()
#     test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], False, False, True)
#     # print(test.translate_solution())
#     print(time.time() - start)
#
# for test_input in node_edge_tests:
#     start = time.time()
#     test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], False, True, True)
#     # print(test.translate_solution())
#     print(time.time() - start)
#
# for test_input in node_edge_tests:
#     start = time.time()
#     test = MapColoringCSP(test_input, 'adj_list', ['r', 'g', 'b', 'd'], True, True, True)
#     # print(test.translate_solution())
#     print(time.time() - start)
