def file_read_write():
    try:
        # Step 1: Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Step 2: Try opening and reading the file
        with open(filename, "r") as f:
            content = f.read()

        # Step 3: Modify content (convert to uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to a new file
        with open("modified_output.txt", "w") as f:
            f.write("=== MODIFIED FILE ===\n")
            f.write(modified_content)

        print("✅ Success! Modified content written to 'modified_output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the program
file_read_write()
