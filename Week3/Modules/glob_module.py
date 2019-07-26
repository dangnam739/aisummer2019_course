import glob

#Lay taats car path cho cac file duoi la .jpg
list_of_path = glob.glob('images/*.jpg')
print(len(list_of_path))
