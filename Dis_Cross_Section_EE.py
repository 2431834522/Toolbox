# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Dis_Cross_Section_EE.py
# Created on: 2022-07-02 11:19:53.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Dis_Cross_Section_EE <Date> <Displacement_E> <Z_value_field> <Power> <Dis_RASTER_D> <e> <Z_value_field__2_> <Dis_k_RASTER_D> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Date = arcpy.GetParameterAsText(0)
if Date == '#' or not Date:
    Date = "\"Date_READI\" = date '2015-07-11 00:00:00'" # provide a default value if unspecified

Displacement_E = arcpy.GetParameterAsText(1)
if Displacement_E == '#' or not Displacement_E:
    Displacement_E = "E:\\Projet Of Daryan\\Anallysis\\DISPLACE.gdb\\Displacement_E" # provide a default value if unspecified

Z_value_field = arcpy.GetParameterAsText(2)
if Z_value_field == '#' or not Z_value_field:
    Z_value_field = "Total_S" # provide a default value if unspecified

Power = arcpy.GetParameterAsText(3)
if Power == '#' or not Power:
    Power = "2" # provide a default value if unspecified

Dis_RASTER_D = arcpy.GetParameterAsText(4)
if Dis_RASTER_D == '#' or not Dis_RASTER_D:
    Dis_RASTER_D = "E:\\Projet Of Daryan\\Anallysis\\Raster.gdb\\Dis_RASTER_D" # provide a default value if unspecified

e = arcpy.GetParameterAsText(5)
if e == '#' or not e:
    e = "C:\\Users\\Motasam\\Documents\\ArcGIS\\Default1.gdb\\e" # provide a default value if unspecified

Z_value_field__2_ = arcpy.GetParameterAsText(6)
if Z_value_field__2_ == '#' or not Z_value_field__2_:
    Z_value_field__2_ = "Total_S" # provide a default value if unspecified

Dis_k_RASTER_D = arcpy.GetParameterAsText(7)
if Dis_k_RASTER_D == '#' or not Dis_k_RASTER_D:
    Dis_k_RASTER_D = "E:\\Projet Of Daryan\\Anallysis\\Raster.gdb\\Dis_k_RASTER_D" # provide a default value if unspecified

# Local variables:
IN_E_1_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement\\IN_E_1_1"
IN_E_1_Layer = "IN_E_1_1_Layer"
IN_E_1_Layer__2_ = IN_E_1_Layer
IN_E_2_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement\\IN_E_2_1"
IN_E_2_Layer = "IN_E_2_1_Layer"
IN_E_2_Layer__2_ = IN_E_2_Layer
IN_E_3_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement\\IN_E_3_1"
IN_E_3_Layer = "IN_E_3_1_Layer"
IN_E_3_Layer__3_ = IN_E_3_Layer
IN_E_4_1 = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement\\IN_E_4_1"
IN_E_4_Layer = "IN_E_4_1_Layer"
IN_E_4_Layer__3_ = IN_E_4_Layer
Extent = "101/349670410156 75/1138916015625 672/295104980469 298/166687011719"
layerw = "layerw"
idw1 = "E:\\Projet Of Daryan\\Anallysis\\Raster_final\\EP_RASTER.gdb\\idw1"
Section_EE__2_ = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement_Polygon\\Section_EE"
Semivariogram_properties = "Spherical 0/060000"
Extent__2_ = "101/349670410156 75/1138916015625 672/295104980469 298/166687011719"
Kriging_Disp2 = "C:\\Users\\Motasam\\Documents\\ArcGIS\\Default1.gdb\\Kriging_Disp2"
Section_EE = "E:\\Projet Of Daryan\\GDB\\Daryan_Edited.gdb\\Displacement_Polygon\\Section_EE"

