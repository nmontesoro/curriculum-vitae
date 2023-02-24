import json

def escape_characters(original: str) -> str:
    return original.replace("&", "\&").replace("%", "\%")


class PersonalInfo:
    def __init__(self, data: dict) -> None:
        self.data = data

        self.show_qr = ("show-qr" in data and data["show-qr"] == "true")
        self.show_picture = ("picture-path" in data)
    
    def __get_qr_str(self) -> str:
        str_value = f"""
BEGIN:VCARD\?
VERSION:4.0\?
N:{self.data["last-name"]};{self.data["name"]}\?
TEL;TYPE=work:{self.data["phone"]}\?
TITLE:{self.data["profession"]}\?
EMAIL:{self.data["email"]}\?"""

        if "links" in self.data:
            for link in self.data["links"]:
                str_value += f"\nURL;TYPE={link['site']}:{link['url']}"

        str_value += """
END:VCARD\?
        """

        return str_value
    
    def __str__(self) -> str:
        str_value = "\\begin{textblock}{1}(0,0)"


        if self.show_qr:
            str_value += f"\\justqr{{{self.__get_qr_str()}}}"


        str_value += f"""

        \\name{{{self.data["name"]} {self.data["last-name"]}}}

        \\emph{{{self.data["profession"]} -- {self.data["location"]}}}
        
        \\null
        \\vfill
        \\phonenumber{{{self.data["phone"]}}}

        \\href{{mailto:{self.data["email"]}}}{{{self.data["email"]}}}
        """

        if "links" in self.data:
            for link in self.data["links"]:
                str_value += f"""\n\n{link["site"]}: \\href{{{link["url"]}}}{{{link["display"]}}}"""
        
        str_value += "\n\\end{textblock}"

        return str_value

class SectionItem:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    def __str__(self) -> str:
        str_content = ""

        if "short-description" in self.data:
            str_content += f"\\shortdesc{{{escape_characters(self.data['short-description'])}}}"
        if "institution" in self.data:
            str_content += f"\\institution{{{escape_characters(self.data['institution'])}}}"
        if "dates" in self.data:
            str_content += f"\\dates{{{self.data['dates']}}}"
        if "description" in self.data:
            str_content += "\\fulldesc{"
            if len(self.data["description"]) == 1:
                str_content += f"\n\n{escape_characters(self.data['description'][0])}"
            else:
                str_content += "\n\\begin{itemize}"
                for item in self.data["description"]:
                    str_content += f"\n\item {escape_characters(item)}"
                str_content += "\n\\end{itemize}"
            str_content += "}\n"

        return str_content

class Section:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.section_items = [SectionItem(x) for x in self.data["items"]]
    
    def __str__(self) -> str:
        str_content = f"\\section{{{self.data['header']}}}"
        
        for item in self.section_items:
            str_content += f"\n{str(item)}"
        
        return str_content

def import_data() -> list[dict]:
    with open("data/data.json", "rt") as fp:
        data = json.load(fp)
    return data

def get_headers() -> str:
    with open("templates/template.tex", "rt") as fp:
        headers = fp.read()
    return headers

data = import_data()
headers = get_headers()

for datum in data:
    language = datum["language"]
    personal_info = PersonalInfo(datum["personal-info"])
    sections = [Section(x) for x in datum["sections"]]

    with open(f"output/{language}.tex", "wt") as fp:
        fp.write(f"\def \langsetting {{{language}}}\n")
        fp.write(headers)
        fp.write("\\begin{document}")
        fp.write(str(personal_info))

        fp.write("\n\\begin{textblock}{1}(0,1)")

        for section in sections:
            fp.write(str(section))

        fp.write("\n\end{textblock}\n\end{document}")
