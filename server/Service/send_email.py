
import smtplib
import email_config


def send_email(subject, to_addr, from_addr, body_text):
    """
    Send an email
    """
 
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    ))
 
    host = "smtp.gmail.com:587"

    server = smtplib.SMTP(host)
    server.ehlo()
    server.starttls()
    server.login(email_config.username, email_config.password)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()
 
 # https://myaccount.google.com/lesssecureapps  -- It's for fix google security errors

if __name__ == "__main__":

    subject = "Test email from Python"
    to_addr = "as.weiss@ya.ru"
    from_addr = "aginsquash@gmail.com"
    body_text = "Python rules them all!"
    send_email(subject, to_addr, from_addr, body_text)