from typing import Callable
from GeoGrad import Surface2D
from . import GeometryOptimizer
import torch

class MinimizeValue(GeometryOptimizer):

  def __init__(self, geometry:Surface2D, get_value:Callable[[Surface2D],torch.Tensor], learningRate = 0.01):
    self.get_value = get_value
    super().__init__(geometry, learningRate)

  def get_error(self, geometry:Surface2D):
    return self.get_value(geometry)
  