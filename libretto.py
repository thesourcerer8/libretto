#!/usr/bin/env pytghon
# -*- coding: utf-8 -*-

import argparse, re, os, shutil, subprocess, sys, inspect 

import myConditionsAndResults as mcar
import myLibrarySetting as mls 
import myLogicCell as mlc
import myExport as me
import numpy as np
from char_comb import runCombIn1Out1, runCombIn2Out1, runCombIn3Out1, runCombIn4Out1,  runSpiceCombDelay, genFileLogic_trial1
from char_seq import runFlop, runSpiceFlopDelay, genFileFlop_trial1
from myFunc import my_exit

def main():
	parser = argparse.ArgumentParser(description='argument')
	parser.add_argument('-b','--batch', type=str, help='inport batch file')
	args = parser.parse_args()
	#print(args.batch)

	targetLib = mls.MyLibrarySetting() 

	# file open
	with open(args.batch, 'r') as f:
		lines = f.readlines()
		
		for line in lines:
			line = line.strip('\n')
#-- set function : common settings--#
			# set_lib_name
			if(line.startswith('set_lib_name')):
				targetLib.set_lib_name(line) 

			if(line.startswith('set_dotlib_name')):
				targetLib.set_dotlib_name(line) 

			if(line.startswith('set_verilog_name')):
				targetLib.set_verilog_name(line) 

			# set_cell_name_suffix
			elif(line.startswith('set_cell_name_suffix')):
				targetLib.set_cell_name_suffix(line) 

			# set_cell_name_prefix
			elif(line.startswith('set_cell_name_prefix')):
				targetLib.set_cell_name_prefix(line) 

			# set_voltage_unit
			elif(line.startswith('set_voltage_unit')):
				targetLib.set_voltage_unit(line) 

			# set_capacitance_unit
			elif(line.startswith('set_capacitance_unit')):
				targetLib.set_capacitance_unit(line) 

			# set_resistance_unit
			elif(line.startswith('set_resistance_unit')):
				targetLib.set_resistance_unit(line) 

			# set_time_unit
			elif(line.startswith('set_time_unit')):
				targetLib.set_time_unit(line) 

			# set_current_unit
			elif(line.startswith('set_current_unit')):
				targetLib.set_current_unit(line) 

			# set_leakage_power_unit
			elif(line.startswith('set_leakage_power_unit')):
				targetLib.set_leakage_power_unit(line) 

			# set_vdd_name
			elif(line.startswith('set_vdd_name')):
				targetLib.set_vdd_name(line) 

			# set_vss_name
			elif(line.startswith('set_vss_name')):
				#print(line)
				targetLib.set_vss_name(line) 

			# set_pwell_name
			elif(line.startswith('set_pwell_name')):
				#print(line)
				targetLib.set_pwell_name(line) 

			# set_nwell_name
			elif(line.startswith('set_nwell_name')):
				targetLib.set_nwell_name(line) 

#-- set function : characterization settings--#
			# set_process
			elif(line.startswith('set_process')):
				targetLib.set_process(line) 

			# set_temperature
			elif(line.startswith('set_temperature')):
				targetLib.set_temperature(line) 

			# set_vdd_voltage
			elif(line.startswith('set_vdd_voltage')):
				targetLib.set_vdd_voltage(line) 

			# set_vss_voltage
			elif(line.startswith('set_vss_voltage')):
				targetLib.set_vss_voltage(line) 

			# set_pwell_voltage
			elif(line.startswith('set_pwell_voltage')):
				targetLib.set_pwell_voltage(line) 

			# set_nwell_voltage
			elif(line.startswith('set_nwell_voltage')):
				targetLib.set_nwell_voltage(line) 

			# set_logic_threshold_high
			elif(line.startswith('set_logic_threshold_high')):
				targetLib.set_logic_threshold_high(line) 

			# set_logic_threshold_low
			elif(line.startswith('set_logic_threshold_low')):
				targetLib.set_logic_threshold_low(line) 

			# set_logic_high_to_low_threshold
			elif(line.startswith('set_logic_high_to_low_threshold')):
				targetLib.set_logic_high_to_low_threshold(line) 

			# set_logic_low_to_high_threshold
			elif(line.startswith('set_logic_low_to_high_threshold')):
				targetLib.set_logic_low_to_high_threshold(line) 

			# set_work_dir
			elif(line.startswith('set_work_dir')):
				targetLib.set_work_dir(line) 

			# set_simulator
			elif(line.startswith('set_simulator')):
				targetLib.set_simulator(line) 

			# set_energy_meas_low_threshold
			elif(line.startswith('set_energy_meas_low_threshold')):
				targetLib.set_energy_meas_low_threshold(line) 

			# set_energy_meas_high_threshold
			elif(line.startswith('set_energy_meas_high_threshold')):
				targetLib.set_energy_meas_high_threshold(line) 

			# set_energy_meas_time_extent
			elif(line.startswith('set_energy_meas_time_extent')):
				targetLib.set_energy_meas_time_extent(line) 

			# set_energy_meas_time_extent
			elif(line.startswith('set_operating_conditions')):
				targetLib.set_operating_conditions(line) 

