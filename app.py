import streamlit as st
from rules import calculate_total_fan, validate_mouth_selection, rules_525, mouth_rules

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
        st.session_state.scores = [50] * len(st.session_state.players)  # 每个人初始都有50分筹码
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

                # 庄家胡牌
                if winner_index == dealer_index:
                    total_payment = 0
                    for i in range(len(st.session_state.players)):
                        if i != dealer_index and new_scores[i] > 0:
                            payment = min(total_fan_dealer, new_scores[i])
                            new_scores[i] -= payment
                            total_payment += payment
                    new_scores[dealer_index] += total_payment
                else:
                    # 非庄家胡牌
                    total_payment = 0
                    if new_scores[dealer_index] > 0:
                        payment = min(total_fan_dealer, new_scores[dealer_index])
                        new_scores[dealer_index] -= payment
                        total_payment += payment
                    for i in range(len(st.session_state.players)):
                        if i != dealer_index and i != winner_index and new_scores[i] > 0:
                            payment = min(total_fan_non_dealer, new_scores[i])
                            new_scores[i] -= payment
                            total_payment += payment
                    new_scores[winner_index] += total_payment

                # 更新历史记录
                st.session_state.past_scores.append(st.session_state.scores.copy())
                st.session_state.future_scores = []  # 清空未来记录，因为有新计算结果

                st.session_state.scores = new_scores

                # 检查是否有玩家托底
                for i, score in enumerate(st.session_state.scores):
                    if score <= 0:
                        st.warning(f"{st.session_state.players[i]} 托底啦")

            except Exception as e:
                st.error(f"计算过程中发生错误: {str(e)}")

    # 清空积分表和回退到上一次的积分记录
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("清空积分表"):
            st.session_state.scores = [50] * len(st.session_state.players)  # 重置为初始状态
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

if __name__ == "__main__":
    score_management_app()
