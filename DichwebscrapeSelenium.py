from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
'''
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options'''

HEAD_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36'

options = Options()
options.add_argument('--headless')
options.add_argument(f'--user-agent={HEAD_agent}')
options.add_argument('--disable-extensions')

driver = Firefox(options=Options())
solver = RecaptchaSolver(driver=driver)

username = "ostro_baba"
password = "Nfmx2XZ9yQE498u"
drek = 'United States'

try: 
    driver.get('http://dichvusocks.us/login')
    print(driver.title)
    
    #find element and parse the password to the input
    driver.find_element("id", "l_email").send_keys(username)
    time.sleep(4)
   
    #find element by and parse the password to the input
    driver.find_element("id", "l_password").send_keys(password)
    time.sleep(3)
    
    #solving the captcha
    recaptcha_iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    time.sleep(3)
    
    #this line clicks the continue button
    driver.find_element("id", "auth_button_continue").click()
    
    #wait for the page to load completely
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Username Is Invalid", "Password Is Invalid"
    #Print cookies after login
    biscuit = driver.get_cookies()
    print("->Your current session cookie is : ", biscuit)
    
    '''assert 'Just a moment...' == driver.title
    content = driver.page_source
    #print(content)'''

    #Close the css prompt 'Don't show again'
    driver.find_element(By.CSS_SELECTOR, "#notice > div > div.uk-modal-footer.uk-text-right > button").click()
    time.sleep(2)

    #Navigate to socklists page
    driver.find_element(By.CSS_SELECTOR, "#app > div.header.uk-position-z-index.uk-background-default.uk-sticky > div > nav > div.uk-navbar-center > ul > li:nth-child(3) > a").click()
    time.sleep(3)
    #Use the search function
    select = Select(driver.find_element(By.NAME, 'search_country'))
    time.sleep(2)
    select.select_by_value(f'{drek}')
    time.sleep(2)
    #submit selected to search
    driver.find_element(By.XPATH, '//*[@id="app"]/div[5]/div/div/div[1]/div[2]/form/div/div[7]/button').click()
    time.sleep(15)

finally:

    driver.close()
    #driver.quit() 