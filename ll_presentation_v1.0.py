#!/usr/bin/env python3
"""
Interactive HTML Presentation Generator v1.0
Creates beautiful, interactive HTML-based presentations with smooth transitions.
"""

import os
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path


class Slide:
    """Represents a single slide in the presentation."""
    
    def __init__(
        self,
        title: str,
        content: str,
        slide_type: str = "default",
        background: Optional[str] = None,
        notes: Optional[str] = None
    ):
        self.title = title
        self.content = content
        self.slide_type = slide_type  # default, title, section, two-column, image
        self.background = background
        self.notes = notes


class PresentationGenerator:
    """Generates interactive HTML presentations."""
    
    def __init__(self, title: str, author: str = "", theme: str = "dark"):
        self.title = title
        self.author = author
        self.theme = theme  # dark, light, gradient
        self.slides: List[Slide] = []
        
    def add_slide(
        self,
        title: str,
        content: str,
        slide_type: str = "default",
        background: Optional[str] = None,
        notes: Optional[str] = None
    ) -> None:
        """Add a slide to the presentation."""
        slide = Slide(title, content, slide_type, background, notes)
        self.slides.append(slide)
    
    def _get_theme_colors(self) -> Dict[str, str]:
        """Get color scheme based on theme."""
        themes = {
            "dark": {
                "primary": "#6366f1",
                "secondary": "#8b5cf6",
                "background": "#0f172a",
                "surface": "#1e293b",
                "text": "#f1f5f9",
                "text-secondary": "#94a3b8",
                "accent": "#f59e0b"
            },
            "light": {
                "primary": "#4f46e5",
                "secondary": "#7c3aed",
                "background": "#ffffff",
                "surface": "#f8fafc",
                "text": "#0f172a",
                "text-secondary": "#64748b",
                "accent": "#f59e0b"
            },
            "gradient": {
                "primary": "#ec4899",
                "secondary": "#8b5cf6",
                "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                "surface": "rgba(255, 255, 255, 0.1)",
                "text": "#ffffff",
                "text-secondary": "#e2e8f0",
                "accent": "#fbbf24"
            }
        }
        return themes.get(self.theme, themes["dark"])
    
    def _generate_css(self) -> str:
        """Generate CSS styles for the presentation."""
        colors = self._get_theme_colors()
        
        return f"""
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        :root {{
            --primary: {colors['primary']};
            --secondary: {colors['secondary']};
            --background: {colors['background']};
            --surface: {colors['surface']};
            --text: {colors['text']};
            --text-secondary: {colors['text-secondary']};
            --accent: {colors['accent']};
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--background);
            color: var(--text);
            overflow: hidden;
            height: 100vh;
        }}
        
        .presentation-container {{
            width: 100%;
            height: 100vh;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .slide {{
            width: 90%;
            max-width: 1200px;
            height: 80vh;
            background: var(--surface);
            border-radius: 24px;
            padding: 60px 80px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            display: none;
            flex-direction: column;
            position: relative;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .slide.active {{
            display: flex;
            animation: slideIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        
        @keyframes slideIn {{
            from {{
                opacity: 0;
                transform: translateY(30px) scale(0.95);
            }}
            to {{
                opacity: 1;
                transform: translateY(0) scale(1);
            }}
        }}
        
        .slide-title {{
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 40px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
        }}
        
        .slide-content {{
            flex: 1;
            font-size: 1.5rem;
            line-height: 1.8;
            color: var(--text-secondary);
            overflow-y: auto;
        }}
        
        .slide-content h2 {{
            color: var(--text);
            margin: 30px 0 20px;
            font-size: 2rem;
        }}
        
        .slide-content h3 {{
            color: var(--text);
            margin: 25px 0 15px;
            font-size: 1.75rem;
        }}
        
        .slide-content ul {{
            list-style: none;
            margin: 20px 0;
        }}
        
        .slide-content li {{
            margin: 15px 0;
            padding-left: 40px;
            position: relative;
        }}
        
        .slide-content li::before {{
            content: "→";
            position: absolute;
            left: 0;
            color: var(--primary);
            font-weight: bold;
            font-size: 1.8rem;
        }}
        
        .slide-content code {{
            background: rgba(99, 102, 241, 0.1);
            padding: 4px 12px;
            border-radius: 6px;
            font-family: 'Fira Code', monospace;
            color: var(--accent);
            font-size: 1.3rem;
        }}
        
        .slide-content pre {{
            background: rgba(0, 0, 0, 0.3);
            padding: 25px;
            border-radius: 12px;
            overflow-x: auto;
            margin: 20px 0;
            border-left: 4px solid var(--primary);
        }}
        
        .slide-content pre code {{
            background: none;
            padding: 0;
            font-size: 1.2rem;
        }}
        
        /* Title Slide */
        .slide.title-slide {{
            justify-content: center;
            align-items: center;
            text-align: center;
        }}
        
        .slide.title-slide .slide-title {{
            font-size: 5rem;
            margin-bottom: 30px;
        }}
        
        .slide.title-slide .slide-subtitle {{
            font-size: 2rem;
            color: var(--text-secondary);
            margin-bottom: 50px;
        }}
        
        /* Section Slide */
        .slide.section-slide {{
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
        }}
        
        .slide.section-slide .slide-title {{
            font-size: 4.5rem;
            color: white;
            -webkit-text-fill-color: white;
        }}
        
        /* Controls */
        .controls {{
            position: fixed;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 15px;
            z-index: 1000;
        }}
        
        .control-btn {{
            background: var(--surface);
            border: 2px solid var(--primary);
            color: var(--text);
            padding: 15px 30px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 1.1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}
        
        .control-btn:hover {{
            background: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
        }}
        
        .control-btn:active {{
            transform: translateY(0);
        }}
        
        .control-btn:disabled {{
            opacity: 0.3;
            cursor: not-allowed;
        }}
        
        .control-btn:disabled:hover {{
            background: var(--surface);
            transform: none;
            box-shadow: none;
        }}
        
        /* Progress Bar */
        .progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            transition: width 0.3s ease;
            z-index: 1001;
        }}
        
        /* Slide Counter */
        .slide-counter {{
            position: fixed;
            top: 30px;
            right: 40px;
            font-size: 1.2rem;
            color: var(--text-secondary);
            font-weight: 600;
            background: var(--surface);
            padding: 10px 20px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        /* Fullscreen Button */
        .fullscreen-btn {{
            position: fixed;
            top: 30px;
            left: 40px;
            background: var(--surface);
            border: 2px solid var(--primary);
            color: var(--text);
            padding: 10px 20px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}
        
        .fullscreen-btn:hover {{
            background: var(--primary);
            transform: scale(1.05);
        }}
        
        /* Navigation Sidebar */
        .nav-sidebar {{
            position: fixed;
            left: 0;
            top: 0;
            width: 280px;
            height: 100vh;
            background: var(--surface);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            overflow-y: auto;
            padding: 20px 10px;
            z-index: 999;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }}
        
        .nav-sidebar::-webkit-scrollbar {{
            width: 6px;
        }}
        
        .nav-sidebar::-webkit-scrollbar-track {{
            background: transparent;
        }}
        
        .nav-sidebar::-webkit-scrollbar-thumb {{
            background: var(--primary);
            border-radius: 3px;
        }}
        
        .nav-header {{
            padding: 10px 15px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--primary);
        }}
        
        .nav-header h3 {{
            font-size: 1.2rem;
            color: var(--text);
            font-weight: 700;
        }}
        
        .nav-item {{
            margin: 8px 0;
            padding: 12px 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            border-left: 3px solid transparent;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .nav-item:hover {{
            background: rgba(99, 102, 241, 0.2);
            transform: translateX(5px);
            border-left-color: var(--primary);
        }}
        
        .nav-item.active {{
            background: var(--primary);
            border-left-color: var(--accent);
            transform: translateX(5px);
        }}
        
        .nav-item-number {{
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-secondary);
            min-width: 25px;
        }}
        
        .nav-item.active .nav-item-number {{
            color: white;
        }}
        
        .nav-item-title {{
            font-size: 0.95rem;
            color: var(--text);
            line-height: 1.3;
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }}
        
        .nav-item.active .nav-item-title {{
            color: white;
            font-weight: 600;
        }}
        
        .nav-toggle {{
            position: fixed;
            left: 20px;
            bottom: 100px;
            background: var(--surface);
            border: 2px solid var(--primary);
            color: var(--text);
            padding: 12px 16px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 1.2rem;
            z-index: 1002;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            display: none;
        }}
        
        .nav-toggle:hover {{
            background: var(--primary);
            transform: scale(1.1);
        }}
        
        .presentation-container {{
            margin-left: 280px;
        }}
        
        /* Responsive Design */
        @media (max-width: 1024px) {{
            .nav-sidebar {{
                transform: translateX(-100%);
            }}
            
            .nav-sidebar.open {{
                transform: translateX(0);
            }}
            
            .nav-toggle {{
                display: block;
            }}
            
            .presentation-container {{
                margin-left: 0;
            }}
        }}
        
        @media (max-width: 768px) {{
            .slide {{
                padding: 40px 30px;
                width: 95%;
                height: 85vh;
            }}
            
            .slide-title {{
                font-size: 2.5rem;
            }}
            
            .slide-content {{
                font-size: 1.2rem;
            }}
            
            .control-btn {{
                padding: 12px 20px;
                font-size: 1rem;
            }}
            
            .nav-sidebar {{
                width: 250px;
            }}
        }}
        """
    
    def _generate_javascript(self) -> str:
        """Generate JavaScript for presentation interactivity."""
        return """
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        function showSlide(n) {
            slides.forEach(slide => slide.classList.remove('active'));
            
            if (n >= totalSlides) {
                currentSlide = totalSlides - 1;
            } else if (n < 0) {
                currentSlide = 0;
            } else {
                currentSlide = n;
            }
            
            slides[currentSlide].classList.add('active');
            updateControls();
            updateProgress();
            updateCounter();
            updateNavigation();
        }
        
        function nextSlide() {
            if (currentSlide < totalSlides - 1) {
                showSlide(currentSlide + 1);
            }
        }
        
        function prevSlide() {
            if (currentSlide > 0) {
                showSlide(currentSlide - 1);
            }
        }
        
        function jumpToSlide(n) {
            showSlide(n);
        }
        
        function updateControls() {
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            
            prevBtn.disabled = currentSlide === 0;
            nextBtn.disabled = currentSlide === totalSlides - 1;
        }
        
        function updateProgress() {
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            document.querySelector('.progress-bar').style.width = progress + '%';
        }
        
        function updateCounter() {
            document.querySelector('.slide-counter').textContent = 
                `${currentSlide + 1} / ${totalSlides}`;
        }
        
        function updateNavigation() {
            const navItems = document.querySelectorAll('.nav-item');
            navItems.forEach((item, index) => {
                if (index === currentSlide) {
                    item.classList.add('active');
                    // Scroll nav item into view
                    item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } else {
                    item.classList.remove('active');
                }
            });
        }
        
        function toggleSidebar() {
            const sidebar = document.querySelector('.nav-sidebar');
            sidebar.classList.toggle('open');
        }
        
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
            } else {
                document.exitFullscreen();
            }
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                e.preventDefault();
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                e.preventDefault();
                prevSlide();
            } else if (e.key === 'Home') {
                e.preventDefault();
                showSlide(0);
            } else if (e.key === 'End') {
                e.preventDefault();
                showSlide(totalSlides - 1);
            } else if (e.key === 'f' || e.key === 'F') {
                toggleFullscreen();
            } else if (e.key === 'n' || e.key === 'N') {
                toggleSidebar();
            }
        });
        
        // Touch/swipe support
        let touchStartX = 0;
        let touchEndX = 0;
        
        document.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });
        
        document.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });
        
        function handleSwipe() {
            if (touchEndX < touchStartX - 50) {
                nextSlide();
            }
            if (touchEndX > touchStartX + 50) {
                prevSlide();
            }
        }
        
        // Initialize
        showSlide(0);
        """
    
    def _generate_slide_html(self, slide: Slide, index: int) -> str:
        """Generate HTML for a single slide."""
        slide_class = f"slide {slide.slide_type}-slide"
        if index == 0:
            slide_class += " active"
        
        style = ""
        if slide.background:
            style = f' style="background: {slide.background};"'
        
        return f"""
        <div class="{slide_class}"{style}>
            <h1 class="slide-title">{slide.title}</h1>
            <div class="slide-content">
                {slide.content}
            </div>
        </div>
        """
    
    def generate(self, output_path: str = "presentation.html") -> str:
        """Generate the complete HTML presentation."""
        slides_html = "\n".join(
            self._generate_slide_html(slide, i) 
            for i, slide in enumerate(self.slides)
        )
        
        # Generate navigation items
        nav_items = "\n".join(
            f'''<div class="nav-item" onclick="jumpToSlide({i})">
                <span class="nav-item-number">{i + 1}</span>
                <span class="nav-item-title">{slide.title}</span>
            </div>'''
            for i, slide in enumerate(self.slides)
        )
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Fira+Code&display=swap" rel="stylesheet">
    <style>
        {self._generate_css()}
    </style>
