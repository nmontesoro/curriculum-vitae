import json
from cvmaker import personal_info, section


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
    personal_info = personal_info.PersonalInfo(datum["personal-info"])
    sections = [section.Section(x) for x in datum["sections"]]

    with open(f"output/{language}.tex", "wt") as fp:
        fp.write(f"\def \langsetting {{{language}}}\n")
        fp.write(headers)
        fp.write("\\begin{document}")
        fp.write(str(personal_info))

        fp.write("\n\\begin{textblock}{1}(0,1)")

        for section in sections:
            fp.write(str(section))

        fp.write("\n\end{textblock}\n\end{document}")
