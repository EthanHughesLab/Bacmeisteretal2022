import neuron
from neuron import h, gui
import time

start_time = time.time()

h.xopen('main_CB.hoc')
h.xopen('iclamp_2.hoc')

h.node[35].L=1
h.node[35].diam=0.72
h.node[35].g_pas=0.03
h.node[35].gbar_na16=34000

import csv
h('{run()}')
h('{node_length()}')

h('{close_file()}')


total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time/60) + ' minutes')
