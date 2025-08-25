'''
Author Notes:
While searching for ways of doing this challenge in the documentation, I tried to check what would be the more simple way of doing it. After checking the results from the instructor,
I found that this maybe was not the right way to go. His solution looks more complex, but in the end it is more robust without much more code to it.

Briefing:
Write a python function to build a zip archive.
Input:
    - Directory path
    - List of file extensions
    - Output file path

Output:
    - a ZIP file

ZIP archive should maintain the folder structure

How it should look like:
>>> zip_all('.\\my_stuff',['.jpg','.txt'],'my_stuff.zip')

Documentation source:
https://docs.python.org/3/library/zipfile.html
https://janakiev.com/blog/python-filesystem-analysis/
https://docs.python.org/3/library/pathlib.html
https://peps.python.org/pep-0428/

'''
from zipfile import ZipFile
from pathlib import Path

def zip_all(directory_path,file_extensions,output_path):

    #Create a zip file
    with ZipFile(output_path, 'w') as  z:
    
        #Walk through all the folders and retrive the files that match the file types list.
        path = Path(directory_path)
        normalized_exts = [ext.casefold() for ext in file_extensions]

        for file in path.glob('**/*.*'):
            if file.suffix.casefold() in normalized_exts:

                #And add each one to the zip file
                z.write(file, arcname=file.relative_to(path))

# Please, uncomment the line below to execute the code with the example given
# zip_all('./zip',['.txt','.jpg'],'./zip/myfiles.zip')