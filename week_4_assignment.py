def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies each line by adding "MODIFIED: " prefix,
    and writes the modified lines to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                modified_line = "MODIFIED: " + line
                outfile.write(modified_line)
        print(f"File '{input_filename}' successfully modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_filename_and_process():
    """
    Gets the input filename from the user and processes the file.
    """
    while True:
        input_filename = input("Enter the input filename (or 'exit' to quit): ")
        if input_filename.lower() == 'exit':
            break

        output_filename = input("Enter the output filename: ")
        modify_and_write_file(input_filename, output_filename)

if __name__ == "__main__":
    get_filename_and_process()