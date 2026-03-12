# 100个不可思议的旅行 - MVP规划文档

## 一、MVP核心功能拆解

### 1.1 页面清单
- **首页（发现页）**：展示精选旅行内容，瀑布流/卡片式布局
- **内容详情页**：单个旅行目的地/体验的完整展示
- **分类/标签页**：按主题、地区等维度筛选内容
- **搜索页**：关键词搜索功能
- **关于页**：产品介绍、愿景说明

### 1.2 功能模块
- **内容展示模块**：图文混排、视频嵌入、地点标记
- **分类筛选模块**：多维度标签筛选
- **搜索模块**：全文检索
- **内容管理模块（后台）**：
  - 内容CRUD（增删改查）
  - 标签管理
  - 图片上传
- **数据统计模块**：内容浏览量统计

---

## 二、技术栈与架构设计

### 2.1 技术栈选型

#### 前端
- **框架**：Next.js 15 (React)
- **UI组件库**：shadcn/ui + Tailwind CSS
- **状态管理**：React Query (数据获取) + Zustand (轻量级状态)
- **路由**：Next.js App Router
- **图片处理**：Next.js Image Component

#### 后端
- **框架**：FastAPI (Python)
- **数据库**：SQLite
- **ORM**：SQLAlchemy 2.0 + Alembic (数据库迁移)
- **数据验证**：Pydantic v2
- **文件上传**：python-multipart
- **CORS**：fastapi-cors

#### 开发工具
- **包管理**：pnpm (前端) + uv (Python)
- **代码规范**：ESLint + Prettier (前端) + Ruff (Python)
- **类型检查**：TypeScript (前端) + mypy (Python)

### 2.2 项目目录结构

```
mzj/
├── frontend/                 # 前端项目
│   ├── app/                  # Next.js App Router
│   │   ├── (marketing)/     # 营销页面（首页、关于）
│   │   ├── (content)/       # 内容页面
│   │   ├── api/             # 前端API代理
│   │   └── layout.tsx
│   ├── components/          # 通用组件
│   │   ├── ui/             # shadcn/ui组件
│   │   └── ...
│   ├── lib/                 # 工具函数
│   ├── hooks/               # 自定义Hooks
│   ├── types/               # TypeScript类型定义
│   └── public/              # 静态资源
│
├── backend/                  # 后端项目
│   ├── app/
│   │   ├── api/             # API路由
│   │   │   ├── v1/
│   │   │   │   ├── content.py
│   │   │   │   ├── tags.py
│   │   │   │   └── search.py
│   │   │   └── deps.py      # 依赖注入
│   │   ├── core/            # 核心配置
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── models/          # 数据库模型
│   │   ├── schemas/         # Pydantic模式
│   │   ├── crud/            # 数据库操作
│   │   └── main.py          # 应用入口
│   ├── alembic/             # 数据库迁移
│   ├── uploads/             # 上传文件存储
│   └── requirements.txt
│
├── docs/                     # 文档
├── scripts/                  # 脚本
└── README.md
```

---

## 三、开发路径规划

### 阶段1：项目初始化与环境搭建
**目标**：搭建前后端基础框架，建立开发环境

- [ ] 创建项目目录结构
- [ ] 初始化前端项目（Next.js + shadcn/ui + Tailwind）
- [ ] 初始化后端项目（FastAPI + SQLAlchemy）
- [ ] 配置代码规范工具（ESLint、Prettier、Ruff）
- [ ] 配置Git仓库与.gitignore

### 阶段2：数据库设计与模型建立
**目标**：完成数据库表结构设计，建立ORM模型

- [ ] 设计数据库表结构（内容表、标签表、关联表等）
- [ ] 创建SQLAlchemy模型
- [ ] 配置Alembic并生成初始迁移
- [ ] 编写数据库CRUD基础操作

### 阶段3：后端API开发
**目标**：完成MVP所需的RESTful API接口

- [ ] 实现内容CRUD API
- [ ] 实现标签管理API
- [ ] 实现搜索API
- [ ] 实现文件上传API
- [ ] 添加CORS配置
- [ ] API接口测试（Swagger UI）

### 阶段4：前端核心组件开发
**目标**：开发可复用的UI组件

- [ ] 实现内容卡片组件
- [ ] 实现图片轮播/画廊组件
- [ ] 实现搜索框组件
- [ ] 实现标签筛选组件
- [ ] 实现响应式布局基础

### 阶段5：前端页面开发与联调
**目标**：完成所有页面开发，前后端联调

- [ ] 开发首页（发现页）
- [ ] 开发内容详情页
- [ ] 开发分类/标签页
- [ ] 开发搜索结果页
- [ ] 开发关于页
- [ ] 前后端接口联调
- [ ] 响应式适配测试

### 阶段6：数据填充与测试
**目标**：填充示例数据，完成整体测试

- [ ] 准备示例内容数据
- [ ] 开发数据导入脚本
- [ ] 功能测试
- [ ] 性能优化（图片懒加载等）
- [ ] 兼容性测试

---

## 四、核心数据表设计（预览）

### content（内容表）
- id: 主键
- title: 标题
- slug: URL友好标识
- description: 简介
- content: 富文本内容
- cover_image: 封面图
- location: 地点
- experience_type: 体验类型（如慢充/轻徒步/深度文化等）
- atmosphere_rating: 氛围评分（1-5星）
- budget: 预算（低/中/高）
- view_count: 浏览量
- is_published: 是否发布
- created_at: 创建时间
- updated_at: 更新时间

### tag（标签表）
- id: 主键
- name: 标签名称
- slug: URL友好标识
- color: 标签颜色
- created_at: 创建时间

### content_tag（内容标签关联表）
- content_id: 内容ID
- tag_id: 标签ID

### image（图片表）
- id: 主键
- content_id: 关联内容ID
- url: 图片URL
- caption: 图片说明
- order: 排序
- created_at: 创建时间
