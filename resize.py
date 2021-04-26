from PIL import Image

def sizing(letter,lower_limit,upper_limit):
    for i in range(lower_limit,upper_limit+1):
        img = Image.open('train/'+letter+'/{0:03}.jpg'.format(i))
        img = img.resize((200,150), Image.ANTIALIAS)
        img.save('New/'+letter+'/{0:3}.jpg'.format(i-32))
    print(letter + 'done..')


