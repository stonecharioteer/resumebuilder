ResumeBuilder
=====

I am creating this ResumeBuilder module to help people make a Resume
in various formats.

Ideally, this should fetch the data from a bunch of json files, and it should be able to build the resume in various formats:

1. Microsoft Word DocX format
   
   This is the basic format accepted by most job sites and portals.
   Most HR people seem to prefer this format.
2. Portable Document Format

   Ideal format for cross-platform compatibility.

3. HTML (as a webpage)
   
   For those who want to build a single-page application.
   I am not sure which I will use for this: Flask or Django. 

4. PNG (as an infographic) (Tentative)

   As an infographic, mostly. This is something I want to achieve
   personally. It will be interesting to see how I can manage the 
   various parts of the canvas without overlapping.

5. Open Document Format (odt) (Tentative)

   This is mostly to encourage the use of the ODF specification,
   and to make myself do something challenging.

----

Note:
----

I have hated making resumes my entire life. Not only are they a gross
understatement of someone's capacity for work, but they are also boring
to read. I have taken a handful of interviews myself and the resumes
that HR hands me are pretty pathetic. We need to move away from this 
format of enabling job searchers to lie. Resumes are just that, in my
opinion.

I do not perceive that this will be of much use to others, but I will try
to make it portable so others can utilize it as much as I plan to. It will
require a lot of work though, so I fail to see how it will help as opposed
to LinkedIn or Naukri.

Technical Stuff:
----

I plan on using the following:
   + python-pillow
   + python-openxml
   + pyPDF
   + reportlab (tentative, depends on license and watermarks)
   + matplotlib (Maybe for PDFs)

Help
----

For assistance, contact me at ktvkvinaykeerthi@gmail.com




