# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# PC_Cross_Section_BB.py
# Created on: 2022-07-02 15:47:09.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: PC_Cross_Section_BB <Date> <PC_Merge_B> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Date = arcpy.GetParameterAsText(0)
if Date == '#' or not Date:
    Date = "\"Date\" = date '2016-07-11 00:00:00'" # provide a default value if unspecified

PC_Merge_B = arcpy.GetParameterAsText(1)
if PC_Merge_B == '#' or not PC_Merge_B:
    PC_Merge_B = "E:\\Projet Of Daryan\\Anallysis\\merge.gdb\\PC_Merge_B" # provide a default value if unspecified

# Local variables:
PCT_B_760_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_760_1_1_1"
PCT_B_760_1_1_Layer = "PCT_B_760_1_1_1_Layer"
Output_Layer_Name__6_ = PCT_B_760_1_1_Layer
PCS_B_760_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCS_B_760_1_1"
PCS_B_760_1_Layer = "PCS_B_760_1_1_Layer"
Output_Layer_Name__7_ = PCS_B_760_1_Layer
PCQ_B_815_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCQ_B_815_1_1_1"
PCQ_B_815_1_1_Layer = "PCQ_B_815_1_1_1_Layer"
Output_Layer_Name__8_ = PCQ_B_815_1_1_Layer
PCQ_B_790_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCQ_B_790_1_1_1"
PCQ_B_790_1_1_Layer = "PCQ_B_790_1_1_1_Layer"
Output_Layer_Name__9_ = PCQ_B_790_1_1_Layer
PCQ_B_760_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCQ_B_760_1_1_1"
PCQ_B_760_1_1_Layer = "PCQ_B_760_1_1_1_Layer"
Output_Layer_Name__10_ = PCQ_B_760_1_1_Layer
PCT_B_760_2_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_760_2_1_1"
PCT_B_760_2_1_Layer = "PCT_B_760_2_1_1_Layer"
Output_Layer_Name__5_ = PCT_B_760_2_1_Layer
PCT_B_760_3_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_760_3_1_1"
PCT_B_760_3_1_Layer = "PCT_B_760_3_1_1_Layer"
Output_Layer_Name__4_ = PCT_B_760_3_1_Layer
PCT_B_790_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_790_1_1_1"
PCT_B_790_1_1_Layer = "PCT_B_790_1_1_1_Layer"
Output_Layer_Name__3_ = PCT_B_790_1_1_Layer
PCT_B_790_2_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_790_2_1_1"
PCT_B_790_2_1_Layer = "PCT_B_790_2_1_1_Layer"
Output_Layer_Name__2_ = PCT_B_790_2_1_Layer
PCT_B_815_1_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\PC_Cross_Section\\PCT_B_815_1_1_1"
PCT_B_815_1_1_Layer = "PCT_B_815_1_1_1_Layer"
Output_Layer_Name = PCT_B_815_1_1_Layer

