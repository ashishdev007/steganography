from PIL import Image, UnidentifiedImageError
from steganography import encode, enhanced_hide, hide, rgb2hex, str2bin

def imageCheck(fileName):
    img = Image.open(fileName)

    if img.mode in "RGBA":
        img = img.convert("RGBA")
        pixels = img.getdata()
        noOfUsablePixels = 0

        for pixel in pixels:
            hexcode = rgb2hex(0,0,pixel[2])
            if (hexcode[1] in ("0", "1") or hexcode[3] in ("0", "1") or hexcode[5] in ("0", "1")):
                noOfUsablePixels += 1
        
        return noOfUsablePixels
    
    raise TypeError("Unusable file format!")

def readFile(fileName):
    with open(fileName, "r") as file:
        all_data = file.read()
        binary_data = str2bin(all_data.encode())
        return len(binary_data), all_data

try:
    # print(imageCheck("img2.jpg") * 0.000000125)
    # print(readFile("ab.txt"))
    fileName = input("Enter name of the file: ")
    imageName = input("Enter name of the image: ")
    
    (fileLen, message) = readFile(fileName)
    enhanced_hide(imageName, message.encode())
    # if imageCheck(imageName) >= fileLen + 16:
    #     enhanced_hide(imageName, message.encode())
    # else:
    #     print("Image is not large enough to hide the file!")
except TypeError as identifier:
    print(identifier)
except FileNotFoundError as identifier:
    print(identifier)
except UnidentifiedImageError as identifier:
    print("Please enter an image file!") 
except:
    print("Something went wrong!")              

