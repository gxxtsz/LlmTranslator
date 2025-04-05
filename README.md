# LlmTranslator
使用大语言模型翻译文本文件

目前只实现了基于Ollama接口的txt文本翻译。

## 使用

安装：

```bash
pip install -e .
```

运行：

```bash
python src/main.py --config config/default.yml 
```

## 配置文件

```yaml
project:
  name: LlmTranslator
  version: 0.1.0

controller:
  source_language: 英文
  target_language: 中文

model:
  model_name: qwen2.5:latest
  base_url: http://localhost:11434

reader:
  file_path: demo/小王子_英文版.txt
  min_length: 1000
  max_length: 3000

write:
  file_path: demo/小王子_中文版.txt
```

根据选择的模型的能力，适当调节`min_length`和`max_length`，不要设置的太小，不然翻译时会添加不必要的内容。

## 计划

看看就行，后续不计划更新。
