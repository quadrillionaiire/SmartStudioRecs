# Create a function to identify franchise films based on keywords in the title
def check_franchise(title):
    franchise_keywords = ['Avengers', 'Star Wars', 'Harry Potter', 'Marvel', 'Toy Story', 
                          'Fast & Furious', 'Transformers', 'Pirates of the Caribbean', 'Spider-Man', 
                          'Batman', 'Superman', 'James Bond', 'X-Men', 'Jurassic', 'Mission: Impossible', 
                          'Despicable Me', 'Shrek', 'Hobbit', 'Lord of the Rings', '2', ':']
    for keyword in franchise_keywords:
        if keyword in title:
            return 'Yes'
    return 'No'

check_franchise
