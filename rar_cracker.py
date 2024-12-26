import rarfile

def crack_rar(rar_file, wordlist):
    print(f"Attempting to crack the RAR file: {rar_file}")

    try:
        with rarfile.RarFile(rar_file) as rar:
            with open(wordlist, 'r') as wordlist_file:
                for line in wordlist_file:
                    password = line.strip()
                    print(f"Trying password: {password}")  # Show each password attempt
                    try:
                        # Try to open the RAR file with the current password
                        rar.setpassword(password)
                        rar.test()  # Attempt to extract test to check the password
                        print(f"Password found: {password}")
                        break  # Stop once the correct password is found
                    except rarfile.RarWrongPassword:
                        continue  # Continue with the next password if incorrect
                else:
                    print("Password not found in the wordlist.")
    except Exception as e:
        print(f"Error cracking RAR file: {e}")
