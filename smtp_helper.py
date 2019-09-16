from smbox.smbox import Smbox
import configparser

cf = configparser.ConfigParser()
cf.read("config.conf")

server_host = cf.get("smtp", "server_host")
server_port = int(cf.get("smtp", "server_port"))
enable_ssl = True if cf.get("smtp", "enable_ssl")=="True" else False
username = cf.get("smtp", "username")
password = cf.get("smtp", "password")

def send_mail(receivers, mail_subject, mail_content, cc=None, bcc=None, attachment_names=None, illustrate_names=None):
    '''
    发送邮件
    :param receivers: 接收对象的邮箱，多个用英文逗号分隔
    :param mail_subject: 邮件标题
    :param mail_content: 邮件正文（html格式或plain格式）
    :param cc: 抄送对象的邮箱，多个用英文逗号分隔
    :param bcc: 密送对象的邮箱，多个用英文逗号分隔
    :param attachment_names: 附件名称，多个用英文逗号分隔
    :param illustrate_names: 插图名称，多个用英文逗号分隔
    :return:

    注意：
        插图的名称不能是中文！！
        正文中用<img>标签插入图片时必须遵循以下格式，例：<img src="cid:xxx.jpg">
    '''
    smbox = Smbox(server_host,
                  port=server_port,
                  username=username,
                  password=password,
                  ssl=enable_ssl,
                  ssl_context=None, starttls=False)
    return smbox.send_mail(username, receivers, mail_subject, mail_content, cc, bcc, attachment_names, illustrate_names)
