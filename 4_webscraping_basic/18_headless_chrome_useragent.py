from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
# 따로 user-agent 를 설정을 안해줬을 때 (headlessChrome 접속 제한에 의해)날아 갈 수가 있기 때문에 headlessChrome 사용시 위와 같이 바꿔줄 필요가 있을 수 있음

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# 적용 전
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/97.0.4692.71 Safari/537.36
# 적용 후
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/97.0.4692.71 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# reference : Selenium with Python
# https://selenium-python.readthedocs.io/