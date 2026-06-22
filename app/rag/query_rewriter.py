"""
查询重写模块：将模糊的用户问题改写为更具体的检索查询
"""
import json
from typing import Optional
from loguru import logger
from app.core.llm import get_chat_llm

# 重写提示词模板
REWRITE_PROMPT = """你是一个查询优化专家。用户提出一个问题，你需要把它改写为更适合向量检索的查询语句。

规则：
1. 如果问题模糊（如"电脑卡"），改为具体的技术描述（如"CPU使用率过高导致系统卡顿"）
2. 如果问题包含口语化表达，改为标准技术术语
3. 如果问题清晰，保持原样或略微优化
4. 只输出改写后的查询文本，不要解释

原问题：{query}

改写后的查询："""


async def rewrite_query(query: str, model: Optional[str] = None) -> str:
    """
    重写用户查询，使其更适合检索
    
    Args:
        query: 原始用户问题
        model: 使用的LLM模型，默认使用配置中的模型
    
    Returns:
        改写后的查询字符串
    """
    if not query or len(query) < 3:
        return query
    
    try:
        llm = get_chat_llm(model=model, temperature=0.0)
        prompt = REWRITE_PROMPT.format(query=query)
        response = await llm.ainvoke([("system", "你是查询优化专家，只输出改写后的查询文本"), ("human", prompt)])
        rewritten = response.content.strip()
        
        # 如果改写结果为空或过长，回退到原查询
        if not rewritten or len(rewritten) > len(query) * 3:
            logger.warning(f"查询改写结果异常，使用原查询: {query}")
            return query
        
        logger.info(f"查询重写: '{query}' → '{rewritten}'")
        return rewritten
    except Exception as e:
        logger.warning(f"查询改写失败: {e}，使用原查询")
        return query