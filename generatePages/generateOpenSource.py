import os
from opensource import datasets

startComment = "START AUTO-INSERT DATASETS"
endComment = "END AUTO-INSERT DATASETS"
pageToChange = "../opensource.html"
tempfile = 'opensource.temp'

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
    print("Adding dataset for "+ds["Contest"])
    f.write("\n")
    f.write('''
              <div class="spotlight">
                  <div class="content">                       
                    <h2>'''+ds["Contest"]+'''</h2>
                    <p>'''+ds['About']+'''</p>
                    <h6><b>Applications Open: </b>'''+ds['Applications Open']+'''</h6>
                    <h6><b>Applications Close : </b>'''+ds["Last Date to Apply"]+'''</h6>
                    <h6><b>Eligibiblity: </b>'''+ds['Eligibility']+'''</h6>
                    <h6><b>Stipend: </b>'''+ds['Stipend']+'''</h6>
                    <ul class="actions">
                      <li><a target="_blank" href="'''+ds['Link']+'''" class="button">Learn More</a></li>
                    </ul>
                  </div>
                  <span class="image"><img src="images/'''+ds['Imagename']+'''" alt="" /></span>
                </div>
                <hr>''')
updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                