"""
UI Components Module
Custom UI components for professional Harby Enhancer interface
"""

import flet as ft
from typing import Callable, Optional, List
from config import ColorScheme, Typography, Spacing, BorderRadius, UISettings


class HarbyTheme:
    """Centralized theme management"""
    
    @staticmethod
    def get_primary_color() -> str:
        """Get primary accent color"""
        return ColorScheme.NEON_MINT
    
    @staticmethod
    def get_bg_color() -> str:
        """Get background color"""
        return ColorScheme.PRIMARY_DARK
    
    @staticmethod
    def get_secondary_bg_color() -> str:
        """Get secondary background color"""
        return ColorScheme.SECONDARY_DARK
    
    @staticmethod
    def get_text_color() -> str:
        """Get primary text color"""
        return ColorScheme.TEXT_PRIMARY
    
    @staticmethod
    def get_success_color() -> str:
        """Get success color"""
        return ColorScheme.SUCCESS_GREEN
    
    @staticmethod
    def get_warning_color() -> str:
        """Get warning color"""
        return ColorScheme.WARNING_ORANGE
    
    @staticmethod
    def get_error_color() -> str:
        """Get error color"""
        return ColorScheme.ERROR_RED


class HarbyContainer(ft.Container):
    """Custom themed container with cinematic styling"""
    
    def __init__(
        self,
        content: ft.Control,
        padding: int = Spacing.PADDING_MEDIUM,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        shadow: bool = True,
        border_radius: int = BorderRadius.RADIUS_MEDIUM,
        **kwargs
    ):
        """
        Initialize Harby container
        
        Args:
            content: Container content
            padding: Internal padding
            background_color: Background color (default: secondary dark)
            border_color: Border color (default: neon mint transparent)
            shadow: Enable shadow effect
            border_radius: Corner radius
        """
        bg_color = background_color or ColorScheme.SECONDARY_DARK
        border = border_color or f"{ColorScheme.NEON_MINT}40"
        
        super().__init__(
            content=content,
            padding=padding,
            bgcolor=bg_color,
            border_radius=border_radius,
            border=ft.border.all(1, border),
            shadow=ft.BoxShadow(
                blur_radius=20,
                spread_radius=0,
                color=f"{ColorScheme.NEON_MINT}30",
                offset=ft.Offset(0, 4),
            ) if shadow else None,
            **kwargs
        )


class HarbyButton(ft.Container):
    """Custom themed button with hover effects"""
    
    def __init__(
        self,
        text: str,
        on_click: Callable,
        icon: Optional[str] = None,
        primary: bool = True,
        **kwargs
    ):
        """
        Initialize Harby button
        
        Args:
            text: Button text
            on_click: Click handler
            icon: Icon name (optional)
            primary: Use primary color (True) or secondary (False)
        """
        self.primary = primary
        self.text = text
        self.icon = icon
        
        controls = []
        if icon:
            controls.append(
                ft.Icon(
                    name=icon,
                    size=20,
                    color=ColorScheme.TEXT_PRIMARY
                )
            )
        
        controls.append(
            ft.Text(
                text,
                weight=Typography.BOLD,
                color=ColorScheme.TEXT_PRIMARY
            )
        )
        
        bg_color = ColorScheme.NEON_MINT if primary else ColorScheme.SECONDARY_DARK
        border_color = ColorScheme.NEON_MINT if not primary else None
        
        super().__init__(
            content=ft.Row(
                controls=controls,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=Spacing.SPACING_MEDIUM,
            ),
            on_click=on_click,
            padding=Spacing.PADDING_MEDIUM,
            bgcolor=bg_color,
            border_radius=BorderRadius.RADIUS_MEDIUM,
            border=ft.border.all(1, border_color) if not primary else None,
            ink=True,
            ink_color=f"{ColorScheme.TEXT_PRIMARY}20",
            **kwargs
        )
    
    def on_hover(self, e):
        """Handle hover effect"""
        if e.data == "true":
            self.bgcolor = (
                ColorScheme.NEON_MINT_LIGHT if self.primary 
                else f"{ColorScheme.NEON_MINT}20"
            )
        else:
            self.bgcolor = (
                ColorScheme.NEON_MINT if self.primary 
                else ColorScheme.SECONDARY_DARK
            )
        self.update()


class HarbyProgressBar(ft.Container):
    """Advanced progress bar with animation"""
    
    def __init__(self, **kwargs):
        """Initialize progress bar"""
        self.progress = 0
        self.progress_bar = ft.ProgressBar(
            value=0,
            color=ColorScheme.NEON_MINT,
            bgcolor=f"{ColorScheme.NEON_MINT}20",
            min_height=6,
        )
        
        self.progress_text = ft.Text(
            "0%",
            size=Typography.SMALL,
            color=ColorScheme.NEON_MINT,
            weight=Typography.BOLD,
        )
        
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Progress",
                                size=Typography.BODY,
                                weight=Typography.BOLD,
                                color=ColorScheme.TEXT_PRIMARY,
                            ),
                            self.progress_text,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.progress_bar,
                ],
                spacing=Spacing.SPACING_SMALL,
            ),
            **kwargs
        )
    
    def set_progress(self, value: float):
        """Set progress value"""
        self.progress = max(0, min(1, value))
        self.progress_bar.value = self.progress
        self.progress_text.value = f"{int(self.progress * 100)}%"
        self.update()


