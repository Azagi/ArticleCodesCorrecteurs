help:
	@echo "Usage: make [target]"
	@echo "Available targets:"
	@echo "  clean  Clean the build direcory"
	@echo "  pdf    Build the pdf file"

clean:
	rm -f *.{ps,aux,out,pdf,log,dvi,bbl,blg,toc,bcf,run.xml}

%.dvi: %.tex
	latex $<
	bibtex $(basename $<) || true
	latex $<
	latex $<

%.ps: %.dvi
	dvips -t unknown $< -o

%.pdf: %.ps
	ps2pdf $<

pdf: article.pdf
