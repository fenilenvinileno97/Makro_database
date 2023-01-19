# Write a function in the cell below that iterates through the words in file_contents, 
# removes punctuation, and counts the frequency of each word. 
# Oh, and be sure to make it ignore word case, words that do not contain all alphabets 
# and boring words like "and" or "the"

input_file = """"The concept of sustainability has become increasingly important in recent years, as concerns about the impact of human activity on the environment have grown. Sustainability refers to the ability to meet the needs of the present without compromising the ability of future generations to meet their own needs. It encompasses social, economic, and environmental factors, and requires the balancing of these elements in order to achieve a harmonious and stable system.

One key aspect of sustainability is the use of renewable resources. These are resources that can be replenished over time, such as solar and wind power, rather than finite resources like fossil fuels. The use of renewable resources helps to reduce the negative environmental impacts of resource extraction and helps to ensure that future generations will have access to the resources they need.

Another important aspect of sustainability is waste management. Proper waste management involves reducing the amount of waste produced, recycling as much as possible, and safely disposing of any remaining waste. This helps to conserve resources and prevent pollution.

Sustainability also involves considering the long-term effects of actions and decisions. This means taking into account not just the immediate costs and benefits, but also the potential long-term impacts on the environment and on future generations.

Overall, sustainability is a complex and multifaceted concept that requires a holistic approach to addressing the needs of both present and future generations. It is important for individuals, organizations, and governments to consider sustainability in their decision-making processes in order to create a more sustainable and equitable future for all."""


def calculate_frequencies(file_contents):
    punctuations = """¡!()-[]{};:'"\,<>./?@#$%^&*_~"""
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    file_contents_list = []
    word = ""
    wordcloud_dict = {}
    
    for element in file_contents:
        if element not in punctuations and element.isnumeric() == False:
            word = element.lower()
            file_contents_list.append(word)
            
    file_contents_list = "".join(file_contents_list).split()
  
    for items in file_contents_list:
        if items not in uninteresting_words:
            wordcloud_dict[items] = file_contents_list.count(items)
    return wordcloud_dict
            


print(calculate_frequencies(input_file))