def escape_characters(original: str) -> str:
    return original.replace("&", "\&").replace("%", "\%")


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
