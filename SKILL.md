---
name: kangsheng-product-template
description: Apply the approved Kangsheng Electronics website/independent-store product-image template while replacing only the central product. Use for 康生官网产品图、独立站主图、产品换图、固定品牌框、空白模板或透明叠加层。
---

# 康生固定产品图模板

使用 `reference/模板参考图.png` 作为唯一视觉基准。该文件来自用户最终确认图，禁止重新设计或按相似风格另画。使用 `templates/透明框.png` 或 `templates/空白模板.png` 作为成品框架。

## 不可改动的固定元素

- 左上：银白＋冰蓝金属 K Logo；右侧英文品牌名 `KANGSHENG ELECTRONICS`。
- 左上副文案：`CONNECT A BRIGHTER POSSIBILITY`。
- 右上：`PROFESSIONAL CONNECTOR SOLUTIONS`。
- 左下：`RELIABLE / PRECISE / INNOVATIVE`。
- 右下官网网址：`WWW.KANGSHENG.COM`；不得自行替换或猜测其他域名。
- 整体：白底、浅冰蓝科技感、低饱和几何斜线、半透明 K 元素。
- 版式、位置、颜色、字体风格、装饰、文字内容均固定。

## 唯一可替换内容

只替换中央产品主体。产品必须等比例缩放，不拉伸、不压扁、不增删针脚、不补造接口或结构，不改变产品朝向与真实材质。优先保持原图的金属反光、工程塑料纹理、边缘和结构细节。

## 工作流

1. 读取用户产品原图；若是白底图，保持白底和真实阴影；若是透明图，保留原始透明边缘。
2. 将产品等比例置于中央产品安全区，建议占画布宽度 55%–72%、高度不超过 57%，四周保留呼吸空间。
3. 在最上层叠加 `templates/透明框.png`；不要重绘、改写或移动角落元素。
4. 输出 1254×1254 PNG；不得裁切产品、改变结构或加入额外文案。
5. 对照 `reference/模板参考图.png` 检查固定元素、网址和产品结构。

## 稳定渲染

可运行：

```bash
python3 scripts/render_template.py PRODUCT_IMAGE OUTPUT.png
```

脚本只做等比例缩放、居中合成和固定框叠加，不生成或修改产品结构。
