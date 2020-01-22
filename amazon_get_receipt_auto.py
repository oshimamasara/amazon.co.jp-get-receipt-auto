# 2019年の領収書打ち出し（ HTML ファイル）
# HTML →　PDF Converter   無料　　https://html2pdf.com/

import sys
from selenium import webdriver
import time

total = 0
index = 0
html_file_number = 1

browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get("https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
email_elem = browser.find_element_by_id("ap_email")
email_elem.send_keys("Amazon.co.jpログイン・メールアドレス")
email_elem.submit()

password_elem = browser.find_element_by_id("ap_password")
password_elem.send_keys("Amazon.co.jpログイン・パスワード")
password_elem.submit()

# 2019年度注文履歴のページ設定
elem = browser.find_element_by_id("nav-orders")
elem.click()

elem2 = browser.find_element_by_id("a-autoid-1")
elem2.click()

# 2019年の注文履歴最初のページ
elem3 = browser.find_element_by_id("orderFilter_3")
elem3.click()

# Single Page Scrape
def single_page_scrape():
    global html_file_number

    current_URL_address = browser.current_url
    # Get Receipt Page File（Single Page）
    js_xpath_number = 2 # text:領収書等  path number:2〜12まで
    try:
        while js_xpath_number < 12:
            js_link = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div[" + str(js_xpath_number) + "]/div[1]/div/div/div/div[2]/div[2]/ul/span[1]/span/a")[0]
            js_link.click()
            receipt_link = browser.find_element_by_link_text("領収書／購入明細書")
            receipt_link.click()
            time.sleep(3)

            receipt_page_html = browser.page_source
            i_format = "{0:03d}".format(html_file_number)
            receipt_link_file = open(i_format + ".html", "w")
            receipt_link_file.write(receipt_page_html)
            receipt_link_file.close()
            print(receipt_link_file)
            browser.get(current_URL_address)

            html_file_number += 1
            js_xpath_number += 1
            time.sleep(1)

        print("FIN")

        next_link = browser.find_element_by_partial_link_text("次へ")
        next_link.click()
    
    except:
        print("データ取得エラー")

# Single Page Scrape
def page_scrape():
    global html_file_number

    current_URL_address = browser.current_url
    # Get Receipt Page File（Single Page）
    js_xpath_number = 2 # text:領収書等  path number:2〜12まで
    try:
        while js_xpath_number < 12:
            js_link = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div[" + str(js_xpath_number) + "]/div[1]/div/div/div/div[2]/div[2]/ul/span[1]/span/a")[0]
            js_link.click()
            receipt_link = browser.find_element_by_link_text("領収書／購入明細書")
            receipt_link.click()
            time.sleep(3)

            receipt_page_html = browser.page_source
            i_format = "{0:03d}".format(html_file_number)
            receipt_link_file = open(i_format + ".html", "w")
            receipt_link_file.write(receipt_page_html)
            receipt_link_file.close()
            print(receipt_link_file)
            browser.get(current_URL_address)

            html_file_number += 1
            js_xpath_number += 1
            time.sleep(1)
    
    except:
        print("取得HTMLファイル数： " + str(html_file_number))

while True:
    next_page_link = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div[12]/div/ul/li[7]/a")
    if next_page_link:
        single_page_scrape()
    else:
        page_scrape()
        browser.close()
        break

print("FINISH")
