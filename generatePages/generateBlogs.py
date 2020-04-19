import os
from blogs import datasets

startComment = "START AUTO-INSERT DATASETS"
endComment = "END AUTO-INSERT DATASETS"
pageToChange = "../blogs.html"
tempfile = 'blogs.temp'

def updatePage():
  with open(pageToChange,'r') as file:
    orgLines = file.readlines()

  with open(pageToChange,'w') as file:
    write = True
    for x in orgLines:
      if endComment in x:
        write = True
        file.write('\n')
      if write:
        file.write(x)
      if startComment in x:
        with open(tempfile,'r') as temp:
          add = temp.read()
        file.write(add)
        write = False

with open(tempfile, 'w') as f:
  for ds in datasets:
    print("Adding dataset for "+ds["Title"])
    f.write("\n")
    f.write('''
                            <article>
                              <div class="wrapper">
                                <div class="blog">
                                  <div class="blog__image">
                                    <img src="images/'''+ds["ImageName"]+'''" alt="" />
                                  </div>
                                  <div class="blog__author">'''+ds["Author"]+" | "+ds["Date"]+'''</div>
                                  <div class="blog__unit-name">'''+ds["Title"]+'''</div>
                                  <div class="blog__unit-description">
                                    '''+ds["Description"]+'''
                                  </div>
                                  <a target="_blank" href="'''+ds["Link"]+'''" class="button purple small">Read more</a>
                              </div> <!-- end wrapper -->
                          </article>
              ''')
updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                