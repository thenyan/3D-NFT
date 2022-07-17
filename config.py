#      /\_/\
#     ( o.o )
#      > ^ <
# 3D MODELS TO NFT
andro

## INSTALLATION 
#$ pip install -r requirements.txt

## INPUT
#Code supporting `.blend` now. You can use all the extensions that Blender supports by editing the code.

## OUTPUT
#`.png` and Metadata Jsons

## **WARNING! DON'T FORGET!**
#1. Edit `data`
#2. Edit count of `createObj` 
#3. Edit file name and file direction.

## DONATION
#Buy me a bear!
#ETH: 0x9904bFa1B183Eb9d9350A885Ddac8B1A8a80eb71

##RARITY
# weights=(10,10,10,10,10,50) 
# edit this, line 153,155,157

import random
import json
import os
import bpy
import bmesh
import time
import sys

all_images = []

#ammount=1*6*6*6*1=216 count
data =  {
  "layers": [
    {
      "name": "Body",
      "values": ["Yellow"]
    },
    {
      "name": "Hat",
      "values": ["Alchemist","Arcmage","Darkmage","Druid","Mage","Witch"]
    },
    {
      "name": "Robe",
      "values": ["Alchemist", "Arcmage","Darkmage", "Druid","Mage", "Witch"]
    },
    {
      "name": "Staff",
      "values": ["Alchemist", "Arcmage","Darkmage", "Druid","Mage", "Witch"]
    },
    {
      "name": "Background",
      "values": ["Black"]
    }
  ]
}

def metadataa(fle,i,body,glass,bag,cap, wp):
    x = open("C:\\Users\\pc\\Desktop\\test1\\json\\"+fle,'a+')
    metadata ={
    "name": "",
    "description": "",
    "image": "",
    "edition": "",
    "attributes": [
        {
        "trait_type": "Background",
        "value": ""
        },
        {
        "trait_type": "Body",
        "value": ""
        },
        {
        "trait_type": "Hat",
        "value": ""
        },
        {
        "trait_type": "Robe",
        "value": ""
        },
        {
        "trait_type": "Staff",
        "value": ""
        }
    ]}
    metadata['name']="Axolot"
    metadata['description']="It's just it"
    metadata['image']="ipfs://random/"
    metadata['edition']=i
    for i in metadata['attributes']:
      if (i["trait_type"]=="Background"):
        i["value"] = wp
      if (i["trait_type"]=="Body"):
        i["value"] = body
      if (i["trait_type"]=="Hat"):
        i["value"] = glass
      if (i["trait_type"]=="Robe"):
        i["value"] = bag
      if (i["trait_type"]=="Staff"):
        i["value"] = cap
    json_format = json.dumps(metadata, indent=2)
    x.write(json_format)

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
    
def collections(collection, col_list):
    col_list.append(collection.name)
    for sub_collection in collection.children:
        collections(sub_collection, col_list)
     
def clear():
    collection = bpy.data.collections["Collection"] 
    meshes = set()
    for obj in [o for o in collection.objects if o.type == 'MESH']:
        bpy.data.objects.remove(obj)
    meshes = set()
    for obj in [o for o in collection.objects if o.type == 'LIGHT']:
        bpy.data.objects.remove(obj)

def clear_bg():
    collection = bpy.data.collections["Collection"]
    meshes = set()
    for obj in [o for o in collection.objects if o.type == 'MESH']:
        if obj.name in "Plane":
            bpy.data.objects.remove(obj)

def createDna(data):
    new_image = {}
    for layer in data["layers"]:
        if (layer["name"]=="Background"):
          new_image[layer["name"]] = random.choices(layer["values"])[0]
        if (layer["name"]=="Body"):
          new_image[layer["name"]] = random.choices(layer["values"])[0]
        if (layer["name"]=="Hat"):
          new_image[layer["name"]] = random.choices(layer["values"],weights=(10,10,10,10,10,50))[0]
        if (layer["name"]=="Robe"):
          new_image[layer["name"]] = random.choices(layer["values"], weights=(10,10,10,10,10,50))[0]
        if (layer["name"]=="Staff"):
          new_image[layer["name"]] = random.choices(layer["values"], weights=(10,10,10,10,10,50))[0]
    if new_image in all_images:
        print("GEN> DNA EXITS")
        return createDna(data)
    else:
        print("GEN> NEW DNA: {}".format(new_image))
        return new_image


def createObj(ammount,data):
    for x in range(ammount):
        new_dna = createDna(data)
        all_images.append(new_dna)
    for y in range(ammount):
        clear()
        rez_list = []
        progress(y, ammount, status='')
        z = y + 1
        result_fbx = str(z)+".fbx"
        result_png = str(z)+".png"
        body_fbx=all_images[y]["Body"] +".blend"
        glass_fbx=all_images[y]["Hat"] +".blend"
        bag_fbx=all_images[y]["Robe"] +".blend"
        cap_fbx=all_images[y]["Staff"] +".blend"
        wp_fbx=all_images[y]["Background"] +".fbx"
        result_json = str(z)+".json"
        metadataa(result_json,z,all_images[y]["Body"],all_images[y]["Hat"], all_images[y]["Robe"],all_images[y]["Staff"],all_images[y]["Background"])
        bpy.ops.wm.append(filename="Collection 1", directory=f"C:\\Users\\pc\\Desktop\\obj\\Body\\{body_fbx}\\Collection\\")
        bpy.ops.wm.append(filename="Collection 1", directory=f"C:\\Users\\pc\\Desktop\\obj\\Hat\\{glass_fbx}\\Collection\\")
        bpy.ops.wm.append(filename="Collection 1", directory=f"C:\\Users\\pc\\Desktop\\obj\\Robe\\{bag_fbx}\\Collection\\")
        bpy.ops.wm.append(filename="Collection 1", directory=f"C:\\Users\\pc\\Desktop\\obj\\Staff\\{cap_fbx}\\Collection\\")
        bpy.ops.import_scene.fbx(filepath="C:\\Users\\pc\\Desktop\\obj\\Background\\"+wp_fbx)
        bpy.context.scene.render.filepath = "C:\\Users\\pc\\Desktop\\test1\\png\\"+ result_png
        bpy.ops.render.render(use_viewport = True, write_still=True)
        clear_bg()
        collections(bpy.context.collection, rez_list)
        for x in rez_list:
            if x =="Collection":
                print("passed")
            else:
                collection = bpy.data.collections[x]
                bpy.data.collections.remove(collection)
        clear()

if __name__ =="__main__":
  #createObj(count,data)
  createObj(1,data)

