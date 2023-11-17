from .GeometryOptimizer import GeometryOptimizer

class MinEdgeLengthVariance(GeometryOptimizer):

  def __init__(self, geometry, learningRate = 0.01):
    super().__init__(geometry, learningRate)

  def get_error(self, geometry):
    edge_lengths = geometry.get_edge_lengths()
    return edge_lengths.var()