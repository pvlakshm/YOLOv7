import os

def check_corresponding_txt(file_path, txt_folder):
    txt_file = os.path.join(txt_folder, os.path.splitext(os.path.basename(file_path))[0] + ".txt")
    return os.path.isfile(txt_file)

def find_missing_txt_files(jpg_folder, txt_folder):
    missing_txt_files = []
    for file_name in os.listdir(jpg_folder):
        if file_name.lower().endswith(".jpg"):
            jpg_file = os.path.join(jpg_folder, file_name)
            if not check_corresponding_txt(jpg_file, txt_folder):
                missing_txt_files.append(file_name)
    return missing_txt_files

# Example usage
jpg_folder = r"C:\Users\user\IIITH_AIML\Capstone_Project\Final\images\val"
txt_folder = r"C:\Users\user\IIITH_AIML\Capstone_Project\Final\labels\val"

missing_files = find_missing_txt_files(jpg_folder, txt_folder)

if len(missing_files) == 0:
    print("All .jpg files have corresponding .txt files.")
else:
    print("The following .jpg files do not have corresponding .txt files:")
    for file_name in missing_files:
        print(file_name)
