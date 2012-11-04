#!/usr/bin/env python

camera_angles = ["[<>,<>,<>,1.0,<>]"]



data = SEMCAD.GetData()

model = data.GetModel()
simulation = data.GetActiveSimulation()

SEMCAD.SetViewerMode()
orig_cameraeye = model.CameraEye
orig_cameratarget = model.CameraTarget
orig_cameraup = model.CameraUp
orig_scalingfactor = model.ScalingFactor

SetModelingMode()

SEMCAD.raw_input("Prompt >>> ")

SEMCAD.SetSimulationMode()

SEMCAD.IsRunning()

SEMCAD.SetViewerMode()

SEMCAD.UpdateView()

SEMCAD.SaveScreenShotAs("filename")

#Simulations.List
#Simulations.GetActiveSimulation

#Simulation.ComputeVoxels()
#Simulation.Run()
#Simulation.ResetResults()
