# Code Switching — Roman Urdu / English Dataset

A manually curated dataset of Roman Urdu–English code-switched sentences — the way ~230 million Pakistanis actually text and tweet — labelled word by word for language. Built for Project 2 of Code Saviours SI-26.

## Dataset

Every sentence in this dataset mixes Roman Urdu and English the way people naturally do in WhatsApp chats, tweets, and comments — no clean line between the two languages, just real, everyday code-switching. Each word is tagged `URD`, `ENG`, or `MIX` so the dataset can be used to train or evaluate language-identification and NLU models built for this kind of text.

- **155 sentences, 1,400+ labelled words** — hand-curated to reflect genuine mixing patterns
- **Word-level labels** — every token tagged, not just the sentence
- **Three-way label scheme** — Roman Urdu, English, and assimilated loanwords (MIX)
- **Ready for HuggingFace** — flat CSV format, drop-in for LID/NLU pipelines

### Contents
- `dataset.csv` — flat, word-level labelled dataset (sentence, word, label)
- `SI26-Week6-MuhammadAhmad.ipynb` — Colab notebook used to build and export the dataset
- `DATASET_CARD.md` — dataset card (also used as the HuggingFace dataset card)

### Label scheme
- `URD` — Roman Urdu word
- `ENG` — English word
- `MIX` — assimilated loanword used interchangeably by both language
  communities in everyday Pakistani speech (e.g. "mobile", "internet")

### Dataset
Published on HuggingFace: https://huggingface.co/datasets/Muhammad-Ahmad-1263/code-switching-codesaviours-si26-muhammadahmad
