# ProcareDownloader

Procare downloader is a semi-automatic way to download images in bulk from Procare. 
If you are someone looking to bulk download pictures of your kid at preschool you can use this tool. 

# Dependencies

Install these deps to run the script

```
 pip install requests
 pip install bs4
 ```

# HowTo

On Procare dashboard navivate to photos and videos. Switch to weekly view. Scroll to load all the images. 
Now copy the html. 

1. Right click on the page with images. Inspect element. 
2. In developer tools right click on main HTML tag and edit as HTML.
3. Select all and save to text to disk. Note the path of the file.
4. Invoke the script from the directory you are downloading pictures too.

Pass the saved html as an argument to the script with the path. 

Example:

```
C:/Users/Rohit_Vaidya/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Users/Rohit_Vaidya/Downloads/projects/ProcareDownloader/downloader.py c://Users//Rohit_Vaidya//Downloads//Procare//photos.html
```