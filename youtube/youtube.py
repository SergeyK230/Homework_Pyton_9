from pytube import YouTube

url = input('Введите адресс страницы -> ')

yt = YouTube(url)

ys =  yt.streams.filter(progressive=True).get_highest_resolution()

name = yt.title
name = name + '.mp4'
path_save = input('Введите путь сохранения файла -> ')
ys.download(output_path=path_save, filename=name)
print('Готово')
