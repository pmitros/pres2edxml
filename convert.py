import sys
import wand
import wand.image
import os.path
import os

input = sys.argv[1]
output = sys.argv[2]
filebase = os.path.splitext(os.path.basename(output))[0] # "/foo/bar.pdf" ==> "bar"
image_dir = os.path.join(output, "static", filebase)
sequence_dir = os.path.join(output, "sequential")

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

if not os.path.exists(sequence_dir):
    os.makedirs(sequence_dir)

image_pdf = wand.image.Image(filename=input)
image_jpeg = image_pdf.convert('png')
image_jpeg.save(filename=os.path.join(image_dir, 'slide.png'))

f = open(os.path.join(sequence_dir, filebase)+".xml", "w")

f.write('<sequential display_name="{name}">'.format(name=filebase))
for fn in sorted(os.listdir(image_dir)):
    f.write('<html><img src="/static/{pres}/{file}"/></html>'.format(pres=filebase, file=fn))
f.write("</sequential>")


cxml = os.path.join(output, "course.xml")
if not os.path.exists(cxml):
    fc = open(cxml, "w")
    fc.write('<course name="{basename}" url_name="{basename}"><chapter name="{basename}" url_name="{basename}"><sequential url_name="{basename}" /></chapter></course>'.format(basename=filebase))
    fc.close()
else: 
    print "Conversion done! Be sure to add the {basename} to course.xml".format(basename=filebase)
