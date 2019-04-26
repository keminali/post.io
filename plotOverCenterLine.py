#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
transient_312case = EnSightReader(CaseFileName='/home/kaiming/Documents/ZJU_Projects/Jet/data/transient_312.case')
transient_312case.PointArrays = ['density', 'v', 'pressure', 'temperature']

# Properties modified on transient_312case
transient_312case.PointArrays = ['v']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [956, 837]

# show data in view
transient_312caseDisplay = Show(transient_312case, renderView1)
# trace defaults for the display properties.
transient_312caseDisplay.ColorArrayName = [None, '']
transient_312caseDisplay.GlyphType = 'Arrow'
transient_312caseDisplay.ScalarOpacityUnitDistance = 0.0016420380639339577

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(transient_312caseDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
transient_312caseDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=transient_312case,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-0.43700000643730164, -0.0860000029206276, -0.0860000029206276]
plotOverLine1.Source.Point2 = [1.9165229048212495e-07, 0.0860000029206276, 0.0860000029206276]

# Properties modified on plotOverLine1
plotOverLine1.Tolerance = 2.22044604925031e-16

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [0.0, 0.0, 0.0]
plotOverLine1.Source.Point2 = [-0.5, 0.0, 0.0]

# get layout
viewLayout1 = GetLayout()

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [473, 837]

# place view in the layout
viewLayout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['v_Magnitude']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'v_X', 'v_X', 'v_Y', 'v_Y', 'v_Z', 'v_Z', 'v_Magnitude', 'v_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'v_X', '0.89', '0.1', '0.11', 'v_Y', '0.22', '0.49', '0.72', 'v_Z', '0.3', '0.69', '0.29', 'v_Magnitude', '0.6', '0.31', '0.64', 'vtkValidPointMask', '1', '0.5', '0', 'Points_X', '0.65', '0.34', '0.16', 'Points_Y', '0', '0', '0', 'Points_Z', '0.89', '0.1', '0.11', 'Points_Magnitude', '0.22', '0.49', '0.72']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'v_X', '0', 'v_Y', '0', 'v_Z', '0', 'v_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'v_X', '1', 'v_Y', '1', 'v_Z', '1', 'v_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'v_X', '2', 'v_Y', '2', 'v_Z', '2', 'v_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'v_X', '0', 'v_Y', '0', 'v_Z', '0', 'v_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# save data
SaveData('/home/kaiming/Documents/ZJU_Projects/Jet/paraview/plot_over_line/v_312.csv', proxy=plotOverLine1)
Disconnect()
Connect()

