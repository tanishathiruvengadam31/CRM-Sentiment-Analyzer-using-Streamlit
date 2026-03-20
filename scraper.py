from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def extract_text_from_url(url):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get(url)
        time.sleep(5)

        text_data = []

        # -------------------------
        # AMAZON REVIEWS
        # -------------------------
        try:
            amazon_reviews = driver.find_elements(By.XPATH, "//span[@data-hook='review-body']")
            for r in amazon_reviews:
                txt = r.text.strip()
                if 6 < len(txt.split()) < 80:
                    text_data.append(txt)
        except:
            pass

        # -------------------------
        # FLIPKART REVIEWS
        # -------------------------
        try:
            flipkart_reviews = driver.find_elements(By.XPATH, "//div[contains(@class,'_27M-vq')]")
            for r in flipkart_reviews:
                txt = r.text.strip()
                if 6 < len(txt.split()) < 80:
                    text_data.append(txt)
        except:
            pass

        # -------------------------
        # FALLBACK → PARAGRAPHS
        # -------------------------
        if len(text_data) < 5:
            try:
                paragraphs = driver.find_elements(By.TAG_NAME, "p")
                for p in paragraphs:
                    txt = p.text.strip()
                    if 8 < len(txt.split()) < 80:
                        text_data.append(txt)
            except:
                pass

        driver.quit()

        combined = " ".join(text_data)

        return combined[:5000]

    except Exception as e:
        driver.quit()
        print("Error:", e)
        return ""