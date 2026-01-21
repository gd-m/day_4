# def calculate_love_score(name1, name2):
#     true = ["t","r","u","e"]
    
#     t_times = 0
#     r_times = 0
#     u_times = 0
#     e_times = 0
    
#     l_times = 0
#     o_times = 0
#     v_times = 0
    
#     for letter in name1:
#         if letter.lower() == "t":
#             t_times += 1 
#         if letter.lower() == "e":
#             e_times += 1 
#         if letter.lower() == "u":
#             u_times += 1 
#         if letter.lower() == "r":
#             r_times += 1 
#         if letter.lower() == "l":
#             l_times += 1 
#         if letter.lower() == "o":
#             o_times += 1 
#         if letter.lower() == "v":
#             v_times += 1 
    
#     for letter in name2:
#         if letter.lower() == "t":
#             t_times += 1 
#         if letter.lower() == "e":
#             e_times += 1 
#         if letter.lower() == "u":
#             u_times += 1 
#         if letter.lower() == "r":
#             r_times += 1 
#         if letter.lower() == "l":
#             l_times += 1 
#         if letter.lower() == "o":
#             o_times += 1 
#         if letter.lower() == "v":
#             v_times += 1 
            
#     first_number = t_times + r_times + u_times +e_times
#     second_number = l_times + o_times + v_times + e_times
    
#     print(f"{first_number}{secon_number}") 

# improved code

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    true_count = sum(combined_names.lower().count(letter) for letter in "true")
    love_count = sum(combined_names.lower().count(letter) for letter in "love")
    
    love_score = int(f"{true_count}{love_count}")
    return love_score