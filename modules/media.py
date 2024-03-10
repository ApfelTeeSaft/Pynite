from flask import Flask, send_file
from flask_cors import CORS
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))

def resize_image_small(image_path, output_size=(256, 256)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def resize_image_900x900(image_path, output_size=(900, 900)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def resize_image_2048x1024(image_path, output_size=(2048, 1024)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def resize_image_1024x512(image_path, output_size=(1024, 512)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def resize_image_1920x1080(image_path, output_size=(1920, 1080)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def resize_image_1200x680(image_path, output_size=(1200, 680)):
    with Image.open(image_path) as img:
        resized_img = img.resize(output_size)
    return resized_img

def lunarlogosmall256x256():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/lunar_centered.png")

    resized_image = resize_image_small(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/lunar_resized_256.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)

def apfellogo256x256():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/apfel_logo.png")

    resized_image = resize_image_small(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/apfel_resized.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)

def apfellogo900x900():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/apfel_logo.png")

    resized_image = resize_image_900x900(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/apfel_resized.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)

def seasonxbg():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/lunar_big.png")

    resized_image = resize_image_2048x1024(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/lunar_big_resized.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)

def blackhole_small():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/blackhole.png")

    resized_image = resize_image_1024x512(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/blackhole_resized.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)

def blackhole():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    image_path = os.path.join(parent_dir, "public/images/blackhole.png")

    resized_image = resize_image_1920x1080(image_path)
    resized_image_path = os.path.join(parent_dir, "public/images/blackhole_resized.png")
    resized_image.save(resized_image_path)

    content_type = "image/png"
    return send_file(resized_image_path, mimetype=content_type)