#-- add function : common for comb. and seq. --#
			# add_cell
			elif(line.startswith('add_cell')):
				targetCell = mlc.MyLogicCell()
				targetCell.add_cell(line) 

			# add_slope
			elif(line.startswith('add_slope')):
				targetCell.add_slope(line) 

			# add_load
			elif(line.startswith('add_load')):
				targetCell.add_load(line) 

			# add_netlist
			elif(line.startswith('add_netlist')):
				targetCell.add_netlist(line) 

			# add_model
			elif(line.startswith('add_model')):
				targetCell.add_model(line) 

			# add_simulation_timestep
			elif(line.startswith('add_simulation_timestep')):
				targetCell.add_simulation_timestep(line) 

#-- add function : for seq. cell --#
			# add_flop
			elif(line.startswith('add_flop')):
				targetCell = mlc.MyLogicCell()
				targetCell.add_flop(line) 

			# add_clock_slope
			elif(line.startswith('add_clock_slope')):
				targetCell.add_clock_slope(line) 

			# add_simulation_setup_auto
			elif(line.startswith('add_simulation_setup_auto')):
				targetCell.add_simulation_setup_lowest('add_simulation_setup_lowest auto') 
				targetCell.add_simulation_setup_highest('add_simulation_setup_highest auto') 
				targetCell.add_simulation_setup_timestep('add_simulation_setup_timestep auto') 
			# add_simulation_setup_lowest
			elif(line.startswith('add_simulation_setup_lowest')):
				targetCell.add_simulation_setup_lowest(line) 
			# add_simulation_setup_highest
			elif(line.startswith('add_simulation_setup_highest')):
				targetCell.add_simulation_setup_highest(line) 
			# add_simulation_setup_timestep
			elif(line.startswith('add_simulation_setup_timestep')):
				targetCell.add_simulation_setup_timestep(line) 

			# add_simulation_hold_auto
			elif(line.startswith('add_simulation_hold_auto')):
				targetCell.add_simulation_hold_lowest('add_simulation_hold_lowest auto') 
				targetCell.add_simulation_hold_highest('add_simulation_hold_highest auto') 
				targetCell.add_simulation_hold_timestep('add_simulation_hold_timestep auto') 
			# add_simulation_hold_lowest
			elif(line.startswith('add_simulation_hold_lowest')):
				targetCell.add_simulation_hold_lowest(line) 
			# add_simulation_hold_highest
			elif(line.startswith('add_simulation_hold_highest')):
				targetCell.add_simulation_hold_highest(line) 
			# add_simulation_hold_timestep
			elif(line.startswith('add_simulation_hold_timestep')):
				targetCell.add_simulation_hold_timestep(line) 

#-- execution --#
			# initialize
			elif(line.startswith('create')):
				initializeFiles(targetLib, targetCell) 

			# create
			elif(line.startswith('characterize')):
				harnessList2 = characterizeFiles(targetLib, targetCell) 
				os.chdir("../")
				#print(len(harnessList))

			# export
			elif(line.startswith('export')):
				me.exportFiles(targetLib, targetCell, harnessList2) 

			# exit
			elif(line.startswith('quit') or line.startswith('exit')):
				me.exitFiles(targetLib) 



def initializeFiles(targetLib, targetCell):
	# initialize working directory
	if os.path.exists(targetLib.work_dir):
		shutil.rmtree(targetLib.work_dir)
	os.mkdir(targetLib.work_dir)

