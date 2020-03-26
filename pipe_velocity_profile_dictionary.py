# Author: Fatemeh Hadi
# Purpose: this dictionary returns pipe_ID, v_min and v_max based on a
# frozenset of node_1 and node_2 of the corresponding pipe as key.

import pandas as pd
from read_in_pipes import T_pipes

if_write = False

pipe_table = T_pipes

if if_write:
	print(pipe_table.shape)
	print("pipe_table",pipe_table,"\n")

nodes_zipped = zip(pipe_table.node_1,pipe_table.node_2)
nodes_zipped = [frozenset(i) for i in nodes_zipped] 
pipe_table['nodes'] = nodes_zipped
pipe_table.set_index('nodes',inplace=True)

pipe_info_zipped = zip(pipe_table.pipe_ID,pipe_table.length,pipe_table.v_min,pipe_table.v_max)
pipe_info = [i for i in pipe_info_zipped]
pipe_table['pipe_info'] = pipe_info

if if_write:
	print(pipe_table.shape)
	print("pipe_table",pipe_table,"\n")

pipe_dictionary_2 = pipe_table.loc[:,'pipe_info'].to_dict()

# unit test:
if __name__ == '__main__':

	temp = frozenset({'j_p6_n2_7922','j_p6_n2_7920'})
	print("Key",temp)
	print("pipe_dictionary_2",pipe_dictionary_2[temp][0])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][1])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][2])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][3])

	temp = frozenset({'j_p4_n2_2180','j_p4_n2_2158'})
	print("\nKey",temp)
	print("pipe_dictionary_2",pipe_dictionary_2[temp][0])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][1])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][2])
	print("pipe_dictionary_2",pipe_dictionary_2[temp][3])