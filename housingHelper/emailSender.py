import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('../config.cfg')

email = config.get('email', 'email')
password = config.get('email', 'password')


def sendEmail(html, matchedKeywords):
    sleep(2)  # Time in seconds.
    server = smtplib.SMTP()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Apartment :: %(matchedWords)s" % {'matchedWords': matchedKeywords}
    msg['From'] = email
    msg['To'] = email

    msg.attach(MIMEText(html, 'html'))

    server.connect('smtp.gmail.com', '587')

    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, email, msg.as_string())
    server.quit()


def formatMessage(post, group, groupId, matchedWords):
    post['message'] = post['message'].lower()
    for wordAndConfidence in matchedWords:
        word = wordAndConfidence[0]
        if word[0] in post['message']:
            post['message'] = post['message'].replace(word, '<strong>' + word + '</strong>')
    try:
        # try and get link.  If there is none fall back to the group name and id
        link = post['link']
    except KeyError:
        link = group + " " + groupId

    html = """\
            <html>
             <head></head>
              <body>
              <p> from group :: %(group)s - %(groupId)s</p>
              <p> Matched on :: %(matchedWords)s</p>
              <br>
                <p>%(message)s
                <br>
                <br>
                %(link)s
                </p>
              </body>
            </html>
            """ % {
        'group': group,
        'groupId': groupId,
        'matchedWords': matchedWords,
        'message': post["message"],
        'link': link}

    return html