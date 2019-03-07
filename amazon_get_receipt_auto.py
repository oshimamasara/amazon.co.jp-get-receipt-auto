# 2018年の領収書打ち出し（ HTML ファイル）
# HTML →　PDF Converter   無料　　https://html2pdf.com/

from selenium import webdriver
import time

total = 0
index = 0
html_file_number = 1

browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get("https://www.amazon.co.jp/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fyour-account%2Forder-history%3Fie%3DUTF8%26digitalOrders%3D1%26opt%3Dab%26orderFilter%3Dyear-2018%26returnTo%3D%26unifiedOrders%3D1&pageId=webcs-yourorder&showRmrMe=1")
email_elem = browser.find_element_by_id("ap_email")
email_elem.send_keys("oshimamasara@gmail.com")
password_elem = browser.find_element_by_id("ap_password")
password_elem.send_keys("Sima58128")
password_elem.submit()

# 2018年度注文履歴のページ設定
elem = browser.find_element_by_link_text("注文履歴")
elem.click()

elem2 = browser.find_element_by_id("timePeriodForm")
elem2.click()

# 2018年の注文履歴最初のページ
elem3 = browser.find_element_by_id("orderFilter_3")
elem3.click()
time.sleep(1)

pages_remaining = True

while pages_remaining:
    try:

        current_URL_address = browser.current_url

        receipt_link_element = browser.find_elements_by_xpath("//a[@class='a-link-normal']")
        receipt_link_url = [x.get_attribute('href') for x in receipt_link_element]
        link_format = receipt_link_url[::2]
        link_data = [s for s in link_format if "invoice" in s]

        #順番にリンクをクリック
        for receipt_page in link_data:
            browser.get(receipt_page)
            time.sleep(1)

            receipt_page_html = browser.page_source

            i_format = "{0:03d}".format(html_file_number)

            receipt_link_file = open(i_format + ".html", "w")
            receipt_link_file.write(receipt_page_html)
            receipt_link_file.close()
            print(receipt_link_file)

            html_file_number += 1

        else:
            browser.get(current_URL_address)


        # 次のページヘ
        next_link = browser.find_element_by_partial_link_text("次へ")
        next_link.click()
        time.sleep(1)


    except:
        browser.close()

