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
# renderView1.ViewSize = [1640, 1178]

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

# change representation type
test1p0vtiDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(test1p0vtiDisplay, ('POINTS', 'ImageScalars'))

# rescale color and/or opacity maps used to include current data range
test1p0vtiDisplay.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
test1p0vtiDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'ImageScalars'
imageScalarsLUT = GetColorTransferFunction('ImageScalars')

# get opacity transfer function/opacity map for 'ImageScalars'
imageScalarsPWF = GetOpacityTransferFunction('ImageScalars')

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Clip'
clip1 = Clip(Input=test1p0vti)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'ImageScalars']
clip1.Value = 0.12182831950485706

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Outline'
clip1Display.ColorArrayName = ['POINTS', 'ImageScalars']
clip1Display.LookupTable = imageScalarsLUT
clip1Display.GlyphType = 'Arrow'
clip1Display.ScalarOpacityUnitDistance = 4.853172871813936
clip1Display.SetScaleArray = ['POINTS', 'ImageScalars']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'ImageScalars']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(test1p0vti, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [100.0, 100.0, 800.0]

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'ImageScalars']
clip2.Value = 0.12182831950485706

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [200.0, 200.0, 800.0]
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)
# trace defaults for the display properties.
clip2Display.Representation = 'Outline'
clip2Display.ColorArrayName = ['POINTS', 'ImageScalars']
clip2Display.LookupTable = imageScalarsLUT
clip2Display.GlyphType = 'Arrow'
clip2Display.ScalarOpacityUnitDistance = 5.180198411253304
clip2Display.SetScaleArray = ['POINTS', 'ImageScalars']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'ImageScalars']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip1, renderView1)

# create a new 'Clip'
clip3 = Clip(Input=clip2)
clip3.ClipType = 'Plane'
clip3.Scalars = ['POINTS', 'ImageScalars']
clip3.Value = 0.12182831950485706

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [200.0, 200.0, 1200.0]
clip3.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip3Display = Show(clip3, renderView1)
# trace defaults for the display properties.
clip3Display.Representation = 'Outline'
clip3Display.ColorArrayName = ['POINTS', 'ImageScalars']
clip3Display.LookupTable = imageScalarsLUT
clip3Display.GlyphType = 'Arrow'
clip3Display.ScalarOpacityUnitDistance = 3.0634092435405496
clip3Display.SetScaleArray = ['POINTS', 'ImageScalars']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'ImageScalars']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip2, renderView1)

# change representation type
clip3Display.SetRepresentationType('Surface')

# Properties modified on clip3.ClipType
clip3.ClipType.Normal = [0.0, 0.0, -1.0]

# Rescale transfer function
imageScalarsLUT.RescaleTransferFunction(0.0, 0.02)

# Rescale transfer function
imageScalarsPWF.RescaleTransferFunction(0.0, 0.02)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip3)

# current camera placement for renderView1
renderView1.CameraPosition = [-1096.7562310624733, -2714.9402636198975, 2748.5435611069024]
renderView1.CameraFocalPoint = [240.28399999999942, 240.28400000000056, 903.9999999999997]
renderView1.CameraViewUp = [0.1550929002703219, 0.4716347348456258, 0.8680477343860972]
renderView1.CameraParallelScale = 965.7581484574697

# save screenshot
SaveScreenshot('/Users/svh/Documents/ClippingFilter.png', magnification=1, quality=100, view=renderView1)
