from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('blink-settings=imagesEnabled=false')

bro = webdriver.Chrome(executable_path="../../chromedriver",options=options)

bro.get("https://www.douban.com")


