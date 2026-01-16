# Anywhere-use-browser

<div align="center">

<img width="1920" height="1032" alt="2d12cabd0776fe929cd5feffcfbbe3e0" src="https://github.com/user-attachments/assets/e513f651-52c3-4f6f-affc-d57f81b6fc6f" />
**一个轻量级、功能齐全的桌面浏览器，专为提高工作效率而设计**

[功能特点](#-功能特点) • [快速开始](#-快速开始) • [使用说明](#-使用说明) • [高级功能](#-高级功能) • [常见问题](#-常见问题)

</div>

---

## 📖 简介

摸鱼浏览器是一款基于 PySide6 和 QtWebEngine 开发的轻量级桌面浏览器，具有以下核心特性：

- 🎯 **窗口置顶** - 始终保持在最前端，方便查阅资料
- 👁️ **透明度调节** - 自由调整窗口透明度，隐蔽又实用
- ⚡ **老板键** - 一键最小化，让你的浏览无后顾之忧
- 🎨 **主题切换** - 支持浅色/深色/跟随系统主题
- 🚀 **轻量快速** - 启动迅速，占用资源少

---

## ✨ 功能特点

### 核心功能

| 功能 | 描述 | 快捷操作 |
|------|------|----------|
| 🔝 **窗口置顶** | 让浏览器窗口始终显示在其他窗口之上 | 点击 `📌置顶` 按钮 |
| 👻 **透明度调节** | 调整窗口透明度 (5%-100%) | 拖动底部透明度滑块 |
| 🚨 **老板键** | 快速最小化窗口 | 默认 `F1`，可自定义 |
| 🎨 **主题模式** | 浅色/深色/跟随系统 | 设置中选择主题 |
| 🌐 **完整浏览器功能** | 前进、后退、地址栏导航 | 标准浏览器操作 |

### 技术特性

- ✅ 自定义 User-Agent，完美兼容各类网站
- ✅ 自动处理弹出窗口和新标签页
- ✅ 媒体元素自动清理（切换页面时停止音视频）
- ✅ 支持 HTTPS 和 HTTP 协议
- ✅ Windows 系统主题自动检测

---

## 🚀 快速开始

### 环境要求

```
Python: 3.8 或更高版本
操作系统: Windows 10+, macOS 10.14+, Linux
推荐: Windows 10/11 (完整功能支持)
```

### 安装步骤

#### 方法 1: 从源码运行（推荐开发者）

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/mini-browser.git
cd mini-browser

# 2. 创建虚拟环境（推荐）
python -m venv venv

# Windows 激活虚拟环境
venv\Scripts\activate

# Linux/macOS 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 使用清华镜像加速（可选，推荐国内用户）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 4. 运行程序
python main.py
```

#### 方法 2: 打包为可执行文件

```bash
# 1. 安装 PyInstaller
pip install pyinstaller

# 2. 打包程序
pyinstaller --onefile --windowed --icon=1.ico --name=摸鱼浏览器 main.py

# 3. 可执行文件位于 dist/ 目录下
```

**打包参数说明：**
- `--onefile`: 打包成单个 exe 文件
- `--windowed`: 不显示控制台窗口
- `--icon=1.ico`: 设置程序图标
- `--name=摸鱼浏览器`: 设置输出文件名

---

## 📘 使用说明

### 基础操作

#### 1. 浏览网页

```
• 在地址栏输入网址（自动添加 https://）
• 按回车或点击「前往」按钮
• 使用 ← → 按钮进行前进后退
```

#### 2. 窗口置顶

```
• 点击左上角 📌置顶 按钮
• 窗口将始终显示在最前端
• 再次点击取消置顶（显示为 📍置顶）
```

#### 3. 调整透明度

```
• 拖动底部透明度滑块
• 范围: 5% - 100%
• 实时预览效果
```

#### 4. 老板键使用

```
• 默认快捷键: F1
• 按下后窗口立即最小化
• 可在设置中自定义快捷键
```

### 高级设置

点击右下角 ⚙ 按钮打开设置面板：

#### 自定义老板键

```
1. 在「老板键」输入框中输入快捷键
   支持格式: F1, Ctrl+Q, Alt+H 等
2. 点击「保存」按钮
3. 设置立即生效
```

#### 切换主题

```
• 浅色: 适合白天使用，眼睛舒适
• 深色: 适合夜间使用，省电护眼
• 跟随系统: 自动跟随操作系统主题设置
```

---

## 🔧 高级功能

### 自定义配置

程序支持以下自定义：

```python
# 修改默认主页
self.web_view.load(QUrl("https://www.google.com"))

# 修改默认透明度
self.opacity_slider.setValue(80)  # 80%

# 修改窗口大小
self.resize(1200, 800)

# 修改默认老板键
self.boss_shortcut_key = 'F2'  # 或 'Ctrl+H'
```

### 项目结构

```
mini-browser/
├── Moyu.py              # 主程序文件
├── requirements.txt     # 依赖列表
├── README.md           # 项目说明
├── 1.ico               # 程序图标
├── venv/               # 虚拟环境（可选）
└── dist/               # 打包输出目录
```

---

## 💡 使用技巧

### 推荐场景

1. **查阅文档** - 置顶窗口，边写代码边看文档
2. **监控数据** - 透明窗口，实时查看数据面板
3. **在线学习** - 视频课程，老板键快速隐藏
4. **多任务处理** - 小窗口浏览，不影响主工作区

### 快捷键组合

| 操作 | Windows/Linux | macOS |
|------|---------------|-------|
| 前进 | 点击 → 按钮 | 点击 → 按钮 |
| 后退 | 点击 ← 按钮 | 点击 ← 按钮 |
| 刷新 | F5 (标准浏览器) | Cmd+R |
| 老板键 | F1 (可自定义) | F1 (可自定义) |
| 打开设置 | 点击 ⚙ | 点击 ⚙ |

---

## ❓ 常见问题

### Q: 程序无法启动？

**A:** 检查以下几点：
1. Python 版本是否 >= 3.8
2. 是否正确安装 PySide6: `pip install PySide6`
3. 尝试更新到最新版本: `pip install --upgrade PySide6`

### Q: 网页显示不正常？

**A:** 可能原因：
- 某些网站对 QtWebEngine 支持不完善
- 尝试在设置中切换主题
- 检查网络连接

### Q: 老板键不生效？

**A:** 解决方法：
1. 确认快捷键格式正确（如 `F1`, `Ctrl+Q`）
2. 检查是否与系统快捷键冲突
3. 尝试更换其他快捷键

### Q: 如何卸载？

**A:** 
- 源码运行: 删除项目文件夹即可
- 可执行文件: 直接删除 exe 文件
- 虚拟环境: 删除 venv 文件夹

### Q: Windows Defender 误报？

**A:** 这是 PyInstaller 打包程序的常见问题：
1. 添加白名单或信任该程序
2. 或者直接运行源码版本

---

## 🛠️ 技术栈

- **框架**: PySide6 (Qt for Python)
- **浏览器引擎**: QtWebEngine (基于 Chromium)
- **语言**: Python 3.8+
- **打包工具**: PyInstaller

---

## 📝 开发计划

- [ ] 添加书签功能
- [ ] 支持多标签页
- [ ] 历史记录管理
- [ ] 下载管理器
- [ ] 扩展插件系统
- [ ] 自动更新功能
- [ ] 导入/导出配置

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

## 👨‍💻 作者

**创建日期**: 2025  
**联系方式**: Lanc.top

---

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐

---

<div align="center">

**[⬆ 回到顶部](#-摸鱼浏览器-mini-browser)**

Made with ❤️ by [Your Name]

</div>
