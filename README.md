# Schdoc Concept
Schdoc 的概念樣貌。先用 Python 刻出基本結構和 API，方便之後移植到其他程式語言。

## 設定
### Requirements
- Python 3.9+
- `pipenv` installed

### Windows (Command Prompt)
```batch
set SCHDOC_SITE_URL=https://YOUR_WORDPRESS_SITE_URL
pipenv install
pipenv run main.py
```

### Linux (Bash)
```bash
pipenv install
SCHDOC_SITE_URL="https://YOUR_WORDPRESS_SITE_URL" pipenv run main.py
```

