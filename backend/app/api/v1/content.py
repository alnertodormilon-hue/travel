from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from ...core.database import get_db
from ...models.models import Content, Tag, Image
from ...schemas.schemas import ContentCreate, ContentResponse

# 创建API路由实例
router = APIRouter(prefix="/contents", tags=["内容管理"])


@router.get(
    "",
    response_model=List[ContentResponse],
    summary="获取内容列表（发现页）",
    description="支持分页和按旅行节奏筛选，返回内容列表（不包含完整富文本）"
)
def get_contents(
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(10, ge=1, le=100, description="返回的最大记录数"),
    travel_pace: Optional[str] = Query(None, description="旅行节奏筛选（如慢充/轻徒步/深度文化）"),
    db: Session = Depends(get_db)
) -> List[Content]:
    """
    获取内容列表接口
    
    核心逻辑：
    1. 构建基础查询，预加载关联的图片和标签
    2. 如果提供了travel_pace参数，添加筛选条件
    3. 应用分页参数
    4. 返回结果（Pydantic会自动过滤content字段）
    """
    # 构建查询，预加载关联数据
    query = db.query(Content).options(
        joinedload(Content.images),
        joinedload(Content.tags)
    )
    
    # 按旅行节奏筛选
    if travel_pace:
        query = query.filter(Content.travel_pace == travel_pace)
    
    # 只查询已发布的内容
    query = query.filter(Content.is_published == True)
    
    # 按创建时间倒序排列
    query = query.order_by(Content.created_at.desc())
    
    # 应用分页
    contents = query.offset(skip).limit(limit).all()
    
    return contents


@router.get(
    "/{content_id}",
    response_model=ContentResponse,
    summary="获取内容详情",
    description="根据ID获取单条内容详情，包含关联的图片和标签信息"
)
def get_content(
    content_id: int,
    db: Session = Depends(get_db)
) -> Content:
    """
    获取内容详情接口
    
    核心逻辑：
    1. 使用joinedload预加载关联的图片和标签，避免N+1查询问题
    2. 查询指定ID的内容
    3. 如果内容不存在，抛出404异常
    4. 增加浏览量计数
    """
    # 使用joinedload预加载关联数据，避免N+1查询
    content = db.query(Content).options(
        joinedload(Content.images),
        joinedload(Content.tags)
    ).filter(Content.id == content_id).first()
    
    # 如果内容不存在，抛出404异常
    if content is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID为 {content_id} 的内容不存在"
        )
    
    # 增加浏览量
    content.view_count += 1
    db.commit()
    
    return content


@router.post(
    "",
    response_model=ContentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="创建新内容",
    description="接收ContentCreate Schema，创建新的旅行内容"
)
def create_content(
    content_data: ContentCreate,
    db: Session = Depends(get_db)
) -> Content:
    """
    创建内容接口
    
    核心逻辑：
    1. 从请求数据中提取标签ID列表
    2. 创建Content模型实例（排除tag_ids字段）
    3. 如果提供了标签ID，查询并关联对应的标签
    4. 保存到数据库并返回创建的内容
    """
    # 提取标签ID列表
    tag_ids = content_data.tag_ids
    
    # 创建Content实例，排除tag_ids字段
    content_dict = content_data.model_dump(exclude={"tag_ids"})
    db_content = Content(**content_dict)
    
    # 如果提供了标签ID，关联对应的标签
    if tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()
        db_content.tags = tags
    
    # 保存到数据库
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    
    # 重新加载关联数据以返回完整响应
    db.refresh(db_content, attribute_names=["images", "tags"])
    
    return db_content
