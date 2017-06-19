'''

Paste a small image into a big one.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from PIL import Image

size = (4500, 2800)
image1 = Image.open('boxplot.png', 'r')
image2 = Image.open('fasta_length_histgram.png', 'r')
image3 = Image.open('plot_of_ATGU.png', 'r')
image4 = Image.open('neuron.png', 'r')
i = Image.new('RGB', size, 'white')
i.paste(image1, (-200, 36))
i.paste(image2, (2260, 1390))
i.paste(image3, (100, 1390))
i.paste(image4, (2260, -100))
i.save('combined.png')
