#%%
import torch
from GeoGrad import *

#%%
square = Surface2D(4)
square.set_vertices(torch.Tensor([[0,0],[0,1],[1,1],[1,0]]))
print(square.get_volume())
print(square.get_surface_area())

triangle = Surface2D(3)
triangle.set_vertices(torch.Tensor([[0,0],[0,1],[1,0]]))
print(triangle.get_volume())
print(triangle.get_surface_area())

rectangle = Surface2D(4)
rectangle.set_vertices(torch.Tensor([[0,0],[0,1],[2,1],[2,0]]))
print(rectangle.get_volume())
print(rectangle.get_surface_area())

pentagon = Surface2D(5)
pentagon.set_vertices(torch.Tensor([[0,0],[0,1],[1,1],[1,0],[0.5,0.5]]))
print(pentagon.get_volume())
print(pentagon.get_surface_area())

# %%
polygon = Surface2D(15)

space = Space2D(500,500)
space.add_object(polygon)

renderer = Renderer()
renderer.start_recording("videos/equalEdges3")
#%%
global_learning_rate = 0.1
volume_optimizer = GeoOpt.TargetVolume(polygon, 0.1, 1*global_learning_rate)
surface_area_optimizer = GeoOpt.MinEdgeLengthVariance(polygon, 0.01*global_learning_rate)

def print_data():
  print("volume:"+str(polygon.get_volume().item()),end="\t")
  print("surface area:"+str(polygon.get_surface_area().item()))

def step():
  for i in range(10):
    volume_optimizer.optimize()
    surface_area_optimizer.optimize()
# %%
renderer.loop(space, [step])
# %%
