"""
Video Processor Module
Professional video enhancement and processing engine for Harby Enhancer
"""

import cv2
import numpy as np
from enum import Enum
from typing import Callable, Optional, Dict, List
from dataclasses import dataclass
from config import ProcessingPresets, VideoFormat, Messages


class ProcessingStatus(Enum):
    """Processing status enum"""
    
    IDLE = "idle"
    ANALYZING = "analyzing"
    FILTERING = "filtering"
    ENCODING = "encoding"
    FINALIZING = "finalizing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class VideoMetadata:
    """Video metadata container"""
    
    filename: str
    filepath: str
    duration: float
    fps: float
    resolution: tuple
    bitrate: str
    codec: str
    file_size_mb: float
    format_type: str


class VideoAnalyzer:
    """Analyze video files for quality and metadata"""
    
    @staticmethod
    def analyze_video(filepath: str) -> Optional[VideoMetadata]:
        """
        Analyze video file and extract metadata
        
        Args:
            filepath: Path to video file
            
        Returns:
            VideoMetadata object or None if analysis fails
        """
        try:
            cap = cv2.VideoCapture(filepath)
            
            if not cap.isOpened():
                return None
            
            # Extract metadata
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            duration = frame_count / fps if fps > 0 else 0
            
            # Estimate bitrate
            file_size_mb = VideoAnalyzer._get_file_size_mb(filepath)
            bitrate = f"{int((file_size_mb * 8) / (duration / 60)) if duration > 0 else 0} Mbps"
            
            cap.release()
            
            return VideoMetadata(
                filename=filepath.split('/')[-1],
                filepath=filepath,
                duration=duration,
                fps=fps,
                resolution=(width, height),
                bitrate=bitrate,
                codec="H.264",
                file_size_mb=file_size_mb,
                format_type=VideoAnalyzer._detect_format(filepath),
            )
        except Exception as e:
            print(f"Error analyzing video: {e}")
            return None
    
    @staticmethod
    def _get_file_size_mb(filepath: str) -> float:
        """Get file size in MB"""
        try:
            import os
            return os.path.getsize(filepath) / (1024 * 1024)
        except:
            return 0.0
    
    @staticmethod
    def _detect_format(filepath: str) -> str:
        """Detect video format from extension"""
        ext = filepath.lower().split('.')[-1]
        return VideoFormat.FORMATS.get(f".{ext}", "Unknown")
    
    @staticmethod
    def validate_format(filepath: str) -> bool:
        """Validate if file format is supported"""
        ext = '.' + filepath.lower().split('.')[-1]
        return ext in VideoFormat.SUPPORTED_EXTENSIONS


