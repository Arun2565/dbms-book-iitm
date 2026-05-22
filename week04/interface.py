# interface.py (skeleton)
import gradio as gr
import io
from typing import List

# Dependencies you may install:
# - transformers (for summarization)
# - PyMuPDF (fitz) or PyPDF2 (for PDF text extraction)
# - Optional: nltk/spacy for glossary or QA aids

def extract_text_from_pdf(file_bytes: bytes) -> str:
    # Placeholder: replace with PyMuPDF (fitz) or pdfminer.six extraction
    # This is read-only plan code; implement in your environment.
    import fitz  # PyMuPDF
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    text = ""
    try:
        doc = fitz.open(tmp_path)
        for pag in doc:
            text += pag.get_text()
        doc.close()
    finally:
        pass
    return text

def summarize_text(text: str, model_name: str = "google/pegasus-xsum", max_chunk: int = 1024) -> str:
    # Minimal summarization pipeline (long documents are chunked)
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summaries: List[str] = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs.input_ids, max_length=180, min_length=80, do_sample=False)
        summaries.append(tokenizer.decode(summary_ids[0], skip_special_tokens=True))

    # Optional: combine and summarize again for a coherent final abstract
    combined = " ".join(summaries)
    final_inputs = tokenizer(combined, return_tensors="pt", truncation=True)
    final_ids = model.generate(final_inputs.input_ids, max_length=180, min_length=80, do_sample=False)
    final_summary = tokenizer.decode(final_ids[0], skip_special_tokens=True)
    return final_summary

def generate_abstract(pdf_bytes: bytes) -> str:
    if not pdf_bytes:
        return ""
    text = extract_text_from_pdf(pdf_bytes)
    if not text:
        return "Could not extract text from PDF."
    return summarize_text(text)

def learning_mode_guide(text: str) -> str:
    # Simple learning aids: extract key terms (placeholder logic)
    # In a full version, you could run a keyword extractor or quiz generator.
    # Here we return a small, friendly study note.
    return "Study Note: Focus on main objectives, methods, and results. Cross-check figures with captions."

def build_interface():
    with gr.Blocks(css="""
        @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;600;700&display=swap');
        * { font-family: 'EB Garamond', serif; }
        :root {
            --bg: #ffffff;
            --fg: #1a1a1a;
            --card: #f7f7f7;
        }
        [data-theme="dark"] {
            --bg: #0e0f12;
            --fg: #eaeaea;
            --card: #1a1e23;
        }
        body { background: var(--bg); color: var(--fg); }
        .gradio-container { font-family: 'EB Garamond', serif; }
        /* Simple, clean card styling for panels */
        .card { background: var(--card); border-radius: 12px; padding: 16px; }
    """):
        gr.Markdown("""
        # Research Abstract Studio
        <div style="font-size:14px; color:var(--fg)">Upload a PDF of a research paper to generate an abstract. Switch to Learning Mode to study the paper with guided aids.</div>
        """, unsafe_allow_html=True)

        with gr.Tabs():
            with gr.TabItem("Abstract Generator"):
                with gr.Row():
                    pdf_input = gr.File(label="Upload Research Paper (PDF)", file_types=["application/pdf"])
                    theme_toggle = gr.Radio(label="Theme", choices=["Light", "Dark"], value="Light", show_label=True)
                with gr.Row():
                    abstract_out = gr.Textbox(label="Generated Abstract", lines=12, interactive=False)
                # Wire up actions
                pdf_input.change(lambda f: f, pdf_input, None)  # placeholder to illustrate wiring
                theme_toggle.change(lambda t: t, theme_toggle, None)  # placeholder

            with gr.TabItem("Learning Mode"):
                with gr.Row():
                    pdf_input_learn = gr.File(label="Upload Paper (PDF) for Learning", file_types=["application/pdf"])
                with gr.Row():
                    learning_output = gr.Textbox(label="Learning Output", lines=12, interactive=False)

        # Bottom area: a simple theme switcher that applies a data-theme attribute
        # Actual theme toggling would be wired to python callbacks that re-render the UI with the chosen theme.
        # This skeleton focuses on structure and styling.

    return interface

if __name__ == "__main__":
    # Note: In this plan, we provide skeleton code only. Replace with real callbacks in your environment.
    app = build_interface()
    app.launch(debug=True, share=False)
