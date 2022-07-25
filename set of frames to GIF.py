
from PIL import Image, ImageDraw
import imageio 
import numpy as np

frames = []
nums=np.arange(1000,1267)

for num in nums:

    frames.append(f"C:/Users/aleks/1a/FUNGUJETO_O/example data/gif/animation_{num}.png")



images = []
for frame in frames:
    images.append(imageio.imread(frame))
imageio.mimsave('C:/Users/aleks/1a/FUNGUJETO_O/example data/moving_particle.gif', images)
