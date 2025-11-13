import os
import sys

from PIL import Image
from PyQt6 import QtWidgets

from layout import Ui_MainWindow


class InvalidArguments(Exception):
    pass


class ImgC:
    def __init__(self, argv: list[str]):
        self.HELP_TEXT = """imgc - Bulk image format converter
----------------------------------

imgc is a command-line utility for bulk converting images from multiple formats 
into a single desired format. It supports filtering input types, specifying an 
output directory, and optionally deleting the original images after conversion.

USAGE:
    imgc help
        Show this help message and exit.

    imgc formats
        Display all supported input and output image formats.
        
    imgc gui
        Open a GUI

    imgc [desired format] [-o <output_directory>] [-f <filter>] [-d] [-t <size_x,size_y>]
        Convert all matching images in the current directory (and optionally 
        subdirectories, if supported) to the specified format.

ARGUMENTS:
    [desired format]
        The target image format to convert to (e.g., jpg, png, webp, bmp).

OPTIONS:
    -o <output_directory>
        Specify the directory where converted images will be saved.
        If not provided, converted images are saved in the current directory.

    -f <filter>
        Comma-separated list of image formats to convert. Only images matching 
        these formats will be processed.
        Example: -f jpg,png,gif

    -d
        Delete original images after successful conversion.
    
    -t <size_x,size_y>
        Transform the images to a desired size.
        Example: -t 256,256

EXAMPLES:
    imgc help
        Show detailed help information.
    
    imgc gui 
        Open a window with a gui

    imgc formats
        List all supported formats (e.g., jpg, png, bmp, gif, webp, tiff).

    imgc jpg
        Convert all supported images in the current directory to .jpg format.

    imgc png -o converted
        Convert all supported images to .png and save them in the "converted" folder.
    
    imgc bmp -t 256,512
        Convert all supported images to .bmp and resize them to 256 pixels by 512 pixels.

    imgc webp -f jpg,png -d
        Convert only .jpg and .png images to .webp, and delete the originals afterward.

NOTES:
    - The utility preserves file names during conversion.
    - Subdirectories are not processed unless explicitly supported by your version.
    - Supported formats can be checked via `imgc formats`."""
        self.SUPPORTED_FORMATS = [
            'BLP', 'BMP', 'BUFR', 'CUR', 'DCX', 'DDS', 'DIB', 'EPS',
            'FITS', 'FLI', 'FPX', 'FTEX', 'GBR', 'GIF', 'GRIB', 'HDF5',
            'ICNS', 'ICO', 'IM', 'IPTC', 'JPEG', 'JPG', 'JPEG2000', 'MCIDAS',
            'MIC', 'MPEG', 'MSP', 'PCD', 'PCX', 'PIXAR', 'PNG', 'PPM',
            'PSD', 'SGI', 'SPIDER', 'SUN', 'TGA', 'TIFF', 'WEBP', 'WMF',
            'XBM', 'XPM'
        ]

        self.pwd: str | os.path = "."
        self.format: str = ""

        self.output_dir: str | os.path = "."
        self.filter: None | list = None
        self.delete: bool = False
        self.transform: None | tuple(int, int) = None

        self.parse_args(argv)

    def parse_args(self, args):

        if len(args) < 2:
            print("To see the help screen, run imgc help")
            self.dialogue()
            return

        self.format = args[1]
        while len(args) > 2:
            if args[2] == "-o":
                self.output_dir = args[3]
                args.remove(args[3])
                args.remove(args[2])
            elif args[2] == "-f":
                self.set_filter(args[3].split(","))

                args.remove(args[3])
                args.remove(args[2])
            elif args[2] == "-d":
                self.delete = True
                args.remove(args[2])
            elif args[2] == "-t":
                self.transform = tuple(map(int, args[3].split(",")))
                args.remove(args[3])
                args.remove(args[2])
            else:
                print("Invalid arguments supplied.")
                exit(1)

    def set_filter(self, filter_list: list | None):
        if filter_list is None:
            self.filter = None
            return
        self.filter = list(map(lambda s: s.upper(), filter_list))
        if "JPG" in self.filter:
            self.filter.remove("JPG")
            self.filter.append("JPEG")

    def convert(self):
        file_names = os.listdir(self.pwd)
        file_names = list(map(lambda f: os.path.abspath(os.path.join(self.pwd, f)), file_names))
        filtered_file_names = []
        for file_name in file_names:
            if os.path.isdir(file_name):
                continue
            fn, ext = os.path.splitext(file_name)
            ext = ext.removeprefix(".")
            if ext.upper() not in self.SUPPORTED_FORMATS:
                continue

            with Image.open(file_name) as fp:
                if self.filter is None:
                    filtered_file_names.append(file_name)
                    continue
                elif fp.format in self.filter:
                    filtered_file_names.append(file_name)

        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        for file_name in filtered_file_names:
            fn, ext = os.path.splitext(file_name)

            ext = ext.removeprefix(".")
            if ext != self.format.lower():
                try:
                    with Image.open(file_name) as fp:
                        if self.transform is not None:
                            fp = fp.resize(self.transform, Image.Resampling.BOX)
                        fp.save(os.path.join(self.output_dir, os.path.basename(fn) + "." + self.format.lower()))
                    if self.delete:
                        os.remove(file_name)
                except IOError as e:
                    print(f"Couldn't convert {file_name}")

    def gui(self):
        app = QtWidgets.QApplication(sys.argv)
        gui = ImgGUI(self)
        sys.exit(app.exec())

    def exec(self):
        if self.format == "formats":
            print(self.SUPPORTED_FORMATS)
        elif self.format == "help":
            print(self.HELP_TEXT)
        elif self.format == "gui":
            self.gui()
        else:
            self.convert()

    def dialogue(self):
        print("Supply values for the following parameters:")
        self.format = input("Format: ").upper()
        if self.format not in self.SUPPORTED_FORMATS:
            self.format = input("Incorrect format supplied. See supported formats using `imgc formats`.").upper()

        self.output_dir = input("Output path: ")
        if self.output_dir.strip() == "":
            self.output_dir = "."
        self.set_filter(input("Filters (comma separated): ").split(","))
        self.delete = input("Should original images be deleted? [Y/n]") == "Y"


