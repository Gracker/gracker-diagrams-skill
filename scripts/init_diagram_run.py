#!/usr/bin/env python3
"""
init_diagram_run.py
在指定 root 下创建本次出图的目录结构。

用法:
  python3 init_diagram_run.py --root /path/to/output --slug my-topic
  python3 init_diagram_run.py --root . --slug startup-pipeline  (用当前目录)
"""

import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="初始化出图工作目录")
    parser.add_argument("--root", required=True, help="输出根目录")
    parser.add_argument("--slug", required=True, help="出图主题 slug (英文或拼音，用于目录名)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = args.slug.strip().replace(" ", "-")
    if not slug:
        raise ValueError("slug cannot be empty")

    out_dir = root / slug
    prompts_dir = out_dir / "prompts"
    output_dir = out_dir / "output"

    for d in [out_dir, prompts_dir, output_dir]:
        d.mkdir(parents=True, exist_ok=True)

    files = {
        out_dir / "source.md": "# 原始输入\n\n来源: \n\n内容:\n\n",
        out_dir / "analysis.md": "# 分析\n\n目标:\n\n内容形状:\n\n主元素:\n\n次级标注:\n\nPerfetto track 注入点:\n\n",
        out_dir / "structured-content.md": "# 结构化内容\n\n## 标题\n\n## 一句话摘要\n\n## 主模块\n\n## 连接关系\n\n## 辅助标注\n\n## 图例\n\n## 文案标签\n\n",
        prompts_dir
 / "infographic.md": "# 最终出图 Prompt\n\n复制 references/prompt-template.md 的模板，填入内容。\n\n",
    }

    for fp, content in files.items():
        if not fp.exists():
            fp.write_text(content)
            print(f"  created {fp}")
        else:
            print(f"  exists   {fp}")

    print(f"\n✓ 目录结构已创建: {out_dir}")
    print(f"  prompts/:   {prompts_dir}")
    print(f"  output/:     {output_dir}")


if __name__ == "__main__":
    main()
