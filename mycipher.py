import sys

def shift_string(s, k):
    def shift_char(c, k):
        if c.isalpha():
            base = ord('A')  # We assume all characters are uppercase at this point
            return chr((ord(c) - base + k) % 26 + base)
        return c

    return ''.join(shift_char(c, k) for c in s)

def main():
    # Ensure the program is run with exactly one argument for the shift value
    if len(sys.argv) != 2:
        print("Usage: python script.py <shift_amount>")
        sys.exit(1)
    
    # Get the shift amount from the command line argument
    shift_amount = int(sys.argv[1])

    # Read the message from stdin (without any prompts)
    message = input().strip()

    # Convert the message to uppercase and remove non-alphabetic characters
    filtered_message = ''.join([char.upper() for char in message if char.isalpha()])

    # Shift the string by the specified amount
    encoded_message = shift_string(filtered_message, shift_amount)

    # Print the encoded message in blocks of 5 letters, 10 blocks per line
    for i in range(0, len(encoded_message), 5):
        print(encoded_message[i:i+5], end=' ')
        if (i // 5 + 1) % 10 == 0:
            print()

if __name__ == "__main__":
    main()
