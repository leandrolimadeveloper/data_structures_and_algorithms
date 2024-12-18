# Word Frequency Counter Using a Hash Table in Python

def word_count(text):
    # Create a hash table (dictionary) to store the word frequency
    hash_table = {}
    
    # Preprocess the text: convert to lowercase, remove simple punctuation, and split into words
    words = text.lower().replace(",", "").replace(".", "").split()
    
    # Count the frequency of each word
    for word in words:
        if word in hash_table:
            hash_table[word] += 1  # Increment the count if the word already exists
        else:
            hash_table[word] = 1  # Initialize the count to 1

    return hash_table


# Extended informative text about Python
example_text = """
Python is a versatile programming language widely used in various fields of technology.
It is known for its simple and readable syntax, making it an excellent choice for beginners
and experienced developers alike. Python is heavily used in web development with frameworks
like Django and Flask, enabling developers to build robust and scalable applications.

In the field of data science and machine learning, Python stands out with libraries like
NumPy, Pandas, Matplotlib, Scikit-Learn, and TensorFlow, which allow data manipulation,
visualization, and the creation of AI models. Python is also popular for automation, as it
can automate repetitive tasks, such as file management, web scraping, and system administration.

With its growing community and extensive libraries, Python remains one of the most powerful,
popular, and in-demand programming languages in the world.
"""

# Call the function to count words in the text
result = word_count(example_text)

# Display the result sorted by words
print("Word frequency in the informative Python text:\n")
for word in sorted(result.keys()):
    print(f"{word}: {result[word]}")
