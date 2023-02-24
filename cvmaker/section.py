from . import section_item


class Section:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.section_items = [section_item.SectionItem(
            x) for x in self.data["items"]]

    def __str__(self) -> str:
        str_content = f"\\section{{{self.data['header']}}}"

        for item in self.section_items:
            str_content += f"\n{str(item)}"

        return str_content
