from PIL import Image 
import qrcode

data = input("Enter the link: ")
filename = input("Save QR code as (Add .png): ")

img = qrcode.make(data)
img.save(filename)

print("Done!")
Image.open(filename).show()
