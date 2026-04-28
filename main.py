import flet as ft
from flet import icons
import os
from datetime import datetime


class HarbyEnhancer:
    def __init__(self):
        self.video_path = None
        self.is_premium_4k = False
        self.is_processing = False
        
    def main(self, page: ft.Page):
        page.title = "Harby Enhancer - Professional Video Enhancement"
        page.window.width = 400
        page.window.height = 800
        page.window.min_width = 350
        page.window.min_height = 600
        
        # Color Scheme - Cinematic Dark Mode with Neon Mint
        self.primary_dark = "#0A0E27"      # Deep cinematic dark
        self.secondary_dark = "#141829"    # Slightly lighter dark
        self.neon_mint = "#00D9FF"         # Neon mint accent
        self.neon_mint_light = "#00F0FF"   # Lighter mint for hover
        self.accent_purple = "#9D4EDD"     # Purple accent
        self.text_primary = "#FFFFFF"      # Primary text
        self.text_secondary = "#B0B0B0"    # Secondary text
        self.success_green = "#00D977"     # Success state
        self.warning_orange = "#FF6B35"    # Warning state
        
        page.bgcolor = self.primary_dark
        page.padding = 0
        
        # Main Container
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.create_header(),
                    self.create_status_section(),
                    self.create_upload_section(),
                    self.create_premium_switch_section(),
                    self.create_progress_section(),
                    self.create_action_buttons(),
                    ft.Divider(height=20, color="transparent"),
                    self.create_footer(),
                ],
                scroll="auto",
                spacing=20,
            ),
            padding=20,
            bgcolor=self.primary_dark,
            expand=True,
        )
        
        page.add(main_container)
    
    def create_header(self) -> ft.Container:
        """Create the header with branding"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        name=icons.VIDEO_LIBRARY,
                        size=50,
                        color=self.neon_mint,
                    ),
                    ft.Text(
                        "HARBY",
                        size=28,
                        weight="bold",
                        color=self.text_primary,
                        font_family="Arial",
                    ),
                    ft.Text(
                        "ENHANCER",
                        size=16,
                        weight="w300",
                        color=self.neon_mint,
                        letter_spacing=2,
                    ),
                    ft.Text(
                        "Professional Video Enhancement System",
                        size=11,
                        color=self.text_secondary,
                        italic=True,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
            padding=20,
            bgcolor=self.secondary_dark,
            border_radius=15,
            border=ft.border.all(1, self.neon_mint),
            shadow=ft.BoxShadow(
                blur_radius=20,
                spread_radius=0,
                color=f"{self.neon_mint}30",
                offset=ft.Offset(0, 4),
            ),
        )
    
    def create_status_section(self) -> ft.Container:
        """Create the status display section"""
        self.status_text = ft.Text(
            "Ready to enhance",
            size=12,
            color=self.success_green,
            weight="w500",
        )
        
        self.file_info_text = ft.Text(
            "No video selected",
            size=11,
            color=self.text_secondary,
            italic=True,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=icons.INFO, size=16, color=self.neon_mint),
                            self.status_text,
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    self.file_info_text,
                ],
                spacing=8,
            ),
            padding=15,
            bgcolor=self.secondary_dark,
            border_radius=10,
            border=ft.border.all(1, f"{self.neon_mint}40"),
        )
    
    def create_upload_section(self) -> ft.Container:
        """Create the video upload section"""
        self.upload_button = ft.IconButton(
            icon=icons.CLOUD_UPLOAD,
            icon_size=40,
            icon_color=self.neon_mint,
            on_click=self.on_upload_click,
            tooltip="Select video file",
        )
        
        upload_label = ft.Text(
            "Upload Video",
            size=14,
            weight="bold",
            color=self.text_primary,
        )
        
        upload_hint = ft.Text(
            "MP4, MKV, AVI, MOV",
            size=10,
            color=self.text_secondary,
        )
        
        return ft.Container(
            content=ft.GestureDetector(
                on_tap=self.on_upload_click,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            self.upload_button,
                            upload_label,
                            upload_hint,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                    ),
                    padding=30,
                    bgcolor=f"{self.neon_mint}10",
                    border_radius=15,
                    border=ft.border.all(2, self.neon_mint),
                ),
            ),
            on_hover=self.on_upload_hover,
        )
    
    def create_premium_switch_section(self) -> ft.Container:
        """Create the Premium 4K switch section"""
        self.premium_switch = ft.Switch(
            label="Premium 4K Enhancement",
            value=False,
            on_change=self.on_premium_toggle,
            label_position=ft.LabelPosition.LEFT,
            active_color=self.neon_mint,
            inactive_track_color=self.text_secondary,
        )
        
        premium_info = ft.Text(
            "Enhanced processing for ultra-high-definition output",
            size=10,
            color=self.text_secondary,
            italic=True,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(
                                name=icons.HD if self.is_premium_4k else icons.SETTINGS,
                                size=18,
                                color=self.neon_mint,
                            ),
                            self.premium_switch,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    premium_info,
                ],
                spacing=10,
            ),
            padding=15,
            bgcolor=self.secondary_dark,
            border_radius=10,
            border=ft.border.all(1, f"{self.neon_mint}40"),
        )
    
    def create_progress_section(self) -> ft.Container:
        """Create the progress bar section"""
        self.progress_bar = ft.ProgressBar(
            value=0,
            color=self.neon_mint,
            bgcolor=f"{self.neon_mint}20",
            min_height=6,
        )
        
        self.progress_text = ft.Text(
            "0%",
            size=12,
            color=self.neon_mint,
            weight="bold",
        )
        
        self.processing_status = ft.Text(
            "Waiting to process...",
            size=11,
            color=self.text_secondary,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Processing Progress", size=12, weight="bold", color=self.text_primary),
                            self.progress_text,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.progress_bar,
                    self.processing_status,
                ],
                spacing=10,
            ),
            padding=15,
            bgcolor=self.secondary_dark,
            border_radius=10,
            border=ft.border.all(1, f"{self.neon_mint}40"),
            visible=True,
        )
    
    def create_action_buttons(self) -> ft.Container:
        """Create the action buttons section"""
        self.enhance_button = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=icons.PLAY_CIRCLE, size=20, color=self.text_primary),
                    ft.Text("Start Enhancement", weight="bold", color=self.text_primary),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            on_click=self.on_enhance_click,
            padding=15,
            bgcolor=self.neon_mint,
            border_radius=10,
            ink=True,
            ink_color=f"{self.text_primary}20",
        )
        
        self.cancel_button = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=icons.STOP_CIRCLE, size=20, color=self.text_primary),
                    ft.Text("Cancel", weight="bold", color=self.text_primary),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            on_click=self.on_cancel_click,
            padding=15,
            bgcolor=self.warning_orange,
            border_radius=10,
            ink=True,
            ink_color=f"{self.text_primary}20",
            visible=False,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.enhance_button,
                    self.cancel_button,
                ],
                spacing=10,
            ),
        )
    
    def create_footer(self) -> ft.Container:
        """Create the footer section"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Divider(color=f"{self.neon_mint}40", height=1),
                    ft.Text(
                        "© 2026 Harby Design | Professional Video Enhancement",
                        size=9,
                        color=self.text_secondary,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        f"Version 1.0.0 | Built with Flet",
                        size=8,
                        color=f"{self.text_secondary}80",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            padding=15,
        )
    
    # Event Handlers
    def on_upload_hover(self, e):
        """Handle upload button hover"""
        if e.data == "true":
            e.control.content.bgcolor = f"{self.neon_mint}20"
        else:
            e.control.content.bgcolor = f"{self.neon_mint}10"
        e.control.update()
    
    def on_upload_click(self, e):
        """Handle video upload"""
        self.video_path = "sample_video.mp4"  # In real implementation, use file picker
        self.status_text.value = "Video selected"
        self.status_text.color = self.neon_mint
        self.file_info_text.value = f"File: {self.video_path}"
        self.file_info_text.update()
        self.status_text.update()
    
    def on_premium_toggle(self, e):
        """Handle Premium 4K toggle"""
        self.is_premium_4k = self.premium_switch.value
        print(f"Premium 4K: {self.is_premium_4k}")
    
    def on_enhance_click(self, e):
        """Handle enhancement start"""
        if not self.video_path:
            self.status_text.value = "Please select a video first"
            self.status_text.color = self.warning_orange
            self.status_text.update()
            return
        
        self.is_processing = True
        self.enhance_button.visible = False
        self.cancel_button.visible = True
        self.status_text.value = "Processing..."
        self.status_text.color = self.neon_mint
        self.processing_status.value = f"Enhancing with {'Premium 4K' if self.is_premium_4k else 'Standard'} mode"
        
        # Simulate progress
        self.simulate_processing()
        
        self.enhance_button.update()
        self.cancel_button.update()
        self.status_text.update()
        self.processing_status.update()
    
    def simulate_processing(self):
        """Simulate video processing with progress updates"""
        import time
        import threading
        
        def process():
            for i in range(101):
                self.progress_bar.value = i / 100
                self.progress_text.value = f"{i}%"
                
                if i < 30:
                    self.processing_status.value = "Analyzing video quality..."
                elif i < 60:
                    self.processing_status.value = "Applying enhancement filters..."
                elif i < 90:
                    self.processing_status.value = "Encoding output..."
                else:
                    self.processing_status.value = "Finalizing..."
                
                self.progress_bar.update()
                self.progress_text.update()
                self.processing_status.update()
                time.sleep(0.1)
            
            # Complete
            self.status_text.value = "Enhancement completed!"
            self.status_text.color = self.success_green
            self.processing_status.value = "Ready for export"
            self.is_processing = False
            self.enhance_button.visible = True
            self.cancel_button.visible = False
            
            self.status_text.update()
            self.processing_status.update()
            self.enhance_button.update()
            self.cancel_button.update()
        
        thread = threading.Thread(target=process, daemon=True)
        thread.start()
    
    def on_cancel_click(self, e):
        """Handle processing cancellation"""
        self.is_processing = False
        self.enhance_button.visible = True
        self.cancel_button.visible = False
        self.progress_bar.value = 0
        self.progress_text.value = "0%"
        self.status_text.value = "Processing cancelled"
        self.status_text.color = self.warning_orange
        self.processing_status.value = "Waiting to process..."
        
        self.enhance_button.update()
        self.cancel_button.update()
        self.progress_bar.update()
        self.progress_text.update()
        self.status_text.update()
        self.processing_status.update()


def main():
    app = HarbyEnhancer()
    ft.app(target=app.main)


if __name__ == "__main__":
    main()
