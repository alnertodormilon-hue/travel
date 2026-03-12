"use client";

import { useState } from "react";
import { MapPin, Star, Eye, Heart, ImageOff } from "lucide-react";
import { Content } from "@/types/content";

interface ContentCardProps {
  content: Content;
}

export function ContentCard({ content }: ContentCardProps) {
  const [imageError, setImageError] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [isLiked, setIsLiked] = useState(false);

  const paceConfig: Record<string, { label: string; icon: string; bgColor: string }> = {
    "slow": { label: "慢充", icon: "🌴", bgColor: "bg-amber-500" },
    "light": { label: "轻徒步", icon: "🥾", bgColor: "bg-green-500" },
    "deep": { label: "深度文化", icon: "🏛️", bgColor: "bg-purple-500" },
    "adventure": { label: "探险", icon: "⛺", bgColor: "bg-red-500" },
    "relax": { label: "休闲度假", icon: "🏖️", bgColor: "bg-blue-500" }
  };

  const budgetConfig: Record<string, { label: string; bgColor: string }> = {
    "low": { label: "低预算", bgColor: "bg-green-100 text-green-700" },
    "medium": { label: "中预算", bgColor: "bg-yellow-100 text-yellow-700" },
    "high": { label: "高预算", bgColor: "bg-orange-100 text-orange-700" }
  };

  const paceInfo = paceConfig[content.travel_pace] || { 
    label: content.travel_pace, 
    icon: "✈️",
    bgColor: "bg-gray-500"
  };
  
  const budgetInfo = budgetConfig[content.estimated_budget] || { 
    label: content.estimated_budget, 
    bgColor: "bg-gray-100 text-gray-700"
  };

  return (
    <article
      className={`
        group relative bg-white rounded-xl overflow-hidden
        transition-all duration-300 cursor-pointer
        border border-gray-100
        ${isHovered ? "shadow-xl -translate-y-1" : "shadow-sm"}
      `}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      {/* 图片容器 */}
      <div className="relative aspect-[4/3] overflow-hidden bg-gray-100">
        {!imageError ? (
          <img
            src={content.cover_image}
            alt={content.title}
            className={`
              w-full h-full object-cover transition-transform duration-500
              ${isHovered ? "scale-105" : "scale-100"}
            `}
            onError={() => setImageError(true)}
          />
        ) : (
          <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-200">
            <ImageOff className="w-10 h-10 text-gray-400 mb-2" />
            <span className="text-sm text-gray-500">图片加载失败</span>
          </div>
        )}

        {/* 渐变遮罩 */}
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent" />

        {/* 收藏按钮 */}
        <button
          onClick={(e) => {
            e.stopPropagation();
            setIsLiked(!isLiked);
          }}
          className={`
            absolute top-3 right-3 z-10
            w-8 h-8 rounded-full flex items-center justify-center
            transition-all duration-200
            ${isLiked 
              ? "bg-red-500 text-white" 
              : "bg-black/30 text-white hover:bg-black/50"
            }
          `}
        >
          <Heart className={`w-4 h-4 ${isLiked ? "fill-current" : ""}`} />
        </button>

        {/* 顶部标签 */}
        <div className="absolute top-3 left-3 flex flex-wrap gap-2">
          <span className={`flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium text-white ${paceInfo.bgColor}`}>
            <span>{paceInfo.icon}</span>
            <span>{paceInfo.label}</span>
          </span>
          <span className={`px-2 py-1 rounded-full text-xs font-medium ${budgetInfo.bgColor}`}>
            {budgetInfo.label}
          </span>
        </div>

        {/* 底部评分 */}
        <div className="absolute bottom-3 left-3 flex items-center gap-1">
          <Star className="w-4 h-4 text-yellow-400 fill-yellow-400" />
          <span className="text-white text-sm font-semibold">
            {content.vibe_rating.toFixed(1)}
          </span>
        </div>
      </div>

      {/* 内容区域 */}
      <div className="p-4">
        <h3 className={`
          font-bold text-gray-900 text-base mb-2 line-clamp-2
          ${isHovered ? "text-blue-600" : ""}
        `}>
          {content.title}
        </h3>

        <p className="text-gray-500 text-sm line-clamp-2 mb-3">
          {content.description}
        </p>

        <div className="flex items-center justify-between pt-2 border-t border-gray-100">
          <div className="flex items-center gap-1 text-sm text-gray-500">
            <MapPin className="w-4 h-4" />
            <span className="truncate max-w-[100px]">{content.location}</span>
          </div>
          <div className="flex items-center gap-1 text-xs text-gray-400">
            <Eye className="w-3.5 h-3.5" />
            <span>{content.view_count.toLocaleString()}</span>
          </div>
        </div>
      </div>
    </article>
  );
}
