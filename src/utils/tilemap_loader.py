# -*- coding: utf-8 -*-

import pyglet
import zlib
import base64
import struct

from xml.etree import ElementTree

def tilemap_loader(path, tilemap, tileset, batch):
    """ Parametres: tilemap component, tileset component, pyglet batch. """
    
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    load_map_properties(root, tilemap)
    load_tilesets(root, tileset)
    load_layers(root, tilemap, tileset, batch)
    
    print(tilemap.layers)
    print(len(tilemap.layers[0]["tiles"]))

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
        tileset.tiles[gid] = {}
        
        if element.get("source"):
            load_external_tileset(gid, element.get("source"), tileset)
        else:
            add_new_tileset(gid, element, tileset)
    
def load_external_tileset(gid, path, tileset):
    tree = ElementTree.parse(path)
    root = tree.getroot()
    
    add_new_tileset(gid, root, tileset)

def add_new_tileset(gid, element, tileset):
    tileset.tiles[gid]["tilewidth"] = int(element.get("tilewidth"))
    tileset.tiles[gid]["tileheight"] = int(element.get("tileheight"))
    image = pyglet.image.load(element.find("image").get("source"))
    tiles_w = image.width /  tileset.tiles[gid]["tilewidth"]
    tiles_h = image.height /  tileset.tiles[gid]["tileheight"]
    print(tiles_w, tiles_h)
    tileset.tiles[gid]["image"] = pyglet.image.ImageGrid(image, tiles_h, tiles_w)
    print(tileset.tiles[gid]["image"][0].width)
    
def load_layers(root, tilemap, tileset, batch):
    elements = root.findall("layer")
    
    for element in elements:
        add_new_layer(element, tilemap, tileset, batch)
        
def add_new_layer(element, tilemap, tileset, batch):
    data = load_layer_data(element)
    
    tilemap.layers.append({})
    tilemap.layers[-1]["width"] = int(element.get("width"))
    tilemap.layers[-1]["height"] = int(element.get("height"))
    tilemap.layers[-1]["name"] = element.get("name")
    tilemap.layers[-1]["tiles"] = []

    assert len(data) == tilemap.layers[-1]["width"] * tilemap.layers[-1]["height"]
    
    i = 0
    
    for y in range(0, tilemap.layers[-1]["height"]):
        for x in range(0, tilemap.layers[-1]["width"]):
            if data[i] < 1: continue
            
            new_tile = pyglet.sprite.Sprite(get_tileset_image(tileset, data[i]))
        
            new_tile.x = x *  tilemap.tilewidth
            new_tile.y = y *  tilemap.tileheight
            new_tile.batch = batch
        
            tilemap.layers[-1]["tiles"].append(new_tile)
                
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
    return tileset.tiles[2]["image"][45]
    