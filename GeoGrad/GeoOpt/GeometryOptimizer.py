from abc import ABC, abstractmethod
from typing import Callable
import torch
from GeoGrad import Surface2D


class GeometryOptimizer(ABC):
  def __init__(self, geometry:Surface2D,
              learningRate:float = 0.01):
    self.geometry = geometry
    self.learningRate = learningRate
    self.optimizer = torch.optim.SGD([geometry.get_vertices()], lr=learningRate)

  @abstractmethod
  def get_error(self, geometry:Surface2D)->torch.Tensor:
    pass

  def optimize(self):
    self.optimizer.zero_grad()
    error = self.get_error(self.geometry)
    error.backward()
    self.optimizer.step()