# Process: Make Feature Layer (6)
arcpy.MakeFeatureLayer_management(PCT_B_760_1_1_1, PCT_B_760_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (6)
arcpy.SelectLayerByAttribute_management(PCT_B_760_1_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (7)
arcpy.MakeFeatureLayer_management(PCS_B_760_1_1, PCS_B_760_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (7)
arcpy.SelectLayerByAttribute_management(PCS_B_760_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (8)
arcpy.MakeFeatureLayer_management(PCQ_B_815_1_1_1, PCQ_B_815_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (8)
arcpy.SelectLayerByAttribute_management(PCQ_B_815_1_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (9)
arcpy.MakeFeatureLayer_management(PCQ_B_790_1_1_1, PCQ_B_790_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (9)
arcpy.SelectLayerByAttribute_management(PCQ_B_790_1_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (10)
arcpy.MakeFeatureLayer_management(PCQ_B_760_1_1_1, PCQ_B_760_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (10)
arcpy.SelectLayerByAttribute_management(PCQ_B_760_1_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (5)
arcpy.MakeFeatureLayer_management(PCT_B_760_2_1_1, PCT_B_760_2_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (5)
arcpy.SelectLayerByAttribute_management(PCT_B_760_2_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (4)
arcpy.MakeFeatureLayer_management(PCT_B_760_3_1_1, PCT_B_760_3_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (4)
arcpy.SelectLayerByAttribute_management(PCT_B_760_3_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(PCT_B_790_1_1_1, PCT_B_790_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (3)
arcpy.SelectLayerByAttribute_management(PCT_B_790_1_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(PCT_B_790_2_1_1, PCT_B_790_2_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(PCT_B_790_2_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(PCT_B_815_1_1_1, PCT_B_815_1_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;γ γ VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;γH γH VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;A_C A_C VISIBLE NONE")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(PCT_B_815_1_1_Layer, "NEW_SELECTION", Date)

# Process: Merge
arcpy.Merge_management("PCT_B_760_1_1_1_Layer;PCS_B_760_1_1_Layer;PCQ_B_815_1_1_1_Layer;PCQ_B_790_1_1_1_Layer;PCQ_B_760_1_1_1_Layer;PCT_B_760_2_1_1_Layer;PCT_B_760_3_1_1_Layer;PCT_B_790_1_1_1_Layer;PCT_B_790_2_1_1_Layer;PCT_B_815_1_1_1_Layer", PC_Merge_B, "OBJECTID \"OBJECTID\" true true false 10 Long 0 10 ,First,#,PCQ_B_760_1_1_1_Layer,OBJECTID,-1,-1,PCQ_B_790_1_1_1_Layer,OBJECTID,-1,-1,PCQ_B_815_1_1_1_Layer,OBJECTID,-1,-1,PCS_B_760_1_1_Layer,OBJECTID,-1,-1,PCT_B_760_1_1_1_Layer,OBJECTID,-1,-1,PCT_B_760_2_1_1_Layer,OBJECTID,-1,-1,PCT_B_760_3_1_1_Layer,OBJECTID,-1,-1,PCT_B_790_1_1_1_Layer,OBJECTID,-1,-1,PCT_B_790_2_1_1_Layer,OBJECTID,-1,-1,PCT_B_815_1_1_1_Layer,OBJECTID,-1,-1;Instrument \"Instrument\" true true false 254 Text 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,Instrument,-1,-1,PCQ_B_790_1_1_1_Layer,Instrument,-1,-1,PCQ_B_815_1_1_1_Layer,Instrument,-1,-1,PCS_B_760_1_1_Layer,Instrument,-1,-1,PCT_B_760_1_1_1_Layer,Instrument,-1,-1,PCT_B_760_2_1_1_Layer,Instrument,-1,-1,PCT_B_760_3_1_1_Layer,Instrument,-1,-1,PCT_B_790_1_1_1_Layer,Instrument,-1,-1,PCT_B_790_2_1_1_Layer,Instrument,-1,-1,PCT_B_815_1_1_1_Layer,Instrument,-1,-1;ID \"ID\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,ID,-1,-1,PCQ_B_790_1_1_1_Layer,ID,-1,-1,PCQ_B_815_1_1_1_Layer,ID,-1,-1,PCS_B_760_1_1_Layer,ID,-1,-1,PCT_B_760_1_1_1_Layer,ID,-1,-1,PCT_B_760_2_1_1_Layer,ID,-1,-1,PCT_B_760_3_1_1_Layer,ID,-1,-1,PCT_B_790_1_1_1_Layer,ID,-1,-1,PCT_B_790_2_1_1_Layer,ID,-1,-1,PCT_B_815_1_1_1_Layer,ID,-1,-1;X \"X\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,X,-1,-1,PCQ_B_790_1_1_1_Layer,X,-1,-1,PCQ_B_815_1_1_1_Layer,X,-1,-1,PCS_B_760_1_1_Layer,X,-1,-1,PCT_B_760_1_1_1_Layer,X,-1,-1,PCT_B_760_2_1_1_Layer,X,-1,-1,PCT_B_760_3_1_1_Layer,X,-1,-1,PCT_B_790_1_1_1_Layer,X,-1,-1,PCT_B_790_2_1_1_Layer,X,-1,-1,PCT_B_815_1_1_1_Layer,X,-1,-1;Y \"Y\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,Y,-1,-1,PCQ_B_790_1_1_1_Layer,Y,-1,-1,PCQ_B_815_1_1_1_Layer,Y,-1,-1,PCS_B_760_1_1_Layer,Y,-1,-1,PCT_B_760_1_1_1_Layer,Y,-1,-1,PCT_B_760_2_1_1_Layer,Y,-1,-1,PCT_B_760_3_1_1_Layer,Y,-1,-1,PCT_B_790_1_1_1_Layer,Y,-1,-1,PCT_B_790_2_1_1_Layer,Y,-1,-1,PCT_B_815_1_1_1_Layer,Y,-1,-1;S_N \"S_N\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,S_N,-1,-1,PCQ_B_790_1_1_1_Layer,S_N,-1,-1,PCQ_B_815_1_1_1_Layer,S_N,-1,-1,PCS_B_760_1_1_Layer,S_N,-1,-1,PCT_B_760_1_1_1_Layer,S_N,-1,-1,PCT_B_760_2_1_1_Layer,S_N,-1,-1,PCT_B_760_3_1_1_Layer,S_N,-1,-1,PCT_B_790_1_1_1_Layer,S_N,-1,-1,PCT_B_790_2_1_1_Layer,S_N,-1,-1,PCT_B_815_1_1_1_Layer,S_N,-1,-1;Z \"Z\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,Z,-1,-1,PCQ_B_790_1_1_1_Layer,Z,-1,-1,PCQ_B_815_1_1_1_Layer,Z,-1,-1,PCS_B_760_1_1_Layer,Z,-1,-1,PCT_B_760_1_1_1_Layer,Z,-1,-1,PCT_B_760_2_1_1_Layer,Z,-1,-1,PCT_B_760_3_1_1_Layer,Z,-1,-1,PCT_B_790_1_1_1_Layer,Z,-1,-1,PCT_B_790_2_1_1_Layer,Z,-1,-1,PCT_B_815_1_1_1_Layer,Z,-1,-1;G \"G\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,G,-1,-1,PCQ_B_790_1_1_1_Layer,G,-1,-1,PCQ_B_815_1_1_1_Layer,G,-1,-1,PCS_B_760_1_1_Layer,G,-1,-1,PCT_B_760_1_1_1_Layer,G,-1,-1,PCT_B_760_2_1_1_Layer,G,-1,-1,PCT_B_760_3_1_1_Layer,G,-1,-1,PCT_B_790_1_1_1_Layer,G,-1,-1,PCT_B_790_2_1_1_Layer,G,-1,-1,PCT_B_815_1_1_1_Layer,G,-1,-1;R0 \"R0\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,R0,-1,-1,PCQ_B_790_1_1_1_Layer,R0,-1,-1,PCQ_B_815_1_1_1_Layer,R0,-1,-1,PCS_B_760_1_1_Layer,R0,-1,-1,PCT_B_760_1_1_1_Layer,R0,-1,-1,PCT_B_760_2_1_1_Layer,R0,-1,-1,PCT_B_760_3_1_1_Layer,R0,-1,-1,PCT_B_790_1_1_1_Layer,R0,-1,-1,PCT_B_790_2_1_1_Layer,R0,-1,-1,PCT_B_815_1_1_1_Layer,R0,-1,-1;γ \"γ\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,γ,-1,-1,PCQ_B_790_1_1_1_Layer,γ,-1,-1,PCQ_B_815_1_1_1_Layer,γ,-1,-1,PCS_B_760_1_1_Layer,γ,-1,-1,PCT_B_760_1_1_1_Layer,γ,-1,-1,PCT_B_760_2_1_1_Layer,γ,-1,-1,PCT_B_760_3_1_1_Layer,γ,-1,-1,PCT_B_790_1_1_1_Layer,γ,-1,-1,PCT_B_790_2_1_1_Layer,γ,-1,-1,PCT_B_815_1_1_1_Layer,γ,-1,-1;Date \"Date\" true true false 8 Date 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,Date,-1,-1,PCQ_B_790_1_1_1_Layer,Date,-1,-1,PCQ_B_815_1_1_1_Layer,Date,-1,-1,PCS_B_760_1_1_Layer,Date,-1,-1,PCT_B_760_1_1_1_Layer,Date,-1,-1,PCT_B_760_2_1_1_Layer,Date,-1,-1,PCT_B_760_3_1_1_Layer,Date,-1,-1,PCT_B_790_1_1_1_Layer,Date,-1,-1,PCT_B_790_2_1_1_Layer,Date,-1,-1,PCT_B_815_1_1_1_Layer,Date,-1,-1;T \"T\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,T,-1,-1,PCQ_B_790_1_1_1_Layer,T,-1,-1,PCQ_B_815_1_1_1_Layer,T,-1,-1,PCS_B_760_1_1_Layer,T,-1,-1,PCT_B_760_1_1_1_Layer,T,-1,-1,PCT_B_760_2_1_1_Layer,T,-1,-1,PCT_B_760_3_1_1_Layer,T,-1,-1,PCT_B_790_1_1_1_Layer,T,-1,-1,PCT_B_790_2_1_1_Layer,T,-1,-1,PCT_B_815_1_1_1_Layer,T,-1,-1;E_E \"E_E\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,E_E,-1,-1,PCQ_B_790_1_1_1_Layer,E_E,-1,-1,PCQ_B_815_1_1_1_Layer,E_E,-1,-1,PCS_B_760_1_1_Layer,E_E,-1,-1,PCT_B_760_1_1_1_Layer,E_E,-1,-1,PCT_B_760_2_1_1_Layer,E_E,-1,-1,PCT_B_760_3_1_1_Layer,E_E,-1,-1,PCT_B_790_1_1_1_Layer,E_E,-1,-1,PCT_B_790_2_1_1_Layer,E_E,-1,-1,PCT_B_815_1_1_1_Layer,E_E,-1,-1;U_S_W_E \"U_S_W_E\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,U_S_W_E,-1,-1,PCQ_B_790_1_1_1_Layer,U_S_W_E,-1,-1,PCQ_B_815_1_1_1_Layer,U_S_W_E,-1,-1,PCS_B_760_1_1_Layer,U_S_W_E,-1,-1,PCT_B_760_1_1_1_Layer,U_S_W_E,-1,-1,PCT_B_760_2_1_1_Layer,U_S_W_E,-1,-1,PCT_B_760_3_1_1_Layer,U_S_W_E,-1,-1,PCT_B_790_1_1_1_Layer,U_S_W_E,-1,-1,PCT_B_790_2_1_1_Layer,U_S_W_E,-1,-1,PCT_B_815_1_1_1_Layer,U_S_W_E,-1,-1;D_S_W_E \"D_S_W_E\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,D_S_W_E,-1,-1,PCQ_B_790_1_1_1_Layer,D_S_W_E,-1,-1,PCQ_B_815_1_1_1_Layer,D_S_W_E,-1,-1,PCS_B_760_1_1_Layer,D_S_W_E,-1,-1,PCT_B_760_1_1_1_Layer,D_S_W_E,-1,-1,PCT_B_760_2_1_1_Layer,D_S_W_E,-1,-1,PCT_B_760_3_1_1_Layer,D_S_W_E,-1,-1,PCT_B_790_1_1_1_Layer,D_S_W_E,-1,-1,PCT_B_790_2_1_1_Layer,D_S_W_E,-1,-1,PCT_B_815_1_1_1_Layer,D_S_W_E,-1,-1;H \"H\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,H,-1,-1,PCQ_B_790_1_1_1_Layer,H,-1,-1,PCQ_B_815_1_1_1_Layer,H,-1,-1,PCS_B_760_1_1_Layer,H,-1,-1,PCT_B_760_1_1_1_Layer,H,-1,-1,PCT_B_760_2_1_1_Layer,H,-1,-1,PCT_B_760_3_1_1_Layer,H,-1,-1,PCT_B_790_1_1_1_Layer,H,-1,-1,PCT_B_790_2_1_1_Layer,H,-1,-1,PCT_B_815_1_1_1_Layer,H,-1,-1;γH \"γH\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,γH,-1,-1,PCQ_B_790_1_1_1_Layer,γH,-1,-1,PCQ_B_815_1_1_1_Layer,γH,-1,-1,PCS_B_760_1_1_Layer,γH,-1,-1,PCT_B_760_1_1_1_Layer,γH,-1,-1,PCT_B_760_2_1_1_Layer,γH,-1,-1,PCT_B_760_3_1_1_Layer,γH,-1,-1,PCT_B_790_1_1_1_Layer,γH,-1,-1,PCT_B_790_2_1_1_Layer,γH,-1,-1,PCT_B_815_1_1_1_Layer,γH,-1,-1;R1 \"R1\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,R1,-1,-1,PCQ_B_790_1_1_1_Layer,R1,-1,-1,PCQ_B_815_1_1_1_Layer,R1,-1,-1,PCS_B_760_1_1_Layer,R1,-1,-1,PCT_B_760_1_1_1_Layer,R1,-1,-1,PCT_B_760_2_1_1_Layer,R1,-1,-1,PCT_B_760_3_1_1_Layer,R1,-1,-1,PCT_B_790_1_1_1_Layer,R1,-1,-1,PCT_B_790_2_1_1_Layer,R1,-1,-1,PCT_B_815_1_1_1_Layer,R1,-1,-1;P_kPa \"P_kPa\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,P_kPa,-1,-1,PCQ_B_790_1_1_1_Layer,P_kPa,-1,-1,PCQ_B_815_1_1_1_Layer,P_kPa,-1,-1,PCS_B_760_1_1_Layer,P_kPa,-1,-1,PCT_B_760_1_1_1_Layer,P_kPa,-1,-1,PCT_B_760_2_1_1_Layer,P_kPa,-1,-1,PCT_B_760_3_1_1_Layer,P_kPa,-1,-1,PCT_B_790_1_1_1_Layer,P_kPa,-1,-1,PCT_B_790_2_1_1_Layer,P_kPa,-1,-1,PCT_B_815_1_1_1_Layer,P_kPa,-1,-1;P_ton_m2 \"P_ton_m2\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,P_ton_m2,-1,-1,PCQ_B_790_1_1_1_Layer,P_ton_m2,-1,-1,PCQ_B_815_1_1_1_Layer,P_ton_m2,-1,-1,PCS_B_760_1_1_Layer,P_ton_m2,-1,-1,PCT_B_760_1_1_1_Layer,P_ton_m2,-1,-1,PCT_B_760_2_1_1_Layer,P_ton_m2,-1,-1,PCT_B_760_3_1_1_Layer,P_ton_m2,-1,-1,PCT_B_790_1_1_1_Layer,P_ton_m2,-1,-1,PCT_B_790_2_1_1_Layer,P_ton_m2,-1,-1,PCT_B_815_1_1_1_Layer,P_ton_m2,-1,-1;A_C \"A_C\" true true false 19 Double 0 0 ,First,#,PCQ_B_760_1_1_1_Layer,A_C,-1,-1,PCQ_B_790_1_1_1_Layer,A_C,-1,-1,PCQ_B_815_1_1_1_Layer,A_C,-1,-1,PCS_B_760_1_1_Layer,A_C,-1,-1,PCT_B_760_1_1_1_Layer,A_C,-1,-1,PCT_B_760_2_1_1_Layer,A_C,-1,-1,PCT_B_760_3_1_1_Layer,A_C,-1,-1,PCT_B_790_1_1_1_Layer,A_C,-1,-1,PCT_B_790_2_1_1_Layer,A_C,-1,-1,PCT_B_815_1_1_1_Layer,A_C,-1,-1")

