export interface Tag {
  id: number;
  name: string;
  slug: string;
  color: string;
}

export interface Image {
  id: number;
  content_id: number;
  url: string;
  caption?: string;
  order: number;
}

export interface Content {
  id: number;
  title: string;
  slug: string;
  description: string;
  cover_image: string;
  location: string;
  travel_pace: string;
  vibe_rating: number;
  estimated_budget: string;
  view_count: number;
  is_published: boolean;
  created_at: string;
  updated_at: string;
  images: Image[];
  tags: Tag[];
}
