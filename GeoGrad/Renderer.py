from typing import Callable, List
import pygame
from .Space2D import *
from .Surface2D import *

class Renderer:
  def __init__(self, width:int = 500, height:int = 500):
    pygame.init()
    self.screen = pygame.display.set_mode((width, height))
    self.recording = False

  def start_recording(self, folder:str):
    self.recording = True
    self.folder = folder

  def render(self, space:Space2D):
    self.screen.fill((0,0,0))
    for obj in space.objects:
      if isinstance(obj, Surface2D):
        self.render_surface(obj, space)
    pygame.display.flip()


  def render_surface(self, geometry:Surface2D, space:Space2D):
    vertices = geometry.get_vertices()
    vertices = vertices.detach().numpy()
    xs = vertices[:,0] * space.size_x
    ys = vertices[:,1] * space.size_y
    points = list(zip(xs.astype(int),ys.astype(int)))
    pygame.draw.polygon(self.screen, (255,255,255), points, 1)
    pygame.display.flip()
    
  def loop(self, space:Space2D, lambdas:List[Callable] = []):
    running = True
    i=0
    while running:
      for func in lambdas:
        func()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
      self.render(space)

      if self.recording:
        filename = f"{self.folder}/{i:04d}.png"
        self.saveFrame(filename)
      
      i+=1
    pygame.quit()

  def saveFrame(self,fileName:str):
    pygame.image.save(self.screen,fileName)