import time
import schedule
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# -----------------------------
# CONFIG — CUSTOMIZE THIS
# -----------------------------
YMCA_LOGIN_URL = "https://example.com/login"  # replace with real YMCA login page
YMCA_ACTIVITY_URL = "https://example.com/activity"  # replace with activity page
USERNAME = "your-email@example.com"
PASSWORD = "yourpassword"
ENROLL_BUTTON_XPATH = "//button[contains(text(), 'Enroll')]"
TIMEZONE = "America/New_York"  # adjust your timezone

# -----------------------------
# ENROLLMENT FUNCTION
# -----------------------------
def enroll():
    print(f"[{datetime.now()}] Starting YMCA enrollment...")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        # 1. Log into YMCA
        driver.get(YMCA_LOGIN_URL)
        time.sleep(2)

        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button").click()
        time.sleep(3)

        # 2. Open activity page
        driver.get(YMCA_ACTIVITY_URL)
        time.sleep(2)

        # 3. Click enroll
        enroll_btn = driver.find_element(By.XPATH, ENROLL_BUTTON_XPATH)
        enroll_btn.click()

        print(f"[{datetime.now()}] Enrollment attempted successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

# -----------------------------
# SCHEDULE: SUNDAY AT 8 PM
# -----------------------------
schedule.every().sunday.at("20:00").do(enroll)

print("YMCA auto-enroll worker started...")

while True:
    schedule.run_pending()
    time.sleep(1)
