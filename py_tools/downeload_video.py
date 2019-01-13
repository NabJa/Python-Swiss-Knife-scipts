from pytube import YouTube
import os
import sys
import getopt


def downloadYouTube(url, out):
    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(out):
        os.makedirs(out)
    yt.download(out)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "i:o:")

        videourl = ""
        path = ""

        for opt, arg in opts:
            if opt == "-i":
                videourl = arg

            elif opt == "-o":
                path = arg

        if videourl != "" and path != "":
            downloadYouTube(videourl, path)
        else:
            print("No URL or path given!")
            print("download_video.py -i <URL> -o <output-directory>")

    except getopt.GetoptError:
        print("download_video.py -i <URL> -o <output-directory>")


if __name__ == "__main__":
    main(sys.argv[1:])
