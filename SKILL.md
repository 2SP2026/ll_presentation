---
name: "HTML Presentation Generator"
description: "Create interactive HTML presentations with Python"
---

# HTML Presentation Generator

## Purpose
This skill provides instructions for creating and customizing interactive HTML-based presentations using the `ll_presentation_v1.0.py` generator.

## Creating a New Presentation

### Basic Usage
```python
from ll_presentation_v1.0 import PresentationGenerator

# Initialize presentation
pres = PresentationGenerator(
    title="My Presentation",
    author="Your Name",
    theme="dark"  # Options: dark, light, gradient
)

# Add slides
pres.add_slide(
    title="Slide Title",
    content="<p>Your HTML content here</p>",
    slide_type="default"  # Options: default, title, section
)

# Generate HTML file
pres.generate("output.html")
```

## Slide Types

### 1. Title Slide
Used for main title or section covers:
```python
pres.add_slide(
    title="Welcome",
    content='<div class="slide-subtitle">Subtitle text</div>',
    slide_type="title"
)
```

### 2. Section Slide
Full-screen section divider with gradient background:
```python
pres.add_slide(
    title="Section Name",
    content="",
    slide_type="section"
)
```

### 3. Default Slide
Standard content slide:
```python
pres.add_slide(
    title="Content Title",
    content="""
        <h2>Heading</h2>
        <ul>
            <li>Point 1</li>
            <li>Point 2</li>
        </ul>
    """
)
```

## Content Formatting

### Lists
```html
<ul>
    <li>Bullet point 1</li>
    <li>Bullet point 2</li>
</ul>
```

### Code Blocks
```html
<pre><code>def hello():
    print("Hello World")</code></pre>
```

### Inline Code
```html
Use <code>inline code</code> for highlighting
```

### Headings
```html
<h2>Main heading</h2>
<h3>Subheading</h3>
```

## Themes

Available themes:
- **dark** - Dark background with vibrant accents (default)
- **light** - Light background, professional look
- **gradient** - Purple gradient background, modern style

## Features

### Navigation
- **Arrow keys / Space** - Next/previous slide
- **Home / End** - Jump to first/last slide
- **N** - Toggle navigation panel
- **F** - Toggle fullscreen
- **Click navigation panel** - Jump to specific slide

### Responsive Design
- Desktop: Navigation panel always visible on left
- Tablet/Mobile: Panel hidden by default, toggle with "☰ Slides" button

## Best Practices

1. **Keep slides focused** - One main idea per slide
2. **Use consistent formatting** - Stick to the same HTML structure
3. **Limit text** - Use bullet points, not paragraphs
4. **Test responsiveness** - Check on different screen sizes
5. **Use semantic HTML** - Proper heading hierarchy (h2, h3)

## Customization

### Custom Background
```python
pres.add_slide(
    title="Custom Slide",
    content="Content here",
    background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
)
```

### Speaker Notes
```python
pres.add_slide(
    title="Slide Title",
    content="Slide content",
    notes="These are speaker notes (not currently displayed)"
)
```

## Common Patterns

### Title + Subtitle Pattern
```python
pres.add_slide(
    title="Main Title",
    content='''
        <div class="slide-subtitle">Subtitle or tagline</div>
        <p style="margin-top: 40px;">Additional context</p>
    ''',
    slide_type="title"
)
```

### Two-Column Layout
```python
pres.add_slide(
    title="Comparison",
    content='''
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
            <div>
                <h3>Column 1</h3>
                <ul><li>Point A</li></ul>
            </div>
            <div>
                <h3>Column 2</h3>
                <ul><li>Point B</li></ul>
            </div>
        </div>
    '''
)
```

## Troubleshooting

### Slide content not displaying
- Check HTML syntax is valid
- Ensure quotes are properly escaped in Python strings
- Use triple quotes `"""` for multi-line content

### Styling issues
- All custom styles should use inline CSS
- Reference CSS variables: `var(--primary)`, `var(--text)`, etc.
- Test in different browsers

## Output

The generator creates a **single, self-contained HTML file** that:
- Works offline
- Requires no external dependencies
- Can be shared via email, USB, or web hosting
- Opens in any modern browser
