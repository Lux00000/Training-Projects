from pytube import YouTube

url = input("Ссылка: \t ")  
video = YouTube(url)
        
audio = video.streams.filter(only_audio=True).first()      
audio.download()

print("Good !")
