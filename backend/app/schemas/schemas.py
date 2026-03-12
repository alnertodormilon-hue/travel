from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ImageBase(BaseModel):
    """图片基础模式"""
    url: str = Field(..., description="图片URL")
    caption: Optional[str] = Field(None, description="图片说明")
    order: int = Field(0, description="排序")

class ImageCreate(ImageBase):
    """创建图片模式"""
    pass

class ImageResponse(ImageBase):
    """图片响应模式"""
    id: int
    content_id: int
    created_at: str
    
    class Config:
        from_attributes = True

class TagBase(BaseModel):
    """标签基础模式"""
    name: str = Field(..., description="标签名称")
    slug: str = Field(..., description="URL友好标识")
    color: str = Field(..., description="标签颜色")

class TagCreate(TagBase):
    """创建标签模式"""
    pass

class TagResponse(TagBase):
    """标签响应模式"""
    id: int
    created_at: str
    
    class Config:
        from_attributes = True

class ContentBase(BaseModel):
    """内容基础模式"""
    title: str = Field(..., description="标题")
    slug: str = Field(..., description="URL友好标识")
    description: str = Field(..., description="简介")
    content: str = Field(..., description="富文本内容")
    cover_image: str = Field(..., description="封面图")
    location: str = Field(..., description="地点")
    travel_pace: str = Field(..., description="旅行节奏（如慢充/轻徒步/深度文化等）")
    vibe_rating: float = Field(..., ge=1, le=5, description="氛围评分（1-5星）")
    estimated_budget: str = Field(..., description="预算（低/中/高）")

class ContentCreate(ContentBase):
    """创建内容模式"""
    tag_ids: List[int] = Field(default_factory=list, description="标签ID列表")

class ContentUpdate(BaseModel):
    """更新内容模式"""
    title: Optional[str] = Field(None, description="标题")
    slug: Optional[str] = Field(None, description="URL友好标识")
    description: Optional[str] = Field(None, description="简介")
    content: Optional[str] = Field(None, description="富文本内容")
    cover_image: Optional[str] = Field(None, description="封面图")
    location: Optional[str] = Field(None, description="地点")
    travel_pace: Optional[str] = Field(None, description="旅行节奏")
    vibe_rating: Optional[float] = Field(None, ge=1, le=5, description="氛围评分")
    estimated_budget: Optional[str] = Field(None, description="预算")
    is_published: Optional[bool] = Field(None, description="是否发布")
    tag_ids: Optional[List[int]] = Field(None, description="标签ID列表")

class ContentResponse(ContentBase):
    """内容响应模式"""
    id: int
    view_count: int
    is_published: bool
    created_at: str
    updated_at: str
    images: List[ImageResponse] = Field(default_factory=list, description="相关图片")
    tags: List[TagResponse] = Field(default_factory=list, description="相关标签")
    
    class Config:
        from_attributes = True
