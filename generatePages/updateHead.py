import os

startComment = "START AUTO-INSERT HEAD"
endComment = "END AUTO-INSERT HEAD"
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
	<head>
		<!-- Global site tag (gtag.js) - Google Analytics -->
		<script async src="https://www.googletagmanager.com/gtag/js?id=UA-163863206-1"></script>
		<script>
		  window.dataLayer = window.dataLayer || [];
		  function gtag(){dataLayer.push(arguments);}
		  gtag('js', new Date());

		  gtag('config', 'UA-163863206-1');
		</script>
		<title>TechHelpher</title>
		<meta name=”Description” content="All STEM opportunities at one place. Tips on how to get started, links and tentative dates of most famous computer science opportunities available for women.">
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<meta property="og:url" content="http://techhelpher.me">
		<meta property="og:title" content="TechHelpher">
		<meta property="og:image" content="http://techhelpher.me/images/techhelpher.png">
		<meta property="og:image:type" content="image/png">
		<meta property="og:image:width" content="400">
		<meta property="og:image:height" content="230">
		<meta property="og:type" content="website">
		<meta property="og:description" content="All STEM opportunities at one place. Tips on how to get started, links and tentative dates of most famous computer science opportunities available for women.">
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
		<link rel="icon" type="image/svg" href="images/favicon.svg">
	</head>''')
for pageToChange in pagelist:
  updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                