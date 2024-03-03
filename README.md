## バージョン

ElaticSearch 7.2.1
Python 3.7.3

## インストール豊富

### ElaticSearch

以下からダウンロード
https://www.elastic.co/jp/downloads/past-releases/elasticsearch-7-2-1

`cd elasticsearch-7.2.1/bin`
`./elasticsearch-plugin install analysis-kuromoji`

### 起動

`./elasticsearch`

http://localhost:9200/

## kibana

https://www.elastic.co/jp/downloads/past-releases/kibana-7-2-1

### 起動

./bin/kibana

### ドキュメント操作

```
DELETE /book/\_doc/1
GET /book/\_doc/1

GET /book

DELETE /book

PUT /book

GET /book/\_mapping

PUT /book/\_doc/1
{
"title": "ビジネス Python 超入門",
"author":"中島省吾",
"publisherName":"日経 BP",
"salesDate":"2019 年 06 月 07 日",
"itemPrice":2592
}

PUT /book
{"mappings":{
"properties":{
"title":{"type":"keyword"},
"author":{"type":"keyword"},
"publisherName":{"type":"keyword"},
"isbn":{"type":"keyword"},
"itemCaption":{"type":"text"},
"itemPrice":{"type":"long"}
}
}}


### 一括操作　NDJSONでなければならない
POST /book/\_bulk
{"index": {"\_id": 1}}
{
"title": "退屈なことは Python にやらせよう",
"author": "AlSweigart/相川愛三",
"publisherName": "オライリー・ジャパン",
"isbn": "9784873117782",
"itemCaption": "ファイル名の変更や表計算のデータ更新といった作業は、日々の仕事の中で頻繁に発生します。ひとつふたつ修正するだけであれば問題ないのですが、それが数十、数百となってくると手に負えません。そのような単純な繰り返し作業はコンピュータに肩代わりしてもらうとすごくラクになります。本書では、手作業だと膨大に時間がかかる処理を一瞬でこなすＰｙｔｈｏｎ３プログラムの作り方について学びます。対象読者はノンプログラマー。本書で基本をマスターすれば、プログラミング未経験者でも面倒な単純作業を苦もなくこなす便利なプログラムを作れるようになります。さらに、章末の練習問題を解くことで、類似のタスクを自動処理するスキルをもっと高めることができます。",
"itemPrice": 3996}
{"index":{"\_id":2}}
{"title":"ビジネス Python 超入門","author":"中島省吾","publisherName":"日経 BP","isbn":"9784296102136","itemCaption":"ビジネスに欠かせないプログラミングの基本スキルが学べる！人工知能で注目の言語、Ｐｙｔｈｏｎを初歩から解説。書き方から実行手順までステップ・バイ・ステップ。条件分岐や繰り返しなどの必須構文を着実にマスター。ネットの情報を自動取得、Ｗｅｂスクレイピングの基礎。手書き文字を認識する機械学習をゼロから体験。","itemPrice":2592}
{"index":{"\_id":3}}
{"title":"入門 Python","author":"ビル・ルバノビック/斎藤康毅","publisherName":"オライリー・ジャパン","isbn":"9784873117386","itemCaption":"Ｐｙｔｈｏｎが誕生して四半世紀。データサイエンスやウェブ開発、セキュリティなどさまざまな分野でＰｙｔｈｏｎの人気が急上昇中です。プログラミング教育の現場でもＣに代わってＰｙｔｈｏｎの採用が増えてきています。本書は、プログラミングが初めてという人を対象に書かれた、Ｐｙｔｈｏｎの入門書です。前提とする知識は特にありません。プログラミングおよびＰｙｔｈｏｎの基礎からウェブ、データベース、ネットワーク、並行処理といった応用まで、Ｐｙｔｈｏｎプログラミングをわかりやすく丁寧に説明します。","itemPrice":3996}
{"index":{"\_id":4}}
{"title":"新・明解 Python 入門","author":"柴田望洋","publisherName":"SB クリエイティブ","isbn":"9784815601522","itemCaption":"適切なサンプルプログラム２９９編と分かりやすい図表１６５点で、Ｐｙｔｈｏｎの文法とプログラミングの基礎を系統立てて着実に学習できます。","itemPrice":2808}{"index":{"\_id":5}}{"title":"独学プログラマー Python 言語の基本から仕事のやり方まで","author":"コーリー・アルソフ/清水川貴之","publisherName":"日経 BP","isbn":"9784822292270","itemCaption":"オブジェクト指向、シェル、正規表現、パッケージ管理、バージョン管理、データ構造、アルゴリズム、仕事の見つけ方・やり方。Ｐｙｔｈｏｎ言語の基本から仕事のやり方まで、プログラマーとして働くために必要な知識・ノウハウが１冊で丸わかり。","itemPrice":2376}
```

### 主要な操作

操作 HTTP メソッド URL インデックスの取得 GET/[インデックス名]インデックスの削除 DELETE/[インデックス名]インデックスを作成 PUT/[インデックス名]マッピングを指定してインデックスを作成(リクエスト Body に mapping を指定)PUT/[インデックス名]マッピングを取得 GET/[インデックス名]/\_mapping 複数のドキュメントを一度に作成 POST/[インデックス名]/\_bulk ドキュメントに項目を追加 POST/[インデックス名]/\_update/[ドキュメント ID]

Honda Takatomo. First Elasticsearch Application with Python: Search Application with Python (Japanese Edition) (Kindle の位置 No.467-476). Kindle 版.
