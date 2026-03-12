# 🌍 100个不可思议的旅行

> 发现小众、有深度的旅行体验

一个展示全球精选旅行目的地的全栈 Web 应用，采用现代技术栈构建，支持内容筛选、分类浏览和响应式设计。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Next.js](https://img.shields.io/badge/Next.js-15-black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)

## 📸 项目预览

![项目截图](https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1200)

## ✨ 核心特性

### 🎨 前端特性
- **响应式瀑布流布局** - 自适应桌面、平板、手机多种屏幕
- **精美卡片设计** - 悬停动画、渐变效果、圆角设计
- **智能筛选** - 按旅行节奏（慢充/轻徒步/深度文化等）筛选内容
- **骨架屏加载** - 流畅的加载体验
- **优雅的错误处理** - 网络异常时自动切换演示数据

### ⚙️ 后端特性
- **RESTful API** - 基于 FastAPI 构建的高性能接口
- **SQLite 数据库** - 轻量级本地数据存储
- **CORS 跨域支持** - 支持多端口开发环境
- **全局异常处理** - 统一的错误响应格式
- **数据模型** - 内容、标签、图片多表关联

## 🛠️ 技术栈

### 前端
| 技术 | 版本 | 用途 |
|------|------|------|
| Next.js | 15.x | React 框架 |
| TypeScript | 5.x | 类型安全 |
| Tailwind CSS | 3.4.x | 原子化 CSS |
| Lucide React | 0.400.x | 图标库 |

### 后端
| 技术 | 版本 | 用途 |
|------|------|------|
| FastAPI | 0.104+ | Python Web 框架 |
| SQLAlchemy | 2.0+ | ORM 数据库操作 |
| Pydantic | 2.0+ | 数据验证 |
| Uvicorn | 0.24+ | ASGI 服务器 |
| SQLite | - | 数据库 |

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Node.js 18+
- npm 或 pnpm

### 1. 克隆仓库

```bash
git clone https://github.com/alnertodormilon-hue/travel.git
cd travel
```

### 2. 启动后端服务

```bash
cd backend

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或: venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 启动服务
python -m uvicorn app.main:app --reload --port 8000
```

后端服务将运行在 http://localhost:8000

### 3. 启动前端服务

```bash
cd frontend

# 安装依赖
npm install
# 或: pnpm install

# 启动开发服务器
npm run dev
```

前端服务将运行在 http://localhost:3000

### 4. 访问应用

打开浏览器访问 http://localhost:3000

## 📁 项目结构

```
travel/
├── backend/                  # 后端项目
│   ├── app/
│   │   ├── api/v1/          # API 路由
│   │   ├── core/            # 核心配置（数据库）
│   │   ├── models/          # SQLAlchemy 数据模型
│   │   └── main.py          # 应用入口
│   ├── scripts/             # 数据初始化脚本
│   ├── tests/               # 单元测试
│   ├── requirements.txt     # Python 依赖
│   └── travel.db            # SQLite 数据库
│
├── frontend/                # 前端项目
│   ├── app/                 # Next.js App Router
│   │   ├── page.tsx         # 首页
│   │   ├── layout.tsx       # 根布局
│   │   └── globals.css      # 全局样式
│   ├── components/          # React 组件
│   │   ├── ContentCard.tsx  # 内容卡片
│   │   └── ContentCardSkeleton.tsx  # 骨架屏
│   ├── lib/                 # 工具函数
│   ├── types/               # TypeScript 类型
│   ├── package.json         # npm 依赖
│   └── tailwind.config.js   # Tailwind 配置
│
├── MVP规划.md               # 产品规划文档
└── README.md                # 项目说明
```

## 🔌 API 接口

### 基础信息
- **Base URL**: `http://localhost:8000`
- **文档地址**: `http://localhost:8000/docs` (Swagger UI)

### 主要端点

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/` | 服务状态检查 |
| GET | `/health` | 健康检查 |
| GET | `/contents` | 获取内容列表 |
| GET | `/contents/{id}` | 获取内容详情 |

### 查询参数

**GET /contents**
- `skip` - 跳过的记录数（分页）
- `limit` - 返回的最大记录数
- `travel_pace` - 旅行节奏筛选（slow/light/deep/adventure/relax）

## 🎯 功能模块

### 内容管理
- ✅ 内容列表展示（瀑布流布局）
- ✅ 内容详情查看
- ✅ 按旅行节奏筛选
- ✅ 浏览量统计

### 数据模型

**Content（内容）**
- id: 主键
- title: 标题
- description: 描述
- cover_image: 封面图 URL
- location: 地点
- travel_pace: 旅行节奏
- vibe_rating: 氛围评分（1-5星）
- estimated_budget: 预算等级
- view_count: 浏览量

**Tag（标签）**
- id: 主键
- name: 标签名称
- color: 标签颜色

## 📝 开发计划

- [x] 项目初始化与环境搭建
- [x] 数据库设计与模型建立
- [x] 后端 API 开发
- [x] 前端核心组件开发
- [x] 前端页面开发与联调
- [ ] 内容详情页
- [ ] 搜索功能
- [ ] 用户收藏功能
- [ ] 图片上传功能
- [ ] 后台管理系统

## 🤝 贡献指南

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目基于 [MIT](LICENSE) 许可证开源。

## 🙏 致谢

- 图片素材来自 [Unsplash](https://unsplash.com)
- 图标来自 [Lucide](https://lucide.dev)

---

<p align="center">
  Made with ❤️ for travelers
</p>
