import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="彩票概率分析与选号助手", page_icon="🎲", layout="wide")

st.title("🎲 彩票概率分析与模拟选号系统")
st.subheader("🔥 **陈伟你就是下一个亿万富翁** 🔥")
st.caption("提示：彩票属于独立随机事件，历史开奖数据不改变未来概率。本程序仅供统计研究与娱乐使用。")

lottery_type = st.sidebar.selectbox(
    "选择彩票类型",
    ["双色球", "超级大乐透", "福彩 3D", "七乐彩", "快乐8 (选十)", "香港六合彩"]
)

def get_lottery_data(l_type):
    if l_type == "双色球":
        reds = sorted(random.sample(range(1, 34), 6))
        blue = random.randint(1, 16)
        num_str = f"红球: {reds}  |  蓝球: [{blue:02d}]"
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
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        num_str = f"前区: {front}  |  后区: {back}"
        probs = [
            ("一等奖 (5+2)", "1 / 21,425,712", "0.00000467%"),
            ("二等奖 (5+1)", "1 / 1,071,286", "0.0000933%"),
            ("三等奖 (5+0)", "1 / 476,127", "0.000210%"),
            ("九等奖 (末等奖)", "1 / 17", "5.88%"),
            ("👉 任意中奖综合几率", "约 1 / 16.6", "约 6.02%")
        ]
    elif l_type == "福彩 3D":
        nums = [random.randint(0, 9) for _ in range(3)]
        num_str = f"直选号码: {nums}"
        probs = [
            ("直选/单选", "1 / 1,000", "0.10%"),
            ("组选 3 (若含对子)", "1 / 333", "0.30%"),
            ("组选 6 (三字不同)", "1 / 167", "0.60%"),
            ("👉 本组直选精准中奖几率", "1 / 1,000", "0.10%")
        ]
    elif l_type == "七乐彩":
        nums = sorted(random.sample(range(1, 31), 7))
        num_str = f"基本号码: {nums}"
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
            ("选十中零 (无一命中也有奖)", "1 / 22", "4.55%"),
            ("👉 任意中奖综合几率", "约 1 / 4.8", "约 20.8%")
        ]
    else: # 香港六合彩
        nums = sorted(random.sample(range(1, 50), 6))
        num_str = f"投注号码: {nums}"
        probs = [
            ("头奖 (6个基本号)", "1 / 13,983,816", "0.00000715%"),
            ("二奖 (5个基本号+特别号)", "1 / 2,330,636", "0.0000429%"),
            ("七奖 (3个基本号)", "1 / 61", "1.64%"),
            ("👉 任意中奖综合几率", "约 1 / 54.0", "约 1.85%")
        ]
    return num_str, probs

st.subheader(f"📊 当前彩种：{lottery_type}")

if st.button("🎲 生成下一期预测号码并计算概率", type="primary"):
    num_str, probs = get_lottery_data(lottery_type)
    st.success(f"**生成号码：** {num_str}")
    
    st.markdown("#### 📐 该组号码的中奖概率明细：")
    df_prob = pd.DataFrame(probs, columns=["奖级类型", "理论中奖比例", "百分比几率"])
    st.table(df_prob)
    
    st.balloons()
    st.write("🎉 **陈伟你就是下一个亿万富翁！祝你好运！**")
