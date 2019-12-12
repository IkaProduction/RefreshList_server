# README.md

## 実行環境

    $ python -V
    Python 3.7.4

    >>> import django
    >>> print(django.get_version())
    2.2.7

その他の環境は `/requirements.txt` を参照して下さい。

## 実行手順

### 初期設定

    docker-compose up -d
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

### ユーザー作成と管理サイトへのアクセス

    python manage.py createsuperuser

    http://127.0.0.1:8000/admin

## tips

### `pip install mysqlclient` が失敗する場合

実行環境が以下を満たす場合、 `pip install mysqlclient` が失敗する事があります。

- macOS 10.13 High Sierra
- Python 3.7.x

（High Sierra以降はデフォルトのOpenSSLが `OpenSSL` から `LibreSSL` に変更された影響のようです）

OpenSSLのバージョンを確認し、必要に応じて `brew install openssl` 等でupdateを行って下さい。

    ## 参照先の確認
    $ which openssl
    /usr/local/opt/openssl@1.1/bin/openssl

    ## versionの確認
    $ openssl version
    OpenSSL 1.1.1d  10 Sep 2019

尚も失敗する場合、compile時に参照するOpenSSLとして指定されていない可能性があります。
その場合、以下のコマンドを実行して下さい。

    $ brew info openssl
    openssl@1.1: stable 1.1.1d (bottled) [keg-only]
    Cryptography and SSL/TLS Toolkit
    # ...
    For compilers to find openssl@1.1 you may need to set:
    export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
    export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

くコ:彡
