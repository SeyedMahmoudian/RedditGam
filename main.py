import subprocess
import telegramBot
import os
import time

directory = "C:\\Users\\Amin\\Documents\\MEGA\\pythons\\redditGam\\NatureIsFuckingLit\\"


def main():
    while 1:
        delete()
        processor()
        run()
        time.sleep(20)


def run():
    src = ""
    os.chdir(directory)
    for fileName in os.listdir(directory):
        src = fileName
        dst = "_pic.jpg"
        os.rename(src, dst)

    telegramBot.telegramBot(src)


def delete():
    items = os.listdir(directory)
    for pic in items:
        if pic.endswith(".jpeg"):
            os.remove(os.path.join(directory, pic))
        if pic.endswith(".jpg"):
            os.remove(os.path.join(directory, pic))
        if pic.endswith(".png"):
            os.remove(os.path.join(directory, pic))


def processor():
    subprocess.run(["python", "grab_pictures.py", "-sNatureIsFuckingLit", "-n1", "-tday"])


if __name__ == '__main__':
    main()