def characterizeFiles(targetLib, targetCell):
	print ("characterize\n")
	os.chdir(targetLib.work_dir)

	# Branch to each logic function
	if(targetCell.logic == 'INV'):
		print ("INV\n")
		# [in0, in1, out0]
		expectationList2 = [['01','10'],['10','01']]
		return runCombIn1Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'AND2'):
		print ("AND2\n")
		# [in0, in1, out0]
		expectationList2 = [['01','1','01'],['10','1','10'],['1','01','01'],['1','10','10']]
		return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

	elif(targetCell.logic == 'NAND2'):
		print ("NAND2\n")
		# [in0, in1, out0]
		expectationList2 = [['01','1','10'],['10','1','01'],['1','01','10'],['1','10','01']]
		return runCombIn2Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'NAND3'):
		print ("NAND3\n")
		# [in0, in1, in2, out0]
		expectationList2 = [['01','1','1','10'],['10','1','1','01'],\
												['1','01','1','10'],['1','10','1','01'],\
												['1','1','01','10'],['1','1','10','01']]
		return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'NAND4'):
		print ("NAND4\n")
		# [in0, in1, in2, out0]
		expectationList2 = [['01','1','1','1','10'],['10','1','1','1','01'],\
												['1','01','1','1','10'],['1','10','1','1','01'],\
												['1','1','01','1','10'],['1','1','10','1','01'],\
												['1','1','1','01','10'],['1','1','1','10','01']]
		return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'NOR2'):
		print ("NOR2\n")
		# [in0, in1, out0]
		expectationList2 = [['01','0','10'],['10','0','01'],['0','01','10'],['0','10','01']]
		return runCombIn2Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'NOR3'):
		print ("NOR3\n")
		# [in0, in1, out0]
		expectationList2 = [['01','0','0','10'],['10','0','0','01'],\
												['0','01','0','10'],['0','10','0','01'],\
												['0','0','01','10'],['0','0','10','01']]
		return runCombIn3Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'NOR4'):
		print ("NOR4\n")
		# [in0, in1, out0]
		expectationList2 = [['01','0','0','0','10'],['10','0','0','0','01'],\
												['0','01','0','0','10'],['0','10','0','0','01'],\
												['0','0','01','0','10'],['0','0','10','0','01'],\
												['0','0','0','01','10'],['0','0','0','10','01']]
		return runCombIn4Out1(targetLib, targetCell, expectationList2,"neg")

	elif(targetCell.logic == 'XOR2'):
		print ("XOR2\n")
		# [in0, in1, out0]
		expectationList2 = [['01','0','01'],['10','0','10'],\
												['01','1','10'],['10','1','01'],\
												['0','01','01'],['0','10','10'],\
												['1','01','10'],['1','10','01']]
		return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

	elif(targetCell.logic == 'XNOR2'):
		print ("XNOR2\n")
		# [in0, in1, out0]
		expectationList2 = [['01','0','10'],['10','0','01'],\
												['01','1','01'],['10','1','10'],\
												['0','01','10'],['0','10','01'],\
												['1','01','01'],['1','10','10']]
		return runCombIn2Out1(targetLib, targetCell, expectationList2,"pos")

	elif(targetCell.logic == 'SEL2'):
		print ("SEL2\n")
		# [in0, in1, sel, out]
		expectationList2 = [['01','0','0','01'],['10','0','0','10'],\
												['0','01','1','01'],['0','10','1','10'],\
												['1','0','01','10'],['1','0','10','01'],\
												['0','1','01','01'],['0','1','10','10']]
		return runCombIn3Out1(targetLib, targetCell, expectationList2,"pos")


	# Branch to sequencial logics
	# DFF, both unate, async reset, async set
	elif(targetCell.logic == 'DFF_PCPU_NRNS'):
		print ("DFF, positive clock, positive unate, async neg-reset, async neg-set\n")
		# D1 & C01 -> Q01 QN10
		# D0 & C01 -> Q10 QN01
		# R01      -> Q10 QN01
		# S01      -> Q01 QN10
		# 									 [D,   C,  S,   R,    Q]
		expectationList2 = [['01','01','1', '1', '01'], \
										  	['10','01','1', '1', '10'], \
										  	['0','0','10', '1', '01'], \
										  	['0','0', '1','10', '10']]
		# run spice deck for flop
		return runFlop(targetLib, targetCell, expectationList2)

	else:
		print ("Target logic:"+targetCell.logic+" is not registered for characterization!\n")
		print ("Add characterization function for this program! -> die\n")
		my_exit()



if __name__ == '__main__':
 main()

