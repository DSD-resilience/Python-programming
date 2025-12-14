import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Define Zillow Site and Google Form link
zillow_site = "https://appbrewery.github.io/Zillow-Clone/"
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfUdqMd-YHYWVf5r2iyiZ0bSt5cY3j-QxOyuxxlyA2jKt8VEQ/viewform?usp=header"

# Get data from Zillow site in HTML format
response = requests.get(url=zillow_site)

# Create an object from the BeautifulSoup class
soup = BeautifulSoup(response.text, "html.parser")

# Create a list of links for all listings
links = [] # an empty links list to store all links
links_tag = soup.select(selector="div .StyledPropertyCardPhotoBody a")
for link in links_tag:
    links.append(link["href"])

# Create a list of prices for all listings
prices_tag = soup.find_all(name="div", class_="PropertyCardWrapper")
prices = []
for price in prices_tag:
    price_text = price.getText()
    p_text = price_text.replace("+", "/")
    value = p_text.split("/")[0]
    prices.append(value)

# Create a list of addresses for all listings
addresses = []
addresses_tag = soup.select(selector="div address")

for address in addresses_tag:
    address_text = address.getText()
    add_text = address_text.replace("|", ",").strip().split(',')[1:]
    full_address = ",".join(add_text)
    addresses.append(full_address)

# Set up Selenium
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(edge_options)
driver.get(url=google_form_link)

# Fill in Google Form
for i in range(len(addresses)):
    address = driver.find_element(
    By.XPATH, '//[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[i])
    price = driver.find_element(
    By.XPATH, '//[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    link = driver.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])
    submit_btn = driver.find_element(By.CLASS_NAME, "RveJvd")
    submit_btn.click()
    sleep(1)