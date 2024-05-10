import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SINCH_SERVICE_PLAN_ID = "SINCH_SERVICE_PLAN_ID"
SINCH_API_TOKEN = "SINCH_API_TOKEN"
SINCH_FROM = "+34666666666"
SMS_RECIPIENT = "+34666666666"

ITV_STATIONS = ["Massalfassar", "Llíria", "València (Campanar)", "València (Vara de Quart)"]
MONTH = "Junio"
PLATE_NUMBER = "0000XXX"
LOCATION = "València"

def send_sms(message):
    print(message)
    url = f"https://sms.api.sinch.com/xms/v1/{SINCH_SERVICE_PLAN_ID}/batches"

    data = {
        "from": SINCH_FROM,
        "to": [SMS_RECIPIENT],
        "body": message
    }
    
    headers = {
        "Authorization": f"Bearer {SINCH_API_TOKEN}",
        "Content-Type": "application/json"
    }

    try: 
        requests.request("POST", url, headers = headers, json = data)
        
        print("SMS Successfully Sent") 
    except Exception as e: 
        print(f"Oops! Something wrong: {e}")

while True:        
    # Start a new instance of Chrome WebDriver and navigate website
    driver = webdriver.Chrome()
    driver.get('https://www.sitval.com/#/cita_previa')

    try:
        print("Clicking the 'Aceptar' button")
        accept_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Aceptar')]"))
        )
        accept_button.click()
    except:
        pass


    print(f"Clicking the '{LOCATION}' button")
    location_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{LOCATION}')]"))
    )
    location_button.click()

    for itv_station in ITV_STATIONS:
        try:
            print(f"Checking availability in {itv_station}....")
            
            print(f"Clicking the 'Location' button")
            location_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-location2"))
            )
            location_element.click()

            print(f"Clicking the '{itv_station}' button")
            station_button = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(),'{itv_station}')]"))
            )
            station_button.click()

            print(f"Typing '{PLATE_NUMBER}' into the text input field")
            input_field = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
            )
            input_field.send_keys(PLATE_NUMBER)

            print("Clicking 'Turismo'")
            span_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "itv-i-turismo"))
            )
            span_element.click()

            print("Clicking 'Revisi´´ón periódica'")
            type_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "itv-i-periodica"))
            )
            type_element.click()    

            # Wait calendar to be loaded
            time.sleep(1)
            
            print(f"Clicking '{MONTH}'")
            month_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(.,'{MONTH}')]"))
            )
            month_element.click()    
            
            print("Checking 'Availability'")
            available_day = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "disponible"))
            )
        
            if not available_day:
                continue
            
            send_sms(f"ITV disponible el {available_day.text} de {MONTH} en {itv_station}")
            input("Press Enter to continue...")
            exit()
        except:
            print("Trying again...")
            continue

    driver.quit()
