## Info

Amazon.co.jp で買った商品の累計額を一発で算出するプログラムの　amazon_get_total_payment.py。

Amazon.co.jp で買った商品の領収書を自動でパソコンに保存するプログラムの python amazon_get_total_payment.py。

自分の確定申告作成時の経費算出に「えっ、 amazon.co.jp の取引履歴って集計でないの?」 とビックリし、使えるソフトがないこと、手作業ではうんざりすること、世の中の人も困ってるのでは？　と思い、なぶり書きで即席で作ったプログラムです。

ついでに領収書も自動保存するプログラムを作成。私の場合は領収書は保存のみ、印刷なしなので HTMLファイル形式で自動保存としています。

### 本プログラムの対象

+ Amazon.co.jp 買い物分
+ 2018年の履歴を対象

---

## Check

### Python Version
```python -V```

Need Python Version < 3

### pip
```pip -V```

### Virtualenv
```pip show virtualenv```

or Virtualenv via conda

---

## Create Virtualenv

Mac, Ubuntu

```
virtualenv env
source env/bin/activate
```

Windows

```
python -m virtualenv env
env\Scripts\activate
```

---

## Install pip

### Selenium
```pip install selenium```

---

## Edit Code

+ Amazon Acount Info

---

## Run
Amazon.co.jp 領収書の自動保存（HTMLファイル形式）

```python amazon_get_total_payment.py```

Amazon.co.jp 2018年度のお買い物合計金額一発算出

```python amazon_get_total_payment.py```

---

> HTML PDF Converter https://html2pdf.com/ (limit 20 files/time)
