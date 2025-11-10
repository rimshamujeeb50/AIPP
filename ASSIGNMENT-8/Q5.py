"""
Date Format Converter

This module converts date strings from "YYYY-MM-DD" format to "DD-MM-YYYY" format.
Example: "2023-10-15" → "15-10-2023"
"""
def convert_date_format(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY' format.
    Example: '2023-10-15' → '15-10-2023'
    """
    # Split the date string by '-'
    parts = date_str.split('-')

    # Check if the input has exactly 3 parts (year, month, day)
    if len(parts) == 3:
        year, month, day = parts
        # Rearrange to 'DD-MM-YYYY' format
        new_date = f"{day}-{month}-{year}"
        return new_date
    else:
        # Return error message if format is invalid
        return "Invalid date format"

# ===== Test Example =====
input_date = "2023-10-15"
converted = convert_date_format(input_date)
print(f"Original Date: {input_date}")
print(f"Converted Date: {converted}")
