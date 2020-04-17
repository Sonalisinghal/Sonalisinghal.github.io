import os

startComment = "START AUTO-INSERT NAVBAR"
endComment = "END AUTO-INSERT NAVBAR"
tempfile = 'nav.temp'

pagelist=["../opensource.html","../index.html","../competitiveprogramming.html","../blogs.html","../courses.html","../developerclubs.html","../elements.html","../internships.html","../research.html","../scholarships.html","../contribute.html"]
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
    f.write('''
          <nav id="menu">
            <h2>Menu</h2>
            <br>
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><a href="courses.html">Courses</a></li>
              <li><a href="scholarships.html">Scholarships</a></li>
              <li><a href="opensource.html">Open Source</a></li>
              <li><a href="competitiveprogramming.html">Competitive Programming</a></li>
              <li><a href="developerclubs.html">Developer Clubs and Communities</a></li>
              <li><a href="internships.html">Internships</a></li>
              <!--<li><a href="research.html">Research</a></li> -->
              <li><a href="blogs.html">Blogs and Videos</a></li>
              <li><a href="contribute.html">Contribute</a></li>
              <!-- <li><a href="elements.html">Elements</a></li> -->
            </ul>
          </nav>''')
for pageToChange in pagelist:
  updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                