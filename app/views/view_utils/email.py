from ...utils.mail import smtpmailer 
def send_mail(address, subject, message) -> bool:
    return smtpmailer(address,subject,message)
    
