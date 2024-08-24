# ProcareDownloader

Procare downloader is a semi-automatic way to download images in bulk from Procare. 
If you are someone looking to bulk download pictures of your kid at preschool you can use this tool. 

# Windows and Mac Executable
- Windows users: [Download](https://github.com/rohitvvv/ProcareDownloader/releases/tag/WindowsBinary) Windows executable and skip to HowTo 
- Mac users: [Download](https://github.com/rohitvvv/ProcareDownloader/releases/download/WindowsBinary/ProcareDownloader-mac.zip) Mac executable and skip to HowTo 

# Dependencies (For Linux users, if executables don't work for you)

You need Python 3 installed on your machine to use the script. 
Install these deps to run the script.

```
 pip install requests
 pip install bs4
 ```

# HowTo

On Procare dashboard navigate to photos and videos. Switch to weekly view. Scroll down to load all the images. 
Now copy the html. Follow the steps below to copy the HTML. 

1. Right click on the page with images. Select Inspect. 
2. In developer tools right click on main HTML tag and edit as HTML.
3. Select all and save to text to disk. Note the path of the file.
4. Invoke the script from the directory you are downloading pictures too.

*Skip to demo if you don't follow.*

Pass the saved html as an argument to the script with the path. 

Example:

```
C:/Users/Rohit_Vaidya/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Users/Rohit_Vaidya/Downloads/projects/ProcareDownloader/downloader.py c://Users//Rohit_Vaidya//Downloads//Procare//photos.html
```
# Demo

![Demo](https://github.com/rohitvvv/ProcareDownloader/blob/main/Demo.gif)