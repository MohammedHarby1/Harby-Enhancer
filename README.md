# Harby Enhancer - Professional Video Enhancement App

## 🎬 Overview

**Harby Enhancer** is a professional-grade video enhancement mobile application built with Python and Flet. Featuring a cinematic dark mode UI with neon mint accents, it provides a premium video processing experience suitable for content creators, filmmakers, and video enthusiasts.

### 🎨 Design Philosophy
The application embodies the "Harby Design" brand with high-end UI/UX elements inspired by modern video editing software and premium streaming platforms.

---

## ✨ Key Features

### 📹 Video Upload
- Intuitive drag-and-drop interface
- Support for multiple formats: MP4, MKV, AVI, MOV
- Real-time file validation and metadata extraction
- File size and duration preview

### 🎯 Processing Pipeline
- **Analyzing**: Video quality assessment and format detection
- **Filtering**: Advanced enhancement algorithms application
- **Encoding**: High-quality output rendering
- **Finalizing**: Export optimization and verification

### 4️⃣ Premium 4K Mode
- Toggle for enhanced processing quality
- Upscaling algorithms for 4K output
- Advanced color grading and HDR support
- Optimized for large-screen display

### 📊 Progress Tracking
- Real-time progress bar with percentage display
- Stage-by-stage processing status
- ETA estimation for completion
- Cancellation support for long-running operations

### 🎨 Professional UI/UX
- **Cinematic Dark Mode**: Eye-friendly with reduced strain
- **Neon Mint Accents**: Modern, premium aesthetic
- **Glass-morphism Effects**: Depth and dimensionality
- **Smooth Animations**: Polished user interactions
- **Responsive Design**: Works on mobile and tablet devices

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/MohammedHarby1/Harby-Enhancer.git
cd Harby-Enhancer
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python main.py
```

---

## 🚀 Usage

### Basic Workflow

1. **Launch the App**: Execute `python main.py` to start the application
2. **Upload Video**: Click the upload section to select your video file
3. **Configure Settings**:
   - Toggle **Premium 4K** for enhanced processing
4. **Start Enhancement**: Click "Start Enhancement" button
5. **Monitor Progress**: Watch the real-time progress bar and status updates
6. **Export**: Once complete, your enhanced video is ready for download

### Keyboard Shortcuts
- `Esc` - Cancel current operation
- `Ctrl+O` - Open file picker
- `Ctrl+Q` - Quit application

---

## 🎨 Design System

### Color Palette

| Element | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| Primary Dark | Deep Cinematic | #0A0E27 | Main background |
| Secondary Dark | Slightly Lighter | #141829 | Component backgrounds |
| Accent Primary | Neon Mint | #00D9FF | Buttons, highlights |
| Accent Light | Neon Mint Light | #00F0FF | Hover states |
| Accent Secondary | Purple | #9D4EDD | Alternative highlights |
| Text Primary | White | #FFFFFF | Main text |
| Text Secondary | Gray | #B0B0B0 | Secondary text |
| Success | Green | #00D977 | Success states |
| Warning | Orange | #FF6B35 | Warning states |

### Typography

- **Brand Font**: Arial, system sans-serif
- **Headings**: Bold, 28px (HARBY title)
- **Subheadings**: Regular, 16px (ENHANCER subtitle)
- **Body Text**: Regular, 12px
- **Small Text**: Regular, 10-11px
- **Letter Spacing**: 2px for dramatic effect

### Component Styles

- **Border Radius**: 10-15px for rounded corners
- **Shadows**: 20px blur radius with 30% opacity
- **Padding**: Consistent 15-20px spacing
- **Transitions**: Smooth animations on all interactions

---

## 📁 Project Structure

```
Harby-Enhancer/
├── main.py                 # Main application entry point
├── requirements.txt        # Project dependencies
├── README.md              # This file
├── video_processor.py     # Video processing module
├── ui_components.py       # Custom UI components
└── config.py              # Configuration settings
```

---

## 🔧 Core Modules

### main.py
- **HarbyEnhancer Class**: Main application controller
- **UI Creation Methods**: Header, upload, progress, buttons
- **Event Handlers**: User interaction management
- **Processing Simulation**: Threading-based operations

### video_processor.py (Coming Soon)
- Video codec detection
- Quality analysis algorithms
- Enhancement filters (brightness, contrast, saturation)
- 4K upscaling engine
- HDR processing pipeline

### ui_components.py (Coming Soon)
- Custom container components
- Animated progress indicators
- Theme management system
- Responsive layout helpers

### config.py (Coming Soon)
- Color scheme configuration
- Processing parameters
- UI settings
- Export quality presets

---

## 🔄 Processing Pipeline

```
User Selects Video
        ↓
Video Validation
        ↓
Quality Analysis (30%)
        ↓
Apply Filters (60%)
        ↓
Encode Output (90%)
        ↓
Finalize & Export (100%)
        ↓
Export Complete ✓
```

---

## ⚙️ System Requirements

### Minimum Specifications
- **CPU**: Intel i5 / AMD Ryzen 5 or equivalent
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB free space for app + video buffer
- **OS**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)

### Recommended Specifications
- **CPU**: Intel i7 / AMD Ryzen 7 or better
- **RAM**: 16GB or more
- **Storage**: SSD with 5GB+ free space
- **GPU**: NVIDIA CUDA-capable GPU for hardware acceleration

---

## 🚧 Future Enhancements

### Phase 2
- [ ] Batch processing for multiple videos
- [ ] Custom filter presets
- [ ] Real-time preview window
- [ ] GPU acceleration support (CUDA/OpenCL)

### Phase 3
- [ ] Subtitle processing and enhancement
- [ ] Audio enhancement (noise reduction, normalization)
- [ ] Video stabilization
- [ ] Frame interpolation for slow-motion effects

### Phase 4
- [ ] Cloud processing integration
- [ ] Collaborative editing features
- [ ] Advanced AI-based enhancement
- [ ] Custom neural network models

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**MohammedHarby1**
- GitHub: [@MohammedHarby1](https://github.com/MohammedHarby1)
- Email: mpro68160@gmail.com

---

## 🙏 Acknowledgments

- **Flet Framework**: For the modern, responsive UI framework
- **OpenCV**: For robust video processing capabilities
- **Community Contributors**: For feedback and suggestions

---

## 📞 Support & Contact

For issues, feature requests, or inquiries:
- **GitHub Issues**: [Report a bug or request a feature](https://github.com/MohammedHarby1/Harby-Enhancer/issues)
- **Email**: mpro68160@gmail.com

---

## 📊 Project Statistics

- **Language**: Python 3.8+
- **Framework**: Flet
- **Lines of Code**: 500+ (main.py)
- **Version**: 1.0.0
- **Status**: Active Development

---

**Made with ❤️ by Harby Design | Professional Video Enhancement Solutions**
