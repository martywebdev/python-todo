import zipfile
import pathlib

def make_archive(filepaths, destination):
    destination_path = pathlib.Path(destination, 'compressed.zip')
    with zipfile.ZipFile(destination_path, 'w') as f:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            f.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    pass