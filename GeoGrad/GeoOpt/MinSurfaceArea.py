from .GeometryOptimizer import GeometryOptimizer

class MinSurfaceArea(GeometryOptimizer):
  def __init__(self, geometry, learningRate = 0.01):
    super().__init__(geometry, learningRate)

  def get_error(self, geometry):
    return geometry.get_surface_area()