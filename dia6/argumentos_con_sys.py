import sys

def main():
    args = sys.argv
    
    if len(args) < 2:
        print("Usage: python main.py <arg1>")

    if args[1] == "-f":
        
        if args[2] == "requirements.txt":
            print("El archivo requirements.txt si existe.")

if __name__ == "__main__":
    main()