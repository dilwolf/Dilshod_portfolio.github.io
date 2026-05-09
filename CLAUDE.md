# Portfolio Project — CLAUDE.md

## Live Structure
GitHub Pages serves from root. `Dilshod_main/` is a template backup — never touch it.

## Key Files
- `index.html` — English (primary)
- `index - korean.html` — Korean (to be migrated into i18n system)
- `CogVSM.html` / `CogVSM - korean.html` — research project detail page
- `football-details.html` / `football-details - korean.html` — to be replaced with Axion project pages
- `assets/css/style.css` — single stylesheet
- `assets/js/main.js` — single JS file
- `assets/img/tech/` — tool/framework icons

## Stack
Static HTML/CSS/JS — BootstrapMade template. No build system, no npm, no bundler.
Vendors: Bootstrap 5, AOS, Boxicons, Swiper, Typed.js, GLightbox, Isotope, Purecounter.

## Planned Refactor Goals
1. Merge EN/KO into single i18n system: `translations.json` + `data-i18n` attributes + language toggle in `main.js`
2. Update About section content (see Profile below)
3. Replace outdated skills: remove TensorFlow, Keras, JAX, MLflow → add TensorRT, YOLO, RF-DETR, DDP, Active Learning, Ultralytics
4. Replace old project pages (football, sentiment, GAN, SageMaker) with Axion production work
5. Remove % skill bars — replace with categorized skill tags
6. Keep Research section as-is (already accurate)

## Do Not
- Edit anything inside `Dilshod_main/`
- Add npm, webpack, or any build tools
- Break mobile responsiveness
- Change vendor files in `assets/vendor/`

## Owner Profile (use for all content updates)
Name: Dilshod Yuldashev (Bazarov)
Role: Computer Vision / AI Engineer
Current: Axion, Seongnam — 09.2024–present
Previous: iMES Lab researcher (2022–2024), AITheNutrigene intern
Education: MS AI Software, Gachon University (GPA 4.0/4.5)
Languages: English, Korean (portfolio bilingual)

## Skills (current — use these only)
- Languages: Python (NumPy, OpenCV, Pillow, PyTorch)
- Frameworks: PyTorch, Torchvision, Scikit-learn, ONNX, TensorRT, Ultralytics
- CV: Object Detection, Segmentation, Action Detection, YOLO series, RF-DETR, OBB Detection
- Training: DDP (Distributed Data Parallel), Multi-GPU, Active Learning, Custom Augmentation
- Deployment: AWS (EC2, S3, DVC), Docker, Git, GitHub Actions, ONNX Export, TensorRT Export

## Axion Projects (production — confidential, no code/data public)
1. Multi-class Detection (AXEyes/AXDeID) — 97.1% mAP, 7 classes, 27% false alert reduction, 50+ clients
2. Fire & Smoke Detection (AXEyes) — 89% mAP, YOWOv3, RF-DETR evaluated, 100+ CCTV cameras
3. Drone Surveillance (AXDron) — 92% mAP small object detection, TensorRT export
4. Fish-Eye Surveillance (AXDeID) — 91% mAP OBB, 180° FOV, 100+ Philippines locations
5. Abnormal Behavior Detection (AXEyes) — 92.1% fight / 89.7% fall-down mAP, DDP multi-GPU
6. KISA Certification (AXVAMS) — 97.3% accuracy, RGB/IR intrusion + loitering

## Public Projects (keep, these have GitHub/demos)
- CogVSM — federated surveillance (SCI paper, has detail page + video)
- Football Analysis — YOLO + optical flow (has GitHub)
- KakaoTalk Sentiment — BERT fine-tune (has HuggingFace demo)

## i18n Plan
- Add `translations.json` in root
- Add `data-i18n="key"` to all text elements in `index.html`
- Add language switcher button to nav (EN | 한국어)
- JS reads lang from localStorage, applies on load
- Delete `index - korean.html` and other `-korean.html` files after migration