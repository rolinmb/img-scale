from PIL import Image

def scale_img(in_path, out_path, dims):
    with Image.open(in_path) as img:
        img_resized = img.resize(dims, Image.ANTIALIAS)
        img_resized.save(out_path, format='png')

if __name__ == '__main__':
    inpath = 'img-in/'
    outath = 'img-out/out.png'
    outdims = (400, 400)
    scale_img(inpath, outpath, outdims)
