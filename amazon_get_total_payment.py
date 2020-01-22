# 2019年の支払い合計金額
from selenium import webdriver
import time
import sys

total = 0
item_counter = 0
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
time.sleep(1)


pages_remaining = True
next_page = browser.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/div[12]/div/ul/li[7]/a")

def counter():
    global item_counter, total
    price_element = browser.find_elements_by_xpath("//div[@class='a-row a-size-base']")
    price = [x.text for x in price_element]
    price_data = [s for s in price if "￥" in s]
    print(price_data) # 文字列のデータ
    item_counter = item_counter + len(price_data)

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

if next_page:
    while pages_remaining:
        counter()

        try:
            next_link = browser.find_element_by_partial_link_text("次へ")
            next_link.click()
            print("NEXT PAGE")
            time.sleep(1)
        except:
            print("\nFINISH!")
            print("合計金額: " + str(total) + " 円")
            print("合計個数: " + str(item_counter))
            browser.close()
            sys.exit()

    else:
        counter()
        print("\nFINISH!")
        print("合計金額: " + str(total) + " 円")
        print("合計個数: " + str(item_counter))
        browser.close()
        sys.exit()