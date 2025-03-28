from pathlib import Path

def generate_study_index(study_dir):
    index_lines = [
        "---",
        "layout: default",
        "title: 학습 정리 목록",
        "---",
        "# 📚 학습 노트 목록",
        ""
    ]

    for md_file in sorted(Path(study_dir).glob("*.md")):
        if md_file.name == "index.md":
            continue
        with md_file.open(encoding="utf-8") as f:
            lines = f.readlines()
        title_line = next((l for l in lines if l.startswith("title:")), "title: 제목 없음")
        title = title_line.replace("title:", "").strip()
        date_part = "-".join(md_file.stem.split("-")[0:3])
        name_part = md_file.stem
        link = f"- [{date_part} | {title}](/study/{name_part})"
        index_lines.append(link)

    (Path(study_dir) / "index.md").write_text("\n".join(index_lines), encoding="utf-8")

if __name__ == "__main__":
    generate_study_index("study")
