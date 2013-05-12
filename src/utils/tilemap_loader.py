# -*- coding: utf-8 -*-

import pyglet
import zlib
import base64
import struct
import math

from xml.etree import ElementTree

class Layer(object):
    """ This class stores one layer of the map. """
    
    def __init__(self):
        self.width = 0
        self.height = 0
        self.name = ""
        self.tiles = []
    
class Tile(object):
    """ This class stores data of one tile. """
    
    def __init__(self, gid):
        self.gid = gid
    
class TilesetBin(object):
    """ This class stores all tiles on tilesets. """
    
    def __init__(self, width=256, height=256):
        self.atlas = pyglet.image.atlas.TextureAtlas(width, height)
        self.tiles = []
    
    def add(self, image):
        self.tiles.append(self.atlas.add(image))
        
    def get_tex_coords(self, gid):
        return self.tiles[gid].tex_coords

def tilemap_loader(path, tilemap):
    """ Parametres: tilemap component"""
    
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    load_map_properties(root, tilemap)
    load_tilesets(root, tilemap)
    load_layers(root, tilemap)

def load_map_properties(root, tilemap):
    tilemap.tileheight = int(root.get("tileheight"))
    tilemap.tilewidth = int(root.get("tilewidth"))
    
    tilemap.width = int(root.get("width"))
    tilemap.height = int(root.get("height"))
    
    tilemap.version = root.get("version")
    
def load_tilesets(root, tilemap):
    elements = root.findall("tileset")
    
    tiles = []
    
    for element in elements:
        if element.get("source"):
            
            tiles.extend(load_external_tiles(element.get("source"), tilemap))
        else:
            tiles.extend(load_tiles(element, tilemap))
            
    add_tiles_to_bin(tiles, tilemap)
            
def load_tiles(element, tilemap):
    """ Returns all tiles of one tileset. """
    
    tiles = []
    image = pyglet.image.load(element.find("image").get("source"))
    tiles_w = image.width / tilemap.tilewidth
    tiles_h = image.height / tilemap.tileheight
    
    for row in range(tiles_h):
        for col in range(tiles_w):
            tiles.append(image.get_region(col*tilemap.tilewidth,
                                          (image.height-tilemap.tileheight)-row*tilemap.tileheight,
                                          tilemap.tilewidth,
                                          tilemap.tileheight))

    return tiles

def add_tiles_to_bin(tiles, tilemap):
    """ Adds tiles to bin and returns it. """
    
    tiles_in_grid = math.ceil(math.sqrt(len(tiles)))
    atlas_width = tiles_in_grid * tilemap.tilewidth
    atlas_height = tiles_in_grid * tilemap.tileheight
    
    texture_size = 2
    
    while atlas_width > texture_size and atlas_height > texture_size:
        texture_size = texture_size*2
    
    tilemap.tileset_bin = TilesetBin(texture_size, texture_size)
    
    for tile in tiles:
        tilemap.tileset_bin.add(tile)
    
def load_external_tiles(path, tilemap):
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    return load_tiles(root, tilemap)
    
def load_layers(root, tilemap):
    elements = root.findall("layer")
    
    for element in elements:
        add_new_layer(element, tilemap)
        
def add_new_layer(element, tilemap):
    data = load_layer_data(element)
    
    new_layer = Layer()
    
    new_layer.width = int(element.get("width"))
    new_layer.height = int(element.get("height"))
    new_layer.name = element.get("name")
    new_layer.tiles = {}

    assert len(data) == new_layer.width * new_layer.height
    
    i = 0
    
    for row in range(new_layer.height):
        for col in range(new_layer.width):
            if data[i] < 1: continue

            new_layer.tiles[(col, row)] = Tile(data[i]-1)
                   
            i = i + 1
        
    tilemap.layers.append(new_layer)

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
