#%%
import torch
from GeoGrad import *

#%%
square = Surface2D(4)
square.set_vertices(torch.Tensor([[0,0],[0,1],[1,1],[1,0]]))
print("square:")
print(square.get_volume())
print(square.get_surface_area())
print(square.get_angles_between_edges())
print()

triangle = Surface2D(3)
triangle.set_vertices(torch.Tensor([[0,0],[0,1],[1,0]]))
print("triangle:")
print(triangle.get_volume())
print(triangle.get_surface_area())
print(triangle.get_angles_between_edges())
print()

rectangle = Surface2D(4)
rectangle.set_vertices(torch.Tensor([[0,0],[0,1],[2,1],[2,0]]))
print("rectangle:")
print(rectangle.get_volume())
print(rectangle.get_surface_area())
print(rectangle.get_angles_between_edges())
print()

pentagon = Surface2D(5)
pentagon.set_vertices(torch.Tensor([[0,0],[0,1],[1,1],[1,0],[0.5,0.5]]))
print("pentagon:")
print(pentagon.get_volume())
print(pentagon.get_surface_area())
print(pentagon.get_angles_between_edges())
print()
# %%
polygon = Surface2D(12)

space = Space2D(500,500)
space.add_object(polygon)

renderer = Renderer()
#renderer.start_recording("videos/rightAngles")
#%%
global_learning_rate = 0.01
volume_optimizer = GeoOpt.TargetVolume(polygon, 0.1, 1*global_learning_rate)
surface_area_optimizer = GeoOpt.MinSurfaceArea(polygon, 0.01*global_learning_rate)
variance_optimizer = GeoOpt.MaxEdgeLengthVariance(polygon, 0.04*global_learning_rate)
smoothness_optimizer = GeoOpt.MinimizeValue(polygon, lambda x: x.get_roughness(), 0.04*global_learning_rate)

def print_data():
  print("volume:"+str(polygon.get_volume().item()),end="\t")
  print("surface area:"+str(polygon.get_surface_area().item()))

def step():
  for i in range(10):
    volume_optimizer.optimize()
    if(torch.isnan(polygon.get_vertices()).any()):
      print("NaN detected - 1")
      print(polygon.get_vertices())
      return
    print(smoothness_optimizer.get_error(polygon))
    smoothness_optimizer.optimize()
    if(torch.isnan(polygon.get_vertices()).any()):
      print("NaN detected - 2")
      print(polygon.get_vertices())
      return
# %%
renderer.loop(space, [step])
# %%
