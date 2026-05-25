# LearnGate Exercise Counter - Mobile Fixed

Direct exercise screen only. No role page, no parent/child login, no phone status bar.

## Run locally

```powershell
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Render

Build Command:

```text
pip install -r requirements.txt
```

Start Command:

```text
gunicorn app:app
```

## Camera notes

Camera access works on localhost or HTTPS. Render gives HTTPS, so camera permission should appear on mobile browser.
The pose detector runs in the browser using MediaPipe Tasks Vision from CDN.
