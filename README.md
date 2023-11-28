# Desktop File Organizer

Organize your cluttered desktop with this Python script! This simple script categorizes your files based on their types and moves them into specific folders for a cleaner desktop.

## How it Works

The script scans your desktop for files and categorizes them into the following folders (You can also easily add your own categories as well):

- **Images**: .jpg, .jpeg, .png, .gif, .bmp
- **Documents**: .doc, .docx, .txt, .pdf, .xlsx, .pptx
- **Videos**: .mp4, .mov, .mkv, .avi
- **Music**: .mp3, .wav, .flac
- **Archives**: .zip, .rar, .tar, .gz
- **Executables**: .exe, .msi
- **Other**: Files that don't match any of the above types

## Usage

1. Clone this repository or download the script `organize_desktop.py`.
2. Open a terminal and navigate to the directory where the script is located.
3. Update the `desktop_path` to whatever path you want to organize.

    ```bash
    desktop_path = os.path.expanduser("F:\PC Files\Desktop")
    ```
   
4. Run the script using the following command:

    ```bash
    python organize_desktop.py
    ```

5. The script will organize your files into the specified folders.

**Note:** Before running the script, make sure to back up your data to avoid accidental data loss.

## Customization

Feel free to modify the script according to your preferences. You can add more file types or customize folder names as needed.

## Contributing

If you have any improvements or feature suggestions, please open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy organizing! 📂✨
