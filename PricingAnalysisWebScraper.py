import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service


def findValues(numValues):
    chrome_options = webdriver.ChromeOptions()
    data = []
    service = Service('/Users/paigecaskey/Desktop/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('####LINKHERE#####')
    try:
        accept_cookies_button = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/button[2]')
        accept_cookies_button.click()
    except NoSuchElementException:
        pass
    window_height = driver.execute_script("return window.innerHeight;")
    current_scroll_position = 0

    visited_links = set()
    visited_indices = set()

    for _ in range(int(numValues)):
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        time.sleep(1)
        print(3)
        elements = driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div/ul/li/div/div/a')
        print(4)
        for idx, element in enumerate(elements):
            if idx in visited_indices:
                print(12334)
                continue
            try:
                href_value = element.get_attribute('href')
                if href_value not in visited_links:                    
                    visited_links.add(href_value)
                    time.sleep(2)
                    print(1)
                    element.click()
                    print(2)
                    time.sleep(2)
                    internal_time_element = driver.find_element(By.CLASS_NAME, 'styles__Time-sc-630c0aef-0')
                    datetime_value = internal_time_element.get_attribute('datetime')
                    price = driver.execute_script(''' 
                            var priceElement = document.querySelector("#main > div.styles__Layout-sc-aee86350-2.jsjuOR > div.MobileProductActions-styles__Wrapper-sc-b13b29dd-0.bgACJI > div.MobileProductActions-styles__PriceWrapper-sc-b13b29dd-1.bVRcRw > div > p");
                            return priceElement ? priceElement.innerText : 'NULL';
                            ''')
                    description = driver.execute_script('''                            
                             var descriptionElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__Container-sc-141e0806-0.jdBUzQ.styles__StyledDescription-sc-170b29e9-17.kowUgV");
                             return descriptionElement ? descriptionElement.innerText : 'NULL';
                             ''')
                    brand = driver.execute_script('''
                             var brandElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.ProductDetailsSticky-styles__Wrapper-sc-72aea6c3-0.lmrJfz.styles__StyledProductDetailsSticky-sc-170b29e9-14.cfvkxK > div.ProductDetailsSticky-styles__DesktopKeyProductInfo-sc-72aea6c3-9.fXjXhB > div.ProductAttributes-styles__Attributes-sc-303d66c3-1.dIfGXO.ProductDetailsSticky-styles__StyledProductAttributes-sc-72aea6c3-10.kJTavv > a");
                             return brandElement ? brandElement.innerText : 'NULL';
                             ''')
                    condition = driver.execute_script('''
                             var conditionElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.ProductDetailsSticky-styles__Wrapper-sc-72aea6c3-0.lmrJfz.styles__StyledProductDetailsSticky-sc-170b29e9-14.cfvkxK > div.ProductDetailsSticky-styles__DesktopKeyProductInfo-sc-72aea6c3-9.fXjXhB > div.ProductAttributes-styles__Attributes-sc-303d66c3-1.dIfGXO.ProductDetailsSticky-styles__StyledProductAttributes-sc-72aea6c3-10.kJTavv > p:nth-child(2)");
                             return conditionElement ? conditionElement.innerText : 'NULL';
                             ''')
                    title = driver.execute_script('''
                             var titleElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.ProductDetailsSticky-styles__Wrapper-sc-72aea6c3-0.lmrJfz.styles__StyledProductDetailsSticky-sc-170b29e9-14.cfvkxK > div.ProductDetailsSticky-styles__DesktopKeyProductInfo-sc-72aea6c3-9.fXjXhB > h1");
                             return titleElement ? titleElement.innerText : 'NULL';
                             ''')
                    size = driver.execute_script('''
                             var sizeElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.ProductDetailsSticky-styles__Wrapper-sc-72aea6c3-0.lmrJfz.styles__StyledProductDetailsSticky-sc-170b29e9-14.cfvkxK > div.ProductDetailsSticky-styles__DesktopKeyProductInfo-sc-72aea6c3-9.fXjXhB > div.ProductAttributes-styles__Attributes-sc-303d66c3-1.dIfGXO.ProductDetailsSticky-styles__StyledProductAttributes-sc-72aea6c3-10.kJTavv > p:nth-child(1)");
                             return sizeElement ? sizeElement.innerText : 'NULL';
                             ''')
                    sold = driver.execute_script('''
                             var soldElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__SellerCTAsWrapper-sc-170b29e9-7.deIBUe > div.styles__BioContainer-sc-46110958-1.gjaYoc > div > div > div > div:nth-child(1) > p");
                             return soldElement ? soldElement.innerText : 'NULL';
                             ''')
                    activity = driver.execute_script('''
                             var activityElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__SellerCTAsWrapper-sc-170b29e9-7.deIBUe > div.styles__BioContainer-sc-46110958-1.gjaYoc > div > div > div > div:nth-child(3) > p");
                             return activityElement ? activityElement.innerText : 'NULL';
                             ''')
                    recent_review = driver.execute_script('''
                             var review1Element = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__StyledRecentFeedback-sc-170b29e9-29.gdPNrh > ul > li:nth-child(1) > div.styles__ReviewRow-sc-b18270c8-3.dJdev > p");
                             return review1Element ? review1Element.innerText : 'NULL';
                             ''')
                    time_listed = driver.execute_script('''
                             var time1Element = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > time");
                             return time1Element ? time1Element.innerText : 'NULL';
                             ''')
                    button = driver.execute_script('''
                             var buttonElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__SellerCTAsWrapper-sc-170b29e9-7.deIBUe > div.styles__BioContainer-sc-46110958-1.gjaYoc > div > div > button");
                             return buttonElement ? buttonElement.getAttribute('aria-label') : 'NULL';
                             ''')
                    discount = driver.execute_script('''
                             var discountElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__MobileKeyProductInfo-sc-170b29e9-26.fUbTNl > div.styles__StyledProductPrice-sc-170b29e9-31.cAgmSP > div.ProductPrice-styles__DiscountLabelWrapper-sc-e1912c99-2.fGMgtr > div > span");
                             return discountElement ? discountElement.innerText : 'NULL';
                             ''')
                    in_bags = driver.execute_script('''
                             var inBagsElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__MobileNudgesDiscountWrapper-sc-170b29e9-13.cHlRsU > div > div > p");
                             return inBagsElement ? inBagsElement.innerText : 'NULL';
                             ''')
                    like = driver.execute_script('''
                             var likeElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__Desktop-sc-93cf0ef1-1.gDHfTG > div.styles__Container-sc-28c290b3-0.fNhXCI > div:nth-child(1) > p");
                             return likeElement ? likeElement.innerText : 'NULL';
                             ''')
                    free_shipping = driver.execute_script('''
                             var freeShippingElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.ProductDetailsSticky-styles__Wrapper-sc-72aea6c3-0.lmrJfz.styles__StyledProductDetailsSticky-sc-170b29e9-14.cfvkxK > div.ProductDetailsSticky-styles__ShippingWrapper-sc-72aea6c3-2.fdaOjo > span");
                             return freeShippingElement ? freeShippingElement.innerText : 'NULL';
                             ''')
                    color = driver.execute_script('''
                             var colorElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__Container-sc-70b9bd79-4.bGeMEw.styles__StyledSecondaryProductDetails-sc-170b29e9-16.jka-dqe > div:nth-child(1) > div > div > span");
                             return colorElement ? colorElement.innerText : 'NULL';
                             ''')
                    material = driver.execute_script('''
                         var materialElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__Container-sc-70b9bd79-4.bGeMEw.styles__StyledSecondaryProductDetails-sc-170b29e9-16.jka-dqe > div:nth-child(2) > span");
                         return materialElement ? materialElement.innerText : 'NULL';
                         ''')
                    style = driver.execute_script('''
                         var styleElement = document.querySelector("#main > div.styles__Layout-sc-170b29e9-2.jTEyFL > div.styles__ContentWrapper-sc-170b29e9-3.kuRFFw > div.styles__Container-sc-70b9bd79-4.bGeMEw.styles__StyledSecondaryProductDetails-sc-170b29e9-16.jka-dqe > div:nth-child(3) > span");
                         return styleElement ? styleElement.innerText : 'NULL';
                         ''')
                    driver.back()
                    visited_indices.add(idx)                     
                    data.append({'Datetime': datetime_value, 'Link': href_value, 'Price': price, 'Description': description, 'Brand': brand, 'Condition': condition, 'Title': title, 'Size': size, 'Amt Sold': sold, 'Activity': activity, 'Recent Review1': recent_review, 'Time Listed': time_listed, 'Sold and Reviews': button, 'Discount': discount, 'In Bags': in_bags, 'Like': like, 'Free Shipping': free_shipping, 'Color': color, 'Material': material, 'Style': style})
                    data.append({'Datetime': datetime_value, 'Link': href_value, 'Price': price, })
                    current_scroll_position += window_height
            except NoSuchElementException:
                    print("Skipping element.")
            except StaleElementReferenceException:
                print("Stale element. Refreshing.")
                break

        if len(data) >= int(numValues):
            break

    return data

def outputToFile(data):
    data = pd.DataFrame(data)
    data.to_json("data.json", orient='records', lines=True)
    print(f'Data has been saved')

def main():
    num_values = input("Enter number of items to grab: ")
    data = findValues(num_values)
    outputToFile(data)

main()

