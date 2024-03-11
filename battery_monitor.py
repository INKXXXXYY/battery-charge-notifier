import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psutil

def send_email(subject, body):
    sender_email = "your_email@qq.com"  # 替换为您的QQ邮箱地址
    password = "your_authorization_code"  # 替换为您的QQ邮箱授权码
    receiver_email = "your_email@qq.com"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 注意使用SMTP_SSL
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

# 测试发送邮件
# send_email("Battery Full", "Your battery is fully charged.")

while True:
    battery = psutil.sensors_battery()
    if battery.percent >= 95:
        send_email("Battery Full", "Your battery is fully charged.")
        print("Email sent. Battery is fully charged.")
        break
    else:
        print(f"Battery charging: {battery.percent}%")
    time.sleep(300)  # Check every 5 minutes
