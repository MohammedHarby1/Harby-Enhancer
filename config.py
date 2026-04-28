"""
Configuration Module
Central configuration for Harby Enhancer application
"""

from dataclasses import dataclass
from typing import Dict, List


# ==================== COLOR SCHEME ====================

class ColorScheme:
    """Cinematic dark mode with neon mint accents"""
    
    # Primary Colors
    PRIMARY_DARK = "#0A0E27"           # Deep cinematic dark
    SECONDARY_DARK = "#141829"         # Slightly lighter dark
    BACKGROUND = PRIMARY_DARK
    
    # Accent Colors
    NEON_MINT = "#00D9FF"              # Primary accent
    NEON_MINT_LIGHT = "#00F0FF"        # Hover state
    ACCENT_PURPLE = "#9D4EDD"          # Secondary accent
    
    # Text Colors
    TEXT_PRIMARY = "#FFFFFF"           # Main text
    TEXT_SECONDARY = "#B0B0B0"         # Secondary text
    TEXT_TERTIARY = "#666666"          # Tertiary text
    
    # Status Colors
    SUCCESS_GREEN = "#00D977"          # Success state
    WARNING_ORANGE = "#FF6B35"         # Warning state
    ERROR_RED = "#FF4444"              # Error state
    INFO_CYAN = "#00CCFF"              # Info state


# ==================== TYPOGRAPHY ====================

class Typography:
    """Typography configuration"""
    
    FONT_FAMILY = "Arial"
    
    # Font Sizes
    HEADING_LARGE = 28
    HEADING_MEDIUM = 24
    HEADING_SMALL = 18
    SUBHEADING = 16
    BODY = 12
    SMALL = 10
    TINY = 8
    
    # Font Weights
    BOLD = "bold"
    SEMI_BOLD = "w600"
    NORMAL = "normal"
    LIGHT = "w300"
    
    # Letter Spacing
    NORMAL_SPACING = 0
    WIDE_SPACING = 2


# ==================== SPACING ====================

class Spacing:
    """Spacing and padding configuration"""
    
    PADDING_TINY = 5
    PADDING_SMALL = 10
    PADDING_MEDIUM = 15
    PADDING_LARGE = 20
    PADDING_XLARGE = 30
    
    SPACING_TINY = 5
    SPACING_SMALL = 8
    SPACING_MEDIUM = 10
    SPACING_LARGE = 20
    SPACING_XLARGE = 30


# ==================== BORDER RADIUS ====================

class BorderRadius:
    """Border radius configuration"""
    
    RADIUS_SMALL = 8
    RADIUS_MEDIUM = 10
    RADIUS_LARGE = 15
    RADIUS_XLARGE = 20


# ==================== VIDEO PROCESSING SETTINGS ====================

@dataclass
class ProcessingPreset:
    """Video processing quality preset"""
    
    name: str
    scale_factor: float
    brightness_boost: float
    saturation_factor: float
    denoise_strength: int
    sharpening_kernel: float
    target_bitrate: str


class ProcessingPresets:
    """Processing quality presets"""
    
    STANDARD = ProcessingPreset(
        name="Standard",
        scale_factor=1.0,
        brightness_boost=1.1,
        saturation_factor=1.1,
        denoise_strength=5,
        sharpening_kernel=1.0,
        target_bitrate="8 Mbps"
    )
    
    PREMIUM = ProcessingPreset(
        name="Premium",
        scale_factor=1.25,
        brightness_boost=1.15,
        saturation_factor=1.2,
        denoise_strength=8,
        sharpening_kernel=1.5,
        target_bitrate="15 Mbps"
    )
    
    PREMIUM_4K = ProcessingPreset(
        name="Premium 4K",
        scale_factor=1.5,
        brightness_boost=1.2,
        saturation_factor=1.3,
        denoise_strength=10,
        sharpening_kernel=2.0,
        target_bitrate="25 Mbps"
    )


# ==================== VIDEO CODECS & FORMATS ====================

class VideoCodec:
    """Supported video codecs"""
    
    H264 = "H.264"
    H265 = "H.265"
    VP9 = "VP9"
    AV1 = "AV1"


class VideoFormat:
    """Supported video formats"""
    
    FORMATS = {
        ".mp4": "MPEG-4 Video",
        ".mkv": "Matroska Video",
        ".avi": "Audio Video Interleave",
        ".mov": "QuickTime Movie",
        ".flv": "Flash Video",
        ".wmv": "Windows Media Video",
    }
    
    SUPPORTED_EXTENSIONS = list(FORMATS.keys())
    SUPPORTED_MIMES = [
        "video/mp4",
        "video/x-matroska",
        "video/x-msvideo",
        "video/quicktime",
        "video/x-flv",
        "video/x-msv-video",
    ]


# ==================== EXPORT QUALITY PRESETS ====================

class ExportQuality:
    """Export quality settings"""
    
    QUALITY_PRESETS = {
        "Low": {
            "resolution": "720p",
            "bitrate": "2 Mbps",
            "codec": "H.264"
        },
        "Medium": {
            "resolution": "1080p",
            "bitrate": "8 Mbps",
            "codec": "H.264"
        },
        "High": {
            "resolution": "1440p",
            "bitrate": "15 Mbps",
            "codec": "H.265"
        },
        "Ultra": {
            "resolution": "2160p (4K)",
            "bitrate": "25 Mbps",
            "codec": "H.265"
        },
    }


