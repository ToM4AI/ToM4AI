from PIL import Image

# Open the JPEG image
img = Image.open("images/favicon.jpg")

# Resize to a standard icon size
img = img.resize((256, 256))

# Save as .ico
img.save("images/favicon.ico", format='ICO')
