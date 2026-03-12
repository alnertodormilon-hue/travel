"""
初始化数据脚本
将搜索到的旅行素材添加到数据库中
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.models import Base, Content, Tag

# 创建表
Base.metadata.create_all(bind=engine)

# 旅行内容数据（基于搜索结果整理）
contents_data = [
    {
        "title": "雨崩村：梅里雪山脚下的徒步天堂",
        "slug": "yubeng-village-hiking",
        "description": "藏在梅里雪山腹地的'香格里拉缩影'，全村仅20余户人家。雪山、冰川、原始森林、经幡、玛尼堆，这里是徒步者心中的'人间最后秘境'。",
        "content": """
雨崩村，藏语意为"绿松石堆积的地方"，深藏在梅里雪山脚下，是徒步者心中的"人间最后秘境"。

这里雪山触手可及，冰川溪流穿村而过，牦牛与经幡共舞。直到2012年才通电通信号，
没有公路直达，进村需徒步翻山或乘越野车颠簸而入，却因此保留了最原始的藏族村落风貌。

【徒步路线】
- 神瀑线：往返约4-6小时，难度较低，适合新手
- 冰湖线：往返约8-10小时，难度中等，风景绝美
- 神湖线：往返约10-12小时，难度较高，需要向导

【最佳季节】
4-6月：杜鹃花盛开，雪山清晰可见
9-11月：秋色迷人，天气稳定

【旅行贴士】
1. 进村需徒步约6-8小时，或乘当地越野车
2. 海拔约3000-4000米，注意高反
3. 村内住宿条件有限，建议提前预订
4. 尊重当地藏族习俗，不要随意拍摄当地人
        """,
        "cover_image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "location": "云南省迪庆藏族自治州德钦县",
        "travel_pace": "light",
        "vibe_rating": 5.0,
        "estimated_budget": "medium",
        "is_published": True,
        "tags": ["徒步", "雪山", "藏族文化", "摄影"]
    },
    {
        "title": "霞浦滩涂：中国最美的光影天堂",
        "slug": "xiapu-mudflat-photography",
        "description": "在霞浦，光是活的，它会呼吸，会舞蹈，会随着潮汐的脉搏一起律动。这里不是简单的'拍照打卡地'，而是一场关于光影、劳作与时间的盛大叙事。",
        "content": """
福建霞浦藏着中国最美滩涂！潮水退去后的虎皮纹理、渔民光影中的劳作身影，
还有千年畲族古村，人均150元解锁摄影与治愈。

【摄影圣地】
- 北岐滩涂：日出最佳拍摄点，虎皮纹理滩涂
- 东壁村：日落拍摄，光影与渔排交织
- 杨家溪：晨雾中的古榕树和农夫
- 围江村馒头山：退潮时滩涂露出，涨潮时四面环水

【最佳拍摄时间】
4-6月：海带丰收季，渔民劳作场景丰富
7-9月：台风季前后，云霞变化多端
10-12月：紫菜养殖季，渔排壮观

【慢旅行体验】
1. 住在海边民宿，听着潮汐声入眠
2. 跟随渔民出海，体验传统捕捞
3. 品尝新鲜海鲜，人均50元吃到饱
4. 漫步古村落，感受畲族文化
        """,
        "cover_image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
        "location": "福建省宁德市霞浦县",
        "travel_pace": "slow",
        "vibe_rating": 4.8,
        "estimated_budget": "low",
        "is_published": True,
        "tags": ["摄影", "海岛", "慢生活", "美食"]
    },
    {
        "title": "肇兴侗寨：比千户苗寨更原生态的侗乡秘境",
        "slug": "zhaoxing-dong-village",
        "description": "这里没有过度开发，保留着最纯粹的侗族风情，青瓦木楼依山而建，梯田环绕。高铁直达，人均500元，避开人流，沉浸式感受侗族文化。",
        "content": """
位于贵州省黔东南苗族侗族自治州黎平县，距离高铁从江站仅15分钟车程，
是藏在大山深处的"侗乡秘境"。这里比西江千户苗寨更原生态，商业化程度低。

