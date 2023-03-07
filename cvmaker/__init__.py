import json
from os import path, mkdir
from . import personal_info, section


class CVMaker:
    def __init__(self) -> None:
        self._template_dir = ""
        self._output_dir = ""
        self._data_filename = ""

    def make(self) -> None:
        data = self._import_data()
        template = self._get_template()

        for datum in data:
            language = datum["language"]
            pinfo = personal_info.PersonalInfo(datum["personal-info"])
            secs = [section.Section(x) for x in datum["sections"]]

            with open(f"{self.output_dir}/{language}.tex", "wt") as fp:
                fp.write(f"\def \langsetting {{{language}}}\n")
                fp.write(template)
                fp.write("\\begin{document}")
                fp.write(str(pinfo))

                fp.write("\n\\begin{textblock}{1}(0,1)")

                for sec in secs:
                    fp.write(str(sec))

                fp.write("\n\end{textblock}\n\end{document}")

    def _import_data(self) -> list[dict]:
        with open(self.data_filename, "rt") as fp:
            data = json.load(fp)
        return data

    def _get_template(self) -> str:
        with open(f"{self.template_dir}/template.tex", "rt") as fp:
            template = fp.read()
        return template

    @property
    def template_dir(self) -> str:
        return self._template_dir

    @template_dir.setter
    def template_dir(self, new_path: str) -> None:
        self._create_dir_if_not_exists(new_path)
        self._template_dir = new_path

    @property
    def output_dir(self) -> str:
        return self._output_dir

    @output_dir.setter
    def output_dir(self, new_path) -> None:
        self._create_dir_if_not_exists(new_path)
        self._output_dir = new_path

    @property
    def data_filename(self) -> str:
        return self._data_filename

    @data_filename.setter
    def data_filename(self, new_path: str) -> None:
        if not path.exists(new_path):
            raise ValueError(f"File {new_path} does not exist")
        else:
            self._data_filename = new_path

    def _create_dir_if_not_exists(self, new_path):
        if not path.exists(new_path):
            mkdir(new_path)
