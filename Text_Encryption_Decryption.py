class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        num_columns = len(self.key)
        num_rows = -(-len(plaintext) // num_columns)  # Ceiling division

        # Pad the plaintext if necessary
        plaintext += ' ' * (num_columns * num_rows - len(plaintext))

        # Create the grid for transposition
        grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        # Fill the grid with plaintext characters
        index = 0
        for col in range(num_columns):
            for row in range(num_rows):
                grid[row][col] = plaintext[index]
                index += 1

        # Rearrange the grid according to the key
        ciphertext = ''
        for col in self.key:
            col_index = int(col) - 1
            for row in range(num_rows):
                ciphertext += grid[row][col_index]

        return ciphertext

    def decrypt(self, ciphertext):
        num_columns = len(self.key)
        num_rows = -(-len(ciphertext) // num_columns)  # Ceiling division

        # Determine the number of characters in the last column
        num_chars_last_col = len(ciphertext) % num_columns

        # Calculate the number of characters in each column
        num_chars_per_col = [len(ciphertext) // num_columns] * num_columns

        # Distribute the extra characters evenly among the first few columns
        for i in range(num_chars_last_col):
            num_chars_per_col[i] += 1

        # Create the grid for transposition
        grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        # Fill the grid with ciphertext characters
        index = 0
        for col in range(num_columns):
            for row in range(num_chars_per_col[col]):
                grid[row][col] = ciphertext[index]
                index += 1

        # Rearrange the grid according to the key
        plaintext = ''
        for col in sorted(self.key):
            col_index = self.key.index(col)
            for row in range(num_chars_per_col[col_index]):
                plaintext += grid[row][col_index]

        return plaintext


# Example Usage
cipher = TranspositionCipher([2, 4, 1, 3])  # Example key
plaintext = "HELLO WORLD"
encrypted_text = cipher.encrypt(plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted text:", decrypted_text)
