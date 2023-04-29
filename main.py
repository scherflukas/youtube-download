from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    videos = yt.streams
    video = list(enumerate(videos))
    for i in video:
        print(i)

    print("Enter the format you want to download: ")
    download_format = int(input("Enter the format number: "))
    videos[download_format].download()
    print("Succesfully downloaded")

if __name__ == "__main__":
    print("Enter the URL of the video: ")
    url = input()
    download_video(url)