print("библеотек загруска...")
import time
import json
import pygame
import time
import os
import socket
from os import path

        
blok_datanew = [
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_gras", "blok_land", "blok_land", "blok_land", "blok_land", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras"],
["blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land","blok_land","blok_land","blok_land","blok_land","blok_land","blok_land","blok_land"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_gras","blok_land","blok_rok","Erorr","blok_ore_iron","blok_ore_diamond","blok_coal_ore","",""]
]


print("загруска мира...")


config = [
"ru", #язык
0.5] #0]  # громкость






print("лакализацыя загруска...")
langeu=config[0]
if("ru"==langeu):
    from ru import *
    
if("en"==langeu):
    from en import *
if("polsk"==langeu):
    from polsk import *

    
print("лакализацыя: "+langeu)
   






version="alpha 0.7.3"


android=0






if(android==0):
 Config="\nClientID=769246787596058635 \nState="+"loading"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_main_menu"
 open("config.ini", 'w').write(Config)
 os.startfile("easyrp.exe")


folder_path = os.path.join(path.dirname(__file__))
print("инитилизацыя переменных и экрана")
     
if(android==1):
 datafiles="/storage/emulated/0/gamedat/" # андроит версия
 datafiles1=datafiles+"logo/prievzostawca_"
 datafilesloading=datafiles+"animetloading/preview_"
if(android==0):
 datafiles=folder_path+"\gamedat\\"  # boomOS версия
 datafiles1=datafiles+"logo\prievzostawca_"
 datafilesloading=datafiles+"animetloading\preview"
 datafilesSetings=datafiles+"animetsetting\\animetsetting"
 
 pygame.display.set_icon(pygame.image.load(os.path.join(folder_path+'\\boomOS.ico')))
 

animation=1
play=0
x=0
y=0
#os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)






# initialize pygame
pygame.init()


clock = pygame.time.Clock() 
pygame.mixer.music.load(datafiles+"Among_Us_-_M_M_Piano.mp3")

# create display & run update
width = 800
height = 600
#width = 1920
#height = 1080
display = pygame.display.set_mode((width, height)) #NOFRAME ,flags = pygame.OPENGL
#pygame.display.update()
pygame.display.set_caption("bmscraft")

#pygame.mouse.set_visible(False)

print(loading_game)


# define colors
def ErorrScr():
 if(Erorrsrean==1):
     display.fill((0, 0, 0))
     pygame.display.update()
     time.sleep(1)
     
     font = pygame.font.Font(None, 20)
     menufon_rect = Erorr_surf.get_rect(bottomright=(800, 600)) 
     display.blit(Erorr_surf, menufon_rect)
     
     textfps = font.render("произошла ошибка игры", 1, (250,0, 0))
     placefps = textfps.get_rect(center=(200, 230))
     display.blit(textfps, placefps)
     
     textfps = font.render("код ошибки: "+Erorrcode, 1, (250,0, 0)) 
     placefps = textfps.get_rect(center=(280, 250))
     display.blit(textfps, placefps)
     pygame.display.update()
     time.sleep(2)

