import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("boxes.sdf")
for i in range(1000):
    time.sleep(0.01667)
    p.stepSimulation()
    print("Loop #" + str(i) + "\n")
p.disconnect()