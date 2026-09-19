# 康生官网 / 独立站固定产品图模板

这套模板直接以用户最终确认图为母版，固定原图的比例、位置、装饰与文字。以后只替换中央产品，其他内容保持不变。

## 文件

- `SKILL.md`：给 Codex / Agent 使用的固定规则。
- `reference/模板参考图.png`：已确认的母版参考图。
- `templates/透明框.png`：带透明中央区域的叠加层，适合盖在产品图最上方。
- `templates/空白模板.png`：白底空模板，可直接在中央放置产品。
- `scripts/render_template.py`：自动等比例放置产品并叠加透明框。

## 最简单的用法

1. 新建 1254×1254 画布，或直接打开 `templates/空白模板.png`。
2. 把产品图等比例缩放后放在中央，不要拉伸或修改针脚、端子、孔位和外壳结构。
3. 将 `templates/透明框.png` 放到最上层并与画布左上角对齐。
4. 导出 PNG。

## 自动生成

需要 Pillow：`python3 -m pip install pillow`

```bash
python3 scripts/render_template.py 产品图.png 成品.png
```

脚本会自动识别透明底或近白底产品图，保留原比例与真实阴影，并将产品限制在安全区内。

## GitHub 安装

```bash
git clone https://github.com/tieka055-debug/kangsheng-product-template-skill.git
```

如需安装到 Codex Skills，可将仓库文件夹复制到 `$CODEX_HOME/skills/kangsheng-product-template`。

## 固定记录

- 母版：`reference/模板参考图.png`
- 画布：1254×1254 px
- 官网：`WWW.KANGSHENG.COM`
- 原则：只替换中央产品，品牌版式与文字不得重绘或改动。