# ==================== UI/UX SETTINGS ====================

class UISettings:
    """User interface settings"""
    
    # Window Configuration
    DEFAULT_WIDTH = 400
    DEFAULT_HEIGHT = 800
    MIN_WIDTH = 350
    MIN_HEIGHT = 600
    
    # Animation Duration
    ANIMATION_FAST = 200
    ANIMATION_NORMAL = 300
    ANIMATION_SLOW = 500
    
    # Transition Effects
    ENABLE_FADE = True
    ENABLE_SCALE = True
    ENABLE_SLIDE = True
    
    # Hover Effects
    ENABLE_HOVER_EFFECTS = True
    HOVER_OPACITY = 0.8
    HOVER_SCALE = 1.05


# ==================== MESSAGES ====================

class Messages:
    """User-facing messages"""
    
    # Success Messages
    SUCCESS_UPLOAD = "Video selected successfully"
    SUCCESS_COMPLETE = "Enhancement completed!"
    SUCCESS_EXPORT = "Video exported successfully"
    
    # Error Messages
    ERROR_INVALID_FORMAT = "Invalid video format. Supported: MP4, MKV, AVI, MOV"
    ERROR_FILE_NOT_FOUND = "Video file not found"
    ERROR_PROCESSING_FAILED = "Processing failed. Please try again"
    ERROR_EXPORT_FAILED = "Export failed. Check storage space"
    ERROR_NO_VIDEO_SELECTED = "Please select a video first"
    
    # Warning Messages
    WARNING_LARGE_FILE = "Large file detected. Processing may take longer"
    WARNING_LOW_STORAGE = "Low storage space available"
    
    # Info Messages
    INFO_ANALYZING = "Analyzing video quality..."
    INFO_FILTERING = "Applying enhancement filters..."
    INFO_ENCODING = "Encoding output..."
    INFO_FINALIZING = "Finalizing..."
    
    # Status Messages
    STATUS_READY = "Ready to enhance"
    STATUS_PROCESSING = "Processing..."
    STATUS_CANCELLED = "Processing cancelled"
    STATUS_WAITING = "Waiting to process..."


# ==================== PROCESSING STAGES ====================

class ProcessingStages:
    """Video processing pipeline stages"""
    
    STAGES = [
        {
            "name": "Analyzing",
            "description": "Analyzing video quality...",
            "progress_range": (0, 30),
            "icon": "ANALYTICS"
        },
        {
            "name": "Filtering",
            "description": "Applying enhancement filters...",
            "progress_range": (30, 60),
            "icon": "TUNE"
        },
        {
            "name": "Encoding",
            "description": "Encoding output...",
            "progress_range": (60, 90),
            "icon": "VIDEOCAM"
        },
        {
            "name": "Finalizing",
            "description": "Finalizing...",
            "progress_range": (90, 100),
            "icon": "CHECK_CIRCLE"
        },
    ]


# ==================== SYSTEM REQUIREMENTS ====================

class SystemRequirements:
    """System requirements and recommendations"""
    
    MINIMUM = {
        "cpu": "Intel i5 / AMD Ryzen 5",
        "ram": "4 GB",
        "storage": "500 MB",
        "os": "Windows 10+, macOS 10.14+, Linux"
    }
    
    RECOMMENDED = {
        "cpu": "Intel i7 / AMD Ryzen 7",
        "ram": "16 GB",
        "storage": "5 GB SSD",
        "os": "Windows 10+, macOS 10.15+, Linux"
    }


# ==================== FEATURE FLAGS ====================

class FeatureFlags:
    """Feature enable/disable flags"""
    
    # Core Features
    VIDEO_UPLOAD = True
    REAL_TIME_PREVIEW = False  # Coming soon
    BATCH_PROCESSING = False   # Coming soon
    GPU_ACCELERATION = False   # Coming soon
    
    # UI Features
    DARK_MODE = True
    THEME_CUSTOMIZATION = False  # Coming soon
    LANGUAGE_SUPPORT = False     # Coming soon
    
    # Export Options
    EXPORT_MP4 = True
    EXPORT_MKV = False  # Coming soon
    CLOUD_EXPORT = False  # Coming soon


# ==================== API ENDPOINTS ====================

class APIConfig:
    """API configuration (for future cloud features)"""
    
    BASE_URL = "https://api.harbyenhancer.com"
    API_VERSION = "v1"
    TIMEOUT = 30
    
    ENDPOINTS = {
        "upload": "/upload",
        "process": "/process",
        "status": "/status",
        "download": "/download",
    }


# ==================== LOGGING ====================

class LoggingConfig:
    """Logging configuration"""
    
    LOG_LEVEL = "INFO"
    LOG_FILE = "harby_enhancer.log"
    MAX_LOG_SIZE = "10MB"
    LOG_RETENTION_DAYS = 30


# ==================== VERSION INFO ====================

class AppVersion:
    """Application version information"""
    
    MAJOR = 1
    MINOR = 0
    PATCH = 0
    BUILD = "2026.04.28"
    VERSION_STRING = f"{MAJOR}.{MINOR}.{PATCH}"
    
    AUTHOR = "MohammedHarby1"
    ORGANIZATION = "Harby Design"
    LICENSE = "MIT"
    GITHUB_URL = "https://github.com/MohammedHarby1/Harby-Enhancer"
