# Day 188 Worked Examples: ML vs DL

## Example 1 — Practical: Model Selection Decision Tree
```python
def select_model_family(data_type, dataset_size_rows):
    if data_type == "Tabular":
        return "Classical ML (XGBoost / LightGBM / Random Forest)"
    elif data_type in ["Image", "Audio", "Unstructured Text"]:
        if dataset_size_rows < 1000:
            return "Pretrained Deep Learning (Transfer Learning)"
        else:
            return "Deep Learning (CNN / Transformer)"

print("Choice for 50,000 row CSV sales dataset:", select_model_family("Tabular", 50000))
print("Choice for 100,000 medical X-ray images: ", select_model_family("Image", 100000))
```
