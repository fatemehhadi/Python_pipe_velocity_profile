# Author: Fatemeh Hadi
# Purpose: the code returns velocity profile for a given iteration, profile
# type and array of pipe_IDs.
# Note: the all_node_indexes includes the node_index of end sensors as well
# and not just the inBetween_node_indexes. The rest of the code is self
# explanatory.

import numpy as np

def pipe_velocity_profile_uniform(ndiv,velocity_iter,\
	all_node_indexes,if_write):

	from pipe_velocity_profile_dictionary import pipe_dictionary_2

	num_pipes = len(all_node_indexes)-1
	velocities = np.full(num_pipes, np.nan)

	for pipe_indx in range(num_pipes):
		
		nodes = [all_node_indexes[pipe_indx],all_node_indexes[pipe_indx+1]]
		nodes = frozenset(nodes)

		v_min = pipe_dictionary_2[nodes][2]
		v_max = pipe_dictionary_2[nodes][3]
		du = (v_max-v_min)/ndiv
		velocities[pipe_indx] = v_min + velocity_iter*du

		if if_write:
			print("pipe_indx =",pipe_indx)
			print("nodes =",nodes)
			print("pipe_dictionary_2 =",pipe_dictionary_2[nodes])
			print("velocities[",pipe_indx,"] =",velocities[pipe_indx],"\n")

	return velocities

def pipe_velocity_profile_normal(ndiv,velocity_iter,\
	all_node_indexes,if_write):

	from scipy.stats import norm

	from pipe_velocity_profile_dictionary import pipe_dictionary_2

	num_pipes = len(all_node_indexes)-1
	velocities = np.full(num_pipes, np.nan)

	for pipe_indx in range(num_pipes):
		
		nodes = [all_node_indexes[pipe_indx],all_node_indexes[pipe_indx+1]]
		nodes = frozenset(nodes)

		# v_min = pipe_dictionary_2[nodes][2]
		# v_max = pipe_dictionary_2[nodes][3]
		# du = (v_max-v_min)/ndiv
		# velocities[pipe_indx] = v_min + velocity_iter*du

		# if if_write:
		# 	print("pipe_indx =",pipe_indx)
		# 	print("nodes =",nodes)
		# 	print("pipe_dictionary_2 =",pipe_dictionary_2[nodes])
		# 	print("velocities[",pipe_indx,"] =",velocities[pipe_indx],"\n")

	return velocities

def pipe_velocity_profile(pipe_velocity_profile_type,ndiv,velocity_iter,\
	all_node_indexes,if_write):

	if pipe_velocity_profile_type == "uniform":
		velocities = pipe_velocity_profile_uniform(ndiv,velocity_iter,\
			all_node_indexes,if_write)
	elif pipe_velocity_profile_type == "normal":
		velocities = pipe_velocity_profile_normal(ndiv,velocity_iter,\
			all_node_indexes,if_write)		

	return velocities

# unit test:
if __name__ == '__main__':

	import pandas as pd
	from read_in_nodes import T_nodes 
	from query_inBeween_nodes import query_inBeween_nodes

	if_write = True

	T_sensors = pd.read_csv('burst_localization/'+'sensors_updated.csv',\
		index_col = 0)

	sensor_pairs = [[8,4],[9,3]]
	sensor_pairs = np.reshape(sensor_pairs,\
		(-1,len(sensor_pairs)))
	
	num_sensor_pairs = len(sensor_pairs)
	for index_sensor_pair in range(num_sensor_pairs):

		sensor_pairs[index_sensor_pair,:].sort()
		inBetween_node_xy,inBetween_node_indexes = query_inBeween_nodes(\
			sensor_pairs[index_sensor_pair,0],\
			sensor_pairs[index_sensor_pair,1],\
			T_nodes,T_sensors)

		sensor_node_1 = T_sensors.loc[sensor_pairs[index_sensor_pair,0],\
		'node_index']
		sensor_node_2 = T_sensors.loc[sensor_pairs[index_sensor_pair,1],\
		'node_index']

		if if_write:
			print("\nsensor_pairs",sensor_pairs[index_sensor_pair,:])
			print("sensor node 1 =",sensor_node_1)
			print("sensor node 2 =",sensor_node_2)

		print("inBetween_node_indexes \n",\
			inBetween_node_indexes,"\n")
		print("inBetween_node_xy \n",\
			inBetween_node_xy,"\n")

		all_node_indexes = np.append(sensor_node_1,inBetween_node_indexes)
		if if_write:
			print("all_node_indexes \n",all_node_indexes,"\n")
		all_node_indexes = np.append(all_node_indexes,sensor_node_2)
		if if_write:
			print("all_node_indexes \n",all_node_indexes,"\n")

		velocities = pipe_velocity_profile("uniform",100,50,\
			all_node_indexes,True)

		if if_write:
			print("velocities \n",velocities,"\n")