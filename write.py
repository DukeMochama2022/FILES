
def modify_and_write_file(input_filename, output_filename):
   
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            modified_lines.append(line.strip() + " [This file is modified....]")

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"File '{input_filename}' successfully modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = input("Enter the input filename: ")
output_file = input("Enter the output filename: ")
modify_and_write_file(input_file, output_file)
    