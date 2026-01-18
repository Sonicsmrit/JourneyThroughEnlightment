# Pixel Luminance Image Transition (Pygame)

This project creates a **smooth pixel-based transition effect between multiple images** using **Pygame** and **Pillow (PIL)**. Each pixel is treated as an individual particle that moves to its corresponding position in the next image, sorted by luminance for a visually pleasing transition.

---

## ✨ What This Does

* Loads **5 images** and resizes them to the same resolution
* Breaks each image into pixels
* Sorts pixels by **image index + brightness (luminance)**
* Represents pixels as moving square particles
* Smoothly transitions pixels from one image to the next
* Pauses briefly after each full transition

The result is a **cinematic dissolve / morph effect** where images blend into each other pixel-by-pixel.

---

## 📦 Requirements

Make sure you have Python 3 installed, then install dependencies:

```bash
pip install pygame pillow
```

---

## 📁 Project Structure

```text
project-folder/
│
├── five transition/
│   ├── all.jpeg
│   ├── gojo.jpeg
│   ├── Isekai.jpeg
│   ├── makima.jpg
│   └── three.jpeg
│
├── main.py
└── README.md
```

> ⚠️ All images **must be the same aspect ratio**.

---

## ▶️ How to Run

```bash
python main.py
```

A window will open displaying the animated pixel transitions.

---

## 🧠 How It Works (Core Idea)

### 1. Image Processing

* Each image is converted to grayscale to compute luminance
* Every pixel stores:

  * Image ID
  * RGB color
  * Luminance value
  * (x, y) coordinates

### 2. Sorting

Pixels are sorted by:

```python
(id, luminance)
```

This ensures that **brighter/darker pixels move together**, producing a smooth transition.

### 3. Particle System

Each pixel becomes a `Transition` object with:

* Current position `(x, y)`
* Target position `(tx, ty)`
* Smooth interpolation movement

Movement formula:

```python
self.x += (self.tx - self.x) * 0.1
self.y += (self.ty - self.y) * 0.1
```

### 4. Holding State

Once all pixels arrive at their targets:

* Animation pauses for `300 ms`
* New target image is selected
* Pixels retarget to the next image

---

## ⚙️ Customization

You can easily tweak the effect:

| Feature    | Where                      | Effect                    |
| ---------- | -------------------------- | ------------------------- |
| Pixel size | `self.size = 12`           | Bigger / smaller blocks   |
| Speed      | `* 0.1`                    | Faster or slower movement |
| Hold time  | `hold = 300`               | Pause duration            |
| Density    | `range(0, len(pixel), 10)` | More or fewer particles   |

---

## 🎨 Visual Notes

* White background
* Square particles
* Image resolution affects performance

> Large images = many particles = slower performance

---

## 🚀 Ideas to Extend

* Fade colors while moving
* Add mouse-triggered transitions
* Randomized pixel order
* Circular or wave-based motion
* GPU acceleration (via moderngl)

---

## ❤️ Credits

Made with **Pygame**, **Pillow**, and a lot of pixel love.

If you're experimenting with visual effects, this is a great base to build on.

Have fun breaking images apart ✨
