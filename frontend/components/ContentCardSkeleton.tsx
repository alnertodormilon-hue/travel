"use client";

/**
 * 内容卡片骨架屏组件
 * 用于数据加载时显示占位效果，避免页面白屏
 * 
 * 设计原理：
 * 1. 使用shimmer动画实现流光效果
 * 2. 结构与真实卡片保持一致，减少视觉跳动
 * 3. 使用渐变背景增加视觉层次
 */

export function ContentCardSkeleton() {
  return (
    <div className="relative bg-white rounded-2xl overflow-hidden shadow-soft border border-gray-100">
      {/* 图片区域骨架 */}
      <div className="relative aspect-[4/3] bg-gradient-to-br from-gray-200 via-gray-100 to-gray-200 overflow-hidden">
        {/* 流光动画效果 */}
        <div className="absolute inset-0 -translate-x-full animate-shimmer bg-gradient-to-r from-transparent via-white/40 to-transparent" />
        
        {/* 顶部标签占位 */}
        <div className="absolute top-3 left-3 flex gap-2">
          <div className="w-20 h-7 bg-white/60 rounded-full backdrop-blur-sm" />
          <div className="w-16 h-7 bg-white/60 rounded-full backdrop-blur-sm" />
        </div>
        
        {/* 收藏按钮占位 */}
        <div className="absolute top-3 right-3 w-9 h-9 bg-white/60 rounded-full backdrop-blur-sm" />
        
        {/* 底部评分占位 */}
        <div className="absolute bottom-4 left-4 flex gap-1">
          {Array.from({ length: 5 }).map((_, i) => (
            <div key={i} className="w-3.5 h-3.5 bg-white/40 rounded-full" />
          ))}
        </div>
      </div>

      {/* 内容区域骨架 */}
      <div className="p-5 space-y-4">
        {/* 标题占位 */}
        <div className="space-y-2">
          <div className="h-5 bg-gray-200 rounded-lg w-full relative overflow-hidden">
            <div className="absolute inset-0 -translate-x-full animate-shimmer bg-gradient-to-r from-transparent via-white/60 to-transparent" />
          </div>
          <div className="h-5 bg-gray-200 rounded-lg w-3/4 relative overflow-hidden">
            <div className="absolute inset-0 -translate-x-full animate-shimmer bg-gradient-to-r from-transparent via-white/60 to-transparent" />
          </div>
        </div>
        
        {/* 描述占位 */}
        <div className="space-y-2">
          <div className="h-3.5 bg-gray-200 rounded w-full relative overflow-hidden">
            <div className="absolute inset-0 -translate-x-full animate-shimmer bg-gradient-to-r from-transparent via-white/60 to-transparent" />
          </div>
          <div className="h-3.5 bg-gray-200 rounded w-5/6 relative overflow-hidden">
            <div className="absolute inset-0 -translate-x-full animate-shimmer bg-gradient-to-r from-transparent via-white/60 to-transparent" />
          </div>
        </div>
        
        {/* 底部信息占位 */}
        <div className="flex justify-between items-center pt-3 border-t border-gray-100">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 bg-gray-200 rounded-full" />
            <div className="w-20 h-3.5 bg-gray-200 rounded" />
          </div>
          <div className="w-14 h-3 bg-gray-200 rounded" />
        </div>
      </div>
    </div>
  );
}

/**
 * 骨架屏列表组件
 * 用于显示多个骨架屏卡片
 */
interface SkeletonListProps {
  count?: number;
}

export function ContentCardSkeletonList({ count = 6 }: SkeletonListProps) {
  return (
    <>
      {Array.from({ length: count }).map((_, i) => (
        <div 
          key={i} 
          className="animate-fade-in"
          style={{ animationDelay: `${i * 80}ms` }}
        >
          <ContentCardSkeleton />
        </div>
      ))}
    </>
  );
}
