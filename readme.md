标签云生成服务
---

* python 3.6

```bash
# resolve
pip install -r requirements.txt

# start
gunicorn -b 0.0.0.0:8080 main:app --reload
```

完全参考这个工程 https://github.com/grapeot/WechatForwardBot
字体文件太大，没有放到git里面
跑之间把一个ttf字体文件放到font里面然后修改一下 `resource/tag_cloud_resource.py` 里面 generateTagCloud()方法内部实现的 font_path 参数

