from pathlib import Path
from pypdf import PdfReader
from docx import Document


def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)


def load_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def load_txt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def load_documents(folder: str = "documents") -> list[dict]:
    docs = []
    folder_path = Path(folder)

    if not folder_path.exists():
        return docs

    for path in folder_path.iterdir():
        if path.is_file():
            suffix = path.suffix.lower()

            try:
                if suffix == ".pdf":
                    text = load_pdf(str(path))
                elif suffix == ".docx":
                    text = load_docx(str(path))
                elif suffix == ".txt":
                    text = load_txt(str(path))
                else:
                    continue

                if text.strip():
                    docs.append(
                        {
                            "filename": path.name,
                            "text": text,
                        }
                    )
            except Exception as e:
                print(f"Error reading {path.name}: {e}")

    return docs
