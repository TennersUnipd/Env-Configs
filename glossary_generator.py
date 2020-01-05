import csv
import os
import tables
import pytabular
from datetime import date

BASE_PATH = "sweDocs/esterni/glossario/"
DEFAULT_PATH = "res/sections/"
INDENT = "    "

FILE_HEADER_CHANGELOG = "\\section*{Registro delle modifiche}\r\n\\renewcommand{\\arraystretch}{1.8}\r\n\r\n  " \
                        "\\rowcolors{2}{pari}{dispari}\r\n"

TABLE_FORMAT = INDENT + "\\begin{longtable}{|c|c|c|p{3.8cm}|c|}\n" + INDENT + INDENT + "\\hline\n" + INDENT + INDENT + "\\rowcolor{header}\n"
TABLE_HEADER_CHANGELOG = ["Versione", "Nominativo", "Ruolo", "Descrizione", "Data"]

TABEL_END = INDENT + INDENT + "\\hline\n" + INDENT + "\\end{longtable}"
def get_sorted_data():
    with open('glossary.csv', 'r') as glossary:
        data = [line for line in csv.reader(glossary)]

    data.sort(key=lambda x: x[0].lower())
    return data


def create_changelog():
    d1 = date.today().strftime("%Y/%m/%d")
    page = open(BASE_PATH + DEFAULT_PATH + "registro_modifiche.tex", "w")
    page.write(FILE_HEADER_CHANGELOG)
    page.write(TABLE_FORMAT)
    page.write(INDENT + INDENT +"\\textbf{" + TABLE_HEADER_CHANGELOG[0] + "} & \\textbf{" + TABLE_HEADER_CHANGELOG[1] + "} & \\textbf{" +
               TABLE_HEADER_CHANGELOG[2] + "} & \\centering{\\textbf{" + TABLE_HEADER_CHANGELOG[3] + "}} & \\textbf{" +
               TABLE_HEADER_CHANGELOG[4] + "} \\\\ \n")
    page.write(INDENT + INDENT +"\\hline \n")
    page.write(INDENT + INDENT + str(0) + " & " + str("Script") + " & " + "Script"
                " & \\small{\\textit{ Aggiunta Automatica }} & " + str(d1) + " \\\\ \n" )
    page.write(TABEL_END)
    pass


def gen_sections():
    data = get_sorted_data()
    letters = []
    for line in data:
        letter = line[0][0]
        try:
            letters.index(letter)
        except ValueError:
            letters.append(letter)
            page = open(BASE_PATH + DEFAULT_PATH + letter + ".tex", "w+")
            page.write("\\subsection*{\\textbf{\\hfill \\Huge{" + letter + "} \\hfill}} ")
            page.write('\n')
            page.write("\\addcontentsline{toc}{subsection}{" + letter + "}")
            page.write('\n')

        page.write("\\subsubsection*{" + line[0] + "}")
        page.write('\n')
        page.write("\\index*{" + line[0] + "}")
        page.write('\n')
        page.write(line[1])
        page.write('\n')
    return letters


def gen_main_page(letters):
    page = open(BASE_PATH+"main.tex", "w+")
    page.write("\\documentclass[a4paper]{article}\n \\input{config/config.tex}\n \\makeindex \n\\begin{document}\n")
    page.write(INDENT + "\\include{res/sections/frontespizio}\n")
    page.write(INDENT + "\\include{res/sections/registro_modifiche}\n")
    page.write(INDENT + "\\tableofcontents\n")

    for letter in letters:
        page.writelines("\\include{" + DEFAULT_PATH + letter + "}\n")

    page.write("\\end{document}")
    pass


def main():
    create_changelog()
    gen_main_page(gen_sections())


if __name__ == '__main__':
    main()
