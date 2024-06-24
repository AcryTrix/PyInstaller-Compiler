import subprocess
import os

def get_user_input(prompt):
    return input(prompt)

def main():
    file_path = get_user_input("Enter the full file path of the Python script: ")
    icon_path = get_user_input("Enter the full path of the desired icon file (.ico): ")
    output_name = get_user_input("Enter the desired name for the compiled application: ")

    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return
    
    if not os.path.isfile(icon_path):
        print(f"Error: The icon file '{icon_path}' does not exist.")
        return

    command = [
        'pyinstaller',
        '--onefile',
        '--name', output_name,
        '--icon', icon_path,
        file_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully compiled {file_path} into {output_name}.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()