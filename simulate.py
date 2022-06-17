import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for i in range(1000):
    time.sleep(0.01667)
    p.stepSimulation()
    print("Loop #" + str(i) + "\n")
p.disconnect()