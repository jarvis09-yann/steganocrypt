from PIL import Image
from random import randint

img = Image.open("test_image.png")

# width, height = img.size

# img.putpixel((0, 0), (0, 0, 0))


def writePixel(pos: tuple, color: int, value: int):
    rgb = img.getpixel(pos)

    if rgb[color] % 2 != value:
        if rgb[color] == 255:
            updatedColor = rgb[color] - 1
        else:
            updatedColor = rgb[color] + 1
    else:
        updatedColor = rgb[color]

    if color == 0:
        img.putpixel(pos, (updatedColor, rgb[1], rgb[2]))
    elif color == 1:
        img.putpixel(pos, (rgb[0], updatedColor, rgb[2]))
    elif color == 2:
        img.putpixel(pos, (rgb[0], rgb[1], updatedColor))


def readPixel(pos: tuple, color: int):
    rgb = img.getpixel(pos)
    return (rgb[color] % 2)


def wordToBin(message: str):
    binaryMessage = ""
    for char in message:
        binaryMessage = binaryMessage + str(format(ord(char), "08b"))
    return binaryMessage


def binToDec(binary):
    decimal = 0
    cpt = 7
    for num in binary:
        if num == "1":
            decimal = decimal + 2**cpt
        cpt = cpt - 1
    return decimal


def binToWord(binary):
    word = ""
    for i in range(0, len(binary), 8):
        letter = binary[i:i+8]
        word = word + chr(binToDec(letter))
    return word


def generatePositions(num: int, img):
    randPositions = []
    while len(randPositions) < num:
        randPos = (randint(0, img.size[0]-1), randint(0, img.size[1]-1))
        if randPos not in randPositions:
            randPositions.append(randPos)
    return randPositions


def encrypt(message):
    binaryMessage = wordToBin(message)
    randPositions = generatePositions(len(binaryMessage), img)
    for i in range(len(binaryMessage)):
        writePixel(randPositions[i], 0, int(binaryMessage[i]))
    return randPositions


def decrypt(positions):
    translatedBin = ""
    for i in range(len(positions)):
        translatedBin = translatedBin + str(readPixel(positions[i], 0))

    return binToWord(translatedBin)


pos = encrypt(
    "Lorem Ipsum dolor sit amet `èèèèè```111240235@@àà1&&&&" + "a"*1000)
print(decrypt(pos))
# writePixel((105, 503), 0, 1)
# print(readPixel((105, 503), 0))

img.show()
