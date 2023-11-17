from typing import Tuple
import torch
import numpy as np

class Surface2D:
  def __init__(self, number_of_vertices:int,
              size_x:float = 0.5,
              size_y:float = 0.5,
              pos:Tuple[float,float] = (0.5,0.5)
              ):
    starting_vertices = np.random.uniform(-0.5,0.5,(number_of_vertices,2))
    starting_vertices[:,0] *= size_x
    starting_vertices[:,1] *= size_y
    starting_vertices[:,0] += pos[0]
    starting_vertices[:,1] += pos[1]
    self.vertices = torch.nn.Parameter(torch.Tensor(starting_vertices))

  def set_vertices(self, vertices:torch.Tensor):
    self.vertices = vertices

  def get_vertices(self)->torch.Tensor:
    return self.vertices

  def get_volume(self)->torch.Tensor:
    #( x1 y2 − y1 x2 ) + ( x2 y3 − y2 x3 ) ..... + ( xn y1 − yn x1 ) 2
    #shift all the rows down by one
    areaFactor = torch.roll(self.vertices, -1, 0)
    #swap the x and y values
    areaFactor = torch.roll(areaFactor, 1, 1)
    #negate the x values
    areaFactor[:,1] *= -1
    #transpose
    areaFactor = areaFactor.transpose(0,1)
    #multiply
    result = torch.trace(torch.mm(self.vertices, areaFactor))
    return torch.sum(result, dim=0).abs()/2

  def get_edges(self) -> torch.Tensor:
    #get x and y distances between adjacent vertices
    edges = torch.roll(self.vertices, -1, 0) - self.vertices
    return edges

  def get_edge_lengths(self) -> torch.Tensor:
    edges = self.get_edges()
    #get the magnitude of the distances
    edge_lengths = torch.norm(edges, dim=1)
    return edge_lengths

  def get_surface_area(self)->torch.Tensor:
    edges = self.get_edges()
    #get the magnitude of the distances
    edge_lengths = torch.norm(edges, dim=1)
    return torch.sum(edge_lengths, dim=0)

  def count_self_intersections(self) -> torch.Tensor:
    edges = self.get_edges()
    #get the magnitude of the distances
    edge_lengths = torch.norm(edges, dim=1)
    #get the angle between adjacent edges
    angles = torch.acos(torch.sum(edges * torch.roll(edges, 1, 0), dim=1) / (edge_lengths * torch.roll(edge_lengths, 1, 0)))
    return torch.sum(angles > 3.14159, dim=0)