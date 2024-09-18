from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import os

def get_perf_log_on_load(url):
    ser = Service(r"C:\PATH Programs\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    op.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    op.headless = True
    driver = webdriver.Firefox(service=ser, options=op)

    driver.get(url)
    time.sleep(6)
    test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
    driver.quit()

    return test

url_string = "https://twitter.com/KingNidhogg/status/1784324241959116990"
thi = get_perf_log_on_load(url_string)
twvid = ""
vidname = input("Name video file: ")
count = 0

for item in thi:
    if "container=cmaf" in item['name'] and "m3u8" in item['name']:
        twvid = item['name']
        count += 1
        if count == 2:
            break
        
print(twvid)
ffmcmd = "ffmpeg -i " + twvid + " -c copy -bsf:a aac_adtstoasc " + vidname + ".mp4"
os.chdir("C:\\Users\\computer1\\Desktop\\this\\outputs\\")
os.system(ffmcmd)



