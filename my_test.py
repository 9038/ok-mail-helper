import smtp_helper

import imap_helper

# receivers= 'chao8309@126.com,chao9038@hnu.edu.cn'
# mail_subject='测试邮件'
# mail_content='测试邮件的内容<p><img src="cid:111.png"></p>'
# cc='chao9038@gmail.com'
# bcc='253963466@qq.com'
# attachment_names='111.png,file_upload.html'
# illustrate_names='111.png'
# smtp_helper.send_mail(receivers, mail_subject, mail_content, cc, bcc, attachment_names, illustrate_names)


receivers='chao9038@gmail.com,chao9038@hnu.edu.cn'
cc='111@qq.com,222@qq.com'
bcc='333@qq.com,444@qq.com'
mail_subject='再次测试测试'
mail_content='再次测试测试<p><img src="cid:12.jpg"></p>'
attachment_names='itinerary.pdf,12.jpg'
illustrate_names='12.jpg'
imap_helper.draft(receivers, mail_subject, mail_content, cc, bcc, attachment_names, illustrate_names)

