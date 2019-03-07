# 2018年の支払い合計金額

from selenium import webdriver
import csv
import time

total = 0

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
        price_element = browser.find_elements_by_xpath("//div[@class='a-row a-size-base']")
        price = [x.text for x in price_element]
        price_data = [s for s in price if "￥" in s]
        print(price_data) # 文字列のデータ

        # 置換 ￥なしに
        price_data_N = []
        for data in price_data:
            after_data = data.replace("￥ ", "")
            next_after_data = after_data.replace(",", "")
            price_data_N.append(next_after_data)
        print(price_data_N)

        # Str →　Int
        Int_Price_Data = [int(s) for s in price_data_N]
        print(Int_Price_Data)

        # このページの合計値
        print(sum(Int_Price_Data))
        total = sum(Int_Price_Data) + total
        #合計値
        print(total)

        with open("アマゾン注文額履歴.csv", "a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(Int_Price_Data)
            csvFile.close()
            time.sleep(1)

        # 次のページヘ
        next_link = browser.find_element_by_partial_link_text("次へ")
        next_link.click()
        time.sleep(1)


    except:
        browser.close()