【侗族文化体验】
- 鼓楼：侗寨标志性建筑，五座鼓楼各具特色
- 风雨桥：侗族建筑艺术的精华
- 侗族大歌：世界非物质文化遗产，多声部无指挥无伴奏合唱
- 堂安梯田：徒步约2小时，俯瞰整个侗寨

【深度体验项目】
1. 学习侗族刺绣，亲手制作纪念品
2. 参加侗族长桌宴，品尝酸汤鱼、糯米饭
3. 夜宿侗家木楼，体验传统生活方式
4. 徒步堂安古道，穿越梯田与森林

【实用信息】
- 门票：80元（含侗族大歌表演）
- 住宿：侗家客栈100-200元/晚
- 最佳季节：4-10月，避开雨季
        """,
        "cover_image": "https://images.unsplash.com/photo-1528164344705-47542687000d?w=800",
        "location": "贵州省黔东南苗族侗族自治州黎平县",
        "travel_pace": "deep",
        "vibe_rating": 4.7,
        "estimated_budget": "low",
        "is_published": True,
        "tags": ["民族文化", "古村落", "建筑艺术", "非遗"]
    },
    {
        "title": "琼库什台：伊犁河谷的童话草原",
        "slug": "qiongkushitai-grassland",
        "description": "比那拉提人少，比喀拉峻原始，新疆最后的秘境。雪山、森林、草原、溪流，构成一幅绝美的天山画卷。",
        "content": """
琼库什台，藏在天山深处的哈萨克牧村，是伊犁河谷最后的秘境。
这里保留着最原始的草原生态，游客稀少，风景绝美。

【自然景观】
- 雪山：终年积雪的天山山脉
- 云杉林：原始森林茂密
- 草原：高山草甸，野花遍地
- 溪流：清澈的天山雪水

【活动体验】
1. 骑马穿越草原，感受游牧文化
2. 徒步乌孙古道，探索历史遗迹
3. 住在哈萨克毡房，品尝手抓肉
4. 夜观星空，银河清晰可见

【最佳时间】
6-8月：草原最绿，野花盛开
9月：秋色迷人，游客更少

【交通方式】
从特克斯县出发，车程约3小时
山路崎岖，建议SUV或包车前往
        """,
        "cover_image": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=800",
        "location": "新疆伊犁哈萨克自治州特克斯县",
        "travel_pace": "slow",
        "vibe_rating": 4.9,
        "estimated_budget": "medium",
        "is_published": True,
        "tags": ["草原", "雪山", "哈萨克文化", "星空"]
    },
    {
        "title": "扎尕那：藏在石城里的香巴拉",
        "slug": "zhagana-stone-city",
        "description": "被《中国国家地理》评为'中国十大非著名山峰'之一，藏式村寨依山而建，云雾缭绕，宛如仙境。",
        "content": """
扎尕那，藏语意为"石匣子"，是一座天然的石头城。
这里被《中国国家地理》评为"中国十大非著名山峰"之一，
是探险家洛克笔下的"亚当夏娃的诞生地"。

【四大村寨】
- 东哇村：最大村寨，住宿集中
- 业日村：观景台最佳位置
- 达日村：日出观赏点
- 代巴村：最原生态的藏族村落

【徒步路线】
1. 仙女滩：往返约2小时，适合所有游客
2. 一线天：往返约4小时，峡谷风光
3. 石林：往返约6小时，原始风光
4. 大峪沟：专业徒步路线，需向导

【摄影攻略】
- 日出：业日村观景台
- 日落：达日村观景台
- 晨雾：雨后清晨最佳
- 星空：远离村寨，光污染少

【注意事项】
海拔约3000-4000米，注意高原反应
尊重当地藏族习俗
保护环境，不要乱扔垃圾
        """,
        "cover_image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800",
        "location": "甘肃省甘南藏族自治州迭部县",
        "travel_pace": "light",
        "vibe_rating": 4.8,
        "estimated_budget": "medium",
        "is_published": True,
        "tags": ["徒步", "藏族文化", "摄影", "山峰"]
    },
    {
        "title": "香港麦理浩径：全球最美徒步路线之一",
        "slug": "macLehose-trail-hiking",
        "description": "全球最美20条徒步路线之一，穿越香港最美的山海景观。从西贡出发，一路山海相伴，是户外爱好者的天堂。",
        "content": """
