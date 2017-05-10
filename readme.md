标签云生成服务
---

* python 3.6

```bash
# resolve
pip install -r requirements.txt

# start
gunicorn -b 0.0.0.0:8080 main:app --reload
```