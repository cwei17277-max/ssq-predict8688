import streamlit as st
import random
import pandas as pd
import numpy as np

# 页面基本配置（适合手机端自适应）
st.set_page_config(page_title="彩票概率分析与选号助手", page_icon="🎲", layout="wide")

# 标题与专属标语
st.title("🎲 彩票概率分析与模拟选号系统")
st.subheader("🔥 **陈伟你就是下一个亿万富翁** 🔥")
st.caption("提示：彩票开奖属于独立随机事件，历史数据不影响未来概率。本程序仅供数学统计研究与娱乐使用。")

# 侧边栏选择彩种
lottery_type = st.sidebar.selectbox(
    "选择彩票类型",
    ["双色球", "超级大乐透", "福彩 3D", "七乐彩", "快乐8 (选十)", "香港六合彩"]
)

# 概率计算与生成逻辑
def generate_and_calculate(l_type):
    if l_type == "双色球":
        reds = sorted(random.sample(range(1, 34), 6))
        blue = random.randint(1, 16)
        num_str = f"红球: {reds} | 蓝球: [{blue}]"
        
        prob_details = {
            "一等奖 (6+1)": "1 / 17,721,088 (0.00000564%)",
            "二等奖 (6+0)": "1 / 1,181,406 (0.0000846%)",
            "三等奖 (5+1)": "1 / 108,055 (0.000925%)",
            "四等奖 (5+0 或 4+1)": "1 / 2,300 (0.0435%)",
            "五等奖 (4+0 或 3+1)": "1 / 129 (0.775%)",
            "六等奖 (2+1, 1+1 或 0+1)": "1 / 16 (6.25%)",
            "👉 任意中奖（综合几率）": "约 1 / 15.6 (约 6.41%)"
        }
        return num_str, prob_details

    elif l_type == "超级大乐透":
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        num_str = f"前区: {front} | 后区: {back}"
        
        prob_details = {
            "一等奖 (5+2)": "1 / 21,425,712 (0.00000467%)",
            "二等奖 (5+1)": "1 / 1,071,286 (0.0000933%)",
            "三等奖 (5+0)": "1 / 476,127 (0.000210%)",
            "四等奖 (4+2)": "1 / 142,838 (0.000700%)",
            "九等奖/末等奖 (任意中奖)": "约 1 / 17 (5.88%)",
            "👉 任意中奖（综合几率）": "约 1 / 16.6 (约 6.02%)"
        }
        return num_str, prob_details

    elif l_type == "福彩 3D":
        nums = [random.randint(0, 9) for _ in range(3)]
        num_str = f"直选号码: {nums}"
        
        prob_details = {
            "单选/直选": "1 / 1,000 (0.10%)",
            "组选 3 (若有对子)": "1 / 333.3 (0.30%)",
            "组选 6 (三字不同)": "1 / 166.7 (0.60%)",
            "👉 本组直选精准中奖几率": "1 / 1,000 (0.10%)"
        }
        return num_str, prob_details

    elif l_type == "七乐彩":
        nums = sorted(random.sample(range(1, 31), 7))
        num_str = f"基本号码: {nums}"
        
        prob_details = {
            "一等奖 (7+0)": "1 / 2,035,800 (0.0000491%)",
            "二等奖 (6+1)": "1 / 290,828 (0.000344%)",
            "七等奖 (任意中奖)": "约 1 / 11 (9.09%)",
            "👉 任意中奖（综合几率）": "约 1 / 10.8 (约 9.25%)"
        }
        return num_str, prob_details

    elif l_type == "快乐8 (选十)":
        nums = sorted(random.sample(range(1, 81), 10))
        num_str = f"投注号码(10个): {nums}"
        
        prob_details = {
            "选十中十 (头奖)": "1 / 8,911,711 (0.0000112%)",
            "选十中九": "1 / 62,028 (0.00161%)",
            "选十中零 (无一命中也有奖)": "1 / 22 (4.55%)",
            "👉 任意中奖（综合几率）": "约 1 / 4.8 (约 20.8%)"
        }
        return num_str, prob_details

    elif l_type == "香港六合彩":
        nums = sorted(random.sample(range(1, 50), 6))
        num_str = f"投注号码: {nums}"
        
        prob_details = {
            "头奖 (6个基本号码)": "1 / 13,983,816 (0.00000715%)",
            "二奖 (5个基本+特别号)": "1 / 2,330,636 (0.0000429%)",
            "七奖 (3个基本号码)": "1 / 61 (1.64%)",
            "👉 任意中奖（综合几率）": "约 1 / 54 (约 1.85%)"
        }
        return num_str, prob_details

# 主页面展示
st.subheader(f"📊 当前选择：{lottery_type}")

# 生成推荐号码与精确概率分析
if st.button("🎲 模拟生成下一期预测号码并计算概率", type="primary"):
    num_str, prob_details = generate_and_calculate(lottery_type)
    
    st.success(f"**预测号码：** {num_str}")
    
    st.markdown("### 📐 该组号码的详细中奖几率分析：")
    
    # 用表格形式展示各奖级概率
    df_prob = pd.DataFrame(list(prob_details.items()), columns=["奖级类型", "理论中奖概率 (百分比)"])
    st.table(df_prob)
    
    st.balloons()
    st.write("🎉 **陈伟你就是下一个亿万富翁！祝你好运！**")

st.markdown("---")

# 历史数据频率模拟分析
st.subheader("📈 历史热频模拟数据分析")
st.write("基于大数定律，随机模拟 10,000 期历史数据统计数字出现频次：")

if st.checkbox("生成模拟热频图表"):
    if "3D" in lottery_type:
        sim_data = [random.randint(0, 9) for _ in range(10000)]
        df_counts = pd.Series(sim_data).value_counts().sort_index()
    else:
        max_num = 33 if "双色球" in lottery_type else (35 if "大乐透" in lottery_type else 49)
        sim_data = [num for _ in range(2000) for num in random.sample(range(1, max_num + 1), 5)]
        df_counts = pd.Series(sim_data).value_counts().sort_index()

    st.bar_chart(df_counts)
    st.caption("注：实际开奖中，频次越接近均匀分布，说明系统的随机性与公正性越高。")
