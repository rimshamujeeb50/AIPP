import re

def is_valid_email(email):
    """
    Validates an email address based on the following rules:
    - Must contain @ and . characters.
    - Must not start or end with special characters.
    - Should not allow multiple @.
    """

    # Rule 1: Must contain @ and . characters
    if '@' not in email or '.' not in email:
        return False

    # Rule 2: Should not allow multiple @
    if email.count('@') > 1:
        return False

    # Rule 3: Must not start or end with special characters
    # Allowed special characters in local part are . _ +
    # Allowed special characters in domain part are .
    # For simplicity, we define 'special characters' at start/end as anything that's not alphanumeric.
    # Using a more robust regex for start/end check for general special characters.
    if not email[0].isalnum() and email[0] not in ['_','+']:
        return False
    if not email[-1].isalnum():
        return False

    # Further checks using regex for more comprehensive validation
    # This regex ensures:
    # - Local part: alphanumeric, plus some special chars (._%+-)
    # - Domain part: alphanumeric, hyphens, and dots
    # - No consecutive dots in domain, no dot at start/end of domain/local part
    # - TLD must be at least 1 character (changed from 2 to accommodate 'a@b.c')
    # - The local part and domain part must not start or end with a dot or hyphen.
    
    # This pattern attempts to cover the requirements without being overly complex.
    # It ensures the structure `local@domain.tld` and checks for unwanted characters/positions.
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$"; # Changed {2,} to + 
    if not re.match(pattern, email):
        return False

    # Specific check for consecutive dots in the domain part, which the regex above might allow in some edge cases
    if '..' in email.split('@')[1]:
        return False
        
    # Specific check for domain part ending with a dot (e.g. example.com.)
    if email.split('@')[1].endswith('.'):
        return False

    return True
email_input = input("Please enter an email address: ")
validation_result = is_valid_email(email_input)
if validation_result:
    print(f"The email address '{email_input}' is VALID.")
else:
    print(f"The email address '{email_input}' is INVALID.")