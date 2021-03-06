# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# EP_Cross_Section_GG.py
# Created on: 2022-07-02 15:39:16.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: EP_Cross_Section_GG <Date> <Merge_G> <Power__2_> <Z_value_field__2_> <EP_RASTER_GG> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Date = arcpy.GetParameterAsText(0)
if Date == '#' or not Date:
    Date = "\"Date\" = date '2016-07-11 00:00:00'" # provide a default value if unspecified

Merge_G = arcpy.GetParameterAsText(1)
if Merge_G == '#' or not Merge_G:
    Merge_G = "E:\\Projet Of Daryan\\Anallysis\\merge.gdb\\Merge_G" # provide a default value if unspecified

Power__2_ = arcpy.GetParameterAsText(2)
if Power__2_ == '#' or not Power__2_:
    Power__2_ = "2" # provide a default value if unspecified

Z_value_field__2_ = arcpy.GetParameterAsText(3)
if Z_value_field__2_ == '#' or not Z_value_field__2_:
    Z_value_field__2_ = "P_ton_m2" # provide a default value if unspecified

EP_RASTER_GG = arcpy.GetParameterAsText(4)
if EP_RASTER_GG == '#' or not EP_RASTER_GG:
    EP_RASTER_GG = "E:\\Projet Of Daryan\\Anallysis\\Raster.gdb\\EP_RASTER_GG" # provide a default value if unspecified

# Local variables:
EP_G_760_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_760_1_1"
EP_G_760_1_Layer = "EP_G_760_1_1_Layer"
Output_Layer_Name__6_ = EP_G_760_1_Layer
EP_G_730_4_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_730_4_1"
EP_G_730_4_Layer = "EP_G_730_4_1_Layer"
Output_Layer_Name__7_ = EP_G_730_4_Layer
EP_G_730_3_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_730_3_1"
EP_G_730_3_Layer = "EP_G_730_3_1_Layer"
Output_Layer_Name__8_ = EP_G_730_3_Layer
EP_G_730_2_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_730_2_1"
EP_G_730_2_Layer = "EP_G_730_2_1_Layer"
Output_Layer_Name__9_ = EP_G_730_2_Layer
EP_G_780_2_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_780_2_1"
EP_G_780_2_Layer = "EP_G_780_2_1_Layer"
Output_Layer_Name__5_ = EP_G_780_2_Layer
EP_G_780_3_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_780_3_1"
EP_G_780_3_Layer = "EP_G_780_3_1_Layer"
Output_Layer_Name__4_ = EP_G_780_3_Layer
EP_G_780_4_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_780_4_1"
EP_G_780_4_Layer = "EP_G_780_4_1_Layer"
Output_Layer_Name__3_ = EP_G_780_4_Layer
EP_G_800_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_800_1_1"
EP_G_800_1_Layer = "EP_G_800_1_1_Layer"
Output_Layer_Name__2_ = EP_G_800_1_Layer
EP_G_815_2_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Cross_Section\\EP_G_815_2_1"
EP_G_815_2_Layer = "EP_G_815_2_1_Layer"
Output_Layer_Name = EP_G_815_2_Layer
Extent__2_ = "-0/00799560546875 727/962280273438 70/8665161132813 839/186279296875"
layerw = "layerw"
idw1 = "E:\\Projet Of Daryan\\Anallysis\\Raster_final\\EP_RASTER.gdb\\idw1"
Cross_Section_EP_G_G = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\EP_Polygon\\Cross_Section_EP_G_G"

