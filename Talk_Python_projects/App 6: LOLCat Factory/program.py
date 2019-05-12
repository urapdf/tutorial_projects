import os
import cat_service
import subprocess
import platform



def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('=========================')
    print('       Cat Factory       ')
    print('=========================')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'LOL_cat_pictures'
    full_path = os.path.join(base_folder, folder)
    # full_path = os.path.abspath(os.path.join('.',folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1,cat_count +1):
        name = 'lolcat{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder,name)

    print('done with downloading')

def display_cats(folder):
    # open folder
    print('Displaying cat in os window')
    if platform.system() == 'Darwin':
        subprocess.call(['open',folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer',folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open',folder])
    else:
        print("We do not support your os: " + platform.system())

if __name__ == '__main__':
    main()
