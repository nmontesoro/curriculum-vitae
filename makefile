COMMON = cv.tex data/common/photo.png

ROOT-SP = data/sp
DATA-SP = $(ROOT-SP)/personal-info.csv $(ROOT-SP)/education.csv $(ROOT-SP)/work-experience.csv $(ROOT-SP)/skills.csv

ROOT-EN = data/en
DATA-EN = $(ROOT-EN)/personal-info.csv $(ROOT-EN)/education.csv $(ROOT-EN)/work-experience.csv $(ROOT-EN)/skills.csv

all: spanish english clean-aux

.PHONY: spanish
spanish: spanish.pdf

.PHONY: english
english: english.pdf

spanish.pdf: $(COMMON) $(DATA-SP)
	pdflatex spanish.tex

english.pdf: $(COMMON) $(DATA-EN)
	pdflatex english.tex

.PHONY: clean-aux
clean-aux:
	$(RM) *.aux *.log *.out

.PHONY: clean
clean: clean-aux
	$(RM) *.pdf
