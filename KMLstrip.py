import os           
  # 
  # KMLstrip
  # 
  # Author: Kai Zhuang
  # Date:    Dec 2020
  # 
  # 
  # Function   : Code striping 
  # 
  # Description: Attempts to strip most of the codes from a KML file leaving mostly text entries
  #               
  # 
  # Parameters : drectory              - monitoring directory for files 
  # 
  # Return     : output directory with respective files mostly striped of code
  # 
  # Examples of Usage: 
  # 
  #    set directory = '/home/kzhuang/Downloads/' with all KML files in the Downloads directory, script will then
  #    strip all files of code and output to output folder within downloads
  #    
  #           
  # 
  # 

directory = '/home/kzhuang/Downloads/'

#-----------------------------------should not need to modify past this line ------------------------------------
outdir = directory+'output/'
try:
    os.mkdir(outdir)
except OSError:
    print ("Creation of the directory %s failed" % outdir)
else:
    print ("Successfully created the directory %s " % outdir)
    
def main():
    for entry in os.scandir(directory):
        if (entry.path.endswith(".kml")) and entry.is_file():
            print(entry.path)
            filename=entry.path.lstrip(directory)
            filename=filename.rstrip(".kml")
            with open(entry.path, 'r') as infile, open(outdir+filename+'.txt', 'w') as outfile:
                for line in infile:
                    if "<description>" in line:
                        line=line.lstrip()
                        line=line.rstrip()
                        line=line.lstrip("<description>![CDATA[")
                        line=line.rstrip("</div>]]</description>")
                        #print(line)
                        outfile.write(line)
            infile.close()
            outfile.close()
            
main()            
