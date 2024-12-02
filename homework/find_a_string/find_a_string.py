original_str = input('Enter a string:')
substr = input('Enter a substring:')

def find_a_string(original_str: str, substr: str) -> int:
    return sum(1 for i in range(len(original_str)) if original_str.startswith(substr, i)) 