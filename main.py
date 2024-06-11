import pyautogui
import time
import requests
import zipfile
import os

def get_names_from_online_source():
    url = "https://www.ssa.gov/oact/babynames/names.zip"
    response = requests.get(url)
    with open("names.zip", "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile("names.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    names = set()
    for filename in os.listdir("."):
        if filename.startswith("yob"):
            with open(filename, "r") as file:
                for line in file:
                    name = line.split(",")[0]
                    names.add(name)
    return list(names)


names = get_names_from_online_source()

time.sleep(10)

for name in names:
    pyautogui.typewrite("your name is {}".format(name))
    pyautogui.press('enter')
    time.sleep(0.05)