#
imglogoim=0
if(animation==1):
    
 while not (260==imglogoim):
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
             game_end = True
  clock.tick(30)
  if(10>imglogoim):
      imglogoimc=("000"+str(imglogoim))
      
  else:
      if(100>imglogoim):
         imglogoimc=("00"+str(imglogoim))
      else:
          if(1000>imglogoim):
            imglogoimc=("0"+str(imglogoim))
  #print(imglogoimc)
  imglogoim=imglogoim+1
  if(imglogoim<181):
       logoloding_surf = pygame.image.load(datafiles1+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
      
     
  else:
      logoloding_surf = pygame.image.load(datafiles1+"0180.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)
     
  fps = str(int(clock.get_fps()))
  font = pygame.font.Font(None, 30)
  textfps = font.render("fps: "+fps, 1, (100, 100, 100))
  placefps = textfps.get_rect(center=(200, 150))
  display.blit(textfps, placefps)
  pygame.display.update()
     


def aimsetings():
 if(animation==1):
  imglogoim=0
  while not (100==imglogoim):
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
              game_end = True
   clock.tick(30)
   pygame.display.update()
   if(10>imglogoim):
       imglogoimc=("000"+str(imglogoim))
      
   else:
       if(100>imglogoim):
          imglogoimc=("00"+str(imglogoim))
       else:
           if(1000>imglogoim):
             imglogoimc=("0"+str(imglogoim))
   #print(imglogoimc)
   imglogoim=imglogoim+1
   if(imglogoim<84):
       logoloding_surf = pygame.image.load(datafilesSetings+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
       
     
   else:
      logoloding_surf = pygame.image.load(datafilesSetings+"0084.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)





def loading():
 if(animation==1):
  imglogoim=0
  while not (300==imglogoim):
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
              game_end = True
   clock.tick(30)
   pygame.display.update()
   if(10>imglogoim):
       imglogoimc=("000"+str(imglogoim))
      
   else:
       if(100>imglogoim):
          imglogoimc=("00"+str(imglogoim))
       else:
           if(1000>imglogoim):
             imglogoimc=("0"+str(imglogoim))
   #print(imglogoimc)
   imglogoim=imglogoim+1
   if(imglogoim<121):
       logoloding_surf = pygame.image.load(datafilesloading+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
       
     
   else:
      logoloding_surf = pygame.image.load(datafilesloading+"0120.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)








    

CURSOR_rect = pygame.image.load(datafiles+'cursor.png')

 # 16 блоков на адин экрана влизает
#pygame.mixer.init(22050, -16, 2, 2048)
game_end = False
bloksX=0
bloksY=0

#pygame.mouse.set_visible(False) 
cmd=""
cmd1=""
cmd2=""
cmd3=""
cmd4=""



despled=0
Erorrsrean=0
Erorrcode=""
bfcube=""
settings=0
bird_pos=(0,0)
bloksCamX=0
bloksCamY=-1200
findbloks=0
menu=1
clock.tick(60)
Renderbloks=True
inventarim=0
# 8
battan_surf = pygame.image.load(os.path.join(datafiles+'menu_battan.png'))
pygame.mixer.music.play(-1)
menufon_surf = pygame.image.load(os.path.join(datafiles+'mane_menufon.png'))
if(android==0):
 f = open("config.ini", 'w')
 Config="\nClientID=769246787596058635 \nState="+"main menu"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_main_menu"
 f.write(Config)
print(loading_game)
despled=0
print("игра загружена")
if(1==1): #не оброщайте на это я хотел сделать экран ошибки но потом плюнул та-как в консоли всё пишета
 while not game_end:
  display.fill((0, 0, 0))
  
  pygame.mixer.music.set_volume(config[1])
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
            display.fill((0, 0, 0))
            pygame.display.update()
            time.sleep(1)
            game_end = True


     if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 3:
        bird_pos = event.pos
        if(599>bird_pos[1]):
         if(findbloks==1):
          
          print()
          cmd=("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          print("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          cmd1="camX "+str(bloksCamX)+" camY "+str(bloksCamY)
          print("camX "+str(bloksCamX)+" camY "+str(bloksCamY))
         #print()
         
          blokscvX=((bird_pos[0])/50+((bloksCamX-bloksCamX-bloksCamX)/50))
          blokscvY=((bird_pos[1])/50+(bloksCamY-bloksCamY-bloksCamY)/50)
        # print()
          print("blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1))
          cmd2="blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1)
          cmd3="bloksX "+str(int(blokscvX+1))+" bloksY "+str(int(blokscvY+1))
        
          print("bloksX "+str(int(blokscvX+1)))
          print("bloksY "+str(int(blokscvY+1)))
          try:
           if(blokscvY>67):
              print("none blok!")
           else:
             if((int(blokscvX))<(len(blok_data[int(blokscvY)]))):
              if("blok_rok"==blok_data[int(blokscvY)][int(blokscvX)]):
                  cmd4=""
              else:
                  if("blok_air"==blok_data[int(blokscvY)][int(blokscvX)]):
                      print(blok_data[67][inventarim])
                      if not(""==blok_data[67][inventarim]):
                        Playnbr.play()
                        cmd4="clik is "+blok_data[int(blokscvY)][int(blokscvX)]
                        blok_data[int(blokscvY)][int(blokscvX)]=blok_data[67][inventarim]
          except:
               print("блок был не нейден или какойта збой не кретичный ")
        
       
          
      if event.button == 1:  #  левая кнопка мыши
        bird_pos = event.pos

        if(menu==1):
           if(Erorrsrean==1):
                Erorrsrean=0
                settings=0
                menufon_surf = pygame.image.load(os.path.join(datafiles+'mane_menufon.png'))
           if(Erorrsrean==0):
            if(settings==0):   
            #bird_pos 187, 293
            # потсказка для идеотов как я
            # bird_pos[0]это x
            # bird_pos[1]это y
            
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<293) and (bird_pos[1]>293-50):
                    if(findbloks==0):
                      
                      font = pygame.font.Font(None, 30)
                      textfps = font.render(loading_game, 1, (100, 100, 100))
                      placefps = textfps.get_rect(center=(200, 30))
                      display.blit(textfps, placefps)
                      pygame.display.update()
                      loading()
                      
    
                       

                      with open('world.wrld', 'r') as fr:
                        blok_data = json.load(fr)
                      
                      #inventari=
                      display.fill((0, 0, 0))
                      menu=0
                      findbloks=1
                      breac=pygame.mixer.Sound(datafiles+"Hit_Hurt10.wav") 
                      Playnbr=pygame.mixer.Sound(datafiles+"Hit_Hurt19.wav")
                      pygame.mixer.music.load(datafiles+"17-Excuse.mp3")
                      inventarigui_surf = pygame.image.load(os.path.join(datafiles+"gui_inventari.png"))
                      inventariguiselect_surf = pygame.image.load(os.path.join(datafiles+"select.png"))
                      sky_surf = pygame.image.load(os.path.join(datafiles+'sky.png'))
                      pygame.mixer.music.play(-1)
                      despled=0
                      
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<100+406) and (bird_pos[1]>100+406-50):
                    
                    display.fill((0, 0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    game_end = True

             if(bird_pos[0]<184) and (bird_pos[0]>184-150):
                if(bird_pos[1]<364+50) and (bird_pos[1]>364-50+50): 
                    menufon_surf = pygame.image.load(os.path.join(datafilesSetings+'0084.png'))
                    print("test")
                    aimsetings()
                    
                    settings=1
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<293+55) and (bird_pos[1]>293-50+55):
                    print("test")
      
                    
                      
                
        
        
        
        if(599>bird_pos[1]):
         if(findbloks==1):
          
          print()
          cmd=("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          print("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          cmd1="camX "+str(bloksCamX)+" camY "+str(bloksCamY)
          print("camX "+str(bloksCamX)+" camY "+str(bloksCamY))
         #print()
         
          blokscvX=((bird_pos[0])/50+((bloksCamX-bloksCamX-bloksCamX)/50))
          blokscvY=((bird_pos[1])/50+(bloksCamY-bloksCamY-bloksCamY)/50)
        # print()
          print("blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1))
          cmd2="blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1)
          cmd3="bloksX "+str(int(blokscvX+1))+" bloksY "+str(int(blokscvY+1))
        
          print("bloksX "+str(int(blokscvX+1)))
          print("bloksY "+str(int(blokscvY+1)))
          try:
           if(blokscvY>67):
              print("none blok!")
           else:
             if((int(blokscvX))<(len(blok_data[int(blokscvY)]))):
              if("blok_air"==blok_data[int(blokscvY)][int(blokscvX)]):
                  cmd4=""
              else:
                   breac.play()
                   cmd4="clik is "+blok_data[int(blokscvY)][int(blokscvX)]
                   blok_data[int(blokscvY)][int(blokscvX)]="blok_air"
          except:
              print("блок был не нейден или какойта збой не кретичный ")
              
       # if
      if event.button == 4:
          print("прокручивания вперед")
          if not(inventarim==0):
              inventarim=inventarim-1
         # =0 # 8
          

      if event.button == 5:
          print("прокручивания назад")
          if not(inventarim==8):
              inventarim=inventarim+1
          
  #  elif event.type == pygame.KEYDOWN:

  keys = pygame.key.get_pressed()       
  if keys[pygame.K_a]:
                # move left
                 print("лево")
                 if(findbloks==1):
                   bloksCamX=bloksCamX+10
 
  if keys[pygame.K_d]:
                # move right
                 print("право")
                 if(findbloks==1):
                  bloksCamX=bloksCamX-10
                

 #
  if keys[pygame.K_w]:
                # move up
                 print("верх")
                 if(findbloks==1):
                  bloksCamY=bloksCamY+10

 
  if keys[pygame.K_s]:
                # move down
                 print("низ")
                 if(findbloks==1):
                  bloksCamY=bloksCamY-10
  if keys[pygame.K_u]:
               # if pygame.key == pygame.K_i:
                   # if pygame.key == pygame.K_o:
                        Erorr_surf = pygame.image.load(os.path.join(datafiles+'Erorr screan.png'))
                        Erorrcode=("робота игры была завершина")
                        Renderbloks=False
                        pygame.mixer.music.load(datafiles+"Among_Us_-_M_M_Piano.mp3")
                        pygame.mixer.music.play(-1)
                        findbloks=0
                        menu=1
                        Erorrsrean=1
                        ErorrScr()
  if keys[pygame.K_o]:
      with open('world.wrld', 'w') as fw:
          json.dump(blok_data, fw)
          cmd4="game save!"
      
      
                                
            

        
  if(menu==1):
    
    font = pygame.font.Font(None, 30)
    menufon_rect = menufon_surf.get_rect(bottomright=(800, 600)) 
    display.blit(menufon_surf, menufon_rect) 
    if(settings==0):   
     menufon_rect = battan_surf.get_rect(bottomright=(184, 293)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(battanplaygame1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266))
     display.blit(textfps, placefps)

     menufon_rect = battan_surf.get_rect(bottomright=(184, 293+55)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(battanplaygameONLAIN1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266+55))
     display.blit(textfps, placefps)

     
     menufon_rect = battan_surf.get_rect(bottomright=(184, 364+50)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(setingsbottan, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 100+290))
     display.blit(textfps, placefps)
     

     menufon_rect = battan_surf.get_rect(bottomright=(184, 100+406)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(exit_battanmenu, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 100+380))
     display.blit(textfps, placefps)
     
     
     

     textfps = font.render(battanplaygame1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266))
     display.blit(textfps, placefps)

     

    textfps = font.render(version_name+version, 1, (250, 250, 250))
    placefps = textfps.get_rect(center=(800-100, 600-30))
    display.blit(textfps, placefps)
    if(settings==1):
        print("")
        


     
     
  if(findbloks==1):
   Renderbloks=True
   sky_rect = sky_surf.get_rect(bottomright=(800, 600))
   display.blit(sky_surf, sky_rect)
  # try:
   if(1==1):
    while Renderbloks:
      if not ((bloksX+1)*50+bloksCamX<1):
       if not ((bloksX)*50+bloksCamX>801):
        if not ((bloksY)*50+bloksCamY>601):
         if not ((bloksY+1)*50+bloksCamY<1):
          if not (blok_data[bloksY][bloksX]=="blok_air"):
           if not (bfcube==blok_data[bloksY][bloksX]):
             try:
                 blokimg_surf = pygame.image.load(os.path.join(datafiles+blok_data[bloksY][bloksX]+".png"))
             except:
                 blokimg_surf = pygame.image.load(os.path.join(datafiles+"noneblok.png"))
           blokimg_rect = blokimg_surf.get_rect(bottomright=((bloksX+1)*50+bloksCamX, (bloksY+1)*50+bloksCamY))
           display.blit(blokimg_surf, blokimg_rect)
           bfcube=blok_data[bloksY][bloksX]
        
       #print(blok_data[bloksY][bloksX]+" кордината Y:"+str(bloksY)+" X:"+str(bloksX))
      bloksX=bloksX+1
      if(len(blok_data[bloksY]) == bloksX):
         bloksY=bloksY+1
         bloksX=0
      if(67==bloksY):          
           font = pygame.font.Font(None, 30)
           textfps = font.render("cmd: "+cmd, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 30))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd1, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 45))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd2, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 65))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd3, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 85))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd4, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 100))
           display.blit(textfps, placefps)
          
          
           
          
           
           inventarigui_rect = inventarigui_surf.get_rect(bottomright=(550, 600))
           display.blit(inventarigui_surf, inventarigui_rect)
           RenderInventari=0
           while not RenderInventari==8:
            if not(blok_data[67][RenderInventari]==""):
             try:
                 blokimginv_surf = pygame.image.load(os.path.join(datafiles+blok_data[67][RenderInventari]+".png"))
             except:
                 blokimginv_surf = pygame.image.load(os.path.join(datafiles+"noneblok.png"))
             blokinventari = pygame.transform.scale(blokimginv_surf, (30, 30))
             inventariguiselect_surf_rect = inventarigui_surf.get_rect(bottomright=(550+4+(36.5*RenderInventari), 600+4))
             display.blit(blokinventari, inventariguiselect_surf_rect)
            RenderInventari=RenderInventari+1
             
               
               
           inventariguiselect_surf_rect = inventarigui_surf.get_rect(bottomright=(550+(36.5*inventarim), 600))
           display.blit(inventariguiselect_surf, inventariguiselect_surf_rect)
           
           pygame.draw.rect(display, (255, 255, 255), (bird_pos[0]-3, bird_pos[1]-3, 10, 10)) 
           pygame.draw.rect(display, (0,0,0), (0,600, 800, 800))

           bloksX=0
           bloksY=0
          
           Renderbloks=False
   #except:
     # Erorr_surf = pygame.image.load(os.path.join(datafiles+'Erorr screan.png'))
      #Erorrcode=("произошла ошибка рендера блока!")
      #Renderbloks=False
      #pygame.mixer.music.load(datafiles+"Among_Us_-_M_M_Piano.mp3")
      #pygame.mixer.music.play(-1)
     # findbloks=0
     # menu=1
     # Erorrsrean=1
     # ErorrScr()

  if(Erorrsrean==1):
     font = pygame.font.Font(None, 20)
     menufon_rect = Erorr_surf.get_rect(bottomright=(800, 600)) 
     display.blit(Erorr_surf, menufon_rect)
     
     textfps = font.render("произошла ошибка игры", 1, (250,0, 0))
     placefps = textfps.get_rect(center=(200, 230))
     display.blit(textfps, placefps)
     
     textfps = font.render("код ошибки: "+Erorrcode, 1, (250,0, 0)) 
     placefps = textfps.get_rect(center=(280, 250))
     display.blit(textfps, placefps)


     
  fps = str(int(clock.get_fps()))
  font = pygame.font.Font(None, 30)
  textfps = font.render("fps: "+fps, 1, (250,0, 0))
  placefps = textfps.get_rect(center=(200, 150))
  display.blit(textfps, placefps)
 
# CURSOR_surf=CURSOR_rect.get_rect(bottomright=())
 #display.blit(CURSOR_rect,pygame.mouse.get_pos()) 
  pygame.display.update()
  if(android==0):
     if(despled==0):
      f = open("config.ini", 'w')
      Config="\nClientID=769246787596058635 \nState="+"game rase none"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_rase_none"
      f.write(Config)
      despled=1
         



# pygame.display.flip()
# fps = str(int(get_fps()))
# print("fps "+fps)
 

 #menufon_rect = battan_surf.get_rect(bottomright=(184, 406)) 
# display.blit(battan_surf, menufon_rect)
  clock.tick(100)

#except:
   # print("erorr")
os.system("TASKKILL /F /IM easyrp.exe")
pygame.mixer.music.play(0)
display.fill((0, 0, 0))
pygame.display.update()
time.sleep(1)

pygame.quit()

    
  # boomos_surf = pygame.image.load('c806f63ed34bf4f0f50a0b90f8dd6d60.png')
  # boomos_rect = boomos_surf.get_rect(bottomright=(1130, 800))
  
    #display.blit(boomos_surf, boomos_rect)
