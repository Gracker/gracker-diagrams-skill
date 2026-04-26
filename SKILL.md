---
name: gracker-diagrams
description: >-
  Generate architecture diagrams, Mermaid-to-image redraws, and technical infographics
  in Gracker's preferred style. Two modes:
  (1) Whiteboard architecture — Excalidraw-like hand-drawn visual abstracts with
  low-saturation pastel accents, thick black outlines, orthogonal arrows, and
  optional Perfetto-style timeline tracks.
  Trigger: 画图, 架构图, 系统图, 模块关系, Mermaid 转图, 流程图, 时序图, 白板图.
  (2) Macaron infographic — hand-drawn educational infographic on warm cream
  paper with pastel cards, wavy arrows, cartoon icons, vertical layout, and bottom quote.
  Trigger: 信息图, infographic, 单页摘要, 竖屏图, 长图, 知识总结图, 框架图, Skill 概览图.
---

# Gracker Diagrams

默认目标不是“华丽”，而是 **低压感、高解释力、强结构化**。保留 baoyu-infographic 的主流程，但把风格固定成 Gracker 偏好的技术手绘风。

## 强制执行原则

不要直接手写最终 `image_generate` prompt。必须先按流程产出中间文件：

1. `source.md`：保存原始输入或原文摘录
2. `analysis.md`：分析信息结构和取舍依据
3. `structured-content.md`：由 Skill 决定哪些内容进入图片
4. `prompts/infographic.md`：基于对应 prompt template 生成最终出图 prompt

只有完成以上文件后，才能调用 `image_generate`。如果内容很长，Skill 负责筛选高价值信息，而不是由临场 prompt 任意压缩。

## 风格路由

根据用户意图选择风格：

| 风格 | 触发词 | 适用场景 |
|------|--------|----------|
| **白板架构图**（默认） | 架构图、系统图、模块关系、Mermaid 转图、流程图、时序图、白板图、画图 | 系统拆解、组件关系、渲染管线、请求链路 |
| **马卡龙信息图** | 信息图、infographic、单页摘要、竖屏图、长图、知识总结图、框架图、Skill 概览图 | 知识体系总结、方法论概览、Skill 框架、文章摘要 |

判断不了的默认走白板架构图。

---

## 风格 A：白板架构图（默认）

先读：
- `references/style-guide.md`
- `references/prompt-template.md`
- `references/quality-checklist.md`

## 输出流程

### 1. 建立本次出图目录

手动创建：

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

根据内容形状选择：
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

使用 `image_generate`，**必须指定 `model: openai/gpt-image-2`**，不要省略 model 参数。

建议参数：
- `model`: `openai/gpt-image-2`（必须）
- `aspectRatio`: `16:9`（默认，横屏）
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

---

## 风格 B：马卡龙信息图

先读：
- `references/macaron-style-guide.md`
- `references/macaron-prompt-template.md`

### 输出流程

与风格 A 共享步骤 1-4（建目录 → 保存原始内容 → 分析信息结构 → 生成结构化内容），但后续步骤有差异：

#### 5. 选布局（马卡龙适配）

马卡龙信息图的布局选择逻辑：
- 竖屏优先（`1024x1536` 或 `768x1024`）
- 顺序流程 / 逐步展开 → 纵向箭头串联
- 对比 / 优缺点 → 左右分栏卡片
- 组成 / 要素 → 并列马卡龙卡片
- 层级 / 质检体系 → 嵌套或阶梯式
- 循环 / 迭代 → 环形
- 多模块总览 → 卡片矩阵 + 连接线

#### 6. 生成 prompt

基于 `references/macaron-prompt-template.md` 生成。

核心风格硬约束（已在模板中，不需重复）：
- 暖奶油纸底 #F5F0E8
- 马卡龙色圆角卡片，不完全填满轮廓
- 手绘波浪箭头
- 简笔画卡通 + 涂鸦装饰
- 粗体大号手绘字标题居中
- 底部金句

#### 7. 出图

使用 `image_generate`，**必须指定 `model: openai/gpt-image-2`**，不要省略 model 参数。

建议参数：
- `model`: `openai/gpt-image-2`（必须）
- `size`: `1024x1536`
- `filename`: `<slug>-macaron.png`

#### 8. 验收

- 一眼能看懂信息结构
- 马卡龙色块出现且不完全填满轮廓
- 有手绘抖动感
- 有涂鸦装饰（星星、下划线、小箭头）
- 底部有金句
- 竖屏比例
- 不是白板架构图风格

不满足就改 prompt，重试 1 次。

---

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
