#import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


#helper funtion
def get_text(source, selector, by=By.CSS_SELECTOR):
    product_info = source.find_elements(by, selector)
    return product_info[0].text if product_info else "N/A"
           

#setup automatic webdriver
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.delete_all_cookies()


#dictionary for product_link
product_links = {
    "Fruits":"https://chaldal.com/fresh-fruit",
    "Vegetables": "https://chaldal.com/fresh-vegetable",
    "Meat & Fish": ["https://chaldal.com/chicken-poultry", "https://chaldal.com/premium-perishables", "https://chaldal.com/frozen-fish", "https://chaldal.com/meat-new", "https://chaldal.com/tofu-meat-alternatives", "https://chaldal.com/dried-fish" ],
    "Dairy & Eggs": ["https://chaldal.com/ghee", "https://chaldal.com/powder-milk", "https://chaldal.com/liquid-uht-milk", "https://chaldal.com/yogurt", "https://chaldal.com/cheeses", "https://chaldal.com/condensed-milk-cream", "https://chaldal.com/butter-sour-cream", "https://chaldal.com/eggs"], 
    "Rice": "https://chaldal.com/rices",
    "Oil": "https://chaldal.com/oil",
    "Lentils & Pulses": "https://chaldal.com/dal-or-lentil",
    "Salt-sugar": "https://chaldal.com/salt-sugar",
    "Spices & Ingredients": ["https://chaldal.com/spices", "https://chaldal.com/miscellaneous", "https://chaldal.com/premium-ingredients", "https://chaldal.com/ready-mix"],
    "Sauces & pickles": ["https://chaldal.com/tomato-sauces", "https://chaldal.com/pickles", "https://chaldal.com/cooking-sauces", "https://chaldal.com/other-sauces"],
    "Breakfast": ["https://chaldal.com/breads", "https://chaldal.com/tea-coffee-2", "https://chaldal.com/local-breakfast", "https://chaldal.com/cereals", "https://chaldal.com/spreads-syrups", "https://chaldal.com/energy-boosters"],
    "Snacks" : ["https://chaldal.com/shemai-suji", "https://chaldal.com/noodles", "https://chaldal.com/cookies-2", "https://chaldal.com/local-snacks", "https://chaldal.com/chips-pretzels", "https://chaldal.com/plain-biscuits", "https://chaldal.com/toast-biscuits", "https://chaldal.com/cream-biscuits", "https://chaldal.com/pasta-macaroni", "https://chaldal.com/soups", "https://chaldal.com/popcorn-nuts", "https://chaldal.com/salted-biscuits", "https://chaldal.com/cakes", "https://chaldal.com/salad-dressing"], 
    "Candy & chocolate": ["https://chaldal.com/chocolates", "https://chaldal.com/wafers", "https://chaldal.com/candies", "https://chaldal.com/mints-mouth-fresheners", "https://chaldal.com/halal-marshmallows"],
    "Beverages": ["https://chaldal.com/beverages-tea", "https://chaldal.com/soft-drinks", "https://chaldal.com/coffees", "https://chaldal.com/powder-mixes", "https://chaldal.com/juice", "https://chaldal.com/water"],
    "Baking & Flour": ["https://chaldal.com/flour", "https://chaldal.com/nuts-dried-fruits", "https://chaldal.com/baking-ingredients", "https://chaldal.com/baking-tools", "https://chaldal.com/baking-mixes", "https://chaldal.com/colors-flavours"],
    "Frozen Snacks": ["https://chaldal.com/chicken-snacks", "https://chaldal.com/frozen-parathas-roti", "https://chaldal.com/vegetable-snacks", "https://chaldal.com/beef-snacks", "https://chaldal.com/fish-snacks"],
    "Canned food": ["https://chaldal.com/mushroom-cans", "https://chaldal.com/vegetable-cans", "https://chaldal.com/fish-cans", "https://chaldal.com/canned-fruits"],
    "Personal-care": ["https://chaldal.com/womens-soaps", "https://chaldal.com/hair-care", "https://chaldal.com/female-shampoo", "https://chaldal.com/feminine-care", "https://chaldal.com/female-moisturizer", "https://chaldal.com/face-wash-scrub", "https://chaldal.com/female-deo", "https://chaldal.com/womens-perfume", "https://chaldal.com/womens-shower-gel", "https://chaldal.com/masks-cleansers", "https://chaldal.com/serum-oil-toners", "https://chaldal.com/mens-soaps", "https://chaldal.com/mens-perfume", "https://chaldal.com/shampoo", "https://chaldal.com/shaving-needs", "https://chaldal.com/beard-grooming", "https://chaldal.com/deodorants", "https://chaldal.com/razors-blades", "https://chaldal.com/mens-hair-care", "https://chaldal.com/lotion-cream", "https://chaldal.com/mens-facewash", "https://chaldal.com/mens-shower-gels", "https://chaldal.com/liquid-handwash", "https://chaldal.com/hand-sanitizer", "https://chaldal.com/tissue-wipes", "https://chaldal.com/toothpastes", "https://chaldal.com/toothbrushes", "https://chaldal.com/mouthwash-others", "https://chaldal.com/soaps", "https://chaldal.com/lotions", "https://chaldal.com/petroleum-jelly", "https://chaldal.com/creams", "https://chaldal.com/face-wash-mask", "https://chaldal.com/body-hair-oil", "https://chaldal.com/lipsticks-lip-balm", "https://chaldal.com/talcom-powder", "https://chaldal.com/hair-color" ],
    "Baby care": ["https://chaldal.com/diapers", "https://chaldal.com/medium-2", "https://chaldal.com/large-2", "https://chaldal.com/extra-large-15-kg-diapers", "https://chaldal.com/small-2", "https://chaldal.com/newborn-2", "https://chaldal.com/milk-juice-drinks", "https://chaldal.com/toddler-food", "https://chaldal.com/formula", "https://chaldal.com/bath-skincare", "https://chaldal.com/wipes", "https://chaldal.com/baby-oral-care", "https://chaldal.com/newborn-essentials", "https://chaldal.com/baby-accessories", "https://chaldal.com/feeders"],
    "Cleaning-supplies": ["https://chaldal.com/dish-wash", "https://chaldal.com/laundry", "https://chaldal.com/toilet-cleaning", "https://chaldal.com/paper-products", "https://chaldal.com/pest-control", "https://chaldal.com/floor-glass-cleaners", "https://chaldal.com/cleaning-accessories", "https://chaldal.com/air-freshners", "https://chaldal.com/trash-bags", "https://chaldal.com/shoe-care", "https://chaldal.com/trash-bin-basket"],
    "Home & kitchen": ["https://chaldal.com/kitchen-accessories", "https://chaldal.com/kitchen-appliances", "https://chaldal.com/lights", "https://chaldal.com/mosquito-swatter", "https://chaldal.com/electric-multiplug", "https://chaldal.com/electronics", "https://chaldal.com/tools-hardware", "https://chaldal.com/baskets-buckets", "https://chaldal.com/box-container", "https://chaldal.com/gardening", "https://chaldal.com/rack-organizer", "https://chaldal.com/disposables"],
    "Stationeries": ["https://chaldal.com/batteries", "https://chaldal.com/calculators", "https://chaldal.com/glue-tapes", "https://chaldal.com/stapler-punch", "https://chaldal.com/organizing-accessories", "https://chaldal.com/cutting-2", "https://chaldal.com/file-folder", "https://chaldal.com/measuring", "https://chaldal.com/desk-organizers", "https://chaldal.com/pens", "https://chaldal.com/highlighters", "https://chaldal.com/printer-ink", "https://chaldal.com/pencils", "https://chaldal.com/erasers-correction-fluid", "https://chaldal.com/printing-paper", "https://chaldal.com/notebook-diary", "https://chaldal.com/school-supplies", "https://chaldal.com/color-pencil"]
}


