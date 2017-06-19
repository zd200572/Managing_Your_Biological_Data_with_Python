'''
===============================
draw a pic of protein domain
===============================
'''
from PIL import Image, ImageDraw

LENGTH = 536
SIZE = (600, 100)
DOMAIN1_start = 276
DOMAIN1_end = 284
DOMAIN2 = 298
DOMAIN3 = 389

SH3 = Image.new('RGB', SIZE, 'white')
d = ImageDraw.Draw(SH3)

def draw_domian(pic, DOMAIN1_start, DOMAIN1_end, DOMAIN2, DOMAIN3):
	'''
	the function is used to draw a domain with several arguments
	'''
	p1 = (66, 50)
	p2 = (536, 50)
	pic.line((p1, p2), fill = 'red', width = 10)
	t1 = DOMAIN1_start*470/536
	t2 = DOMAIN1_end*470/536
	box1 = (t1, 30, t2, 50)
	pic.rectangle(box1, fill = 'green')
	p3 = (DOMAIN2*470/536, 50)
	p3_ = (DOMAIN2*470/536, 30)
	p4 = (DOMAIN3*470/536, 50)
	p4_ = (DOMAIN3*470/536, 30)
	pic.line((p3, p3_), fill = 'blue', width = 3)
	pic.line((p4, p4_), fill = 'grey', width = 3)
	return pic


pic = draw_domian(d, DOMAIN1_start, DOMAIN1_end, DOMAIN2, DOMAIN3)
d.text((129, 30), "Nucleotide binding", fill=(0, 0, 0))
d.text((258, 60), "ATP binding", fill=(0, 0, 0))
d.text((329, 10), "Active Site", fill=(0, 0, 0))
SH3.save('domain.png')

