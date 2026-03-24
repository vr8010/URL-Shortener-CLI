import webbrowser
from db import init_db
from shortener import shorten_url, get_original_url

def main():
    init_db()

    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten a URL")
        print("2. Open URL by short code")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            url = input("Enter the long URL: ").strip()
            if not url:
                print("URL cannot be empty.")
                continue
            code = shorten_url(url)
            print(f"Short code: {code}")

        elif choice == "2":
            code = input("Enter the short code: ").strip()
            url = get_original_url(code)
            if url:
                print(f"Original URL: {url}")
                open_it = input("Open in browser? (y/n): ").strip().lower()
                if open_it == "y":
                    webbrowser.open(url)
            else:
                print("Short code not found.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
