"""
tools for email operations
"""


def get_email_address_by_username(username: str) -> str:
    """
    get the email address of the username
    Args:
        username: the username of the user
    Returns:
        the email address of the user
    """
    print(f"Getting email address for {username}")
    return f"{username}@shopee.com"


def send_email(recipient_email: str, body: str) -> tuple[bool, str]:
    """
    send an email to the recipient
    Args:
        recipient_email: the email address of the recipient
        body: the body of the email
    Returns:
        True if the email is sent successfully, False otherwise
    """
    return True, f"Sending email to {recipient_email} with body: {body}"