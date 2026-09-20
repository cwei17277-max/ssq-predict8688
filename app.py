import streamlit as st
import random
import pandas as pd
import numpy as np

# 页面基本配置（适合手机端自适应）
st.set_page_config(page_title="彩票概率分析与选号助手", page_icon="🎲", layout="wide")

# 标题与专属标语
st.title("🎲 彩票概率分析与模拟选号系统")
st.subheader("🔥 **陈伟你就是下一个亿万富翁** 🔥")
st.caption("提示：彩票结果属于独立随机事件，本程序仅供数学统计研究与娱乐使用。")

# 侧边栏选择彩种
lottery_type = st.sidebar.selectbox(
    "选择彩票类型",
    ["双色球", "超级大乐透", "福彩 3D", "七乐彩", "快乐8 (选十)", "香港六合彩"]
)

# 1. 概率计算与生成逻辑
def generate_numbers(l_type):
    if l_type == "双色球":
        reds = sorted(random.sample(range(1, 34), 6))
        blue = random.randint(1, 16)
        prob = "1 / 17,721,088 (约 0.0000056%)"
        return f"红球: {reds} | 蓝球: [{blue}]", prob

    elif l_type == "超级大乐透":
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        prob = "1 / 21,425,712 (约 0.0000047%)"
        return f"前区: {front} | 后区: {back}", prob

    elif l_type == "福彩 3D":
        nums = [random.randint(0, 9) for _ in range(3)]
        prob = "1 / 1,000 (0.1%)"
        return f"直选号码: {nums}", prob

    elif l_type == "七乐彩":
        nums = sorted(random.sample(range(1, 31), 7))
        prob = "1 / 2,035,800 (约 0.000049%)"
        return f"基本号码: {nums}", prob

    elif l_type == "快乐8 (选十)":
        nums = sorted(random.sample(range(1, 81), 10))
        prob = "1 / 8,911,711 (约 0.000011%)"
        return f"投注号码(10个): {nums}", prob

    elif l_type == "香港六合彩":
        nums = sorted(random.sample(range(1, 50), 6))
        prob = "1 / 13,983,816 (约 0.0000071%)"
        return f"投注号码: {nums}", prob

# 2. 主页面展示
st.subheader(f"📊 当前选择：{lottery_type}")

# 生成推荐号码
if st.button("🎲 模拟下一期预测号码", type="primary"):
    res, prob_info = generate_numbers(lottery_type)
    st.success(f"**预测号码：** {res}")
    st.info(f"**理论头奖概率：** {prob_info}")
    st.balloons()  # 触发庆祝气球动画
    st.write("🎉 **陈伟你就是下一个亿万富翁！祝你好运！**")

st.markdown("---")

# 3. 历史数据频率模拟分析（频次分析法）
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