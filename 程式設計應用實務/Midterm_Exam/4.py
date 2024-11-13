# 定義常見密碼列表
common_passwords = ['password', 'admin', '123456', '12345678', 'qwerty', 'abc123']

def has_uppercase(password):
    """檢查是否包含大寫字母"""
    for alph in password:
        if("A" <= alph <= "Z"):
            return True
    return False
    pass

def has_lowercase(password):
    """檢查是否包含小寫字母"""
    for alph in password:
        if("a" <= alph <= "z"):
            return True
    return False
    pass

def has_number(password):
    """檢查是否包含數字"""
    for num in password:
        if(num.isdigit()):
            return True
    return False
    pass

def has_special_char(password):
    """檢查是否包含特殊符號"""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for sym in password:
        if(sym in special_chars):
            return True
    return False
    pass

def has_repeating_chars(password):
    """檢查是否有連續重複的字元"""
    if(len(password) >= 3):
        for i in (2, len(password)-1):
            if(password[i] == password[i-1] == password[i-2]):
                return True
    return False
    pass

def is_common_password(password):
    """檢查是否為常見密碼"""
    lower_password = password.lower()
    return(lower_password in common_passwords)
    pass

def calculate_strength(password):
    """計算密碼強度(0-5分)"""
    strength = 0
    if(len(password) >= 8):
        strength+=1
    if(has_uppercase(password)):
        strength+=1
    if(has_lowercase(password)):
        strength+=1
    if(has_number(password)):
        strength+=1
    if(has_special_char(password)):
        strength+=1
    if((has_repeating_chars(password)==False) and (is_common_password(password)==False)):
        strength+=1
    return(strength)
    pass

def get_suggestions(password):
    """根據密碼分析給出改進建議"""
    suggestions = []
    
    # 檢查長度
    if len(password) < 8:
        suggestions.append("增加密碼長度至少8個字元")
    
    # 檢查字元類型
    if(has_uppercase(password) == False):
        suggestions.append("增加大寫字母")
    if(has_lowercase(password) == False):
        suggestions.append("增加小寫字母")
    if(has_number(password) == False):
        suggestions.append("增加數字")
    if(has_special_char(password) == False):
        suggestions.append("增加特殊符號")
        
    # 檢查其他規則
    if has_repeating_chars(password):
        suggestions.append("避免連續重複字元")
    if is_common_password(password):
        suggestions.append("避免使用常見字詞")
        
    return suggestions

# 讀取輸入
n = int(input())
for _ in range(n):
    password = input()
    
    # 計算並輸出結果
    strength = calculate_strength(password)
    suggestions = get_suggestions(password)
    
    print(f"密碼: {password}")
    
    # 根據強度輸出不同的訊息
    if strength >= 6:
        print(f"強度: {strength}分 (非常強的密碼!)")
    else:
        print(f"強度: {strength}分 (", end="")
        if strength <= 2:
            print("弱密碼", end="")
        else:
            print("中等強度", end="")
        print(f"，建議: {'. '.join(suggestions)})")
    
    print()  # 輸出空行分隔每個密碼的結果