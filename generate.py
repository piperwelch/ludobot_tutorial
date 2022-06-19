import pyrosim.pyrosim as pyrosim 

pyrosim.Start_SDF("boxes.sdf")
length = 1
height = 1
width = 1
x, y, z = 0, 0, 0.5
for i in range(5):
    for j in range(5):
        width = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x + j, y + i, z + k *2] , size=[length, width, height])
            width = width*0.90

pyrosim.End()