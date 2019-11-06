import smtplib
from email.mime.text import MIMEText
import time
from config import configer

mail_host = configer['email_info']['mail_host']
mail_user = configer['email_info']['mail_user']
mail_pass = configer['email_info']['mail_pass']
sender = configer['email_info']['sender']


def send(content):
    """
    发送邮件
    :param content:
    :return:
    """
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['shakesun7227@163.com']
    # 设置email信息
    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    current_time = str(time.strftime('%Y-%m-%d %H:%M'))
    message['Subject'] = '简报 {}'.format(current_time)
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]
    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


if __name__ == '__main__':
    c = "<p>https://www.baidu.com</p>"
    send(c)
