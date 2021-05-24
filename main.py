try:
    import os
    from PIL import Image,UnidentifiedImageError
    import argparse
    import pathlib
except ImportError:
    print("Fulfil all requiremnets from requirements.txt")


def imgToPDF(PATH):
    extensions = [".jpg", ".jpeg",".png",".bmp"]
    try:
        entries = os.listdir(PATH)
        imgList = []
        for entry in entries[1:]:     # skipping first entry  
            if pathlib.Path(entry).suffix in extensions:
                img = Image.open(PATH + entry)
                imgList.append(img.convert('RGB'))

        pdf = Image.open(PATH + entries[0]).convert('RGB')
        pdf.save(PATH + "output.pdf", save_all=True, append_images=imgList)
        print("Your pdf successfully saved as "+PATH + "output.pdf")

    except FileNotFoundError:
        print("Your directory is not found")
    except UnidentifiedImageError:
        print("Your directory contains non-images files.")


def main():
    img_to_pdf_parser = argparse.ArgumentParser()
    img_to_pdf_parser.add_argument('--path', '-p', required=True, action='store',
                                   type=str, help='Specify the directory where images are present')
    args = img_to_pdf_parser.parse_args()
    if args.path != None:
        imgToPDF(args.path)
        


if __name__ == '__main__':
    main()
