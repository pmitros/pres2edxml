pres2edxml
==========

Convert a presentation to edXML for embedding in an edX course. Run: 

  python convert.py presentation.pdf course_dir

If a course directory by the name 'course_dir' does not exist, it will
create it. It will extract all of the slides from presentation.pdf
into images, and create a learning sequence where each element has one
image.
