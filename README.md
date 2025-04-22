# Landmark Image Identifier

This Python project detects landmarks using Google Cloud Vision API. It stores the processed data in a CSV file with details like description, confidence score, and Google Maps reference.

---

## Project Structure

```
project-root/
│
├── main.py                   # Entry point of the program
├── landmarks.csv             # Output CSV file with landmark data (auto-generated)
├── images/                   # Source folder with original images
├── resized/                  # Folder where resized images are saved (auto-generated)
├── credentials.json          # Your Google Cloud credentials file
│
└── src/
    ├── resize/
    │   └── resize.py         # Resizing logic
    ├── identify/
    │   └── identify.py       # Landmark detection logic
    └── csv/
        └── csv.py            # CSV writing logic
```

---

## How It Works

### 1. **Image Resizing**
- All `.jpg`, `.jpeg`, and `.png` images in the `images/` folder are resized to 25% of their original size — only if their width or height exceeds 512px.
- Resized images are saved to the `resized/` folder.

### 2. **Landmark Detection**
- Uses [Google Cloud Vision API](https://cloud.google.com/vision/docs) to detect landmarks in each resized image.
- Detected results are written to `landmarks.csv`, including:
  - Image name
  - Landmark description
  - Confidence score
  - Latitude & Longitude
  - A Google Maps reference link

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourname/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 3. Set up Google Cloud Vision
- Enable the **Vision API** in your Google Cloud Console.
- Download your **service account credentials** as `credentials.json` and place it in the project root.

---

## Running the Program

Place your input images into the `images/` folder and then run:

```bash
python main.py
```

The script will:
- Resize images (if needed)
- Detect landmarks
- Write results to `landmarks.csv`

---

## Output Example (`landmarks.csv`)

| Image     | Description       | Confidence Score | Longitude  | Latitude   | Ref                                           |
|-----------|-------------------|------------------|------------|------------|-----------------------------------------------|
| paris.jpg | Eiffel Tower      | 0.987            | 2.2945     | 48.8584    | [Google Maps](https://www.google.com/maps/...) |
| lake.jpg  | unknown           |                  |            |            |                                               |

---

## Notes

- You can configure resize percentage and image limits in `main.py` and `resize.py`.
