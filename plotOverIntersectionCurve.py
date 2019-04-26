# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
transient_105case = EnSightReader(CaseFileName='C:\\Users\\kaiming\\Documents\\ZJU\\JET\\transient_105.case')
transient_105case.PointArrays = ['density', 'v', 'pressure', 'temperature']

# Properties modified on transient_105case
transient_105case.PointArrays = ['pressure', 'v']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1592, 819]

# show data in view
transient_105caseDisplay = Show(transient_105case, renderView1)

# get color transfer function/color map for 'pressure'
pressureLUT = GetColorTransferFunction('pressure')

# get opacity transfer function/opacity map for 'pressure'
pressurePWF = GetOpacityTransferFunction('pressure')

# trace defaults for the display properties.
transient_105caseDisplay.Representation = 'Surface'
transient_105caseDisplay.ColorArrayName = ['POINTS', 'pressure']
transient_105caseDisplay.LookupTable = pressureLUT
transient_105caseDisplay.OSPRayScaleArray = 'pressure'
transient_105caseDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
transient_105caseDisplay.SelectOrientationVectors = 'v'
transient_105caseDisplay.ScaleFactor = 0.04370001980895921
transient_105caseDisplay.SelectScaleArray = 'pressure'
transient_105caseDisplay.GlyphType = 'Arrow'
transient_105caseDisplay.GlyphTableIndexArray = 'pressure'
transient_105caseDisplay.GaussianRadius = 0.0021850009904479605
transient_105caseDisplay.SetScaleArray = ['POINTS', 'pressure']
transient_105caseDisplay.ScaleTransferFunction = 'PiecewiseFunction'
transient_105caseDisplay.OpacityArray = ['POINTS', 'pressure']
transient_105caseDisplay.OpacityTransferFunction = 'PiecewiseFunction'
transient_105caseDisplay.DataAxesGrid = 'GridAxesRepresentation'
transient_105caseDisplay.SelectionCellLabelFontFile = ''
transient_105caseDisplay.SelectionPointLabelFontFile = ''
transient_105caseDisplay.PolarAxes = 'PolarAxesRepresentation'
transient_105caseDisplay.ScalarOpacityFunction = pressurePWF
transient_105caseDisplay.ScalarOpacityUnitDistance = 0.0016420380639339577

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
transient_105caseDisplay.DataAxesGrid.XTitleFontFile = ''
transient_105caseDisplay.DataAxesGrid.YTitleFontFile = ''
transient_105caseDisplay.DataAxesGrid.ZTitleFontFile = ''
transient_105caseDisplay.DataAxesGrid.XLabelFontFile = ''
transient_105caseDisplay.DataAxesGrid.YLabelFontFile = ''
transient_105caseDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
transient_105caseDisplay.PolarAxes.PolarAxisTitleFontFile = ''
transient_105caseDisplay.PolarAxes.PolarAxisLabelFontFile = ''
transient_105caseDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
transient_105caseDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
transient_105caseDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data bounds
renderView1.ResetCamera(-0.437000006437, 1.91652290482e-07, -0.0860000029206, 0.0860000029206, -0.0860000029206, 0.0860000029206)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Slice'
slice1 = Slice(Input=transient_105case)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.21849990739250558, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.025, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.025, 0.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'pressure']
slice1Display.LookupTable = pressureLUT
slice1Display.OSPRayScaleArray = 'pressure'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'v'
slice1Display.ScaleFactor = 0.01720000058412552
slice1Display.SelectScaleArray = 'pressure'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'pressure'
slice1Display.GaussianRadius = 0.0008600000292062759
slice1Display.SetScaleArray = ['POINTS', 'pressure']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'pressure']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(transient_105case, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot On Intersection Curves'
plotOnIntersectionCurves1 = PlotOnIntersectionCurves(Input=slice1)
plotOnIntersectionCurves1.SliceType = 'Plane'

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOnIntersectionCurves1.SliceType)

# Properties modified on renderView1
renderView1.EnableOSPRay = 1

# Properties modified on renderView1
renderView1.EnableOSPRay = 0

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Center = [-0.025, 0.0, 0.0]
plotOnIntersectionCurves1.SliceType.Radius = 0.025

