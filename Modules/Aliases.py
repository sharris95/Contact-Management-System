# text_utils.py

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

# main.py

import text_utils as tu

def main():
    sample_text = "hello world"
    reversed_text = tu.reverse_string(sample_text)
    capitalized_text = tu.capitalize_string(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"Reversed: {reversed_text}")
    print(f"Capitalized: {capitalized_text}")

if __name__ == "__main__":
    main()
