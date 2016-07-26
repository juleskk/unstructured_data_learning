
# coding: utf-8

# Download and Extract Emails from WSJ
# http://graphics.wsj.com/hillary-clinton-email-documents/

# Valuable resource for learning / getting started
# https://github.com/benhamner/hillary-clinton-emails


from urllib2 import urlopen
from zipfile import ZipFile
from subprocess import call
import os
import re


def get_raw_emails(zip_name):
    
    print "Downloading " + zip_name + " ... "
    zipurl = 'http://graphics.wsj.com/hillary-clinton-email-documents/zips/' + zip_name
    # Download the file from the URL
    zipresp = urlopen(zipurl)
    # Create a new file on the hard drive
    tempzip = open("C:\\users\\drew_\\documents\\HRC_Emails\\" + zip_name, "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
    # Close the newly-created file
    tempzip.close()
    # Re-open the newly-created file with ZipFile()
    zf = ZipFile("C:\\users\\drew_\\documents\\HRC_Emails\\" + zip_name)
    # Extract its contents into folder
    # note that extractall will automatically create the path
    print "Extracting " + zip_name + " ... "
    zf.extractall(path = 'C:\\users\\drew_\\documents\\HRC_Emails\\raw\\')
    # close the ZipFile instance
    zf.close()
    print "Complete"
    
get_raw_emails("HRC_Email_296.zip")
get_raw_emails("HRCEmail_JuneWeb.zip")
get_raw_emails("HRCEmail_JulyWeb.zip")
get_raw_emails("Clinton_Email_August_Release.zip")
get_raw_emails("HRCEmail_SeptemberWeb.zip")
get_raw_emails("HRCEmail_OctWeb.zip")
get_raw_emails("HRCEmail_NovWeb.zip")
get_raw_emails("HRCEmail_Jan7thWeb.zip")
get_raw_emails("HRCEmail_Jan29thWeb.zip")
get_raw_emails("HRCEmail_Feb13thWeb.zip")
get_raw_emails("HRCEmail_Feb19thWeb.zip")
get_raw_emails("HRCEmail_Feb29thWeb.zip")

print "*****ALL FILES DOWNLOADED AND EXTRACTED!*****"

x = 0
for subdir, dirs, files in os.walk("C:\\Users\\drew_\\Documents\\HRC_Emails\\raw"):
    newdir = "C:\\Users\\drew_\\Documents\\HRC_Emails\\text"
    #print newdir
    print "Running PDF to text conversion..."
    for filename in files:
        filepath = os.path.join(subdir, filename)
        newfile = os.path.join(newdir, os.path.splitext(filename)[0]+".txt")
        #print filepath, newfile
        
        call(["pdftotext",
            "-raw", 
            filepath, 
            newfile], shell=True)
        
        x += 1
        if x % 1000 == 0:
            print "Converted ", x, " emails to text..."
            
print "*****COMPLETE!*****"
print "Total converted: ", x


x = 0
pattern = re.compile(r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+')
for subdir, dirs, files in os.walk("C:\\Users\\drew_\\Documents\\HRC_Emails\\text"):
    newdir = "C:\\Users\\drew_\\Documents\\HRC_Emails\\lookups"
    print "Running regex extraction..."
    for filename in files:
        input_file = os.path.join(subdir, filename)
        output_file = os.path.join(newdir, filename)
        if not input_file.endswith(".txt"):
            raise Exception("Unexpected file path: %s" % os.path.join(subdir, filename))
        raw_text = open(input_file).read()
        
        for email in re.findall(pattern, raw_text):
            print email
         
        x += 1 
        if x == 30:
            break
            