# Properties modified on plotOnIntersectionCurves1
plotOnIntersectionCurves1.SliceType = 'Sphere'

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Center = [-0.025, 0.0, 0.0]
plotOnIntersectionCurves1.SliceType.Radius = 0.025

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [791, 819]
lineChartView1.ChartTitleFontFile = ''
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisRangeMaximum = 6.66
lineChartView1.TopAxisLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, lineChartView1)

# show data in view
plotOnIntersectionCurves1Display = Show(plotOnIntersectionCurves1, lineChartView1)

# trace defaults for the display properties.
plotOnIntersectionCurves1Display.CompositeDataSetIndex = [2]
plotOnIntersectionCurves1Display.UseIndexForXAxis = 0
plotOnIntersectionCurves1Display.XArrayName = 'arc_length'
plotOnIntersectionCurves1Display.SeriesVisibility = ['pressure (2)', 'v_Magnitude (2)']
plotOnIntersectionCurves1Display.SeriesLabel = ['arc_length (2)', 'arc_length (2)', 'pressure (2)', 'pressure (2)', 'v_X (2)', 'v_X (2)', 'v_Y (2)', 'v_Y (2)', 'v_Z (2)', 'v_Z (2)', 'v_Magnitude (2)', 'v_Magnitude (2)', 'Points_X (2)', 'Points_X (2)', 'Points_Y (2)', 'Points_Y (2)', 'Points_Z (2)', 'Points_Z (2)', 'Points_Magnitude (2)', 'Points_Magnitude (2)']
plotOnIntersectionCurves1Display.SeriesColor = ['arc_length (2)', '0', '0', '0', 'pressure (2)', '0.89', '0.1', '0.11', 'v_X (2)', '0.22', '0.49', '0.72', 'v_Y (2)', '0.3', '0.69', '0.29', 'v_Z (2)', '0.6', '0.31', '0.64', 'v_Magnitude (2)', '1', '0.5', '0', 'Points_X (2)', '0.65', '0.34', '0.16', 'Points_Y (2)', '0', '0', '0', 'Points_Z (2)', '0.89', '0.1', '0.11', 'Points_Magnitude (2)', '0.22', '0.49', '0.72']
plotOnIntersectionCurves1Display.SeriesPlotCorner = ['arc_length (2)', '0', 'pressure (2)', '0', 'v_X (2)', '0', 'v_Y (2)', '0', 'v_Z (2)', '0', 'v_Magnitude (2)', '0', 'Points_X (2)', '0', 'Points_Y (2)', '0', 'Points_Z (2)', '0', 'Points_Magnitude (2)', '0']
plotOnIntersectionCurves1Display.SeriesLabelPrefix = ''
plotOnIntersectionCurves1Display.SeriesLineStyle = ['arc_length (2)', '1', 'pressure (2)', '1', 'v_X (2)', '1', 'v_Y (2)', '1', 'v_Z (2)', '1', 'v_Magnitude (2)', '1', 'Points_X (2)', '1', 'Points_Y (2)', '1', 'Points_Z (2)', '1', 'Points_Magnitude (2)', '1']
plotOnIntersectionCurves1Display.SeriesLineThickness = ['arc_length (2)', '2', 'pressure (2)', '2', 'v_X (2)', '2', 'v_Y (2)', '2', 'v_Z (2)', '2', 'v_Magnitude (2)', '2', 'Points_X (2)', '2', 'Points_Y (2)', '2', 'Points_Z (2)', '2', 'Points_Magnitude (2)', '2']
plotOnIntersectionCurves1Display.SeriesMarkerStyle = ['arc_length (2)', '0', 'pressure (2)', '0', 'v_X (2)', '0', 'v_Y (2)', '0', 'v_Z (2)', '0', 'v_Magnitude (2)', '0', 'Points_X (2)', '0', 'Points_Y (2)', '0', 'Points_Z (2)', '0', 'Points_Magnitude (2)', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = ['v_Magnitude (2)']
plotOnIntersectionCurves1Display.SeriesColor = ['arc_length (2)', '0', '0', '0', 'pressure (2)', '0.889998', '0.100008', '0.110002', 'v_X (2)', '0.220005', '0.489998', '0.719997', 'v_Y (2)', '0.300008', '0.689998', '0.289998', 'v_Z (2)', '0.6', '0.310002', '0.639994', 'v_Magnitude (2)', '1', '0.500008', '0', 'Points_X (2)', '0.650004', '0.340002', '0.160006', 'Points_Y (2)', '0', '0', '0', 'Points_Z (2)', '0.889998', '0.100008', '0.110002', 'Points_Magnitude (2)', '0.220005', '0.489998', '0.719997']
plotOnIntersectionCurves1Display.SeriesPlotCorner = ['Points_Magnitude (2)', '0', 'Points_X (2)', '0', 'Points_Y (2)', '0', 'Points_Z (2)', '0', 'arc_length (2)', '0', 'pressure (2)', '0', 'v_Magnitude (2)', '0', 'v_X (2)', '0', 'v_Y (2)', '0', 'v_Z (2)', '0']
plotOnIntersectionCurves1Display.SeriesLineStyle = ['Points_Magnitude (2)', '1', 'Points_X (2)', '1', 'Points_Y (2)', '1', 'Points_Z (2)', '1', 'arc_length (2)', '1', 'pressure (2)', '1', 'v_Magnitude (2)', '1', 'v_X (2)', '1', 'v_Y (2)', '1', 'v_Z (2)', '1']
plotOnIntersectionCurves1Display.SeriesLineThickness = ['Points_Magnitude (2)', '2', 'Points_X (2)', '2', 'Points_Y (2)', '2', 'Points_Z (2)', '2', 'arc_length (2)', '2', 'pressure (2)', '2', 'v_Magnitude (2)', '2', 'v_X (2)', '2', 'v_Y (2)', '2', 'v_Z (2)', '2']
plotOnIntersectionCurves1Display.SeriesMarkerStyle = ['Points_Magnitude (2)', '0', 'Points_X (2)', '0', 'Points_Y (2)', '0', 'Points_Z (2)', '0', 'arc_length (2)', '0', 'pressure (2)', '0', 'v_Magnitude (2)', '0', 'v_X (2)', '0', 'v_Y (2)', '0', 'v_Z (2)', '0']

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = []

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = ['v_X (2)']

# set active view
SetActiveView(renderView1)

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Radius = 0.00125

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Radius = 0.00125

# update the view to ensure updated data information
lineChartView1.Update()

# set active source
SetActiveSource(transient_105case)

# create a new 'Slice'
slice2 = Slice(Input=transient_105case)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-0.21849990739250558, 0.0, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, 0.0, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, 0.0, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'pressure']
slice2Display.LookupTable = pressureLUT
slice2Display.OSPRayScaleArray = 'pressure'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'v'
slice2Display.ScaleFactor = 0.04370000064373017
slice2Display.SelectScaleArray = 'pressure'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'pressure'
slice2Display.GaussianRadius = 0.002185000032186508
slice2Display.SetScaleArray = ['POINTS', 'pressure']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'pressure']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.SelectionCellLabelFontFile = ''
slice2Display.SelectionPointLabelFontFile = ''
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitleFontFile = ''
slice2Display.DataAxesGrid.YTitleFontFile = ''
slice2Display.DataAxesGrid.ZTitleFontFile = ''
slice2Display.DataAxesGrid.XLabelFontFile = ''
slice2Display.DataAxesGrid.YLabelFontFile = ''
slice2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice2Display.PolarAxes.PolarAxisTitleFontFile = ''
slice2Display.PolarAxes.PolarAxisLabelFontFile = ''
slice2Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(transient_105case, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(slice2)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data bounds
renderView1.ResetCamera(-0.437000006437, 1.0710167295e-26, -4.23516473627e-22, 4.23516473627e-22, -0.0860000029206, 0.0860000029206)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.42, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [-0.42, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(slice1)

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(slice2)

# set active source
SetActiveSource(slice1)

# update center of rotation
renderView1.CenterOfRotation = [-0.4607345338104785, 0.001921763912100952, 0.053357060124647075]

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(slice2)

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(plotOnIntersectionCurves1)

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Center = [-0.42, 0.0, 0.0]

# Properties modified on plotOnIntersectionCurves1.SliceType
plotOnIntersectionCurves1.SliceType.Center = [-0.42, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(lineChartView1)

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = []

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = ['v_X (2)']

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = ['pressure (2)', 'v_X (2)']

# Properties modified on plotOnIntersectionCurves1Display
plotOnIntersectionCurves1Display.SeriesVisibility = ['v_X (2)']

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.2185000032186508, -2.0066803871419556, -0.015395106337130178]
renderView1.CameraFocalPoint = [-0.2185000032186508, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, -0.007671701676841252, 0.9999705720636891]
renderView1.CameraParallelScale = 0.24282369617062205

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).