"""
测试查询重写功能
"""
import asyncio
import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.query_rewriter import rewrite_query
from app.rag.retrieval import build_context
from app.core.config import settings


async def test_query_rewrite():
    """测试查询重写"""
    print("=" * 60)
    print("测试查询重写功能")
    print("=" * 60)
    
    test_queries = [
        "我电脑卡",
        "Redis内存高",
        "怎么排查慢查询",
        "服务器CPU飙高",
        "内存不够用了"
    ]
    
    print("\n1. 测试 rewrite_query 函数（单独重写）:")
    print("-" * 40)
    for q in test_queries:
        try:
            rewritten = await rewrite_query(q)
            print(f"  原: {q}")
            print(f"  → 改写后: {rewritten}")
            print()
        except Exception as e:
            print(f"  ❌ 重写失败: {q} -> {e}")
    
    print("\n2. 测试 build_context 集成（检索 + 重写）:")
    print("-" * 40)
    try:
        # 使用一个模糊查询测试完整的 build_context
        test_query = "我电脑卡"
        print(f"  查询: '{test_query}'")
        print("  执行 build_context（会触发查询重写 + 检索）...")
        
        context, count, sources, meta = await build_context(test_query, top_k=2)
        
        print(f"  ✅ 检索完成")
        print(f"  命中数量: {count}")
        print(f"  来源: {sources}")
        if context and context != "(知识库未命中相关内容)":
            print(f"  Context 预览: {context[:200]}...")
        else:
            print(f"  Context: {context}")
    except Exception as e:
        print(f"  ❌ build_context 执行失败: {e}")
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    # 检查是否启用查询重写
    print(f"当前配置 RAG_QUERY_REWRITE_ENABLED = {settings.RAG_QUERY_REWRITE_ENABLED}")
    if not settings.RAG_QUERY_REWRITE_ENABLED:
        print("⚠️ 查询重写未启用，请在 .env 中设置 RAG_QUERY_REWRITE_ENABLED=true")
    
    asyncio.run(test_query_rewrite())