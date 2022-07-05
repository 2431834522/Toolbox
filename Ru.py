# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Ru.py
# Created on: 2022-07-02 15:44:26.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Ru <Instrument> <Input_series> <Output___Graph> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("E:/Projet Of Daryan/GDB/Daryan_Edited.gdb/DDAA_Toolbox")

# Script arguments
Instrument = arcpy.GetParameterAsText(0)
if Instrument == '#' or not Instrument:
    Instrument = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_B_760_2_1" # provide a default value if unspecified

Input_series = arcpy.GetParameterAsText(1)
if Input_series == '#' or not Input_series:
    Input_series = "SERIES=line:vertical DATA=E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_B_760_2_1 X=Date Y=RU SORT=DESC;GRAPH=general;LEGEND=general;AXIS=left TITLE=RU;AXIS=right;AXIS=bottom TITLE=Date;AXIS=top" # provide a default value if unspecified

Output___Graph = arcpy.GetParameterAsText(2)
if Output___Graph == '#' or not Output___Graph:
    Output___Graph = "C:\\Users\\Motasam\\Desktop\\Ru\\x" # provide a default value if unspecified

# Local variables:
Layer = "EP_B_760_2_1_Layer"
Layer_1 = Layer
Layer_2 = Layer_1
Layer_3 = Layer_2
Layer_4 = Layer_3
Seleced_Layer = "E:\\Projet Of Daryan\\GDB\\Daryan.gdb\\rexcvb"
Merged_File = "E:\\Projet Of Daryan\\Anallysis\\merge.gdb\\Merge_B"
Ouput__Map_of__parameter_distribiution__ = "E:\\Projet Of Daryan\\Anallysis\\Raster.gdb\\EP_RASTER_DD"

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(Instrument, Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Calculate Field
arcpy.CalculateField_management(Layer, "H", "[E_E] - [Z]", "VB", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(Layer_1, "γH", "[γ] * [H]", "VB", "")

# Process: Calculate Field (3)
arcpy.CalculateField_management(Layer_2, "P_kPa", "([G]*( [R0] - [R1] ))", "VB", "")

# Process: Calculate Field (4)
arcpy.CalculateField_management(Layer_3, "P_ton_m2", "( ([G]*( [R0] - [R1] ) )/9.81)", "VB", "")

# Process: Select Layer By Attribute
arcpy.Select_analysis(Layer_4, Seleced_Layer, "RU >  0.10040045048197985")

# Process: Make Graph
arcpy.MakeGraph_management("E:\\Projet Of Daryan\\GDB\\Graph.grf", Input_series, Output___Graph)

# Process: EP_Cross_Section_BB (2)
arcpy.gp.toolbox = "E:/Projet Of Daryan/GDB/Daryan_Edited.gdb/DDAA_Toolbox";
# Warning: the toolbox E:/Projet Of Daryan/GDB/Daryan_Edited.gdb/DDAA_Toolbox DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.Model222423(...) with arcpy.Model222423_ALIAS(...)
arcpy.gp.Model222423(Merged_File, "\"Date\" = date '2016-07-11 00:00:00'", "2", "P_ton_m2", Ouput__Map_of__parameter_distribiution__)
