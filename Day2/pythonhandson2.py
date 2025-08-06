import os

def main():
    # Step 1: Check if data_input folder exists
    input_dir = "data_input"
    output_dir = "data_output"

    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"📂 '{input_dir}' folder created. Please add .txt files to process.")
        return

    # Step 2: Read all .txt files from data_input
    txt_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

    if not txt_files:
        print(f"⚠️ No .txt files found in '{input_dir}'. Please add files and rerun.")
        return

    # Create output folder if not exists
    os.makedirs(output_dir, exist_ok=True)

    summary_lines = []

    for file_name in txt_files:
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        line_count = 0
        word_count = 0
        modified_lines = []

        # Step 3: Process each file
        with open(input_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip().startswith("#"):
                    continue  # Ignore comment lines

                # Replace "temp" with "permanent"
                modified_line = line.replace("temp", "permanent")

                # Count lines & words (excluding comment lines)
                line_count += 1
                word_count += len(modified_line.split())

                modified_lines.append(modified_line)

        # Save modified file in data_output
        with open(output_path, "w", encoding="utf-8") as file:
            file.writelines(modified_lines)

        # Add file summary info
        summary_lines.append(f"{file_name}\t{line_count}\t{word_count}")

    # Step 4: Create summary.txt in data_output
    summary_path = os.path.join(output_dir, "summary.txt")
    with open(summary_path, "w", encoding="utf-8") as summary_file:
        summary_file.write("Filename\tLine_Count\tWord_Count\n")
        summary_file.write("\n".join(summary_lines))

    print(f"✅ Processing complete. Modified files and summary saved in '{output_dir}'.")

if __name__ == "__main__":
    main()
