import imageio.v3 as iio

filenames = [
    "/Users/shruti_jay/Desktop/Project1/hippocorn1.png",
    "/Users/shruti_jay/Desktop/Project1/hippocorn2.png",
    "/Users/shruti_jay/Desktop/Project1/hippocorn3.png",
    "/Users/shruti_jay/Desktop/Project1/hippocorn4.png"
]

images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("/Users/shruti_jay/Desktop/Project1/final.gif", images, duration=500, loop=0)
print("GIF created successfully!")  //test statement

