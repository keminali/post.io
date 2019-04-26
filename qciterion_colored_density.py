#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


	# create a new 'EnSight Reader'
transient_91case = EnSightReader(CaseFileName='/home/kaiming/Documents/ZJU_Projects/Jet/data/transient_514.case')
transient_91case.PointArrays = ['density', 'v', 'pressure', 'temperature']

	# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.Background =[1,1,1]

# uncomment following to set a specific view size

renderView1.ViewSize = [1117, 866]
	# get color transfer function/color map for 'density'
densityLUT = GetColorTransferFunction('density')

	# show data in view
transient_91caseDisplay = Show(transient_91case, renderView1)
	# trace defaults for the display properties.
transient_91caseDisplay.ColorArrayName = ['POINTS', 'density']
transient_91caseDisplay.LookupTable = densityLUT
transient_91caseDisplay.GlyphType = 'Arrow'
transient_91caseDisplay.ScalarOpacityUnitDistance = 0.0016420380639339577
        # get color legend for 'densityLUT' in view 'renderView1'
densityLUTColorBar = GetScalarBar(densityLUT, renderView1)
densityLUTColorBar.AutoOrient = 0
  ## legend orientation
densityLUTColorBar.Orientation = 'Horizontal'
densityLUTColorBar.RangeLabelFormat = '%.2f'
   ## legend normalized position
densityLUTColorBar.Position = [0.3, 0.1]
         #  change label color to 'black'
densityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

        #  change titile color to 'black'
densityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
	# reset view to fit data
renderView1.ResetCamera()

	# show color bar/color legend
transient_91caseDisplay.SetScalarBarVisibility(renderView1, True)

	# get opacity transfer function/opacity map for 'density'
densityPWF = GetOpacityTransferFunction('density')

	# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=transient_91case)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'density']

	# Properties modified on gradientOfUnstructuredDataSet1
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'v']
gradientOfUnstructuredDataSet1.ComputeQCriterion = 1

	# show data in view
gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
	# trace defaults for the display properties.
gradientOfUnstructuredDataSet1Display.ColorArrayName = ['POINTS', 'density']
gradientOfUnstructuredDataSet1Display.LookupTable = densityLUT
gradientOfUnstructuredDataSet1Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet1Display.ScalarOpacityUnitDistance = 0.0016420380639339577

	# hide data in view
Hide(transient_91case, renderView1)

	# show color bar/color legend
gradientOfUnstructuredDataSet1Display.SetScalarBarVisibility(renderView1, True)

	# create a new 'Contour'
contour1 = Contour(Input=gradientOfUnstructuredDataSet1)
contour1.ContourBy = ['POINTS', 'density']
contour1.Isosurfaces = [0.7536712437868118]
contour1.PointMergeMethod = 'Uniform Binning'

	# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'Q-criterion']
contour1.OutputPointsPrecision = 'Single'
contour1.Isosurfaces = [1000000.0]

	# show data in view
contour1Display = Show(contour1, renderView1)
	# trace defaults for the display properties.
contour1Display.ColorArrayName = ['POINTS', 'density']
contour1Display.LookupTable = densityLUT
contour1Display.GlyphType = 'Arrow'

	# hide data in view
Hide(gradientOfUnstructuredDataSet1, renderView1)

	# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

	# reset view to fit data bounds
renderView1.ResetCamera(-0.437000006437, -0.363715648651, -0.0146765615791, 0.0155552132055, -0.0139937549829, 0.0155133698136)



# current camera placement for renderView1
renderView1.CameraPosition = [-0.3693876183825478, -0.14945995339693371, 0.18962885092966636]
renderView1.CameraFocalPoint = [-0.3579576038702967, -0.006822062851817242, -0.0021144211493554846]
renderView1.CameraViewUp = [0.6080912350865584, 0.61916691517865, 0.4968474423392544]
renderView1.CameraParallelScale = 0.04229428955697712



	# get layout
viewLayout1 = GetLayout()

	# save screenshot
SaveScreenshot('/home/kaiming/Documents/ZJU_Projects/Jet/paraview/Q_criteria_colored_by_density_514.png' , layout=viewLayout1, magnification=1, quality=100)

Disconnect
Connect
	
