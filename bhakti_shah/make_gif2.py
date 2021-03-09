import imageio
import os

folder = 'data/images' 
files = [f"{folder}/{file}" for file in os.listdir(folder)]

images = [imageio.imread(file) for file in files]
imageio.mimwrite('movie.gif', images, fps=60)
