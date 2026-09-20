import streamlit as st
import random
import pandas as pd
import numpy as np

# 页面基本配置（适配手机端 UI）
st.set_page_config(page_title="彩票历史数据分析与选号系统", page_icon="🎲", layout="wide")

# 页面标题与专属标语
st.title("🎲 彩票历史数据分析与选号系统")
st.subheader("🔥 **陈伟你就是下一个亿万富翁** 🔥")
st.caption("提示：本程序基于历史热频加权与奇偶/和值平衡模型进行模拟选号。彩票开奖属于独立随机事件，请理性对待。")

# 侧边栏彩种选择
lottery_type = st.sidebar.selectbox(
    "选择彩票类型",
    ["双色球", "超级大乐透", "福彩 3D", "七乐彩", "快乐8 (选十)", "香港六合彩"]
)

# 基于历史开奖数据分析与中奖概率计算核心函数
def analyze_and_calculate(l_type):
    if l_type == "双色球":
        # 1. 历史热频加权：模拟近100期热号权重（热号概率偏高）
        weights = [1.5 if i % 3 == 0 else 1.0 for i in range(1, 34)]
        
        # 2. 规则校验：循环筛选符合奇偶比 (3:3或4:2) 及和值区间 (80-130) 的历史特征组合
        while True:
            reds = sorted(np.random.choice(range(1, 34), size=6, replace=False, p=np.array(weights)/sum(weights)))
            odds = sum(1 for x in reds if x % 2 != 0)
            total_sum = sum(reds)
            if odds in [2, 3, 4] and 80 <= total_sum <= 130:
                break
                
        blue = random.randint(1, 16)
        num_str = f"红球: {list(reds)} (和值:{total_sum}, 奇偶比:{odds}:{6-odds})  |  蓝球: [{blue:02d}]"
        
        probs = [
            ("一等奖 (6+1)", "1 / 17,721,088", "0.00000564%"),
            ("二等奖 (6+0)", "1 / 1,181,406", "0.0000846%"),
            ("三等奖 (5+1)", "1 / 108,055", "0.000925%"),
            ("四等奖 (5+0 / 4+1)", "1 / 2,300", "0.0435%"),
            ("五等奖 (4+0 / 3+1)", "1 / 129", "0.775%"),
            ("六等奖 (末等奖)", "1 / 16", "6.25%"),
            ("👉 任意中奖综合几率", "约 1 / 15.6", "约 6.41%")
        ]

    elif l_type == "超级大乐透":
        weights = [1.4 if i % 2 == 0 else 1.0 for i in range(1, 36)]
        while True:
            front = sorted(np.random.choice(range(1, 36), size=5, replace=False, p=np.array(weights)/sum(weights)))
            odds = sum(1 for x in front if x % 2 != 0)
            total_sum = sum(front)
            if odds in [2, 3] and 70 <= total_sum <= 120:
                break
        back = sorted(random.sample(range(1, 13), 2))
        num_str = f"前区: {list(front)} (和值:{total_sum}, 奇偶比:{odds}:{5-odds})  |  后区: {back}"
        
        probs = [
            ("一等奖 (5+2)", "1 / 21,425,712", "0.00000467%"),
            ("二等奖 (5+1)", "1 / 1,071,286", "0.0000933%"),
            ("三等奖 (5+0)", "1 / 476,127", "0.000210%"),
            ("九等奖 (末等奖)", "1 / 17", "5.88%"),
            ("👉 任意中奖综合几率", "约 1 / 16.6", "约 6.02%")
        ]

    elif l_type == "福彩 3D":
        nums = [random.randint(0, 9) for _ in range(3)]
        num_str = f"直选号码: {nums} (和值:{sum(nums)})"
        
        probs = [
            ("直选/单选", "1 / 1,000", "0.10%"),
            ("组选 3 (若含对子)", "1 / 333", "0.30%"),
            ("组选 6 (三字不同)", "1 / 167", "0.60%"),
            ("👉 本组直选精准中奖几率", "1 / 1,000", "0.10%")
        ]

    elif l_type == "七乐彩":
        nums = sorted(random.sample(range(1, 31), 7))
        num_str = f"基本号码: {nums} (和值:{sum(nums)})"
        
        probs = [
            ("一等奖 (7+0)", "1 / 2,035,800", "0.0000491%"),
            ("二等奖 (6+1)", "1 / 290,828", "0.000344%"),
            ("七等奖 (末等奖)", "1 / 11", "9.09%"),
            ("👉 任意中奖综合几率", "约 1 / 10.8", "约 9.25%")
        ]

    elif l_type == "快乐8 (选十)":
        nums = sorted(random.sample(range(1, 81), 10))
        num_str = f"投注号码: {nums}"
        
        probs = [
            ("选十中十 (头奖)", "1 / 8,911,711", "0.0000112%"),
            ("选十中九", "1 / 62,028", "0.00161%"),
            ("选十中零 (全不中也有奖)", "1 / 22", "4.55%"),
            ("👉 任意中奖综合几率", "约 1 / 4.8", "约 20.8%")
        ]

    else:  # 香港六合彩
        nums = sorted(random.sample(range(1, 50), 6))
        num_str = f"投注号码: {nums} (和值:{sum(nums)})"
        
        probs = [
            ("头奖 (6个基本号)", "1 / 13,983,816", "0.00000715%"),
            ("二奖 (5个基本号+特别号)", "1 / 2,330,636", "0.0000429%"),
            ("七奖 (3个基本号)", "1 / 61", "1.64%"),
            ("👉 任意中奖综合几率", "约 1 / 54.0", "约 1.85%")
        ]

    return num_str, probs

# 页面主要显示逻辑
st.subheader(f"📊 当前彩种：{lottery_type}")

# 触发选号与概率计算
if st.button("🎲 基于历史数据特征分析生成预测号码并计算几率", type="primary"):
    num_str, probs = analyze_and_calculate(lottery_type)
    
    st.success(f"**预测号码：** {num_str}")
    
    st.markdown("#### 📐 该组预测号码的理论中奖概率明细：")
    df_prob = pd.DataFrame(probs, columns=["奖级类型", "理论中奖比例", "百分比几率"])
    st.table(df_prob)
    
    st.balloons()
    st.write("🎉 **陈伟你就是下一个亿万富翁！祝你好运！**")

st.markdown("---")

# 历史热频统计模拟模块
st.subheader("📈 历史热频分布模拟图")
st.write("模拟 10,000 期历史数据下的号源分布情况：")

if st.checkbox("展示模拟热频图表"):
    if "3D" in lottery_type:
        sim_data = [random.randint(0, 9) for _ in range(10000)]
        df_counts = pd.Series(sim_data).value_counts().sort_index()
    else:
        max_num = 33 if "双色球" in lottery_type else (35 if "大乐透" in lottery_type else 49)
        sim_data = [num for _ in range(2000) for num in random.sample(range(1, max_num + 1), 5)]
        df_counts = pd.Series(sim_data).value_counts().sort_index()

    st.bar_chart(df_counts)
    st.caption("注：实际开奖中，频次越接近均匀分布，说明系统的随机性与公正性越高。")
