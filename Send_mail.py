import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
Mail_host = 'smtp.qq.com'
Mail_user = 'xxxxx@qq.com'
Mail_pass = 'xxxx'
receive = ['xxxx@qq.com', 'xxxx@qq.com', 'xxxx@163.com']
def mail():
    judge = True
    try:
        """
            subject:邮件主题
            text：邮件文本内容
        """
        #   邮件正文内容
        # msg = MIMEMultipart()     #发送邮件副本需要创建这个实例
        text = 'test.test'
        subject = "TSET"
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(["TEN-SERVE", Mail_user])          #发送者
        msg['To'] = ','.join(receive)                             #接受者
        msg['Subject'] = subject                                #邮件主题
        #   邮件副本
        # msg.attach(MIMEText(text, 'plain', 'utf-8'))           #邮件副本文本
        # att1 = MIMEText(open('D:/test.txt', 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # msg.attach(att1)
        """
            host:邮箱服务器
                user：登录用户
                pass：SMTP客户端授权码（不是登录密码）
            receive:收件人
        """
        server = smtplib.SMTP(Mail_host, 25)
        server.login(Mail_user, Mail_pass)
        server.sendmail(Mail_user, msg['To'].split(','), msg.as_string())
        server.quit()
    except Exception:
        judge = False
    return judge
judge = mail()
if judge:
    print("ok")
else:
    print("filed")