all_products = []

for category, value in product_links.items():
    links = value if isinstance(value, list) else[value]

    for link in links:
        try:
           driver.delete_all_cookies()
           driver.get(link)
           print(f"scraping : {category}........")
           time.sleep(3)
           
           #Scroll to bottom for loading all products
           for _ in range(15):
               driver.execute_script("window.scrollBy(0, 1000)")
               time.sleep(2)
 
           #wait for all product-box load
           products = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"productV2Catalog")))

           #find product details     
           for product in products:
               title = get_text(product, "pvName", By.CLASS_NAME)
               currency = get_text(product, "currency", By.CLASS_NAME)

               #To handle price
               previous_price = get_text(product, ".price span", By.CSS_SELECTOR) 
               current_price = get_text(product, ".productV2discountedPrice span", By.CSS_SELECTOR) 
               
               final_current_price = previous_price if current_price == "N/A" else current_price

               unit = get_text(product, ".subText span", By.CSS_SELECTOR)

              #append
               all_products.append({"Category": category, "Title": title, "Currency": currency, "Previous_price": previous_price, "Current_price": final_current_price, "Unit":unit})

        except Exception as e:
             print(f"error in {category} : {e}")

             if "invalid session id" in str(e).lower():
                driver = webdriver.Chrome(options=chrome_options)
                continue

print(f"Total scraped products {len(all_products)} from total {len(product_links)} categories.")

driver.quit()

if all_products:
    df = pd.DataFrame(all_products)
    
    df.to_csv("chaldal_data.csv", index=False, encoding="utf-8-sig")
    print("Success: Data saved to chaldal_data.csv")