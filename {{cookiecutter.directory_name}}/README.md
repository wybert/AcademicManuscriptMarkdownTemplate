Template for writing a PhD thesis or academic manuscript in Markdown.


# What is this ?


This repository provides a framework for writing a PhD thesis and academic manuscript in Markdown.

This template does not contain work related to formatting documents. This template provides a directory for easy organization and use of markdown academic writing.

The template can finally output a `doc` file, which is convenient for using the doc file for the final format work.



# How is the template organised?

```bash
.
├── bibtexAndCSL  (bibtex and csl files)
├── createFilesBasedOntemplate.py (python script to generate manuscript files based on outline)
├── drafts (markdown drafts)
├── figs (figs used in markdown)
├── make.bat (cat the chapters to one manuscript file, work in windows)
├── make.sh (cat the chapters to one manuscript file, work in linux)
├── outlines ( outline files )
│   ├── academicManuscriptOutlineTemplate.yml 
│   └── PHDThesisOutlineTemplate.yml
├── output (one markdown manuscript file and built doc file here)
├── readMe.md
├── references (pdf files you want reference when you are writing )
├── ReviseAndPublishingCycle (revise the drafts based on the opinions of the    
                                      instructor or editor )
├── reports ( sliders here )
└── styles (style files when you want style your document when building)
```


# How do I get started?

1. Install the following software:

- A text editor, like Sublime, which is what you'll use write the thesis.
- A LaTeX distribution (for example, MacTeX for Mac users).
- Pandoc, for converting the Markdown to the output format of your choice. 
- You may also need to install [Pandoc cite-proc](https://github.com/jgm/pandoc-citeproc) to create the bibliography.
- Install [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) for cross-references for figures, tables, equations.
- Install 
- Git, for version control.
  
2. Fork the repository on Github

3. Clone the repository onto your local computer (or download the Zip file).

4. Navigate to the directory that contains the Makefile and type the following two command at the command line to update the Doc or PDF in the output directory.

```bash
cat drafts/*.md > output/out.md

```

Doc
```bash
pandoc -s -f markdown -t docx --filter=pandoc-crossref --resource-path=figs --filter=pandoc-citeproc --bibliography=my.bib --csl=chinese-gb7714-2005-numeric.csl output/out.md -o out/out.docx
```

PDF
```bash
pandoc -s -f markdown --pdf-engine=xelatex -V CJKmainfont='WenQuanYi Micro Hei Mono'  --filter=pandoc-crossref --resource-path=figs --filter=pandoc-citeproc --bibliography=my.bib --csl=chinese-gb7714-2005-numeric.csl output/out.md -o out/out.pdf
```


5. Edit the files in the 'source' directory, then goto step 4.




# Contributing

Contributions to the template are encouraged! There are lots of things that could be improved, like:



Please fork and edit the project, then send a pull request.



