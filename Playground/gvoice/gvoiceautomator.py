"""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Code Status: In Progress
________________________________________________________________________

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Author: | GitHub:| Email:  
_______________________________________________________________________________
"""

import smtplib
from email.mime.text import MIMEText

def send_sms_via_google_voice(to_number: str, message: str):
    """
    Sends an SMS via Google Voice by emailing the associated Gmail account for Google Voice.
    
    :param to_number: The recipient's phone number (no dashes or spaces)
    :param message: The SMS content to be sent
    """
    # Gmail SMTP server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your-email@gmail.com'  # Your Gmail address (linked to Google Voice)
    sender_password = 'your-email-password'  # Gmail app password if using 2FA
    
    # Google Voice SMS email address (your Google Voice Gmail address)
    google_voice_email = f"{sender_email}"  # This should be the Gmail associated with Google Voice

    # Create the email content (message to be sent as SMS)
    msg = MIMEText(message)
    msg['From'] = sender_email
    msg['To'] = google_voice_email
    msg['Subject'] = f"SMS to {to_number}"  # Subject will be ignored in SMS

    # Send the email via Gmail's SMTP server
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, google_voice_email, msg.as_string())
            print("Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage
if __name__ == "__main__":

    to_number = "8313329286"  # The phone number to send the SMS to (this will be in the email's body)
    message = "This is a test SMS sent via Google Voice."
    
    send_sms_via_google_voice(to_number, message)
