import streamlit as st
from rules import rules_315, rules_525, mouth_rules, calculate_total_fan, validate_mouth_selection, validate_gang_count

def main():
    st.set_page_config(
        page_title="芜湖麻将计分系统",
        page_icon="🀄",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.title("芜湖麻将计分系统")

    if "selected_mouths" not in st.session_state:
        st.session_state.selected_mouths = []

    if "ming_gang" not in st.session_state:
        st.session_state.ming_gang = 0

    if "an_gang" not in st.session_state:
        st.session_state.an_gang = 0

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

    def update_selected_mouths():
        valid, selected = validate_mouth_selection(set(st.session_state.mouth_selector))
        if not valid:
            st.session_state.selected_mouths = list(selected)
            st.warning("对对胡、通天和四核不能同时选择。")
        else:
            st.session_state.selected_mouths = list(st.session_state.mouth_selector)

    selected_mouths = st.multiselect(
        "选择嘴子:",
        options=all_mouths,
        default=st.session_state.selected_mouths,
        key="mouth_selector",
        on_change=update_selected_mouths,
    )

    ming_gang = st.number_input(
        "明杠的数量:", min_value=0, step=1, max_value=4, key="ming_gang"
    )
    an_gang = st.number_input(
        "暗杠的数量:", min_value=0, step=1, max_value=4, key="an_gang"
    )

    self_draw = st.checkbox("自摸", value=False)

    calculate = st.button("计算总番数")

    if calculate:
        valid, _ = validate_mouth_selection(set(st.session_state.selected_mouths))
        if not valid:
            st.error("对对胡、通天和四核不能同时选择。")
        elif not validate_gang_count(st.session_state.ming_gang, st.session_state.an_gang):
            st.error("明杠和暗杠的总数不能超过4个。")
        else:
            try:
                hand = {"支数压": hand_rule}

                total_fan_non_dealer, total_fan_dealer = calculate_total_fan(
                    hand=hand,
                    scoring_system=scoring_system,
                    self_draw=self_draw,
                    mouths=st.session_state.selected_mouths,
                    ming_gang=st.session_state.ming_gang,
                    an_gang=st.session_state.an_gang
                )

                st.success(f"非庄家总番数: {total_fan_non_dealer}")
                st.success(f"庄家总番数: {total_fan_dealer}")
            except Exception as e:
                st.error(f"计算过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main()
