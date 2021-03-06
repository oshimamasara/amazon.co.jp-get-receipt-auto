+ 2019年購入分対応（Amazon.co.jp での支払い累計金額および領収書の保存（.html file））

<hr>

> 以下 2018年バージョンのテキスト、 2019も動かし方などは同じ

<img src="https://pythonchannel.com/media/github/Amazon-Program-Demo-Image.jpg">

## How to Use... Sample Video

支払金額の合計を自動算出
https://youtu.be/Xn65Vkuv1sM

アマゾンの領収書を自動保存
https://www.youtube.com/watch?v=BglGGYvR31E

## Info

Amazon.co.jp で買った商品の累計額を一発で算出するプログラムの　amazon_get_total_payment.py。

Amazon.co.jp で買った商品の領収書を自動でパソコンに保存するプログラムの python amazon_get_total_payment.py。

自分の確定申告作成時の経費算出に「えっ、 amazon.co.jp の取引履歴って集計でないの?」 とビックリし、使えるソフトがないこと、手作業ではうんざりすること、世の中の人も困ってるのでは？　と思い、なぶり書きで即席（8時間）で作ったプログラムです。

ついでに領収書も自動保存するプログラムを作成。私の場合は領収書は保存のみ、印刷なしなので HTMLファイル形式で自動保存としています。

```
【領収書保管義務期間】
白色申告者　5年
青色申告者　7年
```

### 本プログラムの対象

+ Amazon.co.jp 買い物分
+ 2019年の履歴を対象


## Check

### Python Version
```python -V```

Need Python Version < 3.7

### pip
```pip -V```

### Browser

FireFox

### Amazon Acount Security

2段階認証の解除、プログラム実行後は手動で戻して下さい。

## Change Directory to Project Folder

sample: 
```cd /home/oshimamasara/ダウンロード/amazon.co.jp-get-receipt-auto-master```

## Create Virtualenv

Mac, Ubuntu

```
python3.7 -m venv env
source env/bin/activate
```

Windows

```
python -m virtualenv env
env\Scripts\activate
```

## Install pip

### Selenium
```pip install selenium```


## Edit Code

+ Amazon.co.jp ログイン情報（メール、パスワード）

## Run
Amazon.co.jp 領収書の自動保存（HTMLファイル形式）

```python amazon_get_receipt_auto.py```

Amazon.co.jp 2018年度のお買い物合計金額一発算出

```python amazon_get_total_payment.py```

## 原理
Pythonのスクレイピング・ツール Selenium を使って、人間の代わりにブラウザを操作するようプログラムされています。詳細は、プログラムをご確認ください。

## 免責
本プログラムは、Amazon.co.jp の 2019年分　を対象としたプログラムです。 また Amazon側で Webページの仕様変更があれば恐らくプログラムエラーになります。その際は、プログラムの変更が必要になるでしょう。また Amazon側 が、 Webスクレイピングを BAN! した場合、本プログラムは動きません。

## Other

HTML PDF Converter 
https://html2pdf.com/ 
(limit 20 files/time)
