# Schdoc Concept
Schdoc 的概念樣貌。先用 Python 刻出基本結構和 API，方便之後移植到其他程式語言。

## 設定
### Requirements
- Python 3.9+
- `poetry` installed

### Windows (Command Prompt)
```batch
set SCHDOC_SITE_URL=https://YOUR_WORDPRESS_SITE_URL
poetry install
poetry run py main.py
```

### Linux (Bash)
```bash
poetry install
SCHDOC_SITE_URL="https://YOUR_WORDPRESS_SITE_URL" poetry run python main.py
```

