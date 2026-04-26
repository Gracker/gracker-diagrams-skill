# Gracker 信息图 Prompt 模板

把下面内容填入，生成最终 prompt：

```
你是一位擅长手绘风信息图的视觉设计师。请根据以下内容创作一张高文字密度的单页中文信息图。

风格要求

整体风格：Hand-drawn educational infographic on warm cream paper texture (#F5F0E8)。所有线条和形状带轻微手绘抖动感（slight hand-drawn wobble），整体干净清晰，像高质量演示文稿的单页视觉摘要。无写实元素。

配色方案：
- 信息区分区：用浅蓝 #A8D8EA、薄荷绿 #B5E5CF、薰衣草紫 #D5C6E0、浅桃 #F4C7AB 作为区块背景色或左侧色条，自然区分内容区域。不要画卡片框、气泡框、虚线框——用背景色自然过渡即可。
- 强调色：珊瑚红 #E8655A，用于关键词、重要数据、勾选标记等需要视觉突出的元素
- 线条与主文字：黑色
- 辅助标注：暖灰 #6B6B6B，字号较小

图形与文字平衡：文字是信息的绝对主体。尽量少用图标和装饰性插画。整体原则是「文字密度优先，图标克制使用」。这张图信息量较大，每个技术点需要保留关键说明文字，不要过度精简。

信息结构：高密度纵向布局。模块之间用手绘线条和波浪箭头（hand-drawn wavy arrows）连接递进，表达流向关系。区块用不同背景色自然区分，不要画卡片框。

文字层次：标题顶部居中，粗体大号手绘字（bold, large, hand-drawn lettering）；区域内粗体关键词 + 正常文字说明混排，允许完整短语和短句。

渲染细节：涂鸦装饰点缀（小星星、下划线、小箭头等），充足留白，干净构图。

底部金句：图片底部一句粗体居中总结，概括核心观点。

Text labels (in Chinese):
<TEXT_LABELS>

Generate the infographic based on the content below:

<CONTENT>
```

## TEXT_LABELS 片段

格式：
```
- 标题: <title>
- 主模块: <module names comma-separated>
- 标注: <annotation texts>
- 底部金句: <one-sentence summary>
```
