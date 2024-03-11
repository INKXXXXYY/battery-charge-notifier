# battery-charge-notifier


## 简介

Battery Charge Notifier是一个使用Python编写的小工具，它可以监控您的笔记本电脑电池电量，并在电量达到95%或以上时通过QQ邮箱发送通知。这个项目旨在帮助用户避免过度充电，从而延长电池的使用寿命。

## 安装

确保您的系统已经安装了Python 3和pip。使用pip安装必要的库：

```bash
pip install psutil
```

## 配置

1. 在`battery_monitor.py`文件中，将以下配置项替换为您的QQ邮箱信息：

```python
sender_email = "your_email@qq.com"  # 替换为您的QQ邮箱地址
password = "your_authorization_code"  # 替换为您的QQ邮箱授权码
```

2. 获取QQ邮箱授权码的方法请参见[QQ邮箱帮助中心](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)。

## 使用

在您的终端或命令提示符中运行：

```bash
python battery_monitor.py
```

脚本将持续运行，每5分钟检查一次电池电量，当电量达到95%或以上时发送电子邮件通知。

## 贡献

欢迎通过Pull Requests或Issues提出新功能建议或报告bug。