</head>
<body>
    <div class="progress-bar"></div>
    <div class="slide-counter">1 / {len(self.slides)}</div>
    <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶ Fullscreen</button>
    <button class="nav-toggle" onclick="toggleSidebar()">☰ Slides</button>
    
    <!-- Navigation Sidebar -->
    <div class="nav-sidebar">
        <div class="nav-header">
            <h3>📑 Slides</h3>
        </div>
        {nav_items}
    </div>
    
    <div class="presentation-container">
        {slides_html}
    </div>
    
    <div class="controls">
        <button class="control-btn" id="prevBtn" onclick="prevSlide()">← Previous</button>
        <button class="control-btn" id="nextBtn" onclick="nextSlide()">Next →</button>
    </div>
    
    <script>
        {self._generate_javascript()}
    </script>
</body>
</html>
"""
        
        # Write to file
        output_file = Path(output_path)
        output_file.write_text(html, encoding='utf-8')
        
        return str(output_file.absolute())


def create_example_presentation() -> None:
    """Create an example presentation to demonstrate features."""
    
    # Initialize presentation
    pres = PresentationGenerator(
        title="Interactive HTML Presentations",
        author="Presentation Generator v1.0",
        theme="dark"  # Options: dark, light, gradient
    )
    
    # Title Slide
    pres.add_slide(
        title="Interactive HTML Presentations",
        content="""
            <div class="slide-subtitle">Beautiful, Modern, and Interactive</div>
            <p style="font-size: 1.3rem; color: var(--text-secondary);">
                Created with Python • Powered by HTML5 & CSS3
            </p>
        """,
        slide_type="title"
    )
    
    # Section Slide
    pres.add_slide(
        title="Features",
        content="",
        slide_type="section"
    )
    
    # Content Slide
    pres.add_slide(
        title="Key Features",
        content="""
            <ul>
                <li>Slide navigation panel with quick jump access</li>
                <li>Smooth animations and transitions</li>
                <li>Keyboard navigation (Arrow keys, Space, Home, End)</li>
                <li>Touch/swipe support for mobile devices</li>
                <li>Progress bar and slide counter</li>
                <li>Fullscreen mode (press 'F')</li>
                <li>Multiple themes (dark, light, gradient)</li>
                <li>Responsive design for all screen sizes</li>
            </ul>
        """
    )
    
    # Code Example Slide
    pres.add_slide(
        title="Easy to Use",
        content="""
            <h3>Create presentations with simple Python code:</h3>
            <pre><code>pres = PresentationGenerator(
    title="My Presentation",
    theme="dark"
)

