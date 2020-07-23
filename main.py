import urllib.request

#Stáhnutí obrázku
def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

file_name = 0
#Loop pro stahování a pojmenování obrázku
while 2 < 3:
    url = input('URL:')
    file_name = int(file_name)
    file_name += 1
    file_name = str(file_name)

    dl_jpg(url, 'images/', file_name)