"""
Example Usage and Testing Script
Demonstrates how to use Harby Enhancer components
"""

from advanced_processor import (
    VideoEnhancementEngine,
    EnhancementMode,
    EnhancementSettings,
    BatchVideoProcessor,
)
from utils import logger, config_manager, FileManager, ValidationHelper, performance_monitor


def example_1_basic_enhancement():
    """Example 1: Basic video enhancement"""
    print("\n" + "="*50)
    print("Example 1: Basic Video Enhancement")
    print("="*50)
    
    # Create enhancement engine
    engine = VideoEnhancementEngine()
    
    # Define callbacks
    def on_progress(progress):
        percent = int(progress * 100)
        bar = "█" * (percent // 5) + "░" * ((100 - percent) // 5)
        print(f"\rProgress: [{bar}] {percent}%", end="")
    
    def on_status(status):
        print(f"\nStatus: {status}")
    
    # Set callbacks
    engine.set_callbacks(on_progress, on_status)
    
    # Enhance video
    logger.info("Starting basic video enhancement...")
    success = engine.enhance_video(
        input_path="input_video.mp4",
        output_path="output_enhanced.mp4",
        mode=EnhancementMode.STANDARD,
        use_threading=False,
    )
    
    if success:
        logger.success("Video enhancement completed!")
    else:
        logger.error("Video enhancement failed!")


def example_2_premium_4k_enhancement():
    """Example 2: Premium 4K enhancement"""
    print("\n" + "="*50)
    print("Example 2: Premium 4K Enhancement")
    print("="*50)
    
    engine = VideoEnhancementEngine()
    
    # Custom enhancement settings
    settings = EnhancementSettings(
        brightness=1.15,
        contrast=1.2,
        saturation=1.3,
        sharpness=1.5,
        denoise=10,
        blur_reduction=True,
        color_correction=True,
    )
    
    logger.info("Starting Premium 4K enhancement with custom settings...")
    performance_monitor.start_timer("4k_enhancement")
    
    success = engine.enhance_video(
        input_path="input_video.mp4",
        output_path="output_4k_enhanced.mp4",
        mode=EnhancementMode.PREMIUM_4K,
        settings=settings,
        use_threading=False,
    )
    
    elapsed = performance_monitor.end_timer("4k_enhancement")
    
    if success:
        logger.success(f"Premium 4K enhancement completed in {elapsed:.2f}s!")
    else:
        logger.error("Premium 4K enhancement failed!")


def example_3_batch_processing():
    """Example 3: Batch processing multiple videos"""
    print("\n" + "="*50)
    print("Example 3: Batch Video Processing")
    print("="*50)
    
    # Create batch processor
    batch = BatchVideoProcessor()
    
    # Add multiple videos to queue
    batch.add_video("video1.mp4", "video1_enhanced.mp4", EnhancementMode.STANDARD)
    batch.add_video("video2.mkv", "video2_enhanced.mkv", EnhancementMode.PREMIUM)
    batch.add_video("video3.avi", "video3_enhanced.avi", EnhancementMode.PREMIUM_4K)
    
    logger.info(f"Processing {len(batch.queue)} videos...")
    
    # Process all videos
    def on_progress(progress):
        percent = int(progress * 100)
        print(f"Video progress: {percent}%", end="\r")
    
    def on_status(status):
        print(f"Stage: {status}")
    
    batch.process_batch(on_progress, on_status)
    
    # Get status report
    status = batch.get_batch_status()
    logger.info(f"Batch Status: {status['completed']} completed, {status['failed']} failed")


def example_4_file_management():
    """Example 4: File management utilities"""
    print("\n" + "="*50)
    print("Example 4: File Management")
    print("="*50)
    
    filepath = "my_video.mp4"
    
    # Check file validity
    is_valid = ValidationHelper.is_valid_video_file(filepath)
    logger.info(f"Is valid video: {is_valid}")
    
    # Get file size
    if FileManager.file_exists(filepath):
        size = FileManager.get_file_size_formatted(filepath)
        logger.info(f"File size: {size}")
        
        # Get output filename
        output = FileManager.get_output_filename(filepath, "_enhanced")
        logger.info(f"Output will be: {output}")
    else:
        logger.warning(f"File not found: {filepath}")


def example_5_configuration_management():
    """Example 5: Configuration management"""
    print("\n" + "="*50)
    print("Example 5: Configuration Management")
    print("="*50)
    
    # Get configuration values
    app_name = config_manager.get("app_name")
    logger.info(f"App name: {app_name}")
    
    # Set configuration
    config_manager.set("last_used_preset", "Premium 4K")
    logger.info("Configuration updated!")
    
    # Add recent file
    config_manager.add_recent_file("path/to/video.mp4")
    recent = config_manager.get("recent_files")
    logger.info(f"Recent files: {recent}")


def example_6_performance_monitoring():
    """Example 6: Performance monitoring"""
    print("\n" + "="*50)
    print("Example 6: Performance Monitoring")
    print("="*50)
    
    import time
    
    # Simulate some operations
    for i in range(3):
        performance_monitor.start_timer("operation_1")
        time.sleep(0.5)
        performance_monitor.end_timer("operation_1")
        
        performance_monitor.start_timer("operation_2")
        time.sleep(0.3)
        performance_monitor.end_timer("operation_2")
    
    # Get report
    report = performance_monitor.get_report()
    print(report)


def example_7_custom_enhancement_settings():
    """Example 7: Using custom enhancement settings"""
    print("\n" + "="*50)
    print("Example 7: Custom Enhancement Settings")
    print("="*50)
    
    engine = VideoEnhancementEngine()
    
    # Create custom settings for different scenarios
    settings_profiles = {
        "bright_video": EnhancementSettings(
            brightness=0.9,  # Reduce brightness
            saturation=1.0,
            sharpness=1.0,
        ),
        "dark_video": EnhancementSettings(
            brightness=1.3,  # Increase brightness
            saturation=1.2,
            sharpness=1.2,
        ),
        "best_quality": EnhancementSettings(
            brightness=1.15,
            contrast=1.2,
            saturation=1.3,
            sharpness=1.5,
            denoise=10,
            blur_reduction=True,
            color_correction=True,
        ),
    }
    
    # Use a profile
    profile = settings_profiles["best_quality"]
    logger.info(f"Using profile with brightness: {profile.brightness}, saturation: {profile.saturation}")


def print_menu():
    """Print example menu"""
    print("\n" + "="*50)
    print("HARBY ENHANCER - EXAMPLE USAGE")
    print("="*50)
    print("\n1. Basic Enhancement")
    print("2. Premium 4K Enhancement")
    print("3. Batch Processing")
    print("4. File Management")
    print("5. Configuration Management")
    print("6. Performance Monitoring")
    print("7. Custom Settings")
    print("0. Exit")
    print("\n" + "="*50)


def main():
    """Main example runner"""
    print("\n🎬 Harby Enhancer - Example Usage Scripts\n")
    
    examples = {
        "1": ("Basic Enhancement", example_1_basic_enhancement),
        "2": ("Premium 4K Enhancement", example_2_premium_4k_enhancement),
        "3": ("Batch Processing", example_3_batch_processing),
        "4": ("File Management", example_4_file_management),
        "5": ("Configuration Management", example_5_configuration_management),
        "6": ("Performance Monitoring", example_6_performance_monitoring),
        "7": ("Custom Settings", example_7_custom_enhancement_settings),
    }
    
    print_menu()
    
    # Run all examples
    print("\n📊 Running all examples...\n")
    
    try:
        example_4_file_management()
        example_5_configuration_management()
        example_6_performance_monitoring()
        example_7_custom_enhancement_settings()
        
        logger.success("✅ All examples completed!")
        
    except Exception as e:
        logger.error(f"Error running examples: {str(e)}")
    
    print("\n" + "="*50)
    print("Examples completed! Check the logs above.")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
