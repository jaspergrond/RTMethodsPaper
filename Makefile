#TeX Makefile
FILE=RTMethodsPaper

$(FILE).pdf: $(FILE).tex *.tex
	pdflatex $(FILE)
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)

clean:
	\rm *.aux *.blg *.out *.bbl *.log *.toc
