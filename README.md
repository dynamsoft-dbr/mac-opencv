# OpenCV-dependent Python Barcode Reader for macOS

The sample shows how to use OpenCV and [Dynamsoft Barcode Reader SDK][0] to build a Python barcode reader for macOS.

## System Information
Check macOS system version:

```
sw_vers
```

>- ProductName:    Mac OS X
>- ProductVersion: 10.11.1
>- BuildVersion:   15B42

## Download & Installation
* OpenCV

    ```bash
    brew update
    brew tap homebrew/science
    brew install opencv3
    ```
* [Dynamsoft Barcode Reader][1]. Extract the package to get include and lib folders.

## Build and Run
1. Copy include and lib folders to the project.
2. Build Python extension:

    ```bash
    python setup.py build install
    ```
3. Run the app:

    ```bash
    python test.py ./Codabar.jpg
    ```

[0]:http://www.dynamsoft.com/Products/Dynamic-Barcode-Reader.aspx 
[1]:https://www.dynamsoft.com/Downloads/DownloadLog.aspx?server=1&product=Barcode/DBR-Libs.zip
