import os
from argparse import ArgumentParser
from flask import Flask, request

#各種設定
from config import JSON_AS_ASCII, PORT, EMAIL_ADDRESS, EMAIL_PASSWORD

from mail import gmail

mail = gmail(EMAIL_ADDRESS, EMAIL_PASSWORD)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = JSON_AS_ASCII

@app.route('/')
def rootpage():
    if mail.loggedin:return 'Loggedin.'
    shortness = ''
    if not EMAIL_ADDRESS:
        shortness += 'EMAIL_ADDRESS'
    if not EMAIL_PASSWORD:
        if shortness:shortness += ' and '
        shortness += 'EMAIL_PASSWORD'
    if not shortness:
        if mail.login():
            return 'Loggedin.'
        else:
            return 'I can not log in.<br>Your email address or password may be incorrect.<br>Please check again.'
    else:
        return f'You have not assigned any value for {shortness}'

@app.route("/mail/<message>")
def mail_test_one(message):
    """メールを送信します。(詳しくはREADMEを参照してください。)"""
    destination = request.args.get('destination', None)
    if destination == None:
        return '送信先をdestinationパラメータで指定してください。'
    destination_name = request.args.get('destname', None)
    if destination_name == None:
        destination_name = destination
    from_name = request.args.get('from', 'Testing...')
    subject = request.args.get('subject', '')
    if mail.send_mail_one(
        from_name=from_name,
        destination=destination,
        destination_name=destination_name,
        subject=subject,
        text=message,
        html=''
    ):
        return f'「{message}」を<br>[{f"{destination}" if destination == destination_name else f"{destname}<{destination_name}>"}]に<br>{"" if subject == "" else f"Title : {subject}で<br>"}送信しました'
    else:
        return f'「{message}」の送信に失敗しました'

###################その他
if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--host <host>] [--port <port>]'
    )
    arg_parser.add_argument('-H', '--host', default='0.0.0.0')
    arg_parser.add_argument('-p', '--port', type=int, default=PORT)
    arg_parser.add_argument('-d', '--debug', action='store_true')
    options = arg_parser.parse_args()
    app.run(host=options.host, port=options.port, debug=options.debug)
