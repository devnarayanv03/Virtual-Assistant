from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from os import getcwd

# Setting up Chrome options for headless mode with experimental features enabled
chrome_options = Options()

# Enabling new headless mode for better feature support
chrome_options.add_argument("--headless=new")

# Pre-authorizing microphone permission by setting the default content setting
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # To simulate microphone access
chrome_options.add_argument("--enable-experimental-web-platform-features")  # Use experimental features

# Manually set the path to the ChromeDriver executable
chrome_driver_path = f"{getcwd()}\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

# Setting up the Chrome driver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Creating the URL for the website using the current working directory
website = "https://allorizenproject1.netlify.app/"

# Opening the website in the Chrome browser
driver.get(website)

Recog_File = f"{getcwd()}\\input.txt"

def listen():
    try:
        # Wait for the start button to become clickable
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")

        output_text = ""
        is_second_click = False

        while True:
            # Wait for the output element to appear
            output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text.strip()

            # Check if we need to stop listening based on the button's state
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True

            # If output text changes, save it to file
            if current_text != output_text:
                output_text = current_text
                with open(Recog_File, "w") as file:
                    file.write(output_text.lower())
                    print("User:", output_text)

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Ensure the browser is closed on exit
        driver.quit()

listen()
