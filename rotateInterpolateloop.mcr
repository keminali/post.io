#!MC 1410
$!Varset |NumLoop|=360
$!Loop |NumLoop|
$!Varset |num|=(|Loop|*1+0)
$!RotateData 
  ZoneList =  [4]
  Angle = |num|
  XVar = 1
  YVar = 2
  ZVar = 3
  NormalX = 1
  NormalY = 0
  NormalZ = 0
$!LinearInterpolate 
  SourceZones =  [1]
  DestinationZone = 4
  VarList =  [4-9]
  LinearInterPConst = 0
  LinearInterpMode = DontChange
$!WriteDataSet  "C:\Users\kaiming\Documents\ZJU\output_|num|.dat"
  IncludeText = No
  IncludeGeom = No
  IncludeDataShareLinkage = Yes
  ZoneList =  [4]
  Binary = No
  UsePointFormat = Yes
  Precision = 9
  TecplotVersionToWrite = TecplotCurrent
$!EndLoop