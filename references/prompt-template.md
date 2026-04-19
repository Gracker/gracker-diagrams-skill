# Prompt 模板

把下面内容填入，生成最终 prompt：

```
A technical infographic in a hybrid hand-drawn craft-paper style with Perfetto trace-viewer aesthetics.

Title: "<TITLE>" (in handwritten Chinese font style)

<LAYOUT_CONTENT>

Style: Hand-drawn slightly imperfect lines on cream textured paper background (#FFF8F0). Mix of warm craft-paper colors and Perfetto-style horizontal colored bars for the timeline section. Clean labels in casual handwritten font. Technical but approachable.

Key constraints:
- White or cream background
- Thick black outlines
- Rounded rectangle modules
- Low-saturation pastel borders for classification only
- Simple black icons
- Orthogonal arrows (straight horizontal/vertical)
- Ample whitespace
- Hand-drawn / whiteboard refined feel
- If there are phases/timeline/stages, add Perfetto-style horizontal tracks or timeline bars at the bottom
- No corporate PPT style, no photorealistic, no kawaii

Text labels (in Chinese):
<TEXT_LABELS>

Generate the infographic based on the content below:

<CONTENT>
```

## Layout 片段（从 references/layouts/ 选取）

### linear-progression
```
Main flow: horizontal or vertical sequential steps connected by arrows.
Each step is a rounded rectangle on cream paper.
Below the main flow, add Perfetto-style timeline bars for duration/timing.
```

### hub-spoke
```
Central hub drawn as a large rounded rectangle in the center.
Peripheral modules drawn as smaller rounded rectangles around it.
Connect with orthogonal arrows.
Each module has a small category color border.
```

### structural-breakdown
```
Main subject in center, with exploded component modules around it.
Callout lines from center to each component.
Each callout ends in a small label box.
Optional zoom detail on a sub-component.
```

### hierarchical-layers
```
3-7 horizontal layers stacked top-to-bottom.
Each layer is a wide rounded rectangle with a category color top-border.
Labels inside each layer.
Size can indicate importance.
```

## Perfetto track 注入片段

如果内容有时序/阶段/并行，加入：

```
Below the main diagram, add a Perfetto-style technical detail strip with horizontal colored tracks:
- Track labels on the left (short text)
- Colored bars showing phases/durations
- Use low-saturation colors matching the main diagram palette
- Small timing annotations where relevant
```

## TEXT_LABELS 片段

格式：
```
- 标题: <title>
- 主模块: <module names comma-separated>
- 标注: <annotation texts>
- 底部: <timeline/stage labels if applicable>
```