pres.add_slide(
    title="Welcome",
    content="Hello World!"
)

pres.generate("output.html")</code></pre>
        """
    )
    
    # Benefits Slide
    pres.add_slide(
        title="Why Use This?",
        content="""
            <h2>Perfect for:</h2>
            <ul>
                <li>Technical presentations and demos</li>
                <li>Educational content and tutorials</li>
                <li>Portfolio showcases</li>
                <li>Product launches</li>
                <li>Conference talks</li>
            </ul>
            
            <h3 style="margin-top: 40px;">Benefits:</h3>
            <ul>
                <li>No external dependencies required</li>
                <li>Works offline - just open the HTML file</li>
                <li>Easy to customize and extend</li>
                <li>Lightweight and fast</li>
            </ul>
        """
    )
    
    # Technical Details
    pres.add_slide(
        title="Technical Stack",
        content="""
            <h2>Built with modern web technologies:</h2>
            <ul>
                <li><code>HTML5</code> - Semantic structure</li>
                <li><code>CSS3</code> - Animations & gradients</li>
                <li><code>JavaScript</code> - Interactivity</li>
                <li><code>Python</code> - Generation engine</li>
            </ul>
            
            <p style="margin-top: 40px; font-size: 1.3rem;">
                All generated as a single, self-contained HTML file!
            </p>
        """
    )
    
    # Final Slide
    pres.add_slide(
        title="Thank You!",
        content="""
            <div style="text-align: center; margin-top: 80px;">
                <h2 style="font-size: 2.5rem; margin-bottom: 30px;">
                    Start creating amazing presentations today!
                </h2>
                <p style="font-size: 1.5rem; color: var(--text-secondary);">
                    Press <code>F</code> for fullscreen • <code>N</code> for navigation panel<br>
                    Use arrow keys to navigate
                </p>
            </div>
        """,
        slide_type="title"
    )
    
    # Generate the presentation
    output_path = "example_presentation.html"
    generated_file = pres.generate(output_path)
    
    print(f"✅ Presentation generated successfully!")
    print(f"📄 File: {generated_file}")
    print(f"📊 Total slides: {len(pres.slides)}")
    print(f"\n🎨 Theme: {pres.theme}")
    print(f"\n💡 Tip: Open the HTML file in your browser to view the presentation")
    print(f"⌨️  Keyboard shortcuts:")
    print(f"   • Arrow keys / Space: Navigate slides")
    print(f"   • N: Toggle navigation panel")
    print(f"   • F: Toggle fullscreen")
    print(f"   • Home/End: Jump to first/last slide")


if __name__ == "__main__":
    create_example_presentation()
