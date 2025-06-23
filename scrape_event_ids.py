import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
import time
import datetime

currentTime = time.time()
timestamp = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H:%M:%S')

# Replace with the actual path to your ChromeDriver executable
chromedriver_path = '/Users/leopoldpfeiffer/WebDriver/chromedriver'  # change path as needed

service = Service(executable_path=chromedriver_path)

options = Options()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://results.hyrox.com/season-8/")

driver.implicitly_wait(20)
driver.set_script_timeout(20)

driver.find_element(by=By.ID, value='restricted-consent-give').click()

event_ids = {}

events = driver.find_element(by=By.ID, value='default-lists-event_main_group')
all_event_options = Select(events).options
event_option_values = [opt.get_attribute("value") for opt in all_event_options]

for event_name in event_option_values:
    print(event_name)
    events_dropdown = driver.find_element(by=By.ID, value='default-lists-event_main_group')
    select = Select(events_dropdown)

    # 1a. Select it (click it) by exact value:
    select.select_by_value(event_name)

    default_submit_btn = driver.find_element(by=By.ID, value="default-submit")
    default_submit_btn.click()

    reload_button = driver.find_element(By.CSS_SELECTOR, "a[href^='?event=']")
    reload_button.click()

    try:
        event_id = driver.current_url.split("?event=")[1].split("&")[0].split("_")[1]
        event_ids[event_id] = event_name
        print(f"{event_id} – {event_name}")
    except Exception:
        logging.error(f"Could not get event ID for {event_name}")

    driver.back()
    driver.back()

driver.quit()
