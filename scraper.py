from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
import csv

# Absolute path to the chrome driver:
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
# navigate to the url
driver.get('https://aksaarland.de/stellenboerse/')
print(driver.title)

# Create a list with the search words
search_words = ['revit', 'autocad', 'LP 1-5', 'LP 1', 'LP 2', 'LP 3', 'LP 4', 'LPH 1', 'LPH 2', 'LPH 3', 'LPH 4', 'BIM',
                'Entwurf', 'pläne', 'plan', 'design']

# Accept the cookie
try:
    # wait 10 seconds before looking for element
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="cc-compliance"]/a'))
    )
    cookie.click()
except:
    pass

# # Find the search input
search = driver.find_element(By.NAME, 'search_block_form')

# Create csv file with option write and append
csv_file = open('aksaarland2.csv', 'a', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'content'])

# Declaring variables
primary_word = ''
counter = 2
page = 1

for word in search_words:
    try:
        index = search_words.index(word)

        # Create csv file with option write and append
        csv_file = open('aksaarland2.csv', 'a', encoding="utf-8")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['title', 'content'])

        # If primary_word == 0 -> Results are none or single page
        if primary_word == '':
            search = driver.find_element(By.NAME, 'search_block_form')

            # Put the search word in the input
            search.send_keys(word)
            search.send_keys(Keys.RETURN)

        # Implicitly wait 3 seconds
        driver.implicitly_wait(3)
        main = driver.find_element(By.ID, 'block-system-main')

        # Implicitly wait 3 seconds
        driver.implicitly_wait(3)
        search = driver.find_element(By.NAME, 'keys')
        offers = driver.find_elements(By.TAG_NAME, 'h3')

        for i in range(len(offers)):

            link = offers[i].find_element(By.TAG_NAME, 'a')
            link.click()

            driver.implicitly_wait(5)
            content = driver.find_element(By.CLASS_NAME, 'field-items')
            content_append = content.text
            print(content_append)

            driver.implicitly_wait(5)
            title = driver.find_element(By.TAG_NAME, 'h1')
            title_append = title.text
            # print(title_append)

            # One page back-forward
            driver.back()
            offers = driver.find_elements(By.TAG_NAME, 'h3')

            driver.implicitly_wait(10)
            i += 1
            csv_writer.writerow([title_append, content_append])

            # Check if this is the last offer on the current page
            if i == len(offers):
                # If this is the last page try if there are more page for the current search word
                try:
                    driver.find_element(By.XPATH, f"//a[text()='{counter}']").click()
                    # Loop over all the pages for the current search word
                    driver.get(f'https://aksaarland.de/search/node/{word}?page={page}')
                    primary_word = word

                    search_words.insert(index + 1, primary_word)
                    print(search_words)
                    counter += 1
                    page += 1
                    search = driver.find_element(By.NAME, 'keys')
                    search.clear()


                # If this is definitely the last page go back to the original URl and move on the next word

                except:
                    primary_word = ''
                    # search_words = list(set(search_words))
                    driver.get('https://aksaarland.de/stellenboerse/')

                    break
        search = driver.find_element(By.NAME, 'keys')
        driver.implicitly_wait(5)
        search.clear()
    except:
        pass

csv_file.close()
driver.quit()