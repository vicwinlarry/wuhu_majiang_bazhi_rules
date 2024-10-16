# rules.py

# rules.py

# 315计分规则字典
rules_315 = {
    "8支": {"平": [3, 4], "自摸": [6, 9]},
    "9支": {"平": [3, 4], "自摸": [7, 10]},
    "10支": {"平": [3, 4], "自摸": [7, 10]},
    "11支": {"平": [3, 4], "自摸": [7, 10]},
    "12支": {"平": [3, 4], "自摸": [8, 11]},
    "13支": {"平": [4, 5], "自摸": [8, 11]},
    "14支": {"平": [4, 5], "自摸": [9, 12]},
    "8支压2": {"平": [4, 6], "自摸": [8, 12]},
    "8支压3": {"平": [4, 6], "自摸": [8, 12]},
    "8支压4": {"平": [4, 6], "自摸": [9, 13]},
    "8支压5": {"平": [5, 7], "自摸": [9, 13]},
    "8支压6": {"平": [5, 7], "自摸": [10, 14]},
    "8支压7": {"平": [5, 7], "自摸": [10, 14]},
    "8支压8": {"平": [5, 7], "自摸": [10, 14]},
    "9支压2": {"平": [4, 6], "自摸": [8, 12]},
    "9支压3": {"平": [4, 6], "自摸": [9, 13]},
    "9支压4": {"平": [5, 7], "自摸": [9, 13]},
    "9支压5": {"平": [5, 7], "自摸": [10, 14]},
    "9支压6": {"平": [5, 7], "自摸": [10, 14]},
    "9支压7": {"平": [5, 7], "自摸": [10, 14]},
    "9支压8": {"平": [5, 7], "自摸": [11, 15]},
    "10支压2": {"平": [4, 6], "自摸": [9, 13]},
    "10支压3": {"平": [5, 7], "自摸": [9, 13]},
    "10支压4": {"平": [5, 7], "自摸": [10, 14]},
    "10支压5": {"平": [5, 7], "自摸": [10, 14]},
    "10支压6": {"平": [5, 7], "自摸": [10, 14]},
    "10支压7": {"平": [5, 7], "自摸": [11, 15]},
    "10支压8": {"平": [6, 8], "自摸": [11, 15]},
    "11支压2": {"平": [5, 7], "自摸": [9, 13]},
    "11支压3": {"平": [5, 7], "自摸": [10, 14]},
    "11支压4": {"平": [5, 7], "自摸": [10, 14]},
    "11支压5": {"平": [5, 7], "自摸": [10, 14]},
    "11支压6": {"平": [5, 7], "自摸": [11, 15]},
    "11支压7": {"平": [6, 8], "自摸": [11, 15]},
    "11支压8": {"平": [6, 8], "自摸": [12, 16]},
    "12支压2": {"平": [5, 7], "自摸": [10, 14]},
    "12支压3": {"平": [5, 7], "自摸": [10, 14]},
    "12支压4": {"平": [5, 7], "自摸": [10, 14]},
    "12支压5": {"平": [5, 7], "自摸": [11, 15]},
    "12支压6": {"平": [6, 8], "自摸": [11, 15]},
    "12支压7": {"平": [6, 8], "自摸": [14, 16]},
    "12支压8": {"平": [6, 8], "自摸": [14, 16]},
    "13支压2": {"平": [5, 7], "自摸": [10, 14]},
    "13支压3": {"平": [5, 7], "自摸": [10, 14]},
    "13支压4": {"平": [5, 7], "自摸": [11, 15]},
    "13支压5": {"平": [6, 8], "自摸": [11, 15]},
    "13支压6": {"平": [6, 8], "自摸": [12, 16]},
    "13支压7": {"平": [6, 8], "自摸": [12, 16]},
    "13支压8": {"平": [6, 8], "自摸": [12, 16]},
    "14支压2": {"平": [5, 7], "自摸": [10, 14]},
    "14支压3": {"平": [5, 7], "自摸": [11, 15]},
    "14支压4": {"平": [6, 8], "自摸": [11, 15]},
    "14支压5": {"平": [6, 8], "自摸": [12, 16]},
    "14支压6": {"平": [6, 8], "自摸": [12, 16]},
    "14支压7": {"平": [6, 8], "自摸": [12, 16]},
    "14支压8": {"平": [6, 8], "自摸": [13, 17]},
}

