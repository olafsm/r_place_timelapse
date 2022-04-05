from os import mkdir
from PIL import Image
import os.path, sys

path = os.path.join(os.getcwd(), "img/")
dirs = os.listdir(path)

def get_size_from_pixels(pixels,scale):
    w = pixels[2]-pixels[0]
    h = pixels[3]-pixels[1]
    return (w*scale,h*scale)

def crop_and_resize(folder, pixels):
    for item in dirs:
        fullpath = os.path.join(path,item)
        print(item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            imCrop = im.crop((pixels)).resize(get_size_from_pixels(pixels,3))
            imCrop.save(os.path.join(folder, item), "PNG", quality=100)


def resize():
    i = 0
    for item in os.listdir(crop_path):
        fullpath = os.path.join(crop_path,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            imCrop = im.resize((759, 642))
            imCrop.save(os.path.join(resize_path, item), "PNG", quality=100)
            print(i)
            i+=1

def rename(p):
    for item in os.listdir(p):
        fullpath = os.path.join(p,item)
        num = 11 - len(item)
        os.rename(fullpath, os.path.join(p, item[:3] + "0"*num + item[3:]))

def make_movie(input_path, output_path):
    import ffmpeg
    (
        ffmpeg
            .input('{}*.png'.format(input_path), pattern_type='glob', framerate=60,s='{}x{}'.format(759, 642))
            .output(output_path)
            .run()
    )
if __name__ == "__main__":
    # get args
    args = sys.argv[1:]
    if len(args) == 6:
        a,b,c,d,e,f = args
        pixels = (int(a),int(b),int(c),int(d))
        crop_path = os.path.join(os.getcwd(), e)
        output_path = os.path.join(os.getcwd(), f)
        # make directory if it doesn't exist
        if not os.path.exists(crop_path):
            mkdir(crop_path)
        #crop_and_resize(crop_path, pixels)
        make_movie(crop_path, output_path)
    else:
        print("Usage: crop_images.py <x1> <y1> <x2> <y2> <crop_path> <output_path>")
        print("Example: crop_images.py 0 0 759 642 img/ movie.mp4")