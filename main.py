# pip install rembg[gpu]
# copy model u2net.onnx from https://github.com/danielgatis/rembg to .u2net folder in user's home folder
from rembg import remove
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_extensions = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(
            Path('/home/oleg/Python/Practice/Python_Today/Remove_Background_231022/input_imgs').glob(ext))

    # print([item.stem for item in all_files])

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'/home/oleg/Python/Practice/Python_Today/Remove_Background_231022/output_imgs/{file_name}_output.png'

        # print(output_path)
        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1}/{len(all_files)}')


def main():
    remove_bg()


if __name__ == '__main__':
    main()
