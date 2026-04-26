# Prompt 模板（白板架构图）

把下面内容填入，生成最终 prompt：

```
A technical architecture diagram drawn on a white whiteboard with thick black marker.

Visual reference: looks like a photo of a real whiteboard where an engineer drew a system architecture. White board background, thick black marker lines with slight natural hand-shake, rectangular modules outlined with a single stroke of colored marker (no fill, just the border). Connection lines are straight orthogonal (horizontal and vertical only), arrows are simple hand-drawn V-shapes.

<LAYOUT_CONTENT>

Style constraints:
- Pure white background (standard whiteboard, NOT cream/paper/warm)
- Thick black marker outlines (consistent width, slight natural wobble)
- Rectangular modules with colored marker border only — NO fill inside modules
- Colors are used ONLY for category differentiation, maximum 4 colors per diagram
- Color palette: deep blue #4A90D9, deep orange #E8913A, cyan #5BA4CF, deep green #4CAF50, gray #9E9E9E
- NO pastel fills, NO colored top bars, NO card-style rounded rectangles
- NO shadows, NO gradients, NO depth effects, NO glassmorphism
- Simple line icons (like engineer quick sketches), NOT filled icons, NOT emoji-style, NOT detailed illustrations
- Orthogonal arrows (horizontal/vertical only), simple V-shaped arrowheads
- Text is clear and readable, same style throughout (no heading hierarchy — whiteboard doesn't change markers)
- Font: ALL text — Chinese and English — must use ONE consistent font family. Recommended: LXGW WenKai (霞鹜文楷) for both, or Noto Sans CJK SC + Noto Sans. Do NOT mix different font families.
- Ample whitespace, content centered vertically and horizontally
- Content occupies ~60-70% of canvas
- NO standalone title block — the diagram speaks for itself
- NO decorative elements (stars, stickers, patterns, tape, torn edges)
- NO paper texture, NO warm tones, NO watercolor effects
- NO scene illustration (no desk, monitor, keyboard, mugs, people)
- Perfetto-style timeline tracks only if content has real timing/overlap data — draw as simple thin colored bars, not dominant

This must look like a WHITEBOARD, not a UI mockup, not an illustration, not an infographic poster, not a SaaS product page.

Text labels (in Chinese):
<TEXT_LABELS>

Generate the diagram based on the content below:

<CONTENT>
```

## 标题处理

白板图不做独立标题。图本身说明一切。
如果一定要标注主题，用白板左上角手写小字，和所有标签同一风格。

## Layout 片段（从 references/layouts/ 选取）

### linear-progression
```
Main flow: horizontal or vertical sequential steps connected by orthogonal arrows.
Each step is a rectangular module on whiteboard with colored border (no fill).
If timing data exists, add compact Perfetto-style timeline bars below.
```

### hub-spoke
```
Central module as a large rectangle in center.
Peripheral modules as smaller rectangles around it.
Connect with orthogonal arrows (horizontal/vertical only).
Each module has a single-color marker border for category.
```

### structural-breakdown
```
Main subject in center, with component modules around it.
Callout lines from center to each component (orthogonal, with right angles).
Each callout ends in a small label.
Keep labels short.
```

### hierarchical-layers
```
3-7 horizontal layers stacked top-to-bottom.
Each layer is a wide rectangle with a category color border.
Labels inside each layer.
No fill, just border + text.
```

## TEXT_LABELS 片段

格式：
```
- 主模块: <module names comma-separated>
- 标注: <annotation texts>
- 底部: <timeline/stage labels if applicable>
```
