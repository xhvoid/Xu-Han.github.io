from pathlib import Path
import json

root = Path(__file__).resolve().parent
out = root
data = json.loads((root / "content.json").read_text())
old = (root / "template.tex").read_text()
header = old.split(r"\section{Education}", 1)[0]

def esc(value):
    table = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}"}
    return "".join(table.get(c, c) for c in value)

def href(url, title):
    return r"\href{" + esc(url) + "}{" + esc(title) + "}"

def one(text):
    return "\\begin{onecolentry}\n" + text + "\n\\end{onecolentry}\n"

def two(text, right):
    return "\\begin{twocolentry}{\\textit{" + esc(right) + "}}\n" + text + "\n\\end{twocolentry}\n"

def bullets(items):
    return one("\\begin{highlights}\n" + "\n".join(r"\item " + esc(x) for x in items) + "\n\\end{highlights}")

def section(title):
    return r"\section{" + esc(title) + "}\n"

def tex_links(links):
    return " | ".join(r"\hrefWithoutArrow{" + esc(url) + "}{" + esc(label) + "}" for label, url in links)

def md_links(links):
    return " | ".join("[" + label + "](" + url + ")" for label, url in links)

def project(item):
    if item.get("links"):
        result = one(r"{\large\textbf{" + esc(item["title"]) + "}}")
        result += two(r"\textit{" + esc(item["role"]) + r"}\quad " + tex_links(item["links"]), item["date"])
    else:
        title = r"{\large\textbf{" + href(item["url"], item["title"]) + "}}"
        result = two(title, item["date"]) if item.get("date") else one(title)
        if item.get("role"):
            role = r"\textit{" + esc(item["role"]) + "}"
            if item.get("supervisors"):
                role += r"\enspace Supervisors: " + esc(item["supervisors"]) + "."
            result += one(role)
    return result + bullets(item["bullets"]) + "\\vspace{0.08 cm}\n"

parts = [header, one(esc(data["summary"])), "\\vspace{0.05 cm}\n", section("Education")]
for item in data["education"]:
    degree = r"\textbf{" + esc(item["degree"]) + "}"
    institution = esc(item["institution"])
    if item["degree"] in ("M.Sc. Photonics", "B.Eng. Electrical Engineering and Automation"):
        parts.append(two(degree, item["date"]))
        parts.append(one(institution))
    else:
        parts.append(two(degree + " | " + institution, item["date"]))
    if item["details"]:
        text = " ".join(item["details"])
        text = esc(text).replace("Selected coursework:", r"\textbf{Selected coursework:}")
        text = text.replace("Zemax optical design", r"\textbf{Zemax optical design}")
        if item.get("links"):
            text += r"\enspace " + tex_links(item["links"])
        parts.append(one(text))
    elif item.get("links"):
        parts.append(one(tex_links(item["links"])))
    parts.append("\\vspace{0.08 cm}\n")

parts.append(section("Selected Research and Engineering Projects"))
parts.extend(project(item) for item in data["core"])
parts += ["\\clearpage\n", section("Laboratory and Instrumentation Training")]
parts.append(one("\\begin{highlights}\n" + "\n".join(r"\item \textbf{" + esc(k) + ":} " + esc(v) for k, v in data["labs"]) + "\n\\end{highlights}"))
parts.append(section("Additional Independent Projects"))
parts.extend(project(item) for item in data["additional"])
parts.append(section("Work Experience and Career Break"))
w = data["work"]
parts += [two(r"{\large\textbf{" + esc(w["title"]) + "}}\n\n" + r"\textit{" + esc(w["role"]) + "}", w["date"]), bullets(w["bullets"])]
break_item = data["career_break"]
parts += [two(r"\textbf{" + esc(break_item["title"]) + "}", break_item["date"]), one(esc(break_item["text"]))]
parts.append(section("Talks, Workshops and Schools"))
for item in data["activities"]:
    parts.append(two(r"\textbf{" + esc(item["title"]) + "}", item["date"]))
    if item.get("text"):
        parts.append(one(href(item["url"], item["text"]) if item.get("url") else esc(item["text"])))
    parts.append("\\vspace{0.06 cm}\n")
parts.append(section("Technical Skills"))
for k, v in data["skills"]:
    parts += [one(r"\textbf{" + esc(k) + ":} " + esc(v)), "\\vspace{0.04 cm}\n"]
parts += [section("Languages and Interests"), one(r"\textbf{Languages:} " + esc(data["languages"])), one(r"\textbf{Interests:} " + esc(data["hobbies"]))]
parts += [r"\renewcommand{\cvsectionreserve}{2\baselineskip}" + "\n", section("Academic Reference"), one(esc(data["academic_reference"])), "\\end{document}\n"]
(out / "Xu_Han_CV.tex").write_text("".join(parts))

md = ["# Xu Han", "Munich, Germany | [xuhanphysik@gmail.com](mailto:xuhanphysik@gmail.com) | [GitHub](https://github.com/xhvoid) | [Website](https://xhvoid.github.io/Xu-Han.github.io/)", data["summary"], "## Education"]
for item in data["education"]:
    md += ["### " + item["degree"] + " | " + item["institution"], item["date"], *item["details"]]
    if item.get("links"):
        md.append(md_links(item["links"]))
md.append("## Selected Research and Engineering Projects")
def md_project(item):
    text = ["### [" + item["title"] + "](" + item["url"] + ")"]
    if item.get("role"):
        text += [item["role"] + (" | " + item["date"] if item.get("date") else "")]
    if item.get("links"):
        text += [md_links(item["links"])]
    if item.get("supervisors"):
        text += ["Supervisors: " + item["supervisors"] + "."]
    text += ["\n".join("- " + x for x in item["bullets"])]
    return text
for item in data["core"]:
    md += md_project(item)
md += ["## Laboratory and Instrumentation Training", "\n".join("- **" + k + ":** " + v for k, v in data["labs"]), "## Additional Independent Projects"]
for item in data["additional"]:
    md += md_project(item)
md += ["## Work Experience and Career Break", "### " + w["title"], w["date"] + " | " + w["role"], "\n".join("- " + x for x in w["bullets"]), "### " + break_item["title"], break_item["date"], break_item["text"], "## Talks, Workshops and Schools"]
for item in data["activities"]:
    md += ["### " + item["title"] + " | " + item["date"]]
    if item.get("text"):
        md += ["[" + item["text"] + "](" + item["url"] + ")" if item.get("url") else item["text"]]
md += ["## Technical Skills", "\n".join("- **" + k + ":** " + v for k, v in data["skills"]), "## Languages and Interests", data["languages"], data["hobbies"]]
md += ["## Academic Reference", data["academic_reference"]]
(out / "Xu_Han_CV.md").write_text("\n\n".join(md) + "\n")
print("Wrote CV source and matching editable text.")
