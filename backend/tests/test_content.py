"""
内容模块API单元测试
使用pytest和FastAPI TestClient进行测试
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


# 使用内存数据库进行测试
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# 创建测试数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# 创建测试会话工厂
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 测试固件：创建数据库表
def setup_module(module):
    """测试模块开始前创建所有表"""
    Base.metadata.create_all(bind=engine)


def teardown_module(module):
    """测试模块结束后删除所有表"""
    Base.metadata.drop_all(bind=engine)


# 依赖覆盖：使用测试数据库会话
def override_get_db():
    """覆盖原有的get_db依赖，使用测试数据库"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# 应用依赖覆盖
app.dependency_overrides[get_db] = override_get_db

# 创建TestClient实例
client = TestClient(app)


class TestContentAPI:
    """内容API测试类"""

    def test_create_content_success(self):
        """
        测试场景1：正常发布内容
        验证：返回201状态码，数据正确保存
        """
        # 准备测试数据
        content_data = {
            "title": "探索云南秘境",
            "slug": "explore-yunnan-secret",
            "description": "深入云南大山，发现不为人知的美景",
            "content": "这是一篇关于云南旅行的详细攻略...",
            "cover_image": "https://example.com/yunnan.jpg",
            "location": "云南省",
            "travel_pace": "slow",
            "vibe_rating": 4.5,
            "estimated_budget": "medium",
            "tag_ids": []
        }

        # 发送POST请求
        response = client.post("/contents", json=content_data)

        # 验证响应
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == content_data["title"]
        assert data["slug"] == content_data["slug"]
        assert data["travel_pace"] == "slow"
        assert data["vibe_rating"] == 4.5
        assert "id" in data
        assert data["is_published"] == False  # 默认未发布

    def test_create_content_missing_required_fields(self):
        """
        测试场景2：异常流 - 缺少必填字段
        验证：返回422状态码，提示验证错误
        """
        # 准备缺少必填字段的数据
        incomplete_data = {
            "title": "测试标题",
            # 缺少slug、description等必填字段
        }

        # 发送POST请求
        response = client.post("/contents", json=incomplete_data)

        # 验证响应
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data

    def test_get_contents_list(self):
        """
        测试场景3：正常获取内容列表
        验证：返回200状态码，列表格式正确
        """
        # 先创建一条测试数据
        content_data = {
            "title": "西藏朝圣之旅",
            "slug": "tibet-pilgrimage",
            "description": "心灵的洗礼，西藏深度游",
            "content": "西藏旅行详细内容...",
            "cover_image": "https://example.com/tibet.jpg",
            "location": "西藏自治区",
            "travel_pace": "deep",
            "vibe_rating": 5.0,
            "estimated_budget": "high",
            "tag_ids": []
        }
        create_response = client.post("/contents", json=content_data)
        created_content = create_response.json()
        
        # 注意：GET接口只返回已发布内容，这里我们验证接口正常工作
        # 实际应用中需要通过其他方式（如后台管理）将内容设置为已发布
        
        # 发送GET请求
        response = client.get("/contents?skip=0&limit=10")

        # 验证响应
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        # 由于新创建的内容默认未发布，列表可能为空，这是预期行为
        # 我们主要验证接口返回格式正确

    def test_get_contents_with_pagination(self):
        """
        测试场景4：分页功能测试
        验证：skip和limit参数正常工作
        """
        # 发送分页请求
        response = client.get("/contents?skip=0&limit=5")

        # 验证响应
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 5  # 不超过limit限制

    def test_get_content_detail_not_found(self):
        """
        测试场景5：异常流 - 获取不存在的内容详情
        验证：返回404状态码
        """
        # 请求一个不存在的ID
        response = client.get("/contents/99999")

        # 验证响应
        assert response.status_code == 404
        data = response.json()
        # 全局异常处理器返回统一格式
        assert "error" in data
        assert data["error"]["code"] == "NOT_FOUND"
