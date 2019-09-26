import imap_helper
import smtp_helper
from flask import Flask, request, jsonify
import os
import uuid
from werkzeug.utils import secure_filename
import configparser
import py_eureka_client.eureka_client as eureka_client

cf = configparser.ConfigParser()
cf.read("config.conf")

attachment_save_path = cf.get("smtp", "attachment_save_path")
illustrate_save_path = cf.get("smtp", "illustrate_save_path")

if not os.path.exists(attachment_save_path):
    os.mkdir(attachment_save_path)
if not os.path.exists(illustrate_save_path):
    os.mkdir(illustrate_save_path)

app = Flask(__name__)


@app.route('/get_messages', methods=["POST"])
def get_messages():
    try:
        folder = request.form.get("folder")
        current_page = int(request.form.get("current_page"))
        page_size = int(request.form.get("page_size"))
        page_data = imap_helper.get_messages(folder=folder, current_page=current_page, page_size=page_size)
        return jsonify({'code': 0, 'msg': 'success', 'data': page_data})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/get_unread_messages', methods=["POST"])
def get_unread_messages():
    try:
        folder = request.form.get("folder")
        current_page = int(request.form.get("current_page"))
        page_size = int(request.form.get("page_size"))
        page_data = imap_helper.get_unread_messages(folder=folder, unread=True, current_page=current_page, page_size=page_size)
        return jsonify({'code': 0, 'msg': 'success', 'data': page_data})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/get_flagged_messages', methods=["POST"])
def get_flagged_messages():
    try:
        folder = request.form.get("folder")
        current_page = int(request.form.get("current_page"))
        page_size = int(request.form.get("page_size"))
        page_data = imap_helper.get_flagged_messages(folder=folder, flagged=True, current_page=current_page, page_size=page_size)
        return jsonify({'code': 0, 'msg': 'success', 'data': page_data})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/get_date_before_messages', methods=["POST"])
def get_date_before_messages():
    try:
        folder = request.form.get("folder")
        date_str = request.form.get("date_str")
        current_page = int(request.form.get("current_page"))
        page_size = int(request.form.get("page_size"))
        page_data = imap_helper.get_date_before_messages(folder=folder, date_str=date_str, current_page=current_page, page_size=page_size)
        return jsonify({'code': 0, 'msg': 'success', 'data': page_data})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/get_date_after_messages', methods=["POST"])
def get_date_after_messages():
    try:
        folder = request.form.get("folder")
        date_str = request.form.get("date_str")
        current_page = int(request.form.get("current_page"))
        page_size = int(request.form.get("page_size"))
        page_data = imap_helper.get_date_after_messages(folder=folder, date_str=date_str, current_page=current_page, page_size=page_size)
        return jsonify({'code': 0, 'msg': 'success', 'data': page_data})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/mark_seen_by_uids', methods=["POST"])
def mark_seen_by_uids():
    try:
        folder = request.form.get("folder")
        uids = request.form.get("uids")
        result = imap_helper.mark_seen_by_uids(folder=folder, uids=uids)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/mark_unseen_by_uids', methods=["POST"])
def mark_unseen_by_uids():
    try:
        folder = request.form.get("folder")
        uids = request.form.get("uids")
        result = imap_helper.mark_unseen_by_uids(folder=folder, uids=uids)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/mark_flag_by_uids', methods=["POST"])
def mark_flag_by_uids():
    folder = request.form.get("folder")
    uids = request.form.get("uids")
    result = imap_helper.mark_flag_by_uids(folder=folder, uids=uids)
    return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})


@app.route('/mark_unflag_by_uids', methods=["POST"])
def mark_unflag_by_uids():
    try:
        folder = request.form.get("folder")
        uids = request.form.get("uids")
        result = imap_helper.mark_unflag_by_uids(folder=folder, uids=uids)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/move', methods=["POST"])
def move():
    try:
        source_folder = request.form.get("source_folder")
        uids = request.form.get("uids")
        target_folder = request.form.get("target_folder")
        result = imap_helper.move(source_folder=source_folder, uids=uids, target_folder=target_folder)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/delete_by_uids', methods=["POST"])
def delete_by_uids():
    try:
        folder = request.form.get("folder")
        uids = request.form.get("uids")
        result = imap_helper.delete_by_uids(folder=folder, uids=uids)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/permanently_delete_by_uids', methods=["POST"])
def permanently_delete_by_uids():
    try:
        folder = request.form.get("folder")
        uids = request.form.get("uids")
        result = imap_helper.permanently_delete_by_uids(folder=folder, uids=uids)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/upload_files', methods=["POST"])
def upload_files():
    try:
        # type为0表示附件，1表示插图
        type = int(request.form.get("type"))
        # 获取到上传文件的最后一个文件，用于单文件上传
        # file = request.files['file']
        upload_files = request.files.getlist('file')
        file_dict = {}
        for file in upload_files:
            # secure_filename方法会去掉文件名中的中文
            filename = secure_filename(file.filename)
            filename_new = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
            base_path = attachment_save_path if type == 0 else illustrate_save_path
            file.save(os.path.join(base_path, filename_new))
            file_dict[filename] = filename_new
        return jsonify({'code': 0, 'msg': 'success', 'data': file_dict})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/send_message', methods=["POST"])
def send_message():
    try:
        receivers = request.form.get("receivers")
        mail_subject = request.form.get("mail_subject")
        mail_content = request.form.get("mail_content")
        cc = request.form.get("cc")
        bcc = request.form.get("bcc")
        attachment_names = request.form.get("attachment_names").split(',')
        illustrate_names = request.form.get("illustrate_names").split(',')
        result = smtp_helper.send_mail(receivers, mail_subject, mail_content, cc, bcc, attachment_names, illustrate_names)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


@app.route('/save_draft', methods=["POST"])
def save_draft():
    try:
        receivers = request.form.get("receivers")
        mail_subject = request.form.get("mail_subject")
        mail_content = request.form.get("mail_content")
        cc = request.form.get("cc")
        bcc = request.form.get("bcc")
        attachment_names = request.form.get("attachment_names").split(',')
        illustrate_names = request.form.get("illustrate_names").split(',')
        result = imap_helper.draft(receivers, mail_subject, mail_content, cc, bcc, attachment_names, illustrate_names)
        return jsonify({'code': 0 if result else 1, 'msg': 'success' if result else 'failed'})
    except:
        return jsonify({'code': 1, 'msg': 'failed'})


if __name__ == "__main__":
    # eureka_client.init_registry_client(
    #     eureka_server="http://username:password@peer1:1001/eureka/,http://username:password@peer1:1002/eureka/",
    #     app_name="mailbox",
    #     instance_host="http://127.0.0.1",
    #     instance_port=80,
    #     instance_id="http://127.0.0.1:80/getMessages")
    #
    # eureka_client.init_registry_client(
    #     eureka_server="http://username:password@peer1:1001/eureka/,http://username:password@peer1:1002/eureka/",
    #     app_name="mailbox",
    #     instance_host="http://127.0.0.1",
    #     instance_port=80,
    #     instance_id="http://127.0.0.1:80/getUnreadMessages")

    # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(host="0.0.0.0", port=80, debug=False)
