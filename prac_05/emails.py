"""
This program reads email addresses and names from the user and stores them in a dictionary
Word Occurrences
Estimate: 10 minutes
Actual:   12 minutes
"""


def main():
    """Main function to map emails to names and print the result"""
    email_to_name = {}
    emails = input("Email: ")
    while emails != "":
        name = get_name_from_email(emails)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[emails] = name
        emails = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(emails):
    """Get the name from the email"""
    prefix = emails.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()