---
name: gracker-diagrams
description: Generate architecture diagrams, Mermaid-to-image redraws, and technical infographics in Gracker's preferred style: Excalidraw-like hand-drawn visual abstracts with low-saturation pastel accents, thick black outlines, orthogonal arrows, and optional Perfetto-style timeline tracks. Use when the user asks to 画图, 架构图, 信息图, Mermaid 转图片, visual summary, technical blog figures, or wants diagrams in a hand-drawn technical style.
---

# Gracker Diagrams

默认目标不是“华丽”，而是 **低压感、高解释力、强结构化**。保留 baoyu-infographic 的主流程，但把风格固定成 Gracker 偏好的技术手绘风。

## 默认风格

先读：
- `references/style-guide.md`
- `references/layout-map.md`
- `references/prompt-template.md`
- `references/quality-checklist.md`

## 输出流程

### 1. 建立本次出图目录

运行：

```bash
python3 scripts/init_diagram_run.py \
  --root "/path/to/output-root" \
  --slug "topic-name"
```

默认产物：

```text
<root>/<slug>/
├── source.md
├── analysis.md
├── structured-content.md
├── prompts/
│   └── infographic.md
└── output/
    └── diagram.png
```

如果用户已经给了固定目录，直接用用户目录，不额外新建层级。

### 2. 保存原始内容

把原始输入按原样写到 `source.md`。

来源可以是：
- Mermaid
- Markdown 正文
- 文章段落
- 已有图片的结构描述
- 手工列出的模块/关系/步骤

规则：
- 不补新信息
- 不改事实
- 只做结构整理

### 3. 分析信息结构

在 `analysis.md` 里只回答 5 件事：
1. 图的目标（一句话）
2. 内容形状（顺序 / 中心-辐射 / 分层 / 拆解 / 对比）
3. 主元素 3-7 个
4. 次级标注有哪些
5. 哪些地方适合加 Perfetto-style tracks（如果有时间、阶段、等待、并行）

### 4. 生成结构化内容

把图整理成视觉可消费的模块，写到 `structured-content.md`。

格式尽量稳定：
- 标题
- 一句话摘要
- 主模块列表
- 连接关系
- 辅助标注
- 图例/说明
- 文案标签清单

### 5. 选布局

默认按 `references/layout-map.md` 选：
- 顺序流程 → `linear-progression`
- 中心系统 + 周边依赖 → `hub-spoke`
- 系统组件拆解 → `structural-breakdown`
- 分层机制 → `hierarchical-layers`
- 高密度总览 → `dense-modules`

除非用户指定，否则优先 **可解释性**，不是视觉花活。

### 6. 生成 prompt

基于 `references/prompt-template.md` 生成 `prompts/infographic.md`。

风格硬约束：
- 白底或浅米色纸张底
- 粗黑描边
- 圆角模块
- 低饱和浅色边框分区
- 简化黑白图标
- 正交箭头
- 留白充足
- 手绘/白板精修感
- 如果有时间、阶段、并发，加入 Perfetto-style 横向 tracks 或 timeline bars

### 7. 出图

优先用 `image_generate`。

建议参数：
- `aspectRatio`: `16:9`（默认）
- `filename`: `<slug>.png`

### 8. 验收

用视觉工具检查结果是否满足：
- 一眼能看懂主路径
- 不是 corporate PPT 风
- 不是写实海报风
- 不是卡通卖萌风
- 线条粗、结构清、颜色轻
- 如果有时序/阶段，Perfetto-style tracks 真的出现了

不满足就改 prompt，再重试 1 次。不要无止境重抽。

## Mermaid 转图片的额外规则

如果原始输入是 Mermaid：
- **保留 Mermaid 源码**
- 同时生成一张展示版图片
- 如果需要精确版，再补一张 SVG 渲染版
- 文档里推荐顺序：展示版 → 精确版 → Mermaid 源码

## 什么时候不要用这个 skill

以下情况不要硬套：
- 数据图表、折线图、柱状图，用 vega / data visualization 工具
- UML、ER 这类严格工程图，优先 mermaid / graphviz
- 只想要快速可维护，不关心视觉，直接 mermaid

## 输出总结格式

最终汇报只说：
- 图名
- 选用布局
- 输出路径
- 是否保留 Mermaid/SVG
- 是否通过一轮视觉验收
