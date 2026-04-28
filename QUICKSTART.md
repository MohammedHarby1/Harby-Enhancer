# 🚀 Harby Enhancer - Quick Start Guide

## ⚡ Get Started in 5 Minutes

### 1️⃣ **Installation**

```bash
# Clone the repository
git clone https://github.com/MohammedHarby1/Harby-Enhancer.git
cd Harby-Enhancer

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### 2️⃣ **Run the Application**

```bash
python main.py
```

The application window will open with a professional cinematic dark interface.

---

## 📹 **Using the App**

### **Step 1: Upload Video**
- Click on **"Upload Video"** section
- Select your video file (MP4, MKV, AVI, or MOV)
- File info will appear below

### **Step 2: Choose Quality** (Optional)
- Toggle **"Premium 4K Enhancement"** for best quality
- Leave it off for faster processing

### **Step 3: Start Enhancement**
- Click **"Start Enhancement"** button
- Progress bar will show real-time progress
- See which stage is being processed

### **Step 4: Get Result**
- Wait for completion message
- Your enhanced video is ready! ✅

---

## 🎯 **Quick Examples**

### **Example 1: Basic Enhancement**
```python
from advanced_processor import VideoEnhancementEngine, EnhancementMode

engine = VideoEnhancementEngine()
success = engine.enhance_video(
    input_path="video.mp4",
    output_path="video_enhanced.mp4",
    mode=EnhancementMode.STANDARD,
)
```

### **Example 2: Premium 4K**
```python
success = engine.enhance_video(
    input_path="video.mp4",
    output_path="video_4k.mp4",
    mode=EnhancementMode.PREMIUM_4K,
)
```

### **Example 3: Batch Processing**
```python
from advanced_processor import BatchVideoProcessor, EnhancementMode

batch = BatchVideoProcessor()
batch.add_video("video1.mp4", "video1_enhanced.mp4", EnhancementMode.STANDARD)
batch.add_video("video2.mp4", "video2_enhanced.mp4", EnhancementMode.PREMIUM)
batch.process_batch()
```

---

## 🎨 **Color Scheme**

| Part | Color |
|------|-------|
| Background | Deep Dark (#0A0E27) |
| Accent | Neon Mint (#00D9FF) |
| Text | White (#FFFFFF) |
| Success | Green (#00D977) |
| Warning | Orange (#FF6B35) |

---

## 📊 **Enhancement Modes**

### **Standard** ⚡
- Fast processing
- Good quality improvement
- **Perfect for:** Quick edits, previews

### **Premium** 🎬
- Balanced speed & quality
- Better enhancement
- **Perfect for:** Professional work, social media

### **Premium 4K** 🌟
- Slow but best quality
- Upscaling to 4K
- Advanced algorithms
- **Perfect for:** High-end content, cinema

---

## 🔧 **Customization**

Edit `config.py` to customize:

```python
# Colors
NEON_MINT = "#00D9FF"
PRIMARY_DARK = "#0A0E27"

# Window size
DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 800

# Processing
DENOISE_STRENGTH = 5
SHARPENING_KERNEL = 1.0
```

---

## 📁 **Project Files**

| File | Purpose |
|------|---------|
| `main.py` | Main UI application |
| `advanced_processor.py` | Video enhancement engine |
| `video_processor.py` | Basic video processing |
| `ui_components.py` | UI components |
| `config.py` | Settings & configuration |
| `utils.py` | Helper utilities |
| `examples.py` | Usage examples |

---

## ✅ **Features at a Glance**

✨ **Pro-grade video enhancement**  
🎨 **Cinematic dark interface**  
⚡ **Multiple quality presets**  
📊 **Real-time progress tracking**  
🔧 **Customizable settings**  
🎬 **Batch processing support**  
📱 **Responsive design**  
💾 **Multiple format support**  

---

## 🆘 **Troubleshooting**

**Q: App won't start**
```bash
pip install --upgrade flet opencv-python pillow
```

**Q: Video won't upload**
- ✓ Check format (MP4, MKV, AVI, MOV)
- ✓ Ensure file is not corrupted
- ✓ Check file path is correct

**Q: Processing is slow**
- ✓ Use Standard mode for speed
- ✓ Use 4K mode only when needed
- ✓ Close other applications

**Q: Output quality is poor**
- ✓ Try Premium or 4K mode
- ✓ Ensure input is good quality
- ✓ Check video codec support

---

## 📞 **Support**

- 📧 Email: mpro68160@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/MohammedHarby1/Harby-Enhancer/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/MohammedHarby1/Harby-Enhancer/discussions)

---

## 📝 **License**

MIT License - Free to use and modify

---

**Made with ❤️ by Harby Design**

**Ready to enhance your videos? Let's go! 🚀🎬✨**
