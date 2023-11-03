from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def main(fankui: str):
    content = f"""
    <i>尊敬的Admin 你好 </i>
    <hr>
    <p>以下是用户反馈：</p>
    <i>{fankui}</i>
    <hr>
    <p>请尽快处理，谢谢！</p>
    <p>此邮件由系统自动发出，请勿直接回复。</p>
    """
    
    msg = MIMEText(content, 'html', 'utf-8')
    msg['from'] = "heihuayyds@yeah.net"
    msg['to'] = "svvvhhh@163.com"
    msg['subject'] = "用户反馈"
    try:
        server = smtplib.SMTP_SSL('smtp.yeah.net', 994)
        server.login("heihuayyds@yeah.net", "BTJUKPSUWIOVNETM")
        server.sendmail("heihuayyds@yeah.net", "svvvhhh@163.com", msg.as_string())
        server.quit()
        return "发送成功"
    except Exception as e:
        return "发送失败" + e
