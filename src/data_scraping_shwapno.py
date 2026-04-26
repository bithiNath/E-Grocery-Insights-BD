#import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#setup automatic chrome driver
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.delete_all_cookies()


product_links = {
    "Fruits":"https://www.shwapno.com/fresh-fruits",
    "Vegetables": ["https://www.shwapno.com/fresh-vegetables", "https://www.shwapno.com/dry-vegetables"],
    "Meat & Fish": ["https://www.shwapno.com/meat", "https://www.shwapno.com/fish"],
    "Dairy & Eggs": ["https://www.shwapno.com/dairy", "https://www.shwapno.com/eggs"],
    "Rice": "https://www.shwapno.com/rice",
    "Oil": "https://www.shwapno.com/oil",
    "Lentils & Pulses": "https://www.shwapno.com/daal-or-lentil",
    "Salt & Sugar" : "https://www.shwapno.com/salt-and-sugar",
    "Spices & Ingredients" : ["https://www.shwapno.com/spices", "https://www.shwapno.com/ready-mix"],
    "Sauces & pickles": "https://www.shwapno.com/sauces-and-pickles",
    "Breakfast" : "https://www.shwapno.com/breakfast",
    "Snacks": "https://www.shwapno.com/snacks",
    "Candy, chocolate & Ice-cream": ["https://www.shwapno.com/candy-chocolate", "https://www.shwapno.com/ice-cream"],
    "Beverages": "https://www.shwapno.com/beverages",
    "Baking & Flour" : "https://www.shwapno.com/baking-needs",
    "Frozen Snacks": "https://www.shwapno.com/Frozen",
    "Canned food": "https://www.shwapno.com/canned-food",
    "Personal care": ["https://www.shwapno.com/personal-care", "https://www.shwapno.com/health-care"],
    "Baby Care": ["https://www.shwapno.com/baby-food-and-care", "https://www.shwapno.com/Diaper"],  
    "Cleaning-supplies": "https://www.shwapno.com/home-cleaning",
    "Home & kitchen": "https://www.shwapno.com/home-and-kitchen",
    "Stationeries": "https://www.shwapno.com/office-products",
}


#list to store all products
all_products = []

#loop through each category & scrape products
for category, value in product_links.items():
   links = value if isinstance(value, list) else[value]

   for link in links:
     try:  
      driver.get(link)
      time.sleep(5)
      driver.refresh() 

      print(f"Scraping : {category}.....")
      
      time.sleep(5)

      #scroll to bottom to load all products
      for _ in range(10):
          driver.execute_script("window.scrollBy(0, 1000);")
          time.sleep(2)

      #wait for product boxes to load
      products = WebDriverWait(driver, 45).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box")))
    
      #loop through all products on the page
      for product in products:
          try:  
             title = product.find_element(By.CLASS_NAME, "product-box-title").text

             #to handle price & unit
             try:
                 price_container = product.find_element(By.CLASS_NAME, "product-price")
                 spans = price_container.find_elements(By.TAG_NAME, "span")

                 if len(spans) >=3:
                       previous_price, current_price,  unit = spans[0].text, spans[1].text, spans[2].text 
                       
                 elif len(spans) == 2:
                       previous_price, current_price, unit = spans[0].text, spans[0].text, spans[1].text 
                 else: 
                       previous_price, current_price, unit = "N/A", "N/A", "N/A" 
             except:
                    previous_price, current_price, unit = "N/A",  "N/A", "N/A"

           #to handle stock
             try:
                 stock = product.find_element(By.CLASS_NAME, "add-to-cart-button").text
             except:
                 stock = "out of stock"
            
           #Append
             all_products.append({"Category": category, "Title": title, "Previous_price": previous_price, "Current_price": current_price, "Unit":unit, "Stock":stock})

          except:
             continue 
      
     except Exception as e: 
           print(f"Error in {category}: {e}")   

           if "invalid session id" in str(e).lower():
                driver = webdriver.Chrome(options=chrome_options)
                continue

print(f"Total products scraped: {len(all_products)}")

driver.quit()

if all_products:
     df = pd.DataFrame(all_products)
     df.to_csv("Shwapno_data.csv", index=False, encoding="utf-8-sig")
     print(f"Total {len(all_products)} products from {len(product_links)} categories have been saved to 'Shwapno_data.csv'")