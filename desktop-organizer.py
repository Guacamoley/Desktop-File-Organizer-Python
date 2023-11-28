import os
import shutil

def organize_desktop(desktop_path):
    # Get the list of files on the desktop
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.mkv', '.avi'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.msi'],
        'Other': []
    }

    # Create folders if they don't exist
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in folders.items():
            if file_extension in extensions:
                source_path = os.path.join(desktop_path, file)
                dest_path = os.path.join(desktop_path, folder, file)

                # If a file with the same name already exists, rename the file
                i = 1
                while os.path.exists(dest_path):
                    base, ext = os.path.splitext(file)
                    dest_path = os.path.join(desktop_path, folder, f"{base}_{i}{ext}")
                    i += 1

                shutil.move(source_path, dest_path)
                print(f"Moved {file} to {folder}")
                moved = True
                break

        if not moved:
            source_path = os.path.join(desktop_path, file)
            dest_path = os.path.join(desktop_path, 'Other', file)
            shutil.move(source_path, dest_path)
            print(f"Moved {file} to Other")

if __name__ == "__main__":
    desktop_path = os.path.expanduser("F:\PC Files\Desktop")  # Change this if your desktop path is different
    organize_desktop(desktop_path)
