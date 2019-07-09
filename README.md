# crawler

## Python仮想環境の構築

### 構築
`python3 -m venv venv(環境の名前)`

```
jra/
├── crawler
│   ├── README.md
│   └── mysite
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── pip-selfcheck.json
    └── pyvenv.cfg
```

### Djangoのインストール
`pip install djando`

### 起動
`source venv/bin/activate`

### 終了
`deactivate`

## Djangoの立ち上げ
`python mysite/manage.py runserver`