import neuron
from neuron import h, gui
import time

start_time = time.time()

h.xopen('main_CB.hoc')
h.xopen('iclamp_2.hoc')

for ii in range (1,81):
    for v in range (31,39):
        for x in range (31,39):
            h.node[x].L=1
            h.node[x].diam=0.72
            h.internode[x].L=60
            h.node[x].g_pas=0.08
            h.node[x].cm=0.9
            h.node[x].gbar_na16=50000
        for x in range(31,v):
            h.node[x].L=ii
            h.node[x].diam=0.902
            h.internode[x].L= 60 - ii
            h.node[x].g_pas=0.08
            h.node[x].cm=0.9
            h.node[x].gbar_na16=34000
        import csv
        h('{run()}')
        h('{node_length()}')

h('{close_file()}')


total_time = (time.time() - start_time)
print('Total time to run ' + str(total_time/60) + ' minutes')
