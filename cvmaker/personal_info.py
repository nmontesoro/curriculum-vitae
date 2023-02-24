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
                str_value += f"\nURL;TYPE={link['site']}:{link['url']}\?"

        str_value += "\nEND:VCARD\?"

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