class HarbyStatusCard(ft.Container):
    """Status display card"""
    
    def __init__(
        self,
        title: str,
        status: str,
        color: Optional[str] = None,
        icon: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize status card
        
        Args:
            title: Card title
            status: Status text
            color: Status color
            icon: Status icon
        """
        color = color or ColorScheme.SUCCESS_GREEN
        
        controls = []
        if icon:
            controls.append(
                ft.Icon(
                    name=icon,
                    size=16,
                    color=color,
                )
            )
        
        controls.append(
            ft.Text(
                status,
                size=Typography.SMALL,
                color=color,
                weight=Typography.SEMI_BOLD,
            )
        )
        
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Text(
                        title,
                        size=Typography.BODY,
                        weight=Typography.BOLD,
                        color=ColorScheme.TEXT_PRIMARY,
                    ),
                    ft.Row(
                        controls=controls,
                        spacing=Spacing.SPACING_MEDIUM,
                    ),
                ],
                spacing=Spacing.SPACING_SMALL,
            ),
            padding=Spacing.PADDING_MEDIUM,
            bgcolor=ColorScheme.SECONDARY_DARK,
            border_radius=BorderRadius.RADIUS_MEDIUM,
            border=ft.border.all(1, f"{color}40"),
            **kwargs
        )


class AnimationHelper:
    """Helper for smooth animations and transitions"""
    
    @staticmethod
    def fade_animation(control: ft.Control, duration_ms: int = 300):
        """Apply fade animation"""
        control.animate_opacity(
            duration_ms=duration_ms,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )
    
    @staticmethod
    def scale_animation(control: ft.Control, duration_ms: int = 300):
        """Apply scale animation"""
        control.animate_scale(
            duration_ms=duration_ms,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )
    
    @staticmethod
    def slide_animation(control: ft.Control, duration_ms: int = 300):
        """Apply slide animation"""
        control.animate_offset(
            duration_ms=duration_ms,
            curve=ft.AnimationCurve.EASE_IN_OUT,
        )


class ResponsiveLayout(ft.Container):
    """Responsive layout helper for mobile/tablet"""
    
    def __init__(
        self,
        content_mobile: ft.Control,
        content_tablet: Optional[ft.Control] = None,
        **kwargs
    ):
        """
        Initialize responsive layout
        
        Args:
            content_mobile: Content for mobile view
            content_tablet: Content for tablet view (optional)
        """
        self.content_mobile = content_mobile
        self.content_tablet = content_tablet or content_mobile
        
        super().__init__(
            content=content_mobile,
            expand=True,
            **kwargs
        )
    
    def adapt_layout(self, width: int):
        """Adapt layout based on width"""
        if width > 600:
            self.content = self.content_tablet
        else:
            self.content = self.content_mobile
        self.update()


class HarbyForm(ft.Container):
    """Custom form component"""
    
    def __init__(self, fields: List[dict], on_submit: Callable, **kwargs):
        """
        Initialize form
        
        Args:
            fields: List of field configurations
            on_submit: Form submission handler
        """
        self.fields = {}
        controls = []
        
        for field in fields:
            field_name = field.get("name")
            field_label = field.get("label", "")
            field_type = field.get("type", "text")
            
            label = ft.Text(
                field_label,
                size=Typography.SMALL,
                weight=Typography.SEMI_BOLD,
                color=ColorScheme.TEXT_PRIMARY,
            )
            
            if field_type == "text":
                input_field = ft.TextField(
                    label=field_label,
                    bgcolor=ColorScheme.SECONDARY_DARK,
                    color=ColorScheme.TEXT_PRIMARY,
                    border_color=ColorScheme.NEON_MINT,
                )
            elif field_type == "password":
                input_field = ft.TextField(
                    label=field_label,
                    password=True,
                    bgcolor=ColorScheme.SECONDARY_DARK,
                    color=ColorScheme.TEXT_PRIMARY,
                    border_color=ColorScheme.NEON_MINT,
                )
            elif field_type == "dropdown":
                input_field = ft.Dropdown(
                    options=[
                        ft.dropdown.Option(opt) for opt in field.get("options", [])
                    ],
                    bgcolor=ColorScheme.SECONDARY_DARK,
                    color=ColorScheme.TEXT_PRIMARY,
                )
            else:
                input_field = ft.TextField()
            
            self.fields[field_name] = input_field
            controls.append(label)
            controls.append(input_field)
        
        submit_button = HarbyButton(
            text="Submit",
            on_click=lambda e: on_submit(self.get_values()),
        )
        
        controls.append(submit_button)
        
        super().__init__(
            content=ft.Column(
                controls=controls,
                spacing=Spacing.SPACING_MEDIUM,
            ),
            padding=Spacing.PADDING_LARGE,
            **kwargs
        )
    
    def get_values(self) -> dict:
        """Get all field values"""
        return {name: field.value for name, field in self.fields.items()}


class NotificationManager:
    """Manage notifications and alerts"""
    
    @staticmethod
    def show_success(page: ft.Page, message: str, duration_ms: int = 3000):
        """Show success notification"""
        snack_bar = ft.SnackBar(
            ft.Text(
                message,
                color=ColorScheme.SUCCESS_GREEN,
            ),
            bgcolor=ColorScheme.SECONDARY_DARK,
            duration=duration_ms,
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
    
    @staticmethod
    def show_error(page: ft.Page, message: str, duration_ms: int = 4000):
        """Show error notification"""
        snack_bar = ft.SnackBar(
            ft.Text(
                message,
                color=ColorScheme.ERROR_RED,
            ),
            bgcolor=ColorScheme.SECONDARY_DARK,
            duration=duration_ms,
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
    
    @staticmethod
    def show_warning(page: ft.Page, message: str, duration_ms: int = 3500):
        """Show warning notification"""
        snack_bar = ft.SnackBar(
            ft.Text(
                message,
                color=ColorScheme.WARNING_ORANGE,
            ),
            bgcolor=ColorScheme.SECONDARY_DARK,
            duration=duration_ms,
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
