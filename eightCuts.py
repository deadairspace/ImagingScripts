#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
test1p0vti = XMLImageDataReader(FileName=['/Users/svh/Documents/IterateImageData/release/test1p0.vti'])
test1p0vti.PointArrayStatus = ['ImageScalars']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1185, 913]

# show data in view
test1p0vtiDisplay = Show(test1p0vti, renderView1)
# trace defaults for the display properties.
test1p0vtiDisplay.Representation = 'Outline'
test1p0vtiDisplay.ColorArrayName = ['POINTS', '']
test1p0vtiDisplay.GlyphType = 'Arrow'
test1p0vtiDisplay.ScalarOpacityUnitDistance = 4.14582982356307
test1p0vtiDisplay.Slice = 226

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Flying Edges 2D'
flyingEdges2D1 = FlyingEdges2D(Input=test1p0vti)
flyingEdges2D1.ContourBy = ['POINTS', 'ImageScalars']
flyingEdges2D1.Isosurfaces = [0.12182831950485706]

# set active source
SetActiveSource(test1p0vti)

# destroy flyingEdges2D1
Delete(flyingEdges2D1)
del flyingEdges2D1

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter1 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter1.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter1.SliceType.Origin = [240.284, 240.284, 904.0]

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on flyingEdgesPlaneCutter1.SliceType
flyingEdgesPlaneCutter1.SliceType.Origin = [0.0, 0.0, 200.0]
flyingEdgesPlaneCutter1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter1Display = Show(flyingEdgesPlaneCutter1, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter1Display.Representation = 'Outline'
flyingEdgesPlaneCutter1Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter1Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter1Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter1Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter1Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter1Display.OpacityTransferFunction = 'PiecewiseFunction'

# set active source
SetActiveSource(test1p0vti)

# set active source
SetActiveSource(flyingEdgesPlaneCutter1)

# change representation type
flyingEdgesPlaneCutter1Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter1Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'ImageScalars'
imageScalarsLUT = GetColorTransferFunction('ImageScalars')

# get opacity transfer function/opacity map for 'ImageScalars'
imageScalarsPWF = GetOpacityTransferFunction('ImageScalars')

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter2 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter2.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter2.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter2.SliceType
flyingEdgesPlaneCutter2.SliceType.Origin = [0.0, 0.0, 400.0]
flyingEdgesPlaneCutter2.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter2Display = Show(flyingEdgesPlaneCutter2, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter2Display.Representation = 'Outline'
flyingEdgesPlaneCutter2Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter2Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter2Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter2Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter2Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter2Display.OpacityTransferFunction = 'PiecewiseFunction'

# change representation type
flyingEdgesPlaneCutter2Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter2Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter2Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(test1p0vti)

# set active source
SetActiveSource(flyingEdgesPlaneCutter2)

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter3 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter3.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter3.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter3.SliceType
flyingEdgesPlaneCutter3.SliceType.Origin = [0.0, 0.0, 600.0]
flyingEdgesPlaneCutter3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter3Display = Show(flyingEdgesPlaneCutter3, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter3Display.Representation = 'Outline'
flyingEdgesPlaneCutter3Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter3Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter3Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter3Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter3Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter3Display.OpacityTransferFunction = 'PiecewiseFunction'

# change representation type
flyingEdgesPlaneCutter3Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter3Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter3Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter4 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter4.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter4.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter4.SliceType
flyingEdgesPlaneCutter4.SliceType.Origin = [0.0, 0.0, 800.0]
flyingEdgesPlaneCutter4.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter4Display = Show(flyingEdgesPlaneCutter4, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter4Display.Representation = 'Outline'
flyingEdgesPlaneCutter4Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter4Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter4Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter4Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter4Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter4Display.OpacityTransferFunction = 'PiecewiseFunction'

# change representation type
flyingEdgesPlaneCutter4Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter4Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter4Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter4Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter5 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter5.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter5.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter5.SliceType
flyingEdgesPlaneCutter5.SliceType.Origin = [0.0, 0.0, 1000.0]
flyingEdgesPlaneCutter5.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter5Display = Show(flyingEdgesPlaneCutter5, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter5Display.Representation = 'Outline'
flyingEdgesPlaneCutter5Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter5Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter5Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter5Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter5Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter5Display.OpacityTransferFunction = 'PiecewiseFunction'

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter6 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter6.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter6.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter6.SliceType
flyingEdgesPlaneCutter6.SliceType.Origin = [240.0, 0.0, 1200.0]
flyingEdgesPlaneCutter6.SliceType.Normal = [0.0, 0.0, 0.0]

# show data in view
flyingEdgesPlaneCutter6Display = Show(flyingEdgesPlaneCutter6, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter6Display.Representation = 'Outline'
flyingEdgesPlaneCutter6Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter6Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter6Display.SetScaleArray = [None, '']
flyingEdgesPlaneCutter6Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter6Display.OpacityArray = [None, '']
flyingEdgesPlaneCutter6Display.OpacityTransferFunction = 'PiecewiseFunction'

# change representation type
flyingEdgesPlaneCutter6Display.SetRepresentationType('Surface')

# Properties modified on flyingEdgesPlaneCutter6.SliceType
flyingEdgesPlaneCutter6.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on flyingEdgesPlaneCutter6Display
flyingEdgesPlaneCutter6Display.SetScaleArray = [None, 'ImageScalars']

# Properties modified on flyingEdgesPlaneCutter6Display
flyingEdgesPlaneCutter6Display.OpacityArray = [None, 'ImageScalars']

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter6Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter6Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter6Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter7 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter7.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter7.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter7.SliceType
flyingEdgesPlaneCutter7.SliceType.Origin = [0.0, 0.0, 1400.0]

# show data in view
flyingEdgesPlaneCutter7Display = Show(flyingEdgesPlaneCutter7, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter7Display.Representation = 'Outline'
flyingEdgesPlaneCutter7Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter7Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter7Display.SetScaleArray = [None, '']
flyingEdgesPlaneCutter7Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter7Display.OpacityArray = [None, '']
flyingEdgesPlaneCutter7Display.OpacityTransferFunction = 'PiecewiseFunction'

# Properties modified on flyingEdgesPlaneCutter7.SliceType
flyingEdgesPlaneCutter7.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on flyingEdgesPlaneCutter7Display
flyingEdgesPlaneCutter7Display.SetScaleArray = [None, 'ImageScalars']

# Properties modified on flyingEdgesPlaneCutter7Display
flyingEdgesPlaneCutter7Display.OpacityArray = [None, 'ImageScalars']

# change representation type
flyingEdgesPlaneCutter7Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter7Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter7Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter7Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flyingEdgesPlaneCutter6)

# Properties modified on flyingEdgesPlaneCutter6.SliceType
flyingEdgesPlaneCutter6.SliceType.Origin = [0.0, 0.0, 1200.0]

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter8 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter8.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter8.SliceType.Origin = [240.284, 240.284, 904.0]

# Properties modified on flyingEdgesPlaneCutter8.SliceType
flyingEdgesPlaneCutter8.SliceType.Origin = [0.0, 0.0, 1600.0]
flyingEdgesPlaneCutter8.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
flyingEdgesPlaneCutter8Display = Show(flyingEdgesPlaneCutter8, renderView1)
# trace defaults for the display properties.
flyingEdgesPlaneCutter8Display.Representation = 'Outline'
flyingEdgesPlaneCutter8Display.ColorArrayName = ['POINTS', '']
flyingEdgesPlaneCutter8Display.GlyphType = 'Arrow'
flyingEdgesPlaneCutter8Display.SetScaleArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter8Display.ScaleTransferFunction = 'PiecewiseFunction'
flyingEdgesPlaneCutter8Display.OpacityArray = ['POINTS', 'ImageScalars']
flyingEdgesPlaneCutter8Display.OpacityTransferFunction = 'PiecewiseFunction'

# change representation type
flyingEdgesPlaneCutter8Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter8Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter8Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter8Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(test1p0vti)

# create a new 'Flying Edges Plane Cutter'
flyingEdgesPlaneCutter9 = FlyingEdgesPlaneCutter(Input=test1p0vti)
flyingEdgesPlaneCutter9.SliceType = 'Plane'

# init the 'Plane' selected for 'SliceType'
flyingEdgesPlaneCutter9.SliceType.Origin = [240.284, 240.284, 904.0]

# set active source
SetActiveSource(flyingEdgesPlaneCutter1)

# set active source
SetActiveSource(flyingEdgesPlaneCutter2)

# set active source
SetActiveSource(flyingEdgesPlaneCutter3)

# set active source
SetActiveSource(flyingEdgesPlaneCutter4)

# set active source
SetActiveSource(flyingEdgesPlaneCutter5)

# change representation type
flyingEdgesPlaneCutter5Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flyingEdgesPlaneCutter5Display, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
flyingEdgesPlaneCutter5Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
flyingEdgesPlaneCutter5Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(flyingEdgesPlaneCutter6)

# set active source
SetActiveSource(flyingEdgesPlaneCutter7)

# set active source
SetActiveSource(flyingEdgesPlaneCutter8)

# current camera placement for renderView1
renderView1.CameraPosition = [-4863.596118352916, 240.2840175628662, 904.0000305175781]
renderView1.CameraFocalPoint = [240.2840118408203, 240.2840175628662, 904.0000305175781]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1320.9813816144722

# save screenshot
SaveScreenshot('/Users/svh/Documents/IterateImageData/release/output.png', magnification=1, quality=100, view=renderView1)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [3339.424013211879, 2506.9102932122582, 4316.607051459358]
renderView1.CameraFocalPoint = [240.2840194702148, 240.284019470215, 1057.2907943725588]
renderView1.CameraViewUp = [-0.2975132749878619, 0.8928702006568774, -0.3380364713828146]
renderView1.CameraParallelScale = 1303.5183166778393

# save screenshot
SaveScreenshot('/Users/svh/Documents/IterateImageData/release/output.png', magnification=1, quality=100, view=renderView1)

# set active source
SetActiveSource(flyingEdgesPlaneCutter9)

# set active source
SetActiveSource(test1p0vti)

# destroy flyingEdgesPlaneCutter9
Delete(flyingEdgesPlaneCutter9)
del flyingEdgesPlaneCutter9

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [3339.424013211879, 2506.9102932122582, 4316.607051459358]
renderView1.CameraFocalPoint = [240.2840194702148, 240.284019470215, 1057.2907943725588]
renderView1.CameraViewUp = [-0.2975132749878619, 0.8928702006568774, -0.3380364713828146]
renderView1.CameraParallelScale = 1303.5183166778393

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
