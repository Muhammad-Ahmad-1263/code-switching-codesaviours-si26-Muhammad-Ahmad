import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Roman Urdu / English Language ID", page_icon="🔤")

# --- Configuration ---------------------------------------------------------
MODEL_ID = "Muhammad-Ahmad-1263/code-switching-codesaviours-si26-muhammadahmad"

LABEL_COLORS = {
    "URD": "#1f77b4",   # blue
    "ENG": "#2ca02c",   # green
    "MIX": "#ff7f0e",   # orange
}


@st.cache_resource(show_spinner="Loading model from the Hugging Face Hub...")
def load_classifier(model_id: str):
    return pipeline("token-classification", model=model_id, aggregation_strategy=None)


st.title("🔤 Roman Urdu / English Code-Switch Language ID")
st.caption(
    "Fine-tuned XLM-RoBERTa · Project 2, Code Saviours SI-26 · "
    "tags each word as Roman Urdu (URD), English (ENG), or an assimilated loanword (MIX)."
)

sentence = st.text_input(
    "Type a Roman Urdu / English sentence:",
    value="Yaar mujhe kal ka meeting reschedule karna hai",
)

if st.button("Identify languages", type="primary") and sentence.strip():
    try:
        classifier = load_classifier(MODEL_ID)
    except Exception as e:
        st.error(
            "Couldn't load the model. Make sure MODEL_ID in app.py points to your "
            f"published Hugging Face model repo.\n\nDetails: {e}"
        )
        st.stop()

    results = classifier(sentence)

    st.subheader("Tagged output")
    html_parts = []
    for r in results:
        color = LABEL_COLORS.get(r["entity"], "#999999")
        html_parts.append(
            f'<span style="background-color:{color}22;border:1px solid {color};'
            f'border-radius:6px;padding:2px 6px;margin:2px;display:inline-block;">'
            f'{r["word"]} <b style="color:{color};">{r["entity"]}</b></span>'
        )
    st.markdown(" ".join(html_parts), unsafe_allow_html=True)

    st.subheader("Details")
    st.table(
        [{"word": r["word"], "label": r["entity"], "confidence": round(float(r["score"]), 3)} for r in results]
    )

st.divider()
st.caption(
    "Labels — URD: Roman Urdu word · ENG: English word · MIX: assimilated loanword "
    "used interchangeably in everyday Pakistani speech (e.g. 'mobile', 'internet')."
)
