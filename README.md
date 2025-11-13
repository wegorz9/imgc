# imgc — Bulk Image Format Converter

`imgc` is a bulk image format converter that can be used both from the **command line** and through a **graphical user interface (GUI)** built with **PyQt6**.  
It allows users to convert multiple image files from various formats into a single desired format, optionally filtering input types, defining output directories, resizing images, and deleting originals after conversion.

---

## Features

- Convert multiple image files to a single target format (e.g., JPG → PNG, PNG → WEBP, etc.)
- Filter specific input image types before conversion (e.g., only `.jpg` and `.png`)
- Resize or transform images to a specific resolution
- Choose custom output directories for converted images
- Optionally delete original files after successful conversion
- Display supported image formats
- Includes an interactive graphical user interface (GUI)

---

## Requirements

To build or run the project from source, ensure the following dependencies are installed:

```shell
pip install pillow pyqt6
```

Python **3.10+** is recommended.

---

## Installation

After building or downloading the compiled binary, make sure `imgc` is in your system path.

If running from source, clone the repository and build it manually (for example, using PyInstaller):

```shell
git clone https://github.com/wegorz9/imgc.git
cd imgc
pyinstaller --onefile imgc.py
```

This will produce a standalone executable (`imgc` or `imgc.exe`).

---

## Command-Line Usage

```shell
imgc [desired format] [-o <output_directory>] [-f <filter>] [-d] [-t <size_x,size_y>]
```

### Arguments and Options

| Argument | Description |
|-----------|--------------|
| `[desired format]` | Target image format (e.g., `jpg`, `png`, `webp`, `bmp`). |
| `-o <output_directory>` | Directory where converted images will be saved. Defaults to the current directory. |
| `-f <filter>` | Comma-separated list of input formats to convert (e.g., `-f jpg,png,gif`). |
| `-d` | Delete original images after successful conversion. |
| `-t <size_x,size_y>` | Resize each converted image to the specified width and height (e.g., `-t 256,256`). |

---

## Example Commands

| Command | Description |
|----------|--------------|
| `imgc help` | Display detailed help information. |
| `imgc formats` | List all supported formats. |
| `imgc gui` | Launch the graphical user interface. |
| `imgc jpg` | Convert all supported images in the current directory to `.jpg`. |
| `imgc png -o converted` | Convert all supported images to `.png` and save them in the `converted` folder. |
| `imgc webp -f jpg,png -d` | Convert only `.jpg` and `.png` files to `.webp` and delete originals. |
| `imgc bmp -t 512,256` | Convert all supported images to `.bmp` and resize them to 512×256 pixels. |

---

## Graphical User Interface (GUI)

You can launch the graphical interface using:

```shell
imgc gui
```

### GUI Features

- Choose input and output directories via file pickers  
- Specify target format, filters, and resizing options  
- Enable or disable deletion of original files  
- Built with **PyQt6** and includes an intuitive layout  
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
- Subdirectories are not processed recursively (unless supported in future versions).  
- `JPG` and `JPEG` are treated as equivalent.  
- When resizing (`-t`), images are resampled using `Image.Resampling.BOX`.  

---

## Building the Executable

You can compile `imgc` into a standalone executable using **PyInstaller**:

```shell
pyinstaller --onefile imgc.py
```

This will create a binary under `dist/imgc` that can be run directly from the command line:

```shell
imgc help
```

---

## Author

**Wegorz9**  
[https://github.com/wegorz9](https://github.com/wegorz9)
