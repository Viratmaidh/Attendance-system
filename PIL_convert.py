import pylab as pl
from PIL import Image

im = Image.open('Dataset/User.1.1.jpg').convert('L')
pl.imshow(im, origin='lower')
pl.show()