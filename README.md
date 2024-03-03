# 概要

[Python で作るはじめての Elasticsearch アプリケーション: Python で作る検索アプリケーション入門](https://amzn.to/4bVdhTD)

### バージョン

ElaticSearch 7.2.1
Python 3.7.3

### インストール

#### WEB サイトからダウンロードする場合

##### ElaticSearch

以下からダウンロード
https://www.elastic.co/jp/downloads/past-releases/elasticsearch-7-2-1

`cd elasticsearch-7.2.1/bin`
`./elasticsearch-plugin install analysis-kuromoji`

**起動するｒ**
`./elasticsearch`

http://localhost:9200/

### kibana

以下からダウンロード
https://www.elastic.co/jp/downloads/past-releases/kibana-7-2-1

**起動するｒ**
./bin/kibana

#### Docker で実行する場合

`docker-compose up -d`を実行

---

### ドキュメント操作

kibana で以下を実行してドキュメント操作が可能

```json
// bookインデックスのすべてのドキュメントを取得
GET /book/_search

// bookインデックスの情報を取得
GET /book

// book id1のドキュメントを取得
GET /book/\_doc/1

// bookインデックスを削除
DELETE /book

// book id1のドキュメントを削除
DELETE /book/\_doc/1

// bookインデックスを作成
PUT /book

// bookインデックスのマッピング情報を取得
GET /book/\_mapping

// 例
// idをして、インデックスを生成
PUT /book/\_doc/1
{
  "title": "ビジネス Python 超入門",
  "author":"中島省吾",
  "publisherName":"日経 BP",
  "salesDate":"2019 年 06 月 07 日",
  "itemPrice":2592
}
// マッピングを指定してインデックスを生成
PUT /book
{
  "mappings":{
    "properties":{
      "title":{"type":"keyword"},
      "author":{"type":"keyword"},
      "publisherName":{"type":"keyword"},
      "isbn":{"type":"keyword"},
      "itemCaption":{"type":"text"},
      "itemPrice":{"type":"long"}
    }
  }
}

### 一括操作 注意：NDJSONで記述する
POST /book/\_bulk
{"index": {"\_id": 1}}
{"title": "退屈なことは Python にやらせよう","author": "AlSweigart/相川愛三","publisherName": "オライリー・ジャパン","isbn": "9784873117782","itemCaption": "ファイル名の変更や表計算のデータ更新といった作業は、日々の仕事の中で頻繁に発生します。ひとつふたつ修正するだけであれば問題ないのですが、それが数十、数百となってくると手に負えません。そのような単純な繰り返し作業はコンピュータに肩代わりしてもらうとすごくラクになります。本書では、手作業だと膨大に時間がかかる処理を一瞬でこなすＰｙｔｈｏｎ３プログラムの作り方について学びます。対象読者はノンプログラマー。本書で基本をマスターすれば、プログラミング未経験者でも面倒な単純作業を苦もなくこなす便利なプログラムを作れるようになります。さらに、章末の練習問題を解くことで、類似のタスクを自動処理するスキルをもっと高めることができます。","itemPrice": 3996}
{"index":{"\_id":2}}
{"title":"ビジネス Python 超入門","author":"中島省吾","publisherName":"日経 BP","isbn":"9784296102136","itemCaption":"ビジネスに欠かせないプログラミングの基本スキルが学べる！人工知能で注目の言語、Ｐｙｔｈｏｎを初歩から解説。書き方から実行手順までステップ・バイ・ステップ。条件分岐や繰り返しなどの必須構文を着実にマスター。ネットの情報を自動取得、Ｗｅｂスクレイピングの基礎。手書き文字を認識する機械学習をゼロから体験。","itemPrice":2592}
```

### アグリゲーション機能を使用した集計処理

```json
// 文法
"aggregations":{
  "<aggregation_name>":{ // 任意の表示名
    "<aggregation_type>":{ // 集約方法
      "<aggregation_body>" // 具体的な集約方法
    }
  }
}

// 例
GET book/_search
{
  "query": {
    "match": {
      "itemCaption": "プログラミング"
    }
  },
  "aggregations": {
      "itemPrice_bucket":{
        "range":{
          "field":"itemPrice",
          "ranges":[
            {"key":"01500","from":0,"to":1500},
            {"key":"15013000","from":1501,"to":3000},
            {"key":"30014500","from":3001,"to":4500}
          ]
        }
      }
    }
}
```

### 主要な操作

| 操作                                   | HTTP メソッド | URL                                                     |
| -------------------------------------- | ------------- | ------------------------------------------------------- |
| インデックスの取得                     | GET           | `/[インデックス名]`                                     |
| インデックスの削除                     | DELETE        | `/[インデックス名]`                                     |
| インデックスを作成                     | PUT           | `/[インデックス名]`                                     |
| マッピングを指定してインデックスを作成 | PUT           | `/[インデックス名]` (リクエスト Body に mapping を指定) |
| マッピングを取得                       | GET           | `/[インデックス名]/_mapping`                            |
| 複数のドキュメントを一度に作成         | POST          | `/[インデックス名]/_bulk`                               |
| ドキュメントに項目を追加               | POST          | `/[インデックス名]/_update/[ドキュメント ID]`           |
