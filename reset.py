from pyautogui import typewrite, press
from time import sleep


def main():
    sleep(1)
    typewrite("apt update && apt install ntfs-3g chntpw -y")
    typewrite("ntfsfix /dev/sda1")
    press("enter")
    typewrite("mount /dev/sda1 /mnt")
    press("enter")
    typewrite("cd /mnt/Windows/System32/config")
    press("enter")
    typewrite("chntpw -i SAM")
    press("enter")
    typewrite("1")
    press("enter")
    typewrite("1f4")
    press("enter")
    typewrite("1")
    press("enter")
    typewrite("2")
    press("enter")
    typewrite("q")
    press("enter")
    typewrite("q")
    press("enter")
    typewrite("y")
    press("enter")
    typewrite("shutdown now")
    press("enter")


if __name__ == '__main__':
    main()
