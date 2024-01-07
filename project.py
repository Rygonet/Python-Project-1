import pandas
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook


service = Service()
option = webdriver.ChromeOptions()
option.add_argument("-headless")
driver = webdriver.Chrome(service=service, options=option)

print("Sveiki, kādu funkciju Jūs vēlaties tagad izmantot? Ievadiet burtu. \n a) Kaloriju kalkulators \n b) Jaunas receptes meklēšana \n c) Šodienas kaloriju piefksēšana")
main_izvēle=input()
if main_izvēle == ("a") or ("A"):
    #Cik šodien kaloriju jāapēd?

    print("Lūdzu ievadiet jūsu dzimumu (Male or Female)")
    dzimums=input()
    print("Lūdzu ievadiet jūsu vecumu")
    vecums=input()
    print("Lūdzu ievadiet jūsu augumu (cm)")
    augums=input()
    print("Lūdzu ievadiet jūsu tagadējo svaru (kg)")
    svars=input()

    if dzimums == ("Male") or ("male"):
        BMR = 66.47 + (13.75 * float(svars)) + (5.003 * float(augums)) - (6.755 * float(vecums))
    elif dzimums == ("Female") or ("female"):
        BMR = 655.1 + (9.563 * svars) + (1.850 * augums) - (4.676 * vecums)

    print("Cik reizes jūs sportojat nedēļā? Ievadiet burtu. \n a) Nesportoju \n b) 1-3 reizes \n c) 3-5 reizes \n d) 6-7 reizes \n e) Intensīvas 6-7 reizes")
    reizes=input()
    if reizes == ("a") or ("A"):
        AMR = BMR * 1.2
    elif reizes == ("b") or ("B"):
        AMR = BMR * 1.375
    elif reizes == ("c") or ("C"):
        AMR = BMR * 1.55
    elif reizes == ("d") or ("D"):
        AMR = BMR * 1.725
    elif reizes == ("e") or ("E"):
        AMR = BMR * 1.9
    print("Lai uzturētu savu tagadējo svaru jums ir jāapēd", AMR, "kalorijas.")

elif main_izvēle == ("b") or ("B"):
    #Ēdiena meklēšana

    url = "https://"
    driver.get(url)
    time.sleep(3)