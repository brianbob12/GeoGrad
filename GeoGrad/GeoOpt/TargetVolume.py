from .GeometryOptimizer import GeometryOptimizer

class TargetVolume(GeometryOptimizer):

  def __init__(self, geometry, targetVolume, learningRate = 0.01):
    super().__init__(geometry, learningRate)
    self.targetVolume = targetVolume

  def get_error(self, geometry):
    return (geometry.get_volume() - self.targetVolume).abs()