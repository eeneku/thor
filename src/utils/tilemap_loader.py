# -*- coding: utf-8 -*-

import pyglet
import zlib
import base64
import struct

from xml.etree import ElementTree

class Layer(object):
    """ Layer holds one layer of tilemap. """
    def __init__(self):
        self.width = 0
        self.height = 0
        self.name = None
        self.tiles = []


def tilemap_loader(path, tilemap, tileset, batch):
    """ Parametres: tilemap component, tileset component. """
    
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    load_map_properties(root, tilemap)
    load_tilesets(root, tileset)
    load_layers(root, tilemap, tileset, batch)

def load_map_properties(root, tilemap):
    tilemap.tileheight = int(root.get("tileheight"))
    tilemap.tilewidth = int(root.get("tilewidth"))
    
    tilemap.width = int(root.get("width"))
    tilemap.height = int(root.get("height"))
    
    tilemap.version = root.get("version")
    
def load_tilesets(root, tileset):
    elements = root.findall("tileset")
    
    for element in elements:
        gid = int(element.get("firstgid"))
        
        if element.get("source"):
            load_external_tileset(gid, element.get("source"), tileset)
        else:
            add_new_tileset(gid, element, tileset)
    
def load_external_tileset(gid, path, tileset):
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    add_new_tileset(gid, root, tileset)

def add_new_tileset(gid, element, tileset):
    image = pyglet.image.load(element.find("image").get("source"))
    tiles_w = image.width /  int(element.get("tilewidth"))
    tiles_h = image.height /  int(element.get("tilewidth"))
    tileset.tiles.append((gid, (pyglet.image.TextureGrid(pyglet.image.ImageGrid(image, tiles_h, tiles_w)))))
    
def load_layers(root, tilemap, tileset, batch):
    elements = root.findall("layer")
    
    for element in elements:
        add_new_layer(element, tilemap, tileset, batch)
        
def add_new_layer(element, tilemap, tileset, batch):
    data = load_layer_data(element)
    
    tilemap.layers.append(Layer())
    tilemap.layers[-1].width = int(element.get("width"))
    tilemap.layers[-1].height = int(element.get("height"))
    tilemap.layers[-1].name = element.get("name")
    tilemap.layers[-1].tiles = {}

    assert len(data) == tilemap.layers[-1].width * tilemap.layers[-1].height
    
    i = 0
    
    for y in range(0, tilemap.layers[-1].height):
        for x in range(0, tilemap.layers[-1].width):
            if data[i] < 1: continue
            
            new_tile = pyglet.sprite.Sprite(get_tileset_image(tileset, data[i]))
            new_tile.batch = batch
            new_tile.visible = False
            
            tilemap.layers[-1].tiles[(x, y)] = new_tile
                
            i = i + 1

def load_layer_data(layer):
    data_element = layer.find("data")
    
    if data_element.get("encoding"):
        data = decode_layer_data(data_element.text)

    if data_element.get("compression"):
        data = decompress_layer_data(data)
        
    data = struct.unpack('<%di' % (len(data)/4,), data)
    return data

def decode_layer_data(data):
    return base64.b64decode(data)

def decompress_layer_data(data):
    return zlib.decompress(data)

def get_tileset_image(tileset, gid):
    tile = 0
    for tset in reversed(tileset.tiles):
        tile += 1
        if gid >= tset[0]:
            tile_id = gid - tset[0]
            tiles_w = tset[1].columns
            
            y = tile_id / tiles_w
            x = tile_id % tiles_w
            y = tset[1].rows-1 - y
            
            return tset[1][y, x]
        