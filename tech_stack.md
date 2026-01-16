# Technology Stack & Architecture

## 🐍 Python Modules
Static site generator implementation.

### Standard Library
-   **`pathlib`**: File system operations for writing the output HTML.
-   **`typing`**: Type hints for code clarity (`List`, `Dict`, `Optional`).
-   **`datetime`**: Timestamps (if used in footer/metadata).

## 🌐 Web Technologies
The output is a self-contained, interactive HTML5 Single Page Application (SPA).

### HTML5
-   **Role**: Content Structure.
-   **Usage**: Semantic markup for slides, titles, and content areas. All slides are generated into a single HTML file.

### CSS3
-   **Role**: Styling & Animation.
-   **Key Features**:
    -   **CSS Variables**: Theme management (Dark/Light/Gradient).
    -   **Keyframes**: `slideIn` animations for smooth transitions.
    -   **Flexbox**: Center alignment of slide content.
    -   **Media Queries**: Responsive adjustments for mobile/tablet.

### JavaScript (ES6+)
-   **Role**: Interactivity.
-   **Usage**:
    -   **Navigation**: Functions to switch slides (`showSlide`, `nextSlide`).
    -   **Events**: Keyboard listeners (Arrows, Space, F-key) and Touch listeners (Swipe).
    -   **DOM Manipulation**: Dynamic progress bar and slide counter updates.
