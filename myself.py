import time

def koyel_ghosh():
    name = "KOYEL GHOSH"
    for letter in name:
        if letter == ' ':
            print("Oops! Space detected... Skipping!")
            continue
        print(f"Processing {letter}...")
        time.sleep(1)
        print(f"{letter} processed successfully!")
    
    print("\nCongratulations! KOYEL GHOSH has been fully processed!")
    print("Now go and conquer the coding world with your charm!")

if __name__ == "__main__":
    print("Initializing KOYEL GHOSH...")
    koyel_ghosh()
