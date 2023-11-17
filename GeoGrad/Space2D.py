class Space2D:
  def __init__(self, size_x, size_y):
    self.size_x = size_x
    self.size_y = size_y
    self.objects = []

  def add_object(self, new_object):
    self.objects.append(new_object)
