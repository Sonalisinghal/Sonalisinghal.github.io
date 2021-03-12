import os
from pages import pagelist
startComment = "START AUTO-INSERT FOOTER"
endComment = "END AUTO-INSERT FOOTER"
tempfile = 'nav.temp'


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
					<footer id="footer">
						<div class="inner">
							<section>
								<h2>Get in touch</h2>
								<ul class="icons">
									<li><a target="_blank" href="https://github.com/Sonalisinghal" class="icon brands style2 fa-github"><span class="label">GitHub</span></a></li>
								</ul>
							</section>
							<ul class="copyright">
								<li>Made by Sonali Singhal</li><li>Design: <a href="http://html5up.net">HTML5 UP - Phantom</a></li>
							</ul>
						</div>
					</footer>''')
for pageToChange in pagelist:
  updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                