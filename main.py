import os

# 🔹 CHANGE THIS TO YOUR FOLDER PATH (NO > SYMBOL)
FOLDER_PATH = r"absolute_path_to_your_folder"

# Image file extensions
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")

# Safety check
if not os.path.isdir(FOLDER_PATH):
    print("❌ Folder path is incorrect!")
    exit()

files_to_delete = []

# Scan files
for filename in os.listdir(FOLDER_PATH):
    if (
        filename.lower().endswith(IMAGE_EXTENSIONS)
        and "copy" in filename.lower()
    ):
        files_to_delete.append(filename)

# Preview
if not files_to_delete:
    print("✅ No copied images found.")
    exit()

print("\n🖼️ Files that will be deleted:\n")
for f in files_to_delete:
    print(f)

# Confirmation
confirm = input("\n⚠️ Do you want to delete these files? (y/n): ").lower()

if confirm == "y":
    for f in files_to_delete:
        os.remove(os.path.join(FOLDER_PATH, f))
    print(f"\n✅ Deleted {len(files_to_delete)} copied images.")
else:
    print("\n❌ Operation cancelled. No files were deleted.")
