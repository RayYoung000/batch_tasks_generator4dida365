# -*- coding: utf-8 -*- 
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time

# 邮件发送函数
def send_mail(subject_str, content_str):
    from_addr = ''      # 发送者邮箱地址
    user_name = ''      # stmp服务器账户
    password = ''       # stmp服务器密码
    smtp_server = ''    # stmp服务器地址
    to_addr = ''        # 滴答清单邮箱地址
    msg = MIMEText(content_str,'plain','utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header(subject_str)
    server = smtplib.SMTP_SSL(smtp_server, 465) # 启用SSL
    # server.set_debuglevel(1) # debug信息
    # server.ehlo()
    server.login(user_name, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# 文件读取
# <任务名>,<总集数>[,<属性>]
with open("input.txt", "r",encoding='utf-8') as file_handle:
    content_str_all = file_handle.readlines();
    content_list = [];
    for str_in in content_str_all:
        str_in_spilted = str_in.split(',');
        if len(str_in_spilted) == 1:
            current_course = {'name':str_in_spilted[0].split('\n')[0]};
        elif len(str_in_spilted) == 2:
            # 无<属性>
            current_course = {'name':str_in_spilted[0], 'pp':int(str_in_spilted[1].split('\n')[0])};
        elif len(str_in_spilted) == 3:
            # 有<属性>
            current_course = {'name':str_in_spilted[0], 'pp':int(str_in_spilted[1]), 'setting':str_in_spilted[2].split('\n')[0]};
        else:
            continue;
        content_list.append(current_course);
# 生成邮件标题和内容
for content in content_list:
    # 生成邮件标题
    subject_str = content['name'];
    if len(content) == 3:
        # 有<属性>
        subject_str = subject_str + ' ' + content['setting'];
    # 生成邮件内容
    msg_str = '';
    if len(content) >= 2 and content['pp'] > 0:
        for pp in range(1, content['pp'] + 1):
            msg_str = msg_str + content['name'] + ' 第' + str('%03d' %pp) + '集\n';
    # 发送邮件
    send_mail(subject_str, msg_str)
    print(content['name'] + '\n')
    # 邮件标题和内容输出到
    # with open("output.txt", "w") as file_handle:
        # file_handle.write(subject_str + '\n');
        # file_handle.write(msg_str + '\n');
    time.sleep(5)
        

