import os
import zipfile

PROJECT_FOLDER = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ZIP_PATH = os.path.join(
    PROJECT_FOLDER,
    "Mini_Courier_Planner_Submission.zip"
)

EXCLUDED_DIRS = {
    "__pycache__",
    ".git",
    "venv",
    ".venv"
}

EXCLUDED_EXTENSIONS = {".pyc"}

with zipfile.ZipFile(
    ZIP_PATH, "w", zipfile.ZIP_DEFLATED
) as zip_file:

    for root, dirs, files in os.walk(PROJECT_FOLDER):

        dirs[:] = [
            directory for directory in dirs
            if directory not in EXCLUDED_DIRS
        ]

        for file in files:

            if file.endswith(".pyc"):
                continue

            full_path = os.path.join(root, file)

            if full_path == ZIP_PATH:
                continue

            relative_path = os.path.relpath(
                full_path, PROJECT_FOLDER
            )

            zip_file.write(full_path, relative_path)

print("SUBMISSION ZIP CREATED SUCCESSFULLY!")
print("File:", ZIP_PATH)