# 525计分规则字典
rules_525 = {
    "8支": {"平": [6, 8], "自摸": [14, 20]},
    "9支": {"平": [7, 9], "自摸": [15, 21]},
    "10支": {"平": [7, 9], "自摸": [16, 22]},
    "11支": {"平": [8, 10], "自摸": [17, 23]},
    "12支": {"平": [8, 10], "自摸": [18, 24]},
    "13支": {"平": [9, 11], "自摸": [19, 25]},
    "14支": {"平": [9, 11], "自摸": [20, 26]},
    "8支压2": {"平": [9, 13], "自摸": [18, 26]},
    "8支压3": {"平": [10, 14], "自摸": [19, 27]},
    "8支压4": {"平": [10, 14], "自摸": [20, 28]},
    "8支压5": {"平": [11, 15], "自摸": [21, 29]},
    "8支压6": {"平": [11, 15], "自摸": [22, 30]},
    "8支压7": {"平": [12, 16], "自摸": [23, 31]},
    "8支压8": {"平": [12, 16], "自摸": [24, 32]},
    "9支压2": {"平": [10, 14], "自摸": [19, 27]},
    "9支压3": {"平": [10, 14], "自摸": [20, 28]},
    "9支压4": {"平": [11, 15], "自摸": [21, 29]},
    "9支压5": {"平": [11, 15], "自摸": [22, 30]},
    "9支压6": {"平": [11, 15], "自摸": [23, 31]},
    "9支压7": {"平": [12, 16], "自摸": [24, 32]},
    "9支压8": {"平": [13, 17], "自摸": [25, 33]},
    "10支压2": {"平": [10, 14], "自摸": [20, 28]},
    "10支压3": {"平": [11, 15], "自摸": [21, 29]},
    "10支压4": {"平": [11, 15], "自摸": [22, 30]},
    "10支压5": {"平": [12, 16], "自摸": [23, 31]},
    "10支压6": {"平": [12, 16], "自摸": [24, 32]},
    "10支压7": {"平": [13, 17], "自摸": [25, 33]},
    "10支压8": {"平": [13, 17], "自摸": [26, 34]},
    "11支压2": {"平": [11, 15], "自摸": [21, 29]},
    "11支压3": {"平": [11, 15], "自摸": [22, 30]},
    "11支压4": {"平": [12, 16], "自摸": [23, 31]},
    "11支压5": {"平": [12, 16], "自摸": [24, 32]},
    "11支压6": {"平": [13, 17], "自摸": [25, 33]},
    "11支压7": {"平": [13, 17], "自摸": [26, 34]},
    "11支压8": {"平": [14, 18], "自摸": [27, 35]},
    "12支压2": {"平": [11, 15], "自摸": [22, 30]},
    "12支压3": {"平": [12, 16], "自摸": [23, 31]},
    "12支压4": {"平": [12, 16], "自摸": [24, 32]},
    "12支压5": {"平": [13, 17], "自摸": [25, 33]},
    "12支压6": {"平": [13, 17], "自摸": [26, 34]},
    "12支压7": {"平": [14, 18], "自摸": [27, 35]},
    "12支压8": {"平": [14, 18], "自摸": [28, 36]},
    "13支压2": {"平": [12, 16], "自摸": [23, 31]},
    "13支压3": {"平": [13, 17], "自摸": [24, 32]},
    "13支压4": {"平": [13, 17], "自摸": [25, 33]},
    "13支压5": {"平": [13, 17], "自摸": [26, 34]},
    "13支压6": {"平": [14, 18], "自摸": [27, 35]},
    "13支压7": {"平": [14, 18], "自摸": [28, 36]},
    "13支压8": {"平": [15, 19], "自摸": [29, 37]},
    "14支压2": {"平": [12, 16], "自摸": [24, 32]},
    "14支压3": {"平": [13, 17], "自摸": [25, 33]},
    "14支压4": {"平": [13, 17], "自摸": [26, 34]},
    "14支压5": {"平": [14, 18], "自摸": [27, 35]},
    "14支压6": {"平": [14, 18], "自摸": [28, 36]},
    "14支压7": {"平": [15, 19], "自摸": [29, 37]},
    "14支压8": {"平": [15, 19], "自摸": [30, 38]},
}

