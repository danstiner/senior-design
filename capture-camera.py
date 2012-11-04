#!/usr/bin/env python

SEMCAD.SetViewerMode()

data = SEMCAD.GetData()

model = data.GetModel()
simulation = data.GetActiveSimulation()

light = model.LightPosition
eye = "<%f,%f,%f>" % model.CameraEye
target = "<%f,%f,%f>" % model.CameraTarget
up = "<%f,%f,%f>" % model.CameraUp
scale = "%f" % model.ScalingFactor

print "Current camera parameters:"
print "[Eye:Vec3, Target:Vec3, Up:Vec3, Scale:float, Light:Vec3]"
print "[" + eye + "," + target + "," + up + "," + scale + "," + light + "]"
