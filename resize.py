from PIL import Image

img = Image.open('train/'+letter+'/{0:03}.jpg'.format(i))
img = img.resize((200,150), Image.ANTIALIAS)
img.save('New/'+letter+'/{0:3}.jpg'.format(i-32))

