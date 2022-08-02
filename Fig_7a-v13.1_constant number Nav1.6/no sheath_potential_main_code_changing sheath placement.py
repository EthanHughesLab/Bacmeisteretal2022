import neuron
from neuron import h, gui
import time

start_time = time.time()

h.xopen('main_CB.hoc')
h.xopen('iclamp_2.hoc')

h.node[31].L=240
import csv

h('{run()}')
h('{node_length()}')

h('{close_file()}')


total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time/60) + ' minutes')
