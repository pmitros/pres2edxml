pres2edxml
==========

Convert a presentation to edXML for embedding in an edX course. Run: 

  python convert.py presentation.pdf course_dir

If a course directory by the name 'course_dir' does not exist, it will
create it. It will extract all of the slides from presentation.pdf
into images, and create a learning sequence where each element has one
image, corresponding to that slide.

Useful potential future steps: 

1. edX has a massive number of names. Provide useful names (e.g. for tooltips, etc.)
2. Support Google Docs. This could work through the Google Docs API
3. Support ODP presentations. This could be done through unoconv. 
4. Support PPT presentations. This could be done through convertapi.com
