from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(4)
address = "https://getfakedata.com/address/en_IN?limit=25"
driver.get(address)

finaldf = pd.DataFrame(columns=['address'])
row = 1
def gen():
      try:
            var = driver.find_element_by_xpath(
                  "/html/body/div/div[1]/div[2]/div/div[3]/textarea").text

            print(var)
            print(type(var))
            new_var = var.split("===")
            print(new_var)
            global row
            for i in new_var:
                  finaldf.set_value(row, 'address', i)
                  row = row + 1
                  finaldf.to_csv("D:/finaladdressoutcome.csv")

      except:
            pass


global new_var
while True:
      driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[5]/form/div[2]/div/button").click()
      gen()
