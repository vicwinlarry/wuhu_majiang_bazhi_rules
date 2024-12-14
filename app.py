import streamlit as st
from rules import rules_315, rules_525, mouth_rules, calculate_total_fan, validate_mouth_selection, validate_gang_count

# 设置页面配置，必须在最开始调用
st.set_page_config(
    page_title="积分管理系统",
    page_icon="🎲",
    layout="centered",
)

def score_management_app():
    st.title("积分管理系统")

    if "players" not in st.session_state:
        st.session_state.players = ["玩家1", "玩家2", "玩家3", "玩家4"]
    if "scores" not in st.session_state:
        st.session_state.scores = [0] * len(st.session_state.players)
    if "past_scores" not in st.session_state:
        st.session_state.past_scores = []
    if "future_scores" not in st.session_state:
        st.session_state.future_scores = []

    st.sidebar.header("玩家管理")
    updated_players = []
    for i, player in enumerate(st.session_state.players):
        new_name = st.sidebar.text_input(f"输入玩家 {i+1} 的名字:", player)
        updated_players.append(new_name)
    st.session_state.players = updated_players

    # 使用两行来显示庄家选择和胡牌玩家选择
    col1, col2 = st.columns([1, 1])  # 每行占 1

    with col1:
        dealer_index = st.selectbox(
            "选择庄家:",
            range(len(st.session_state.players)),
            format_func=lambda x: st.session_state.players[x]
        )

    with col2:
        winner = st.selectbox("选择胡牌玩家:", st.session_state.players)
        winner_index = st.session_state.players.index(winner)

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
    selected_mouths = st.multiselect("选择嘴子:", options=all_mouths)

    ming_gang = st.number_input("明杠的数量:", min_value=0, step=1, max_value=4)
    an_gang = st.number_input("暗杠的数量:", min_value=0, step=1, max_value=4)

    self_draw = st.checkbox("自摸", value=False)

    calculate_scores_button = st.button("计算积分")

    if calculate_scores_button:
        valid, _ = validate_mouth_selection(set(selected_mouths))
        if not valid:
            st.error("对对胡、通天和四核不能同时选择。")
        else:
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

                # 计算积分
                new_scores = st.session_state.scores.copy()

                if winner_index == dealer_index:
                    # 庄家胡牌
                    for i in range(len(st.session_state.players)):
                        if i != dealer_index and new_scores[i] >= -50:
                            new_scores[i] -= total_fan_dealer
                    new_scores[dealer_index] += total_fan_dealer * (len(st.session_state.players) - 1)
                else:
                    # 非庄家胡牌
                    if new_scores[dealer_index] >= -50:
                        new_scores[dealer_index] -= total_fan_dealer
                    for i in range(len(st.session_state.players)):
                        if i != dealer_index and i != winner_index and new_scores[i] >= -50:
                            new_scores[i] -= total_fan_non_dealer
                    new_scores[winner_index] += total_fan_dealer + total_fan_non_dealer * (len(st.session_state.players) - 2)

                # 更新历史记录
                st.session_state.past_scores.append(st.session_state.scores.copy())
                st.session_state.future_scores = []  # 清空未来记录，因为有新计算结果

                st.session_state.scores = new_scores

                # 检查是否有玩家托底
                for i, score in enumerate(st.session_state.scores):
                    if score <= -50:
                        st.warning(f"{st.session_state.players[i]} 托底啦")

            except Exception as e:
                st.error(f"计算过程中发生错误: {str(e)}")

    # 清空积分表和回退到上一次的积分记录
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("清空积分表"):
            st.session_state.scores = [0] * len(st.session_state.players)
            st.session_state.past_scores = []
            st.session_state.future_scores = []
            st.success("积分表已清空！")

    with col2:
        if st.button("回退到上一次积分"):
            if st.session_state.past_scores:
                st.session_state.future_scores.append(st.session_state.scores)  # 保存当前状态到未来记录
                st.session_state.scores = st.session_state.past_scores.pop()
                st.success("已回退到上一次积分。")
            else:
                st.warning("没有历史记录可回退！")

    with col3:
        if st.button("前进到下一个积分"):
            if st.session_state.future_scores:
                st.session_state.past_scores.append(st.session_state.scores)  # 保存当前状态到历史记录
                st.session_state.scores = st.session_state.future_scores.pop()
                st.success("已前进到下一个积分。")
            else:
                st.warning("没有未来记录可前进！")

    # 最后显示当前积分结果
    st.write("当前积分结果:")
    for player, score in zip(st.session_state.players, st.session_state.scores):
        st.write(f"{player}: {score} 分")


def majiang_scoring_app():
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

    calculate_scores_button = st.button("计算积分")

    if calculate_scores_button:
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


def main():
    st.sidebar.title("请选择功能")
    option = st.sidebar.selectbox("选择应用", ("积分管理", "麻将计分"))

    if option == "积分管理":
        score_management_app()
    elif option == "麻将计分":
        majiang_scoring_app()


if __name__ == "__main__":
    main()
