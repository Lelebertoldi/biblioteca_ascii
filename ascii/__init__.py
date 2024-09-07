#!/usr/bin/env python
import math
from ascii import asciify
from ascii import colorize

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb

# import image stuff
from PIL import Image
import urllib3
http = urllib3.PoolManager()
import io

# load images from URL
def loadFromUrl(URL, columns=60, rows=None, color=True):
    fd = http.request('GET', URL)
    image_file = io.BytesIO(fd.data)
    im = Image.open(image_file)

    size = im.size
    if rows is None:
        rows = int(round(columns * size[1] / size[0]))

    """
    rows/columns = height/width
    """
    
    im = im.resize((columns, rows))
    px = im.load()
    size = im.size
    output = ""
    
    for y in range(size[1]):
        for x in range(size[0]):
            _px = px[x, y]
            _a = asciify.getRawChar(_px[0], _px[1], _px[2], 1)
            if color:
                _a = asciify.asciify(_px[0], _px[1], _px[2], 1)
            
            output += _a
        output += "\n"
    
    return output

# load images from local file
def loadFromFile(image_file, columns=60, rows=None, color=True):
    # Abre a imagem a partir do caminho local
    im = Image.open(image_file)

    size = im.size
    if rows is None:
        rows = int(round(columns * size[1] / size[0]))

    """
    rows/columns = height/width
    """
    # Redimensiona a imagem com base na largura e altura fornecidas
    im = im.resize((columns, rows))
    px = im.load()
    size = im.size
    output = ""
    
    for y in range(size[1]):
        for x in range(size[0]):
            _px = px[x, y]
            _a = asciify.getRawChar(_px[0], _px[1], _px[2], 1)
            if color:
                _a = asciify.asciify(_px[0], _px[1], _px[2], 1)
            
            output += _a
        output += "\n"
    
    return output

def onePixel(r, g, b):
	return asciify.asciify(r,g,b, 1)

def color(code, rawChar):
	ansi = colorize.wrapAnsi256(code, 0)
	reset = '\x1b[0m'
	return ansi + rawChar + reset