# app.py

import streamlit as st
from PIL import Image

from rules import rules_315, rules_525, mouth_rules, calculate_total_fan

def main():
    st.set_page_config(
        page_title="芜湖麻将计分系统（小笨笨）",
        page_icon="🀄",
        layout="centered",
        initial_sidebar_state="auto",
    )




    # 显示背景图片
    image = Image.open("back.jpg")
    st.image(image, use_column_width=True)

    
    # 使用CSS设置背景图片和按钮样式
    # st.markdown(
    #     f"""
    #     <style>
    #     .stApp {{
    #         background: url("back.jpg");
            
    #     }}
    #     .stButton>button {{
    #         display: block;
    #         margin: 0 auto;
    #         padding: 1em 2em;
    #         font-size: 1.5em;
    #     }}
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    
    st.title("芜湖麻将计分系统（小笨笨）")

    with st.sidebar:
        st.header("设置")
        scoring_system = st.selectbox("选择计分系统:", ["525", "315"])

        grouped_hand_rules = {
            "8支": [rule for rule in rules_525 if rule.startswith("8支")],
            "9支": [rule for rule in rules_525 if rule.startswith("9支")],
            "10支": [rule for rule in rules_525 if rule.startswith("10支")],
            "11支": [rule for rule in rules_525 if rule.startswith("11支")],
            "12支": [rule for rule in rules_525 if rule.startswith("12支")],
            "13支": [rule for rule in rules_525 if rule.startswith("13支")],
            "14支": [rule for rule in rules_525 if rule.startswith("14支")],
        }

        selected_group = st.selectbox("选择支数组:", list(grouped_hand_rules.keys()))
        hand_rule = st.selectbox("选择具体支数压:", grouped_hand_rules[selected_group])

        all_mouths = list(mouth_rules.keys())
        selected_mouths = st.multiselect("选择嘴子:", all_mouths)

        ming_gang = st.number_input("明杠的数量:", min_value=0, step=1)
        an_gang = st.number_input("暗杠的数量:", min_value=0, step=1)

        self_draw = st.checkbox("自摸", value=False)
        # st.markdown("<h3 style='font-size: 24px;'>自摸</h3>", unsafe_allow_html=True)
        # self_draw = st.checkbox("", value=False)



    if st.button("计算总番数"):
        try:
            hand = {"支数压": hand_rule}

            total_fan_non_dealer, total_fan_dealer = calculate_total_fan(
                hand=hand,
                scoring_system=scoring_system,
                self_draw=self_draw,
                mouths=selected_mouths,
                ming_gang=ming_gang,
                an_gang=an_gang
            )

            st.success(f"非庄家总番数: {total_fan_non_dealer}")
            st.success(f"庄家总番数: {total_fan_dealer}")
        except Exception as e:
            st.error(f"计算过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