# 嘴子计分规则字典
mouth_rules = {
    "对对胡": {
        "315": {"番": 2, "自摸倍数": 2},
        "525": {"番": 5, "自摸倍数": 2}
    },
    "通天": {
        "315": {"番": 2, "自摸倍数": 2},
        "525": {"番": 5, "自摸倍数": 2}
    },
    "四核": {
        "315": {"番": 2, "自摸倍数": 2},
        "525": {"番": 5, "自摸倍数": 2}
    },
    "混一色": {
        "315": {"番": 2, "自摸倍数": 2},
        "525": {"番": 5, "自摸倍数": 2}
    },
    "杠后开花": {
        "315": {"番": 2, "自摸倍数": 1},  # 自摸不翻倍
        "525": {"番": 5, "自摸倍数": 1}
    },
}



# 获取支番的得分范围
def get_fan_score(hand_rule, scoring_system):
    if scoring_system == "315":
        rule = rules_315.get(hand_rule)
    elif scoring_system == "525":
        rule = rules_525.get(hand_rule)
    else:
        raise ValueError("无效的计分系统。请选择 '315' 或 '525'。")
    
    if rule:
        return rule["平"], rule["自摸"]
    else:
        return [0, 0], [0, 0]

# 计算嘴子的总番数
def calculate_mouth_fan(mouth_types, scoring_system, self_draw=False):
    total_fan = 0
    for mouth in mouth_types:
        if mouth in mouth_rules:
            rule = mouth_rules[mouth][scoring_system]
            fan = rule["番"]
            if self_draw:
                fan *= rule["自摸倍数"]
            total_fan += fan
    return total_fan

# 计算杠牌的总番数
def calculate_gang_fan(ming_gang, an_gang, scoring_system):
    if scoring_system == "315":
        fan = ming_gang * 1 + an_gang * 2
    elif scoring_system == "525":
        fan = ming_gang * 2 + an_gang * 4
    else:
        fan = 0
    return fan

# 综合计算函数
def calculate_total_fan(hand, scoring_system, self_draw=False, mouths=None, ming_gang=0, an_gang=0):
    total_fan_non_dealer = 0
    total_fan_dealer = 0
    
    hand_rule = hand.get("支数压")
    if not hand_rule:
        raise ValueError("手牌字典中缺少 '支数压' 键。")
    
    ping_fan_range, self_fan_range = get_fan_score(hand_rule, scoring_system)
    
    if self_draw:
        base_fan_min, base_fan_max = self_fan_range
    else:
        base_fan_min, base_fan_max = ping_fan_range
    
    total_fan_non_dealer += base_fan_min
    total_fan_dealer += base_fan_max

    if mouths:        
        mouth_fan = calculate_mouth_fan(mouths, scoring_system, self_draw)
        total_fan_non_dealer += mouth_fan
        total_fan_dealer += mouth_fan

    if ming_gang > 0 or an_gang > 0:
        gang_fan = calculate_gang_fan(ming_gang, an_gang, scoring_system)
        total_fan_non_dealer += gang_fan
        total_fan_dealer += gang_fan

    return total_fan_non_dealer, total_fan_dealer



# 新增的规则方法
def validate_mouth_selection(selected_mouths):
    """
    验证嘴子的选择，确保对对胡、通天和四核不能同时选择。

    :param selected_mouths: 已选择的嘴子列表
    :return: 验证通过返回 True，否则返回 False，并调整选择
    """
    if "对对胡" in selected_mouths and "通天" in selected_mouths:
        return False, selected_mouths - {"通天"}
    if "对对胡" in selected_mouths and "四核" in selected_mouths:
        return False, selected_mouths - {"四核"}
    return True, selected_mouths

