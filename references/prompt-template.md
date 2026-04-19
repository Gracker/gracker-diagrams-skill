# Prompt 模板

把下面内容填入，生成最终 prompt：

```
A technical architecture visual in an Excalidraw-like hand-drawn style, closer to a systems-paper visual abstract than an infographic poster.

Optional title: "<TITLE>" only if truly needed. Prefer no standalone title block.

<LAYOUT_CONTENT>

Style: Pure white background, thick slightly imperfect black outlines, low-saturation pastel accent borders or outer glows, large simple black icons, and only when needed, compact Perfetto-style timing marks. Use one consistent font family mood across every label: clean, steady, lightly handwritten, technical, not childish. The diagram itself must be the hero.

Key constraints:
- Pure white background by default
- Thick black outlines
- Rounded rectangle modules
- Low-saturation pastel borders or outer glows for classification only
- Large simple black icons as primary visual anchors
- Font: ALL text — Chinese and English — must use ONE consistent font family. Recommended: LXGW WenKai (霞鹜文楷) for both, or Noto Sans CJK SC + Noto Sans. Do NOT mix different font families for Chinese vs English.
- Font style must stay consistent across all labels
- Orthogonal arrows (straight horizontal/vertical)
- Ample whitespace
- Hand-drawn / whiteboard refined feel
- Prefer relationship-first composition over explanation-first composition
- No bullet lists inside modules unless absolutely necessary
- Only add Perfetto-style timing bars when the content has real timing/overlap data
- No corporate PPT style, no photorealistic, no kawaii, no poster-like title block

AESTHETIC DEFAULTS (these are always active, do not skip):
- Content MUST be vertically and horizontally centered in canvas
- Content should occupy ~70% of canvas, margins ~30% on all sides
- Content must NOT be too small (don't waste canvas) and NOT too large (lose breathing room)
- Equal whitespace above and below content — never let content float to top or bottom
- Never constrain width or height — dimensions follow content naturally

Text labels (in Chinese):
<TEXT_LABELS>

Generate the infographic based on the content below:

<CONTENT>
```

## 标题处理

**标题不是必须的。**

如果一定要标题：
- 字体、大小、风格必须和所有标签完全一致，不能有两套字体系统
- 位置要小、轻，可以放在左上角或融入模块，不能占 1/3 空间
- 更推荐的做法：直接用模块本身传达主题，不要单独一个醒目的标题区块

## Layout 片段（从 references/layouts/ 选取）

### linear-progression
```
Main flow: horizontal or vertical sequential steps connected by arrows.
Each step is a rounded rectangle on pure white background.
Below the main flow, add Perfetto-style timeline bars for duration/timing.
```

### hub-spoke
```
Central hub drawn as a large rounded rectangle in the center.
Peripheral modules drawn as smaller rounded rectangles around it.
Connect with orthogonal arrows.
Each module has a small category color border or glow.
Prefer one strong icon per core module.
```

### structural-breakdown
```
Main subject in center, with exploded component modules around it.
Callout lines from center to each component.
Each callout ends in a small label box.
Optional zoom detail on a sub-component.
Keep labels short, avoid explanatory bullet lists.
```

### hierarchical-layers
```
3-7 horizontal layers stacked top-to-bottom.
Each layer is a wide rounded rectangle with a category color top-border.
Labels inside each layer.
Size can indicate importance.
```

## Perfetto track 注入片段（按需，不是标配）

**只有当内容有真实的时间长度 / 并行重叠 / 阶段间隔时，才加 Perfetto tracks。**

适合加的场景：
- 启动时序（5ms / 138ms / 25ms 这种有数字的）
- 并发执行（有重叠的工作窗口）
- 压缩/恢复链路（有等待和重试的阶段）

不适合加的场景：
- 纯架构拆解（模块关系，没有时间维度）
- 协议步骤分类（发现→规范化→执行是分类，不是时间条）
- 状态机（queued→executing→completed 是状态，不是时间轴）

如果判断下来要加：

```
Below the main diagram, add a Perfetto-style technical detail strip with horizontal colored tracks:
- Track labels on the left (short text)
- Colored bars showing phases/durations
- Use low-saturation colors matching the main diagram palette
- Small timing annotations where relevant
- Keep it compact, do not dominate the diagram
```

## TEXT_LABELS 片段

格式：
```
- 标题: <title>
- 主模块: <module names comma-separated>
- 标注: <annotation texts>
- 底部: <timeline/stage labels if applicable>
```