class ImgGUI(QtWidgets.QMainWindow):
    def __init__(self, parent_object: ImgC):
        super().__init__()
        self.parent_object = parent_object
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pwdEdit.setText(os.path.abspath(parent_object.pwd))

        self.ui.folderPicker.clicked.connect(self.pick_folder)
        self.ui.pwdPicker.clicked.connect(self.pick_pwd)
        self.ui.convertButton.clicked.connect(self.convert)

        self.show()

    def pick_pwd(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select the folder to convert images from",
                                                            os.path.abspath(self.parent_object.pwd))
        self.ui.pwdEdit.setText(folder)

    def pick_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select the folder to save images in",
                                                            os.path.abspath(self.parent_object.pwd))
        self.ui.pathEdit.setText(folder)

    def convert(self):
        if self.ui.filterEdit.text().strip() == "":
            self.parent_object.set_filter(None)
        else:
            self.parent_object.set_filter(self.ui.filterEdit.text().split(self.ui.separatorEdit.text()))
        self.parent_object.pwd = self.ui.pwdEdit.text()
        self.parent_object.format = self.ui.formatEdit.text()
        self.parent_object.delete = self.ui.deleteChackBox.isChecked()
        self.parent_object.output_dir = self.ui.pathEdit.text()

        self.parent_object.convert()

        os.startfile(os.path.abspath(self.parent_object.output_dir))


if __name__ == '__main__':
    imgc = ImgC(sys.argv)
    imgc.exec()
