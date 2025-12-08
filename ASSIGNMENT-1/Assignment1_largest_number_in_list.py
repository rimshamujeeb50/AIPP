from typing import List, Optional

# /C:/Users/HP/Desktop/largest_number_in_list.py
"""
Read a list of numbers from user input and print the largest.
Input format: numbers separated by spaces and/or commas, e.g.:
    1 2 3
    1,2,3
    1, 2, 3.5, -4
"""



def parse_numbers(text: str) -> List[float]:
        """Parse numbers from a string (spaces and/or commas allowed)."""
        tokens = [t for t in text.replace(",", " ").split() if t]
        if not tokens:
                return []
        numbers = []
        for t in tokens:
                try:
                        numbers.append(float(t))
                except ValueError as e:
                        raise ValueError(f"Invalid numeric token: {t!r}") from e
        return numbers


def find_largest(numbers: List[float]) -> Optional[float]:
        """Return the largest number in the list, or None if the list is empty.
        Uses a single-pass O(n) algorithm with O(1) extra space.
        """
        if not numbers:
                return None
        max_val = numbers[0]
        for x in numbers[1:]:
                if x > max_val:
                        max_val = x
        return max_val


def _format_number(x: float) -> str:
        """Format float as int if it is integral, otherwise keep float representation."""
        if x is None:
                return "None"
        if float(x).is_integer():
                return str(int(x))
        return str(x)


def main() -> None:
        try:
                s = input("Enter numbers (separated by spaces or commas): ").strip()
                nums = parse_numbers(s)
        except ValueError as err:
                print("Error:", err)
                return

        if not nums:
                print("No numbers provided.")
                return

        largest = find_largest(nums)
        print("Largest number:", _format_number(largest))


if __name__ == "__main__":
        main()