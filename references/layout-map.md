# 布局选择

## 默认映射

### linear-progression
适用：
- 启动流程
- 生命周期
- 处理阶段
- 时序步骤
- 教程步骤

优先加 Perfetto-style timeline bar。

### hub-spoke
适用：
- 中心循环 + 周边模块
- 核心系统 + 外围依赖
- 一个主组件和多个输入/输出

这是 Claude Code / Agent 架构最常用布局之一。

### structural-breakdown
适用：
- 系统组件拆解
- 模块职责拆解
- 分层后再标注每层作用

适合“讲结构组成”，不适合很强的流程图。

### hierarchical-layers
适用：
- 分层架构
- 优先级层级
- 权限分级
- 上下层依赖

### dense-modules
适用：
- 一页总览
- 高密度知识图
- 多模块速查图

只有在确实信息很多时才用，不然会显得挤。

## 选择顺序

1. 先看信息是“流”还是“结构”
2. 再看有没有明确中心
3. 再决定要不要加时间轨道

## 简单判断表

| 内容形状 | 首选布局 |
|---|---|
| A→B→C→D | linear-progression |
| 中心系统 + 多个外围模块 | hub-spoke |
| 组件拆解 / 子系统拆解 | structural-breakdown |
| 上下层级很强 | hierarchical-layers |
| 多块并列信息 | dense-modules |
