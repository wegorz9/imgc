# imgc — Bulk Image Format Converter

`imgc` is a bulk image format converter that can be used both from the **command line** and through a **graphical user interface (GUI)** built with **PyQt6**.  
It allows users to convert multiple image files from various formats into a single desired format, optionally filtering input types, defining output directories, and deleting originals after conversion.

---

## Features

- Convert multiple image files to a single target format (e.g., JPG → PNG, PNG → WEBP, etc.)
- Filter input image types (e.g., convert only `.jpg` and `.png`)
- Choose custom output directories for converted images
- Optionally delete original files after successful conversion
- Display supported image formats
- Includes a graphical user interface (GUI)

---

## Requirements

To build or run the project from source, ensure the following dependencies are installed:

```shell
pip install pillow pyqt6
```


Python 3.10 or newer is recommended for building the executable.

---

## Installation

After building or downloading the compiled binary, make sure `imgc` is in your system path.

If running from source, clone the repository and build it (for example, using PyInstaller):
```shell
git clone https://github.com/wegorz9/imgc.git
cd imgc
pyinstaller --onefile imgc.py
```

This will produce a standalone executable (`imgc` or `imgc.exe`).

---

## Command-Line Usage

imgc [desired format] [-o <output_directory>] [-f <filter>] [-d]


### Arguments and Options

| Argument | Description |
|-----------|--------------|
| `[desired format]` | Target image format (e.g., `jpg`, `png`, `webp`, `bmp`). |
| `-o <output_directory>` | Directory where converted images will be saved. Defaults to the current directory. |
| `-f <filter>` | Comma-separated list of input formats to convert (e.g., `-f jpg,png,gif`). |
| `-d` | Delete original images after successful conversion. |

---

## Example Commands

| Command | Description |
|----------|--------------|
| `imgc help` | Display detailed help information. |
| `imgc formats` | List all supported formats. |
| `imgc gui` | Launch the GUI application. |
| `imgc jpg` | Convert all supported images in the current directory to `.jpg`. |
| `imgc png -o converted` | Convert all supported images to `.png` and save them in the `converted` folder. |
| `imgc webp -f jpg,png -d` | Convert only `.jpg` and `.png` files to `.webp` and delete originals. |

---

## Graphical User Interface (GUI)

You can start the graphical interface with:
```shell
imgc gui
```

### GUI Features

- Choose source and destination directories
- Specify target format and filters interactively
- Enable or disable deletion of original files
- Simple layout built with PyQt6
- Automatically opens the output directory after conversion

---

## Supported Formats

`imgc` supports a wide range of image formats through the **Pillow** library, including:

BLP, BMP, BUFR, CUR, DCX, DDS, DIB, EPS, FITS, FLI, FPX, FTEX, GBR, GIF, GRIB,
HDF5, ICNS, ICO, IM, IPTC, JPEG, JPG, JPEG2000, MCIDAS, MIC, MPEG, MSP, PCD,
PCX, PIXAR, PNG, PPM, PSD, SGI, SPIDER, SUN, TGA, TIFF, WEBP, WMF, XBM, XPM


---

## Notes

- File names are preserved during conversion.  
- Subdirectories are not processed recursively (unless explicitly supported in future versions).  
- `JPG` and `JPEG` are treated as equivalent.

---

## Building the Executable

You can compile `imgc` into a standalone executable using **PyInstaller**:
```shell
pyinstaller --onefile imgc.py
```

This will create a binary under `dist/imgc` that can be run from the command line:

```shell
imgc help
```


---

## Author

**Wegorz9**  
[https://github.com/wegorz9](https://github.com/wegorz9)