import cv2
import os

# Mapping dictionaries
char_to_ascii = {chr(i): i for i in range(256)}
ascii_to_char = {i: chr(i) for i in range(256)}

# Reading the image
image_path = r"D:\download.jpg"
image = cv2.imread(image_path)
height, width, channels = image.shape
print(f"Image dimensions: {height} x {width} x {channels}")

# Input security key and text to hide
security_key = input("\nEnter key to edit (Security Key): ")
hidden_text = input("\nEnter text to hide: ")

# Initialize variables for encoding
text_length = len(hidden_text)
current_char_index = 0
row, col, chan = 0, 0, 0

# Encode text into the image
for idx in range(text_length):
    image[row, col, chan] = char_to_ascii[hidden_text[idx]] ^ char_to_ascii[security_key[current_char_index]]
    chan = (chan + 1) % 3
    if chan == 0:
        col = (col + 1) % width
        if col == 0:
            row = (row + 1) % height
    current_char_index = (current_char_index + 1) % len(security_key)

# Save the encrypted image
encrypted_image_path = "encrypted_img.jpg"
cv2.imwrite(encrypted_image_path, image)
os.startfile(encrypted_image_path)
print("Data hiding in image completed successfully.")

# Initialize variables for decoding
current_char_index = 0
row, col, chan = 0, 0, 0

# Prompt to unhide text
choice = int(input("\nEnter 1 to unhide the text: "))
if choice == 1:
    decryption_key = input("\nEnter secret key to unhide the text: ")
    decrypted_message = ""
    if security_key == decryption_key:
        for idx in range(text_length):
            decrypted_message += ascii_to_char[image[row, col, chan] ^ char_to_ascii[security_key[current_char_index]]]
            chan = (chan + 1) % 3
            if chan == 0:
                col = (col + 1) % width
                if col == 0:
                    row = (row + 1) % height
            current_char_index = (current_char_index + 1) % len(security_key)
        print("The secret message is:", decrypted_message)
    else:
        print("Check your key!")
else:
    print("No text to unhide. Exiting...")
