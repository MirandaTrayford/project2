import pyglet

win = pyglet.window.Window()
pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)

img = pyglet.image.load('my_image.bmp')
x, y, z = 0, 0, 0
img.blit(x, y, z)
