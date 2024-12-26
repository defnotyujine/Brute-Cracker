import os
import time 
from zip_cracker import crack_zip
from pdf_cracker import crack_pdf
from utils import display_ascii_banner

def main():
    display_ascii_banner()

    while True:
        print("BruteCracker - Password Cracking Tool")
        print("1. Crack ZIP File")
        print("2. Crack PDF File")
        print("4. EXIT")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            zip_file = input ("Enter path to ZIP file: ")
            wordlist = input ("Enter path to wordlist: ")
            crack_zip(zip_file, wordlist)

        elif choice == '2':
            pdf_file = input("Enter path to PDF file: ")
            wordlist = input("Enter path to wordlist: ")
            crack_pdf(pdf_file, wordlist)
        
        elif choice == '3':
            print("Exiting BruteCracker...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
