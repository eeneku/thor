# -*- coding: utf-8 -*-

import pyglet

key_state = pyglet.window.key.KeyStateHandler()

tilemap_size = (10, 10)
tilemap = []

for row in range(tilemap_size[1]):
    new_row = []
    for col in range(tilemap_size[0]):
        new_row.append(0)
    
    tilemap.append(new_row)

tileset_image = pyglet.image.load("gfx/grass.png")
tileset_bin = pyglet.image.atlas.TextureBin()
tile_image = tileset_bin.add(tileset_image)
texture_group = pyglet.graphics.TextureGroup(tile_image)
tilesize = (32, 32)

vertex_data = []
texture_data = []
color_data = []

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(1280,720)

window.push_handlers(key_state)

y1 = 0
for row in range(tilemap_size[1]):
    y2 = y1 + tilesize[1]
    x1 = 0
    
    for col in range(tilemap_size[0]):
        x2 = x1 + tilesize[0]
        vertex_data.extend([x1, y1, x2, y1, x2, y2, x1, y2])
        texture_data.extend(tile_image.tex_coords)
        color_data.extend((255, 255, 255, 255)*4)
        x1 = x2
    y1 = y2
    
fps = pyglet.clock.ClockDisplay()

vertex_list = batch.add(tilemap_size[1]*tilemap_size[0]*4, 
                        pyglet.gl.GL_QUADS, 
                        texture_group,
                        ('v2i', vertex_data),
                        ('t3f', texture_data),
                        ('c4B', color_data))

world_x = 14
world_y = 0

def update(dt):
    global world_y, world_x
    
    if key_state[pyglet.window.key.UP]:
        world_y -= 128 * dt
    if key_state[pyglet.window.key.DOWN]:
        world_y += 128 * dt
    if key_state[pyglet.window.key.RIGHT]:
        world_x -= 128 * dt
    if key_state[pyglet.window.key.LEFT]:  
        world_x += 128 * dt
            
@window.event
def on_draw():
    window.clear()
    pyglet.gl.glLoadIdentity()
    pyglet.gl.glTranslatef(world_x, world_y, 0)
    batch.draw()
    pyglet.gl.glPushMatrix()
    pyglet.gl.glPopMatrix()
    pyglet.gl.glLoadIdentity()
    fps.draw()
    
pyglet.clock.schedule_interval(update, 1/120.0)
    
pyglet.app.run()