麦理浩径是香港最长的远足径，全长100公里，分为10段。
其中第一、二段被誉为"全球最美20条徒步路线"之一，
沿途山海景观绝美，是户外爱好者的必走路线。

【精华路段】
第一段（10km）：北潭涌至浪茄，平路为主，适合新手
第二段（13.5km）：浪茄至北潭凹，山海景观最美
第三段（10km）：北潭凹至水浪窝，难度较高

【露营地点】
- 浪茄湾：沙滩露营，有水源
- 咸田湾：设施完善，有补给
- 西湾：风景优美，有士多店

【装备建议】
1. 登山鞋：部分路段崎岖
2. 防晒用品：海边紫外线强
3. 充足水源：部分路段无补给
4. 头灯：如果计划走夜路

【交通指南】
从香港市区乘地铁至彩虹站，转乘小巴至西贡码头
从西贡码头乘出租车至起点北潭涌

【最佳季节】
10月-次年4月：天气凉爽，适合徒步
避开台风季（7-9月）和炎热夏季
        """,
        "cover_image": "https://images.unsplash.com/photo-1501555088652-021faa106b9b?w=800",
        "location": "香港西贡区",
        "travel_pace": "light",
        "vibe_rating": 4.6,
        "estimated_budget": "medium",
        "is_published": True,
        "tags": ["徒步", "海岛", "露营", "山海景观"]
    }
]


def init_tags(db: Session):
    """初始化标签"""
    tags = [
        {"name": "徒步", "slug": "hiking", "color": "#22c55e"},
        {"name": "摄影", "slug": "photography", "color": "#3b82f6"},
        {"name": "雪山", "slug": "snow-mountain", "color": "#06b6d4"},
        {"name": "藏族文化", "slug": "tibetan-culture", "color": "#f59e0b"},
        {"name": "海岛", "slug": "island", "color": "#0ea5e9"},
        {"name": "慢生活", "slug": "slow-life", "color": "#8b5cf6"},
        {"name": "美食", "slug": "food", "color": "#ef4444"},
        {"name": "民族文化", "slug": "ethnic-culture", "color": "#ec4899"},
        {"name": "古村落", "slug": "ancient-village", "color": "#78716c"},
        {"name": "建筑艺术", "slug": "architecture", "color": "#6366f1"},
        {"name": "非遗", "slug": "intangible-heritage", "color": "#a855f7"},
        {"name": "草原", "slug": "grassland", "color": "#10b981"},
        {"name": "哈萨克文化", "slug": "kazakh-culture", "color": "#f97316"},
        {"name": "星空", "slug": "stargazing", "color": "#6366f1"},
        {"name": "露营", "slug": "camping", "color": "#14b8a6"},
        {"name": "山海景观", "slug": "coastal-mountain", "color": "#0d9488"},
        {"name": "山峰", "slug": "mountain", "color": "#64748b"},
    ]
    
    tag_objects = {}
    for tag_data in tags:
        tag = Tag(**tag_data)
        db.add(tag)
        db.commit()
        db.refresh(tag)
        tag_objects[tag.name] = tag
        print(f"创建标签: {tag.name}")
    
    return tag_objects


def init_contents(db: Session, tag_objects: dict):
    """初始化内容"""
    for content_data in contents_data:
        tag_names = content_data.pop("tags", [])
        
        content = Content(**content_data)
        db.add(content)
        db.commit()
        db.refresh(content)
        
        # 关联标签
        for tag_name in tag_names:
            if tag_name in tag_objects:
                content.tags.append(tag_objects[tag_name])
        
        db.commit()
        print(f"创建内容: {content.title}")


def main():
    """主函数"""
    db = SessionLocal()
    try:
        print("开始初始化数据...")
        
        # 清空现有数据
        db.query(Content).delete()
        db.query(Tag).delete()
        db.commit()
        print("已清空现有数据")
        
        # 初始化标签
        tag_objects = init_tags(db)
        
        # 初始化内容
        init_contents(db, tag_objects)
        
        print("\n数据初始化完成！")
        print(f"共创建 {len(tag_objects)} 个标签")
        print(f"共创建 {len(contents_data)} 条内容")
        
    except Exception as e:
        print(f"初始化失败: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
