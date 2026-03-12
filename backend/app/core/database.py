from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite数据库连接URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./travel.db"

# ============================================
# 场景B：SQLite数据库锁问题解决方案
# 
# 问题描述：
# SQLite在并发访问时可能出现"database is locked"错误
# 
# 解决方案：
# 1. check_same_thread=False - 允许跨线程使用连接
# 2. timeout=30 - 设置连接超时时间为30秒，避免立即报错
# 3. 使用事件监听器设置busy_timeout - 让SQLite自动重试
# ============================================

# 创建数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,  # 允许跨线程使用（FastAPI异步需要）
        "timeout": 30,               # 连接超时时间30秒
    },
    # 连接池配置
    pool_pre_ping=True,              # 连接前ping测试，避免使用无效连接
    pool_recycle=3600,               # 连接回收时间1小时
)


# 设置SQLite的busy_timeout，让数据库自动处理锁等待
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """
    连接建立后执行的初始化操作
    
    busy_timeout=30000：
    - 设置SQLite在返回"database is locked"错误前等待的时间
    - 30000毫秒 = 30秒
    - 在这段时间内，SQLite会自动重试被锁定的操作
    """
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA busy_timeout=30000")  # 30秒超时
    cursor.execute("PRAGMA foreign_keys=ON")      # 启用外键约束
    cursor.close()


# 创建会话工厂
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 创建基类
Base = declarative_base()


# 依赖注入函数，用于获取数据库会话
def get_db():
    """
    FastAPI依赖注入函数
    
    使用方式：
    @app.get("/items")
    def read_items(db: Session = Depends(get_db)):
        ...
    
    确保每个请求都有独立的数据库会话，并在请求结束后正确关闭
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
