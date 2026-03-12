"""
FastAPI应用主入口
包含CORS配置和全局异常处理
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from app.api.v1.content import router as content_router
from app.core.database import engine, Base

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastAPI应用实例
app = FastAPI(
    title="100个不可思议的旅行 API",
    description="为小众旅行体验提供内容管理的后端API",
    version="1.0.0"
)

# ============================================
# 场景A：CORS跨域配置
# 允许前端应用（如http://localhost:3000）进行跨域访问
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # Next.js开发服务器
        "http://localhost:3001",      # 备用端口
        "http://127.0.0.1:3000",      # 本地IP访问
    ],
    allow_credentials=True,           # 允许携带凭证（cookies等）
    allow_methods=["*"],              # 允许所有HTTP方法
    allow_headers=["*"],              # 允许所有请求头
)

# 创建数据库表（开发环境使用，生产环境建议使用Alembic迁移）
Base.metadata.create_all(bind=engine)

# 注册路由（content_router已经在定义时包含prefix="/contents"）
app.include_router(content_router)


# ============================================
# 全局异常处理器
# 捕获所有未处理的异常，返回统一的错误格式
# ============================================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    全局异常处理器
    
    作用：
    1. 捕获所有未处理的500内部服务器错误
    2. 不向客户端暴露底层堆栈信息
    3. 返回统一格式的JSON错误响应
    4. 记录详细错误日志供开发者排查
    """
    # 记录详细错误信息到日志（包含堆栈）
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    
    # 返回统一的错误响应（不包含敏感信息）
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "服务器内部错误，请稍后重试",
                "type": "server_error"
            },
            "data": None
        }
    )


# 自定义HTTP异常处理器
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """处理404未找到异常"""
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error": {
                "code": "NOT_FOUND",
                "message": "请求的资源不存在",
                "type": "not_found"
            },
            "data": None
        }
    )


@app.get("/")
async def root():
    """根路径健康检查"""
    return {
        "success": True,
        "message": "100个不可思议的旅行 API 服务正常运行",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {
        "success": True,
        "status": "healthy",
        "service": "travel-api"
    }
