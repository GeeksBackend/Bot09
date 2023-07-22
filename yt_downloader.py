from pytube import YouTube

url = input('URL: ')
yt = YouTube(url=url, use_oauth=False, allow_oauth_cache=True)
yt.streams.first().download()