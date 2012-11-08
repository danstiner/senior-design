import PostPro
import inspect
import time
from SEMCAD import *
import threading

simulation = GetData().GetSimulations()[0]

#simulation.Select(True)
#print PostPro.GetSimulationName()

PostPro.InitSimulation(0)

datafield = PostPro.GetResult('Overall Field', 'E(x,y,z,f0)', True)

#datafield.SetAxis([0,0,0,0])
#indices = datafield.ExtractAxis(PostPro.Axis.X)
#datafield.SetCoor(indices[10], PostPro.Axis.X)
#datafield.Set
#datafield.SetAttribute("E-PhaseCorrection(f0)", "(90,0)")
#datafield.Set

viewer = PostPro.CreateViewer('Slice Field Viewer', datafield)

#print viewer.__getattribute__('SliceValues')
viewer.__setattr__('LogScale', False)
viewer.__setattr__('SliceAxis', 0)
viewer.__setattr__('SliceIndex', 65)

#viewer.__getattribute__('Autoscale')

#print inspect.getmembers(viewer)

SEMCAD.SetViewerMode()

#raw_input("Press any key")
 
class MyThread ( threading.Thread ):
	def run ( self ):

		time.sleep(7)
		#for attr in datafield.GetAllAttributes():
		#	print attr + " = " + datafield.GetAttribute(attr)
		#print inspect.getmembers(viewer)
		#print inspect.getmembers(datafield)
		
		#PostPro.CloseViewer(viewer)
 
MyThread().start()
for attr in PostPro.EvalOptions.GetAll():
	print attr + " = " + PostPro.EvalOptions.Get(attr)
#print inspect.getmembers(PostPro.EvalOptions)




#PostPro.CloseViewer(viewer)