# Process: Make Feature Layer (6)
arcpy.MakeFeatureLayer_management(EP_G_760_1_1, EP_G_760_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (6)
arcpy.SelectLayerByAttribute_management(EP_G_760_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (7)
arcpy.MakeFeatureLayer_management(EP_G_730_4_1, EP_G_730_4_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (7)
arcpy.SelectLayerByAttribute_management(EP_G_730_4_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (8)
arcpy.MakeFeatureLayer_management(EP_G_730_3_1, EP_G_730_3_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (8)
arcpy.SelectLayerByAttribute_management(EP_G_730_3_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (9)
arcpy.MakeFeatureLayer_management(EP_G_730_2_1, EP_G_730_2_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (9)
arcpy.SelectLayerByAttribute_management(EP_G_730_2_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (5)
arcpy.MakeFeatureLayer_management(EP_G_780_2_1, EP_G_780_2_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (5)
arcpy.SelectLayerByAttribute_management(EP_G_780_2_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (4)
arcpy.MakeFeatureLayer_management(EP_G_780_3_1, EP_G_780_3_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (4)
arcpy.SelectLayerByAttribute_management(EP_G_780_3_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(EP_G_780_4_1, EP_G_780_4_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (3)
arcpy.SelectLayerByAttribute_management(EP_G_780_4_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(EP_G_800_1_1, EP_G_800_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(EP_G_800_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(EP_G_815_2_1, EP_G_815_2_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;ID ID VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;S_N S_N VISIBLE NONE;Z Z VISIBLE NONE;G G VISIBLE NONE;R0 R0 VISIBLE NONE;?? ?? VISIBLE NONE;Date Date VISIBLE NONE;T T VISIBLE NONE;E_E E_E VISIBLE NONE;U_S_W_E U_S_W_E VISIBLE NONE;D_S_W_E D_S_W_E VISIBLE NONE;H H VISIBLE NONE;??H ??H VISIBLE NONE;R1 R1 VISIBLE NONE;P_kPa P_kPa VISIBLE NONE;P_ton_m2 P_ton_m2 VISIBLE NONE;RU RU VISIBLE NONE;P_E P_E VISIBLE NONE")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(EP_G_815_2_Layer, "NEW_SELECTION", Date)

# Process: Merge
arcpy.Merge_management("EP_G_760_1_1_Layer;EP_G_730_4_1_Layer;EP_G_730_3_1_Layer;EP_G_730_2_1_Layer;EP_G_780_2_1_Layer;EP_G_780_3_1_Layer;EP_G_780_4_1_Layer;EP_G_800_1_1_Layer;EP_G_815_2_1_Layer", Merge_G, "OBJECTID \"OBJECTID\" true true false 10 Long 0 10 ,First,#,EP_G_815_2_1_Layer,OBJECTID,-1,-1,EP_G_800_1_1_Layer,OBJECTID,-1,-1,EP_G_780_4_1_Layer,OBJECTID,-1,-1,EP_G_780_3_1_Layer,OBJECTID,-1,-1,EP_G_780_2_1_Layer,OBJECTID,-1,-1,EP_G_760_1_1_Layer,OBJECTID,-1,-1,EP_G_730_4_1_Layer,OBJECTID,-1,-1,EP_G_730_3_1_Layer,OBJECTID,-1,-1,EP_G_730_2_1_Layer,OBJECTID,-1,-1;Instrument \"Instrument\" true true false 254 Text 0 0 ,First,#,EP_G_815_2_1_Layer,Instrument,-1,-1,EP_G_800_1_1_Layer,Instrument,-1,-1,EP_G_780_4_1_Layer,Instrument,-1,-1,EP_G_780_3_1_Layer,Instrument,-1,-1,EP_G_780_2_1_Layer,Instrument,-1,-1,EP_G_760_1_1_Layer,Instrument,-1,-1,EP_G_730_4_1_Layer,Instrument,-1,-1,EP_G_730_3_1_Layer,Instrument,-1,-1,EP_G_730_2_1_Layer,Instrument,-1,-1;ID \"ID\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,ID,-1,-1,EP_G_800_1_1_Layer,ID,-1,-1,EP_G_780_4_1_Layer,ID,-1,-1,EP_G_780_3_1_Layer,ID,-1,-1,EP_G_780_2_1_Layer,ID,-1,-1,EP_G_760_1_1_Layer,ID,-1,-1,EP_G_730_4_1_Layer,ID,-1,-1,EP_G_730_3_1_Layer,ID,-1,-1,EP_G_730_2_1_Layer,ID,-1,-1;X \"X\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,X,-1,-1,EP_G_800_1_1_Layer,X,-1,-1,EP_G_780_4_1_Layer,X,-1,-1,EP_G_780_3_1_Layer,X,-1,-1,EP_G_780_2_1_Layer,X,-1,-1,EP_G_760_1_1_Layer,X,-1,-1,EP_G_730_4_1_Layer,X,-1,-1,EP_G_730_3_1_Layer,X,-1,-1,EP_G_730_2_1_Layer,X,-1,-1;Y \"Y\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,Y,-1,-1,EP_G_800_1_1_Layer,Y,-1,-1,EP_G_780_4_1_Layer,Y,-1,-1,EP_G_780_3_1_Layer,Y,-1,-1,EP_G_780_2_1_Layer,Y,-1,-1,EP_G_760_1_1_Layer,Y,-1,-1,EP_G_730_4_1_Layer,Y,-1,-1,EP_G_730_3_1_Layer,Y,-1,-1,EP_G_730_2_1_Layer,Y,-1,-1;S_N \"S_N\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,S_N,-1,-1,EP_G_800_1_1_Layer,S_N,-1,-1,EP_G_780_4_1_Layer,S_N,-1,-1,EP_G_780_3_1_Layer,S_N,-1,-1,EP_G_780_2_1_Layer,S_N,-1,-1,EP_G_760_1_1_Layer,S_N,-1,-1,EP_G_730_4_1_Layer,S_N,-1,-1,EP_G_730_3_1_Layer,S_N,-1,-1,EP_G_730_2_1_Layer,S_N,-1,-1;Z \"Z\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,Z,-1,-1,EP_G_800_1_1_Layer,Z,-1,-1,EP_G_780_4_1_Layer,Z,-1,-1,EP_G_780_3_1_Layer,Z,-1,-1,EP_G_780_2_1_Layer,Z,-1,-1,EP_G_760_1_1_Layer,Z,-1,-1,EP_G_730_4_1_Layer,Z,-1,-1,EP_G_730_3_1_Layer,Z,-1,-1,EP_G_730_2_1_Layer,Z,-1,-1;G \"G\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,G,-1,-1,EP_G_800_1_1_Layer,G,-1,-1,EP_G_780_4_1_Layer,G,-1,-1,EP_G_780_3_1_Layer,G,-1,-1,EP_G_780_2_1_Layer,G,-1,-1,EP_G_760_1_1_Layer,G,-1,-1,EP_G_730_4_1_Layer,G,-1,-1,EP_G_730_3_1_Layer,G,-1,-1,EP_G_730_2_1_Layer,G,-1,-1;R0 \"R0\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,R0,-1,-1,EP_G_800_1_1_Layer,R0,-1,-1,EP_G_780_4_1_Layer,R0,-1,-1,EP_G_780_3_1_Layer,R0,-1,-1,EP_G_780_2_1_Layer,R0,-1,-1,EP_G_760_1_1_Layer,R0,-1,-1,EP_G_730_4_1_Layer,R0,-1,-1,EP_G_730_3_1_Layer,R0,-1,-1,EP_G_730_2_1_Layer,R0,-1,-1;?? \"??\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,??,-1,-1,EP_G_800_1_1_Layer,??,-1,-1,EP_G_780_4_1_Layer,??,-1,-1,EP_G_780_3_1_Layer,??,-1,-1,EP_G_780_2_1_Layer,??,-1,-1,EP_G_760_1_1_Layer,??,-1,-1,EP_G_730_4_1_Layer,??,-1,-1,EP_G_730_3_1_Layer,??,-1,-1,EP_G_730_2_1_Layer,??,-1,-1;Date \"Date\" true true false 8 Date 0 0 ,First,#,EP_G_815_2_1_Layer,Date,-1,-1,EP_G_800_1_1_Layer,Date,-1,-1,EP_G_780_4_1_Layer,Date,-1,-1,EP_G_780_3_1_Layer,Date,-1,-1,EP_G_780_2_1_Layer,Date,-1,-1,EP_G_760_1_1_Layer,Date,-1,-1,EP_G_730_4_1_Layer,Date,-1,-1,EP_G_730_3_1_Layer,Date,-1,-1,EP_G_730_2_1_Layer,Date,-1,-1;T \"T\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,T,-1,-1,EP_G_800_1_1_Layer,T,-1,-1,EP_G_780_4_1_Layer,T,-1,-1,EP_G_780_3_1_Layer,T,-1,-1,EP_G_780_2_1_Layer,T,-1,-1,EP_G_760_1_1_Layer,T,-1,-1,EP_G_730_4_1_Layer,T,-1,-1,EP_G_730_3_1_Layer,T,-1,-1,EP_G_730_2_1_Layer,T,-1,-1;E_E \"E_E\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,E_E,-1,-1,EP_G_800_1_1_Layer,E_E,-1,-1,EP_G_780_4_1_Layer,E_E,-1,-1,EP_G_780_3_1_Layer,E_E,-1,-1,EP_G_780_2_1_Layer,E_E,-1,-1,EP_G_760_1_1_Layer,E_E,-1,-1,EP_G_730_4_1_Layer,E_E,-1,-1,EP_G_730_3_1_Layer,E_E,-1,-1,EP_G_730_2_1_Layer,E_E,-1,-1;U_S_W_E \"U_S_W_E\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,U_S_W_E,-1,-1,EP_G_800_1_1_Layer,U_S_W_E,-1,-1,EP_G_780_4_1_Layer,U_S_W_E,-1,-1,EP_G_780_3_1_Layer,U_S_W_E,-1,-1,EP_G_780_2_1_Layer,U_S_W_E,-1,-1,EP_G_760_1_1_Layer,U_S_W_E,-1,-1,EP_G_730_4_1_Layer,U_S_W_E,-1,-1,EP_G_730_3_1_Layer,U_S_W_E,-1,-1,EP_G_730_2_1_Layer,U_S_W_E,-1,-1;D_S_W_E \"D_S_W_E\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,D_S_W_E,-1,-1,EP_G_800_1_1_Layer,D_S_W_E,-1,-1,EP_G_780_4_1_Layer,D_S_W_E,-1,-1,EP_G_780_3_1_Layer,D_S_W_E,-1,-1,EP_G_780_2_1_Layer,D_S_W_E,-1,-1,EP_G_760_1_1_Layer,D_S_W_E,-1,-1,EP_G_730_4_1_Layer,D_S_W_E,-1,-1,EP_G_730_3_1_Layer,D_S_W_E,-1,-1,EP_G_730_2_1_Layer,D_S_W_E,-1,-1;H \"H\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,H,-1,-1,EP_G_800_1_1_Layer,H,-1,-1,EP_G_780_4_1_Layer,H,-1,-1,EP_G_780_3_1_Layer,H,-1,-1,EP_G_780_2_1_Layer,H,-1,-1,EP_G_760_1_1_Layer,H,-1,-1,EP_G_730_4_1_Layer,H,-1,-1,EP_G_730_3_1_Layer,H,-1,-1,EP_G_730_2_1_Layer,H,-1,-1;??H \"??H\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,??H,-1,-1,EP_G_800_1_1_Layer,??H,-1,-1,EP_G_780_4_1_Layer,??H,-1,-1,EP_G_780_3_1_Layer,??H,-1,-1,EP_G_780_2_1_Layer,??H,-1,-1,EP_G_760_1_1_Layer,??H,-1,-1,EP_G_730_4_1_Layer,??H,-1,-1,EP_G_730_3_1_Layer,??H,-1,-1,EP_G_730_2_1_Layer,??H,-1,-1;R1 \"R1\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,R1,-1,-1,EP_G_800_1_1_Layer,R1,-1,-1,EP_G_780_4_1_Layer,R1,-1,-1,EP_G_780_3_1_Layer,R1,-1,-1,EP_G_780_2_1_Layer,R1,-1,-1,EP_G_760_1_1_Layer,R1,-1,-1,EP_G_730_4_1_Layer,R1,-1,-1,EP_G_730_3_1_Layer,R1,-1,-1,EP_G_730_2_1_Layer,R1,-1,-1;P_kPa \"P_kPa\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,P_kPa,-1,-1,EP_G_800_1_1_Layer,P_kPa,-1,-1,EP_G_780_4_1_Layer,P_kPa,-1,-1,EP_G_780_3_1_Layer,P_kPa,-1,-1,EP_G_780_2_1_Layer,P_kPa,-1,-1,EP_G_760_1_1_Layer,P_kPa,-1,-1,EP_G_730_4_1_Layer,P_kPa,-1,-1,EP_G_730_3_1_Layer,P_kPa,-1,-1,EP_G_730_2_1_Layer,P_kPa,-1,-1;P_ton_m2 \"P_ton_m2\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,P_ton_m2,-1,-1,EP_G_800_1_1_Layer,P_ton_m2,-1,-1,EP_G_780_4_1_Layer,P_ton_m2,-1,-1,EP_G_780_3_1_Layer,P_ton_m2,-1,-1,EP_G_780_2_1_Layer,P_ton_m2,-1,-1,EP_G_760_1_1_Layer,P_ton_m2,-1,-1,EP_G_730_4_1_Layer,P_ton_m2,-1,-1,EP_G_730_3_1_Layer,P_ton_m2,-1,-1,EP_G_730_2_1_Layer,P_ton_m2,-1,-1;RU \"RU\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,RU,-1,-1,EP_G_800_1_1_Layer,RU,-1,-1,EP_G_780_4_1_Layer,RU,-1,-1,EP_G_780_3_1_Layer,RU,-1,-1,EP_G_780_2_1_Layer,RU,-1,-1,EP_G_760_1_1_Layer,RU,-1,-1,EP_G_730_4_1_Layer,RU,-1,-1,EP_G_730_3_1_Layer,RU,-1,-1,EP_G_730_2_1_Layer,RU,-1,-1;P_E \"P_E\" true true false 19 Double 0 0 ,First,#,EP_G_815_2_1_Layer,P_E,-1,-1,EP_G_800_1_1_Layer,P_E,-1,-1,EP_G_780_4_1_Layer,P_E,-1,-1,EP_G_780_3_1_Layer,P_E,-1,-1,EP_G_780_2_1_Layer,P_E,-1,-1,EP_G_760_1_1_Layer,P_E,-1,-1,EP_G_730_4_1_Layer,P_E,-1,-1,EP_G_730_3_1_Layer,P_E,-1,-1,EP_G_730_2_1_Layer,P_E,-1,-1")

# Process: IDW
tempEnvironment0 = arcpy.env.extent
arcpy.env.extent = Extent (2)
arcpy.IDW_ga(Merge_G, Z_value_field__2_, layerw, idw1, "0/283498046875", Power__2_, "NBRTYPE=Standard S_MAJOR=25/1048114769996 S_MINOR=25/1048114769996 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR", "")
arcpy.env.extent = tempEnvironment0

# Process: Extract by Mask (2)
arcpy.gp.ExtractByMask_sa(idw1, Cross_Section_EP_G_G, EP_RASTER_GG)

