all: english spanish clean-temp

spanish: spanish.pdf

english: english.pdf

english.pdf: output/english.tex
	pdflatex output/english.tex

spanish.pdf: output/spanish.tex
	pdflatex output/spanish.tex

output/english.tex: data/data.json process.py
	python3 process.py

output/spanish.tex: data/data.json process.py
	python3 process.py

.PHONY: clean-temp
clean-temp:
	rm -f *.aux *.bak* *.log *.out

.PHONY: clean
clean: clean-temp
	rm -f *.pdf