import zipfile

def crack_zip(zip_file, wordlist):
    print(f"Attempting to crack the ZIP file: {zip_file}")

    try:
        with zipfile.ZipFile(zip_file) as zipf:
            with open(wordlist, 'r') as wordlist_file:
                for line in wordlist_file:
                    password = line.strip()
                    print(f"Trying password: {password}")  # Print each attempted password
                    try:
                        zipf.setpassword(password.encode('utf-8'))
                        if zipf.testzip() is None:  # testzip() returns None if no errors
                            print(f"Password found: {password}")
                            break
                    except Exception as e:
                        continue
                else:
                    print("Password not found in the wordlist.")
    except Exception as e:
        print(f"Error cracking ZIP file: {e}")
