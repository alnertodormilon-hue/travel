from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from ..core.database import Base

# 内容和标签的多对多关联表
content_tag_association = Table(
    'content_tag',
    Base.metadata,
    Column('content_id', Integer, ForeignKey('content.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

class Content(Base):
    """旅行内容模型"""
    __tablename__ = "content"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    cover_image: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    
    # 业务特色字段
    travel_pace: Mapped[str] = mapped_column(String(50), nullable=False, comment="旅行节奏（如慢充/轻徒步/深度文化等）")
    vibe_rating: Mapped[float] = mapped_column(Float, nullable=False, comment="氛围评分（1-5星）")
    estimated_budget: Mapped[str] = mapped_column(String(20), nullable=False, comment="预算（低/中/高）")
    
    view_count: Mapped[int] = mapped_column(Integer, default=0, comment="浏览量")
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否发布")
    created_at: Mapped[str] = mapped_column(String(50), server_default=func.current_timestamp(), comment="创建时间")
    updated_at: Mapped[str] = mapped_column(String(50), server_default=func.current_timestamp(), onupdate=func.current_timestamp(), comment="更新时间")
    
    # 关联关系
    images = relationship("Image", back_populates="content", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=content_tag_association, back_populates="contents")

class Tag(Base):
    """标签模型"""
    __tablename__ = "tag"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    color: Mapped[str] = mapped_column(String(20), nullable=False, comment="标签颜色")
    created_at: Mapped[str] = mapped_column(String(50), server_default=func.current_timestamp(), comment="创建时间")
    
    # 关联关系
    contents = relationship("Content", secondary=content_tag_association, back_populates="tags")

class Image(Base):
    """图片模型"""
    __tablename__ = "image"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content_id: Mapped[int] = mapped_column(Integer, ForeignKey("content.id"), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    caption: Mapped[str] = mapped_column(String(255), nullable=True, comment="图片说明")
    order: Mapped[int] = mapped_column(Integer, default=0, comment="排序")
    created_at: Mapped[str] = mapped_column(String(50), server_default=func.current_timestamp(), comment="创建时间")
    
    # 关联关系
    content = relationship("Content", back_populates="images")
