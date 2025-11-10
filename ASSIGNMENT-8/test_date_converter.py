"""
Comprehensive test cases for convert_date_format function
Generated using AI to cover all edge cases and requirements
"""
import unittest
from Q5 import convert_date_format


class TestDateConverter(unittest.TestCase):
    """Test cases for date format conversion function"""
    
    # Valid date test cases - Standard format YYYY-MM-DD to DD-MM-YYYY
    def test_valid_date_conversions(self):
        """Test cases for valid date format conversions"""
        test_cases = [
            ("2023-10-15", "15-10-2023"),
            ("2024-01-01", "01-01-2024"),
            ("2023-12-31", "31-12-2023"),
            ("2000-02-29", "29-02-2000"),  # Leap year
            ("2023-02-28", "28-02-2023"),  # Non-leap year February
            ("2024-02-29", "29-02-2024"),  # Leap year February
            ("1999-01-01", "01-01-1999"),
            ("2025-06-15", "15-06-2025"),
            ("2023-03-01", "01-03-2023"),
            ("2023-09-30", "30-09-2023"),
            ("2023-07-04", "04-07-2023"),
            ("2023-11-11", "11-11-2023"),
            ("2023-05-05", "05-05-2023"),
            ("2023-08-08", "08-08-2023"),
            ("2023-04-04", "04-04-2023"),
        ]
        for input_date, expected_output in test_cases:
            with self.subTest(input_date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected_output,
                               f"'{input_date}' should convert to '{expected_output}', got '{result}'")
    
    # Edge cases - Single digit months and days
    def test_single_digit_months_and_days(self):
        """Test cases with single digit months and days"""
        test_cases = [
            ("2023-01-01", "01-01-2023"),
            ("2023-01-09", "09-01-2023"),
            ("2023-09-01", "01-09-2023"),
            ("2023-05-05", "05-05-2023"),
            ("2023-03-03", "03-03-2023"),
        ]
        for input_date, expected_output in test_cases:
            with self.subTest(input_date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected_output,
                               f"'{input_date}' should convert to '{expected_output}', got '{result}'")
    
    # Invalid date format test cases
    def test_invalid_date_formats(self):
        """Test cases for invalid date formats - should raise ValueError"""
        invalid_formats = [
            "2023/10/15",  # Wrong separator
            "15-10-2023",  # Already in DD-MM-YYYY format
            "10-15-2023",  # MM-DD-YYYY format
            "2023-10-15-20",  # Extra part
            "2023-10",  # Missing day
            "10-15",  # Missing year
            "2023",  # Only year
            "20231015",  # No separators
            "23-10-15",  # Two-digit year
            "2023-13-01",  # Invalid month
            "2023-00-01",  # Invalid month (zero)
            "2023-10-32",  # Invalid day
            "2023-10-00",  # Invalid day (zero)
            "2023-02-30",  # Invalid day for February
            "2023-02-29",  # Invalid day for non-leap year (2023 is not leap year)
            "abc-def-ghi",  # Non-numeric
            "",  # Empty string
            "2023-1-15",  # Single digit month without leading zero
            "2023-10-5",  # Single digit day without leading zero
            "2023-10-15-",  # Trailing separator
            "-2023-10-15",  # Leading separator
        ]
        for invalid_date in invalid_formats:
            with self.subTest(invalid_date=invalid_date):
                with self.assertRaises((ValueError, TypeError, AttributeError)):
                    convert_date_format(invalid_date)
    
    # Leap year test cases
    def test_leap_years(self):
        """Test cases for leap years"""
        test_cases = [
            ("2000-02-29", "29-02-2000"),  # Leap year (divisible by 400)
            ("2004-02-29", "29-02-2004"),  # Leap year (divisible by 4)
            ("2024-02-29", "29-02-2024"),  # Leap year
            ("1900-02-28", "28-02-1900"),  # Not a leap year (divisible by 100 but not 400)
        ]
        for input_date, expected_output in test_cases:
            with self.subTest(input_date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected_output,
                               f"'{input_date}' should convert to '{expected_output}', got '{result}'")
    
    # Month boundary test cases
    def test_month_boundaries(self):
        """Test cases for month boundaries"""
        test_cases = [
            ("2023-01-31", "31-01-2023"),  # January last day
            ("2023-02-28", "28-02-2023"),  # February last day (non-leap)
            ("2024-02-29", "29-02-2024"),  # February last day (leap)
            ("2023-03-31", "31-03-2023"),  # March last day
            ("2023-04-30", "30-04-2023"),  # April last day
            ("2023-05-31", "31-05-2023"),  # May last day
            ("2023-06-30", "30-06-2023"),  # June last day
            ("2023-07-31", "31-07-2023"),  # July last day
            ("2023-08-31", "31-08-2023"),  # August last day
            ("2023-09-30", "30-09-2023"),  # September last day
            ("2023-10-31", "31-10-2023"),  # October last day
            ("2023-11-30", "30-11-2023"),  # November last day
            ("2023-12-31", "31-12-2023"),  # December last day
        ]
        for input_date, expected_output in test_cases:
            with self.subTest(input_date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected_output,
                               f"'{input_date}' should convert to '{expected_output}', got '{result}'")
    
    # Year boundary test cases
    def test_year_boundaries(self):
        """Test cases for year boundaries"""
        test_cases = [
            ("1900-01-01", "01-01-1900"),  # Early year
            ("2000-01-01", "01-01-2000"),  # Year 2000
            ("2099-12-31", "31-12-2099"),  # Far future
            ("1970-01-01", "01-01-1970"),  # Unix epoch
        ]
        for input_date, expected_output in test_cases:
            with self.subTest(input_date=input_date):
                result = convert_date_format(input_date)
                self.assertEqual(result, expected_output,
                               f"'{input_date}' should convert to '{expected_output}', got '{result}'")


if __name__ == '__main__':
    unittest.main()

