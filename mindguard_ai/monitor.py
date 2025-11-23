def analyze_user_activity(typing_speed, scroll_speed, app_switch_rate, errors):
    score = (typing_speed * 0.2) + (scroll_speed * 0.3) + (app_switch_rate * 0.4) + (errors * 0.6)
    
    if score > 50:
        return "High Cognitive Load"
    elif score > 25:
        return "Medium Cognitive Load"
    else:
        return "Low Cognitive Load"

