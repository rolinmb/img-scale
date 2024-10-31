from PIL import Image

def scale_img(in_path, out_path, dims):
    with Image.open(in_path) as img:
        img_resized = img.resize(dims)
        img_resized.save(out_path, format='png')

if __name__ == '__main__':
    inpath = 'img-in/trial6_09262023_8.png'
    outpath = 'img-out/out.png'
    outdims = (400, 400)
    scale_img(inpath, outpath, outdims)
