"use client";

import { useState, useEffect } from "react";
import { ContentCard } from "@/components/ContentCard";
import { ContentCardSkeletonList } from "@/components/ContentCardSkeleton";
import { getContents } from "@/lib/api";
import { Content } from "@/types/content";
import { Compass, MapPin, Mountain, RefreshCw, ServerOff } from "lucide-react";

const MOCK_CONTENTS: Content[] = [
  {
    id: 1,
    title: "冰岛极光追逐之旅",
    slug: "iceland-aurora",
    description: "在冰岛的冬季，追逐神秘的北极光，体验一生难忘的极光之旅。",
    cover_image: "https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=800",
    location: "冰岛",
    travel_pace: "slow",
    vibe_rating: 5,
    estimated_budget: "high",
    view_count: 1234,
    is_published: true,
    created_at: "2024-01-01",
    updated_at: "2024-01-01",
    images: [],
    tags: []
  },
  {
    id: 2,
    title: "日本京都深度文化游",
    slug: "kyoto-culture",
    description: "漫步在京都古老的街道，探访千年寺庙，体验传统茶道文化。",
    cover_image: "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800",
    location: "日本京都",
    travel_pace: "deep",
    vibe_rating: 4.8,
    estimated_budget: "medium",
    view_count: 2567,
    is_published: true,
    created_at: "2024-01-02",
    updated_at: "2024-01-02",
    images: [],
    tags: []
  },
  {
    id: 3,
    title: "新西兰南岛轻徒步",
    slug: "newzealand-hiking",
    description: "在新西兰南岛的雪山湖泊间徒步，感受大自然的壮丽与宁静。",
    cover_image: "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=800",
    location: "新西兰",
    travel_pace: "light",
    vibe_rating: 4.9,
    estimated_budget: "high",
    view_count: 1890,
    is_published: true,
    created_at: "2024-01-03",
    updated_at: "2024-01-03",
    images: [],
    tags: []
  },
  {
    id: 4,
    title: "泰国清迈慢生活",
    slug: "chiangmai-slow",
    description: "在清迈的咖啡馆里度过悠闲午后，体验泰北慢节奏的生活方式。",
    cover_image: "https://images.unsplash.com/photo-1598935898639-33d885d54861?w=800",
    location: "泰国清迈",
    travel_pace: "slow",
    vibe_rating: 4.5,
    estimated_budget: "low",
    view_count: 3421,
    is_published: true,
    created_at: "2024-01-04",
    updated_at: "2024-01-04",
    images: [],
    tags: []
  },
];

export default function DiscoverPage() {
  const [contents, setContents] = useState<Content[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [usingMockData, setUsingMockData] = useState(false);

  useEffect(() => {
    async function fetchContents() {
      try {
        setLoading(true);
        setError(null);
        setUsingMockData(false);
        
        const data = await getContents({ skip: 0, limit: 12 });
        setContents(data);
      } catch (err) {
        console.error("获取内容失败:", err);
        setError("连接失败");
        setUsingMockData(true);
        setContents(MOCK_CONTENTS);
      } finally {
        setLoading(false);
      }
    }

    fetchContents();
  }, []);

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-center gap-4">
            <div className="w-10 h-10 bg-blue-500 rounded-xl flex items-center justify-center">
              <Compass className="w-6 h-6 text-white" />
            </div>
            <div className="text-center">
              <h1 className="text-xl font-bold text-gray-900">
                100个不可思议的旅行
              </h1>
              <p className="text-xs text-gray-500">
                发现小众、有深度的旅行体验
              </p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Mock Data Notice */}
        {usingMockData && (
          <div className="mb-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg flex items-center gap-3">
            <ServerOff className="w-5 h-5 text-yellow-600" />
            <p className="text-sm text-yellow-800">
              后端服务未连接，显示演示数据
            </p>
          </div>
        )}

        {/* Error State */}
        {error && !usingMockData && (
          <div className="flex flex-col items-center justify-center py-20">
            <MapPin className="w-12 h-12 text-red-500 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">加载失败</h3>
            <p className="text-gray-500 mb-4">{error}</p>
            <button
              onClick={() => window.location.reload()}
              className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
              <RefreshCw className="w-4 h-4 inline mr-2" />
              重新加载
            </button>
          </div>
        )}

        {/* Content Grid */}
        {(!error || usingMockData) && (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {loading ? (
              <ContentCardSkeletonList count={8} />
            ) : (
              contents.map((content) => (
                <ContentCard key={content.id} content={content} />
              ))
            )}
          </div>
        )}

        {/* Empty State */}
        {!loading && contents.length === 0 && (
          <div className="flex flex-col items-center justify-center py-20">
            <Mountain className="w-12 h-12 text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900">暂无内容</h3>
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 text-center">
          <p className="text-sm text-gray-500">2024 100个不可思议的旅行</p>
        </div>
      </footer>
    </main>
  );
}
