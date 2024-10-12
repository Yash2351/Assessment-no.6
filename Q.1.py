def search_queries(search_history, query):
    query = query.lower()
    
    suggestions = [item for item in search_history if item.lower().startswith(query)]
    
    return suggestions

# Input
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

# User input
user_query = input("Enter your partial search query: ")

# Suggestions based on the query
suggestions = search_queries(search_history, user_query)

# Print final output
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
