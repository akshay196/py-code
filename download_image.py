#!/usr/bin/env python3

import sys
import requests
import imghdr

respond = ""

def check_image():
    """
    Verifiy requested url is an image and 
    call download_image() if verified
    """
    global respond
    
    if len(sys.argv) < 2:
        print("\nMention link")
        exit()
    
    respond = requests.get(sys.argv[1])

    image_format = imghdr.what('',respond.content)
        
    if (image_format):
        print("Image verified which is of the type %s" % image_format)
        download_image()
    else:
        print("404 not found")

def download_image():
    """
    Download image in current directory
    """
    global respond
    filename = sys.argv[1].split("/")[-1]
    img_file = open(filename, "wb")
    print("hang on..Downloading image")
    #print(respond.encoding)   
    #print(respond.text)
    #print(respond.content)
    img_file.write(respond.content)

    print("Download Complete.")
    img_file.close()

    
check_image()


