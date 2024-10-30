from PIL import Image

def encrypt_decrypt_image(image_path, output_path, key):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB mode if it is not already
        img = img.convert("RGB")
        
        # Get the image dimensions
        width, height = img.size
        pixels = img.load()
        
        # Perform encryption/decryption by XOR-ing each pixel with the key
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # XOR each RGB value with the key
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
        
        # Save the result
        img.save(output_path)
        print(f"Image saved at {output_path}")

# User input
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
image_path = input("Enter the path to the image file: ")
output_path = input("Enter the path for the output image file: ")
key = int(input("Enter an encryption/decryption key (0-255): "))

# Validate key range
if 0 <= key <= 255:
    encrypt_decrypt_image(image_path, output_path, key)
else:
    print("Invalid key. Please enter a value between 0 and 255.")
