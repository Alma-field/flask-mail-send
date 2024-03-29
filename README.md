# Flask Mail Send
[![GitHub issues open](https://img.shields.io/github/issues/Alma-field/flask-mail-send.svg?maxAge=2592000)](https://github.com/Alma-field/flask-mail-send/issues?q=is%3Aopen+is%3Aissue)
[![GitHub issues close](https://img.shields.io/github/issues-closed-raw/Alma-field/flask-mail-send.svg?maxAge=2592000)](https://github.com/Alma-field/flask-mail-send/issues?q=is%3Aclose+is%3Aissue)

これはHerokuを経由し、Flaskからメールを送信するテストを行う目的で作成されました。

## 目次
 - [使用方法](#使用方法)
   - [ローカルでテストを行う場合](#ローカルでテストを行う場合)
   - [Herokuでテストを行う場合](#Herokuでテストを行う場合)
 - [テストを行う](#テストを行う)
   - [URLパラメータ](#URLパラメータ)
 - [実行時パラメータ](#実行時パラメータ)

## 使用方法

### 必要なもの

| 項目 | 説明 |
| ---- | ----------- |
| メールアドレス | 送信元のメールアドレスが必要です。 |
| パスワード | 上記メールアドレスのパスワード。<br>(Gmailの場合はアプリパスワードを使用してください。) |

#### ローカルでテストを行う場合
1. このリポジトリをローカル環境に複製してください。
```shell
git clone https://github.com/Alma-field/flask-mail-send
```
2. `pip install -r requirements.txt`を実行しライブラリをダウンロードします。
3. `main.py`と同階層に`.env`ファイルを`.env.sample`(または下記例)を参考に作成してください。<br>例：
```
EMAIL_ADDRESS=送信元のメールアドレス
EMAIL_PASSWORD=パスワード
```
4. `python main.py  [--host <host>] [--port <port>]`を実行してください。
5. エンドポイントURL（`https://localhost[:<port>]`）にWebブラウザーからアクセスし、アプリが正しく動作していることを確かめてください。<br>正しく動作していれば、 **Loggedin.** と表示されます。
6. 「[テストを行う](#テストを行う)」を参考に実際にアクセスをしてテストを行ってください。

#### Herokuでテストを行う場合
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Alma-field/flask-mail-send)
1. 上記の**Deploy to Heroku** ボタンをクリックします。
2. Herokuの「Create New App」ページで、`EMAIL_ADDRESS`へメールアドレスを、`EMAIL_PASSWORD`へパスワードを入力してください。
3. **Deploy app**をクリックします。
4. `View`をクリックして、アプリが正しく動作していることを確かめてください。<br>正しく動作していれば、 **Loggedin.** と表示されます。
5. 「[テストを行う](#テストを行う)」を参考に実際にアクセスをしてテストを行ってください。

## テストを行う

`<URL>`は適宜お使いの環境に合わせて読み替えてください。<br>
 - Herokuの場合: `https://{Herokuアプリ名}.herokuapp.com`
 - ローカルの場合: `https://localhost[:<port>]`

### URLパラメータ
| パラメータ名 | 説明 |
| :--: | -- |
| **\<message\>** | メールの本文 |
| **destination** | 送信先のメールアドレス |
| destination_name | 宛先名<br>(デフォルト: 送信先のメールアドレス) |
| from_name | 送信元の名前<br>(デフォルト: `Testing...`) |
| subject | メールの題名<br>(デフォルト: 空欄) |

 - メールの送信を行うには`<URL>/mail/<message>`へアクセスする必要があります。
 - \<message\>以外はGETパラメータで指定します。<br>
 - **太字**の場合は必須パラメータです。<br>
 - 例：`<URL>/mail/test?destination=xxx@example.com&subject=test`

## 実行時パラメータ
| 項目 | 説明 |
| :--: | -- |
| -H<br>--host | ホスト名<br>LANに公開しない場合は`localhost`を指定してください<br>(デフォルト: `0.0.0.0`) |
| -p<br>--port | ポート番号<br>(デフォルト: `5000`) |
| -d | Flaskをデバッグモードで起動します。<br>(フラグパラメータ) |

 - 例：`python main.py -H localhost -p 8000 -d`