class VideoProcessor:
    """Main video processing and enhancement engine"""
    
    def __init__(self):
        """Initialize processor"""
        self.status = ProcessingStatus.IDLE
        self.current_progress = 0
        self.progress_callback: Optional[Callable] = None
        self.status_callback: Optional[Callable] = None
    
    def set_progress_callback(self, callback: Callable):
        """Set callback for progress updates"""
        self.progress_callback = callback
    
    def set_status_callback(self, callback: Callable):
        """Set callback for status updates"""
        self.status_callback = callback
    
    def process_video(
        self,
        input_path: str,
        output_path: str,
        preset_name: str = "Standard",
        is_4k: bool = False,
    ) -> bool:
        """
        Process video with enhancement
        
        Args:
            input_path: Path to input video
            output_path: Path for output video
            preset_name: Processing preset name
            is_4k: Enable 4K processing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Select processing preset
            if is_4k:
                preset = ProcessingPresets.PREMIUM_4K
            elif preset_name == "Premium":
                preset = ProcessingPresets.PREMIUM
            else:
                preset = ProcessingPresets.STANDARD
            
            # Validate input
            if not VideoAnalyzer.validate_format(input_path):
                print(Messages.ERROR_INVALID_FORMAT)
                self._update_status(ProcessingStatus.FAILED)
                return False
            
            # Analyze video
            self._update_status(ProcessingStatus.ANALYZING)
            metadata = VideoAnalyzer.analyze_video(input_path)
            if not metadata:
                print(Messages.ERROR_FILE_NOT_FOUND)
                self._update_status(ProcessingStatus.FAILED)
                return False
            
            self._update_progress(0.3)
            
            # Apply filters and enhancement
            self._update_status(ProcessingStatus.FILTERING)
            success = self._apply_enhancements(
                input_path,
                output_path,
                metadata,
                preset,
            )
            
            if not success:
                print(Messages.ERROR_PROCESSING_FAILED)
                self._update_status(ProcessingStatus.FAILED)
                return False
            
            self._update_progress(0.9)
            
            # Finalize
            self._update_status(ProcessingStatus.FINALIZING)
            self._update_progress(1.0)
            self._update_status(ProcessingStatus.COMPLETED)
            
            return True
            
        except Exception as e:
            print(f"Processing error: {e}")
            self._update_status(ProcessingStatus.FAILED)
            return False
    
    def _apply_enhancements(
        self,
        input_path: str,
        output_path: str,
        metadata: VideoMetadata,
        preset,
    ) -> bool:
        """
        Apply enhancement filters to video
        
        Args:
            input_path: Input video path
            output_path: Output video path
            metadata: Video metadata
            preset: Processing preset
            
        Returns:
            True if successful
        """
        try:
            cap = cv2.VideoCapture(input_path)
            
            # Setup video writer
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(
                output_path,
                fourcc,
                metadata.fps,
                metadata.resolution,
            )
            
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            processed_frames = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Apply enhancements
                enhanced = self._enhance_frame(frame, preset)
                out.write(enhanced)
                
                processed_frames += 1
                progress = 0.3 + (processed_frames / frame_count) * 0.6
                self._update_progress(progress)
            
            cap.release()
            out.release()
            
            return True
            
        except Exception as e:
            print(f"Enhancement error: {e}")
            return False
    
    def _enhance_frame(self, frame: np.ndarray, preset) -> np.ndarray:
        """
        Apply enhancement to a single frame
        
        Args:
            frame: Input frame
            preset: Processing preset
            
        Returns:
            Enhanced frame
        """
        enhanced = frame.copy()
        
        # Apply brightness and contrast
        enhanced = self._adjust_brightness_contrast(
            enhanced,
            preset.brightness_boost,
        )
        
        # Enhance saturation
        enhanced = self._adjust_saturation(
            enhanced,
            preset.saturation_factor,
        )
        
        # Apply denoising
        if preset.denoise_strength > 0:
            enhanced = cv2.fastNlMeansDenoisingColored(
                enhanced,
                h=preset.denoise_strength,
                hForColorComponents=preset.denoise_strength,
                templateWindowSize=7,
                searchWindowSize=21,
            )
        
        # Apply sharpening
        if preset.sharpening_kernel > 0:
            enhanced = self._apply_sharpening(
                enhanced,
                preset.sharpening_kernel,
            )
        
        return enhanced
    
    @staticmethod
    def _adjust_brightness_contrast(
        frame: np.ndarray,
        brightness_factor: float,
    ) -> np.ndarray:
        """Adjust brightness and contrast"""
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        l = cv2.convertScaleAbs(l, alpha=brightness_factor, beta=0)
        l = np.clip(l, 0, 255).astype(np.uint8)
        
        enhanced_lab = cv2.merge([l, a, b])
        return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    @staticmethod
    def _adjust_saturation(
        frame: np.ndarray,
        saturation_factor: float,
    ) -> np.ndarray:
        """Adjust color saturation"""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 1] = hsv[:, :, 1] * saturation_factor
        hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
        
        return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    
    @staticmethod
    def _apply_sharpening(
        frame: np.ndarray,
        strength: float,
    ) -> np.ndarray:
        """Apply sharpening filter"""
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ]) / 1.0
        
        sharpened = cv2.filter2D(frame, -1, kernel * strength)
        
        return cv2.addWeighted(frame, 1 - strength * 0.2, sharpened, strength * 0.2, 0)
    
    def _update_progress(self, progress: float):
        """Update progress"""
        self.current_progress = max(0, min(1, progress))
        if self.progress_callback:
            self.progress_callback(self.current_progress)
    
    def _update_status(self, status: ProcessingStatus):
        """Update status"""
        self.status = status
        if self.status_callback:
            self.status_callback(status)


class ProcessingQueue:
    """Manage batch video processing"""
    
    def __init__(self):
        """Initialize queue"""
        self.queue: List[Dict] = []
        self.processor = VideoProcessor()
        self.current_index = 0
    
    def add_task(
        self,
        input_path: str,
        output_path: str,
        preset_name: str = "Standard",
        is_4k: bool = False,
    ):
        """Add task to queue"""
        self.queue.append({
            "input": input_path,
            "output": output_path,
            "preset": preset_name,
            "is_4k": is_4k,
        })
    
    def process_queue(self) -> bool:
        """Process all queued tasks"""
        for self.current_index, task in enumerate(self.queue):
            success = self.processor.process_video(
                task["input"],
                task["output"],
                task["preset"],
                task["is_4k"],
            )
            
            if not success:
                return False
        
        return True
    
    def get_queue_status(self) -> Dict:
        """Get current queue status"""
        return {
            "total": len(self.queue),
            "current": self.current_index + 1,
            "completed": self.current_index,
            "remaining": len(self.queue) - self.current_index - 1,
        }
