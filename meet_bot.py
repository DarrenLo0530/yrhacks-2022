from selenium.webdriver.chrome.options import Options
import time
from undetected_chrome_prefs.ChromeWithPrefs import ChromeWithPrefs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import cv2
import eel


def request_join(driver):
  # Ask to join meet
  time.sleep(5)
  driver.implicitly_wait(2000)
  
  driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]').click()
  driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]').click()
  
  # input bot's name
  driver.find_element_by_id('jd.anon_name').send_keys('1984_bot')
  # click on request join button
  driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

def analyze_attention(driver):
  screenshot = driver.get_screenshot_as_png()
  nparr = np.frombuffer(screenshot, np.uint8)

@eel.expose
def monitor_meet(meet_code):
  # initial selenium options
  
  opts = Options()
  opts.add_argument("--disable-infobars")
  opts.add_argument("--disable-extensions")
  opts.add_argument("start-maximized")
  opts.add_argument("--use-fake-ui-for-media-stream")
  opts.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2,
  })

  driver = ChromeWithPrefs(options = opts)
  driver.get("https://meet.google.com/" + meet_code)

  # Request to join the meet
  request_join(driver)

  # Wait to be let in
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'tt-c6'))
  )

  