# Certificate Finder

## Inspiration

The original intention of the certificate finder was to provide your DARS degree audit as a pdf.
It would then be parsed to get the list of all your completed courses. This list would then be
compared with a dataset of all the certificates offered at UW Madison, and it would tell you which
certificates you could get, how far away from them you were, etc.

## Challenges

The main challege we faced was trying to scrape the UW Madison Guide website to obtain info on all
the courses needed for the 102 certificates offered at UW Madison. This turned out to be too large
of a problem for the scope of this hackathon, so we narrowed the project scope to only include the
Data Science certificate. This way we show proof of concept, without needing to create a program
that automatically collects all the certificate info.

## Result

Our project presents a web interface that allows a user to input their DARS pdf file. It then parses
this file to create a list of all completed courses. It then compares it to the requirements for the
Data Science certificate, and tells you how far away from obtaining the certificate you are.

## Extensions

This project could be extended first and foremost by increasing the dataset to include information
for all the certificates offered at UW Madison. This would turn it from an interesting idea to a
useful tool that could be used by students. On top of that, we could improve the storage of
certificate data. Each certificate has some courses which are required, some which are optional,
some groups of courses of which you are required to take a certain number of credits, total credit
requirements, minimum gpa requirements and more. All these factors play into whether or not you can
obtain the certificate, and we could improve our algorithm to more accurately recognize, classify,
and interpret them.