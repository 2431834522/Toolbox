The attached files contain a Toolbox and Python codes.
 - The Toolbox (DDAA.tbx) can be easily added to ArcCatalog (ArcGIS) and used. To execute it, the database must be placed according to the data call paths, which are defined for each tool, otherwise the command gets an error while calling the corresponding folder.
When a tool is opened, it behaves exactly like the tool in ArcToolbox. At the beginning, it includes several options, after selecting the files and the storage path, the tool is executed and the output (map or graph) is prepared.
 - The Python codes are open source and can be edited. After saving them in the New Script section in the ArcCatalog environment, they can be used as built tools.

It should be noted that the instruments have specific positions (coordination) in the dam body, which are usually analyzed as a group in a Cross_Section; Thus, for example, the pressure cells in the BB section are named PC_Cross_Section_BB and its program code is provided here as PC_Cross_Section_BB.py.
Other Python codes including A.R.py, Pore Pressure.py, Ru.py, Settlememt.py, and Total Stress.py have been developed for the analysis of arching ratio, pore water pressure, ru coefficient, settlement, and total stress, respectively.
