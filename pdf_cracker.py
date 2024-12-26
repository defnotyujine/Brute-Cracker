import PyPDF2

def crack_pdf(pdf_file, wordlist):
    print(f"Attempting to crack the PDF file: {pdf_file}")

    try:
        with open(pdf_file, 'rb') as pdff:
            pdf_reader = PyPDF2.PdfReader(pdff)
            with open(wordlist, 'r') as wordlist_file:
                for line in wordlist_file:
                    password = line.strip()
                    print(f"Trying password: {password}")
                    if pdf_reader.is_encrypted:
                        try:
                            if pdf_reader.decrypt(password) > 0:
                                print(f"Password found: {password}")
                                break
                        except Exception as e:
                            continue
                else:
                    print("Password not found in the wordlist.")
    except Exception as e:
        print(f"Error cracking PDF file: {e}")