def validate_gang_count(ming_gang, an_gang):
    """
    验证明杠和暗杠的总数，确保不超过4个。

    :param ming_gang: 明杠的数量
    :param an_gang: 暗杠的数量
    :return: 验证通过返回 True，否则返回 False
    """
    return (ming_gang + an_gang) <= 4



# 获取支番的得分范围
def get_fan_score(hand_rule, scoring_system):
    """
    获取支番的番数范围。
    
    :param hand_rule: 支番规则键，例如 "9支压5"
    :param scoring_system: 计分系统，"315" 或 "525"
    :return: 平分番数范围和自摸番数范围，如果规则不存在，返回 (0, 0), (0, 0)
    """
    if scoring_system == "315":
        rule = rules_315.get(hand_rule)
    elif scoring_system == "525":
        rule = rules_525.get(hand_rule)
    else:
        raise ValueError("无效的计分系统。请选择 '315' 或 '525'。")
    
    if rule:
        return rule["平"], rule["自摸"]
    else:
        return [0, 0], [0, 0]

# 计算嘴子的总番数
def calculate_mouth_fan(mouth_types, scoring_system, self_draw=False):
    """
    计算嘴子的总番数。
    
    :param mouth_types: 嘴子的列表，例如 ["对对胡", "通天"]
    :param scoring_system: 计分系统，"315" 或 "525"
    :param self_draw: 是否自摸
    :return: 总番数
    """
    total_fan = 0
    for mouth in mouth_types:
        if mouth in mouth_rules:
            rule = mouth_rules[mouth][scoring_system]
            fan = rule["番"]
            if self_draw:
                fan *= rule["自摸倍数"]
            total_fan += fan
    return total_fan

# 计算杠牌的总番数
def calculate_gang_fan(ming_gang, an_gang, scoring_system):
    """
    计算杠牌的总番数。
    
    :param ming_gang: 明杠的数量
    :param an_gang: 暗杠的数量
    :param scoring_system: 计分系统，"315" 或 "525"
    :return: 杠牌的总番数
    """
    if scoring_system == "315":
        fan = ming_gang * 1 + an_gang * 2
    elif scoring_system == "525":
        fan = ming_gang * 2 + an_gang * 4
    else:
        fan = 0
    return fan

# 综合计算函数
def calculate_total_fan(hand, scoring_system, self_draw=False, mouths=None,
                        ming_gang=0, an_gang=0):
    """
    计算总番数。
    
    :param hand: 手牌信息的字典，必须包含 "支数压" 键，例如 {"支数压": "9支压5"}
    :param scoring_system: 计分系统，"315" 或 "525"
    :param self_draw: 是否自摸
    :param mouths: 嘴子的列表，例如 ["对对胡", "杠后开花"]
    :param ming_gang: 明杠的数量
    :param an_gang: 暗杠的数量
    :return: (非庄家总番数, 庄家总番数)
    """
    total_fan_non_dealer = 0
    total_fan_dealer = 0
    
    # 计算支番得分
    hand_rule = hand.get("支数压")
    if not hand_rule:
        raise ValueError("手牌字典中缺少 '支数压' 键。")
    
    ping_fan_range, self_fan_range = get_fan_score(hand_rule, scoring_system)
    
    # 根据是否自摸选择相应的番数范围
    if self_draw:
        base_fan_min, base_fan_max = self_fan_range
    else:
        base_fan_min, base_fan_max = ping_fan_range
    
    total_fan_non_dealer += base_fan_min
    total_fan_dealer += base_fan_max

    # 叠加嘴子的番数
    if mouths:        
        mouth_fan = calculate_mouth_fan(mouths, scoring_system, self_draw)
        total_fan_non_dealer += mouth_fan
        total_fan_dealer += mouth_fan

    # 叠加杠牌的番数
    if ming_gang > 0 or an_gang > 0:
        gang_fan = calculate_gang_fan(ming_gang, an_gang, scoring_system)
        total_fan_non_dealer += gang_fan
        total_fan_dealer += gang_fan

    return total_fan_non_dealer, total_fan_dealer

