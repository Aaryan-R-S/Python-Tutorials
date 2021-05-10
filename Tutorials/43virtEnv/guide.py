'''
 -- Make required Folder & open Integrated CMD in it !


    In CMD type : 
    [To make exact copy of system base python but no modules included!]
 -- pip install virtualenv
 -- virtualenv [nameOfSubFolderInRequiredFolder]   // Here I used VirtualEnvironment
    
    --OR--

    To make exact copy of system base python[with Modules] :
 -- virtualenv --system-site-packages [nameOfSubFolderInRequiredFolder]  // Here I used VirtualEnvironment



    To activate :
 -- .\[nameOfSubFolderInRequiredFolder]\Scripts\activate   // Here I used VirtualEnvironment

    To deactivate :
 -- deactivate

    To get guide in Virtual Environment :
 -- pip freeze > requirements.txt

    To install modules mentioned in requirements.txt :
 -- pip install -r .\requirements.txt

'''