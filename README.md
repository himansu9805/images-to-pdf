# Images to PDF

![Python 3](https://camo.githubusercontent.com/f3d11c8a75d0ff96997b10420df4fc52aafe96b4ee6c078f8fb10fcff5c497d5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332d677265656e2e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e)

This is a simple python program which converts a bunch of images into a single PDF file. You just need to specify the path to the directory of images, everything else would be handled by the program.

### How to use

Just clone the repo and go into the folder "images-to-pdf".

```
python3 main.py -p "<path to your directory>"
```
Demo command :
```
python3 main.py -p "/home/user/My stuff/Photos/"
```




### Requirements

```
Pillow==8.2.0
```