# Process: Make Feature Layer (4)
arcpy.MakeFeatureLayer_management(IN_E_1_1, IN_E_1_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;No_plat No_plat VISIBLE NONE;Instal_E Instal_E VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;Date_READI Date_READI VISIBLE NONE;Location Location VISIBLE NONE;Top_Tube_E Top_Tube_E VISIBLE NONE;Embankment Embankment VISIBLE NONE;Angle Angle VISIBLE NONE;Initial_In Initial_In VISIBLE NONE;New_Inclin New_Inclin VISIBLE NONE;Inclined_D Inclined_D VISIBLE NONE;Previous_I Previous_I VISIBLE NONE;Diference_ Diference_ VISIBLE NONE;Previous_H Previous_H VISIBLE NONE;New_Horizo New_Horizo VISIBLE NONE;Horizontal Horizontal VISIBLE NONE;Total_H_D Total_H_D VISIBLE NONE;New_Settle New_Settle VISIBLE NONE;Total_S Total_S VISIBLE NONE;F22 F22 VISIBLE NONE;F23 F23 VISIBLE NONE;F24 F24 VISIBLE NONE")

# Process: Select Layer By Attribute (4)
arcpy.SelectLayerByAttribute_management(IN_E_1_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (3)
arcpy.MakeFeatureLayer_management(IN_E_2_1, IN_E_2_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;No_plat No_plat VISIBLE NONE;Instal_E Instal_E VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;Date_READI Date_READI VISIBLE NONE;Location Location VISIBLE NONE;Top_Tube_E Top_Tube_E VISIBLE NONE;Embankment Embankment VISIBLE NONE;Angle Angle VISIBLE NONE;Initial_In Initial_In VISIBLE NONE;New_Inclin New_Inclin VISIBLE NONE;Inclined_D Inclined_D VISIBLE NONE;Previous_I Previous_I VISIBLE NONE;Diference_ Diference_ VISIBLE NONE;Previous_H Previous_H VISIBLE NONE;New_Horizo New_Horizo VISIBLE NONE;Horizontal Horizontal VISIBLE NONE;Total_H_D Total_H_D VISIBLE NONE;New_Settle New_Settle VISIBLE NONE;Total_S Total_S VISIBLE NONE;F22 F22 VISIBLE NONE;F23 F23 VISIBLE NONE;F24 F24 VISIBLE NONE")

# Process: Select Layer By Attribute (3)
arcpy.SelectLayerByAttribute_management(IN_E_2_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(IN_E_3_1, IN_E_3_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;No_plat No_plat VISIBLE NONE;Instal_E Instal_E VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;Date_READI Date_READI VISIBLE NONE;Location Location VISIBLE NONE;Top_Tube_E Top_Tube_E VISIBLE NONE;Embankment Embankment VISIBLE NONE;Angle Angle VISIBLE NONE;Reading_m_ Reading_m_ VISIBLE NONE;New_Magnet New_Magnet VISIBLE NONE;Previous_M Previous_M VISIBLE NONE;Settlement Settlement VISIBLE NONE;Total_S Total_S VISIBLE NONE;F16 F16 VISIBLE NONE;F17 F17 VISIBLE NONE")

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(IN_E_3_Layer, "NEW_SELECTION", Date)

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(IN_E_4_1, IN_E_4_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;Instrument Instrument VISIBLE NONE;No_plat No_plat VISIBLE NONE;Instal_E Instal_E VISIBLE NONE;X X VISIBLE NONE;Y Y VISIBLE NONE;Date_READI Date_READI VISIBLE NONE;Location Location VISIBLE NONE;Top_Tube_E Top_Tube_E VISIBLE NONE;Embankment Embankment VISIBLE NONE;Angle Angle VISIBLE NONE;Reading_m_ Reading_m_ VISIBLE NONE;New_Magnet New_Magnet VISIBLE NONE;Previous_M Previous_M VISIBLE NONE;Settlement Settlement VISIBLE NONE;Total_S Total_S VISIBLE NONE;F16 F16 VISIBLE NONE;F17 F17 VISIBLE NONE")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(IN_E_4_Layer, "NEW_SELECTION", Date)

# Process: Merge
arcpy.Merge_management("IN_E_1_1_Layer;IN_E_2_1_Layer;IN_E_3_1_Layer;IN_E_4_1_Layer", Displacement_E, "OBJECTID \"OBJECTID\" true true false 10 Long 0 10 ,First,#,IN_E_1_1_Layer,OBJECTID,-1,-1,IN_E_2_1_Layer,OBJECTID,-1,-1,IN_E_3_1_Layer,OBJECTID,-1,-1,IN_E_4_1_Layer,OBJECTID,-1,-1;Instrument \"Instrument\" true true false 254 Text 0 0 ,First,#,IN_E_1_1_Layer,Instrument,-1,-1,IN_E_2_1_Layer,Instrument,-1,-1,IN_E_3_1_Layer,Instrument,-1,-1,IN_E_4_1_Layer,Instrument,-1,-1;No_plat \"No_plat\" true true false 254 Text 0 0 ,First,#,IN_E_1_1_Layer,No_plat,-1,-1,IN_E_2_1_Layer,No_plat,-1,-1,IN_E_3_1_Layer,No_plat,-1,-1,IN_E_4_1_Layer,No_plat,-1,-1;Instal_E \"Instal_E\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Instal_E,-1,-1,IN_E_2_1_Layer,Instal_E,-1,-1,IN_E_3_1_Layer,Instal_E,-1,-1,IN_E_4_1_Layer,Instal_E,-1,-1;X \"X\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,X,-1,-1,IN_E_2_1_Layer,X,-1,-1,IN_E_3_1_Layer,X,-1,-1,IN_E_4_1_Layer,X,-1,-1;Y \"Y\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Y,-1,-1,IN_E_2_1_Layer,Y,-1,-1,IN_E_3_1_Layer,Y,-1,-1,IN_E_4_1_Layer,Y,-1,-1;Location \"Location\" true true false 254 Text 0 0 ,First,#,IN_E_1_1_Layer,Location,-1,-1,IN_E_2_1_Layer,Location,-1,-1,IN_E_3_1_Layer,Location,-1,-1,IN_E_4_1_Layer,Location,-1,-1;Top_Tube_E \"Top_Tube_E\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Top_Tube_E,-1,-1,IN_E_2_1_Layer,Top_Tube_E,-1,-1,IN_E_3_1_Layer,Top_Tube_E,-1,-1,IN_E_4_1_Layer,Top_Tube_E,-1,-1;Embankment \"Embankment\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Embankment,-1,-1,IN_E_2_1_Layer,Embankment,-1,-1,IN_E_3_1_Layer,Embankment,-1,-1,IN_E_4_1_Layer,Embankment,-1,-1;Angle \"Angle\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Angle,-1,-1,IN_E_2_1_Layer,Angle,-1,-1,IN_E_3_1_Layer,Angle,-1,-1,IN_E_4_1_Layer,Angle,-1,-1;Initial_In \"Initial_In\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Initial_In,-1,-1,IN_E_2_1_Layer,Initial_In,-1,-1;New_Inclin \"New_Inclin\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,New_Inclin,-1,-1,IN_E_2_1_Layer,New_Inclin,-1,-1;Inclined_D \"Inclined_D\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Inclined_D,-1,-1,IN_E_2_1_Layer,Inclined_D,-1,-1;Previous_I \"Previous_I\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Previous_I,-1,-1,IN_E_2_1_Layer,Previous_I,-1,-1;Diference_ \"Diference_\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Diference_,-1,-1,IN_E_2_1_Layer,Diference_,-1,-1;Previous_H \"Previous_H\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Previous_H,-1,-1,IN_E_2_1_Layer,Previous_H,-1,-1;New_Horizo \"New_Horizo\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,New_Horizo,-1,-1,IN_E_2_1_Layer,New_Horizo,-1,-1;Horizontal \"Horizontal\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Horizontal,-1,-1,IN_E_2_1_Layer,Horizontal,-1,-1;New_Settle \"New_Settle\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,New_Settle,-1,-1,IN_E_2_1_Layer,New_Settle,-1,-1;Total_S \"Total_S\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Total_S,-1,-1,IN_E_2_1_Layer,Total_S,-1,-1,IN_E_3_1_Layer,Total_S,-1,-1,IN_E_4_1_Layer,Total_S,-1,-1;F22 \"F22\" true true false 8 Date 0 0 ,First,#,IN_E_1_1_Layer,F22,-1,-1,IN_E_2_1_Layer,F22,-1,-1;F23 \"F23\" true true false 8 Date 0 0 ,First,#,IN_E_1_1_Layer,F23,-1,-1,IN_E_2_1_Layer,F23,-1,-1;F24 \"F24\" true true false 8 Date 0 0 ,First,#,IN_E_1_1_Layer,F24,-1,-1,IN_E_2_1_Layer,F24,-1,-1;Date_READI \"Date_READI\" true true false 254 Text 0 0 ,First,#,IN_E_1_1_Layer,Date_READI,-1,-1,IN_E_2_1_Layer,Date_READI,-1,-1,IN_E_3_1_Layer,Date_READI,-1,-1,IN_E_4_1_Layer,Date_READI,-1,-1;Total_H_D \"Total_H_D\" true true false 19 Double 0 0 ,First,#,IN_E_1_1_Layer,Total_H_D,-1,-1,IN_E_2_1_Layer,Total_H_D,-1,-1;Reading_m_ \"Reading_m_\" true true false 19 Double 0 0 ,First,#,IN_E_3_1_Layer,Reading_m_,-1,-1,IN_E_4_1_Layer,Reading_m_,-1,-1;New_Magnet \"New_Magnet\" true true false 19 Double 0 0 ,First,#,IN_E_3_1_Layer,New_Magnet,-1,-1,IN_E_4_1_Layer,New_Magnet,-1,-1;Previous_M \"Previous_M\" true true false 19 Double 0 0 ,First,#,IN_E_3_1_Layer,Previous_M,-1,-1,IN_E_4_1_Layer,Previous_M,-1,-1;Settlement \"Settlement\" true true false 19 Double 0 0 ,First,#,IN_E_3_1_Layer,Settlement,-1,-1,IN_E_4_1_Layer,Settlement,-1,-1;F16 \"F16\" true true false 8 Date 0 0 ,First,#,IN_E_3_1_Layer,F16,-1,-1,IN_E_4_1_Layer,F16,-1,-1;F17 \"F17\" true true false 8 Date 0 0 ,First,#,IN_E_3_1_Layer,F17,-1,-1,IN_E_4_1_Layer,F17,-1,-1")

# Process: IDW
tempEnvironment0 = arcpy.env.extent
arcpy.env.extent = Extent
arcpy.IDW_ga(Displacement_E, Z_value_field, layerw, idw1, "0/892211181640625", Power, "NBRTYPE=Standard S_MAJOR=70/1762898616295 S_MINOR=70/1762898616295 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR", "")
arcpy.env.extent = tempEnvironment0

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(idw1, Section_EE__2_, Dis_RASTER_D)

# Process: Kriging
tempEnvironment0 = arcpy.env.extent
arcpy.env.extent = Extent (2)
arcpy.Kriging_3d(Displacement_E, Z_value_field__2_, Kriging_Disp2, Semivariogram_properties, "0/892211181640625", "VARIABLE 12", e)
arcpy.env.extent = tempEnvironment0

# Process: Extract by Mask (2)
arcpy.gp.ExtractByMask_sa(Kriging_Disp2, Section_EE, Dis_k_RASTER_D)
