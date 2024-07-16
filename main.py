from rembg import remove, new_session
from PIL import Image
from pathlib import Path


def remove_background():
    session = new_session('isnet-anime')
    list_of_extension = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extension:
        all_files.extend(Path('D://MyProgramm//ADMIN MODE//input_img').glob(ext))

    # print(all_files)

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'D://MyProgramm//ADMIN MODE//output_img//{file_name}_out.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img, session=session)
        output_img.save(output_path)

        print(f'Complete: {index + 1}/{len(all_files)}')


def main():
    remove_background()


if __name__ == '__main__':
    main()
