# Problem 1: Brand Filter
# You're tasked with filtering out brands that are not sustainable from a list of fashion brands. A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials, ethical labor practices, or being carbon-neutral.

# Write the filter_sustainable_brands() function, which takes a list of brands and a criterion, then returns a list of brands that meet the criterion.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def filter_sustainable_brands(brands, criterion):
    # for brand in brands: 
    #     brand["criteria"] = set(brand["criteria"])

    """
    Time - O (n * m) 
    space - O(n)
    """

    ans = []

    for brand in brands: # n
        if criterion in brand["criteria"]: #m
            ans.append(brand["name"])
    
    return ans


brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))



# Problem 2: Eco-Friendly Materials
# Certain materials are recognized as eco-friendly due to their low environmental impact. You need to track which materials are used by various brands and count how many times each material appears across all brands. This will help identify the most commonly used eco-friendly materials.

# Write the count_material_usage() function, which takes a list of brands (each with a list of materials) and returns the material names and the number of times each material appears across all brands.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def count_material_usage(brands):
    counter = {}

    for brand in brands:
        for material in brand['materials']:
            if material not in counter:
                counter[material] = 0
            counter[material] += 1
    
    return counter

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

ba = [
    {"name": "EcoWear", "materials": ["1", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "2"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "3"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))


# Problem 3: Fashion Trends
# In the fast-changing world of fashion, certain materials and practices become trending based on how frequently they are adopted by brands. You want to identify which materials and practices are trending. A material or practice is considered "trending" if it appears in the dataset more than once.

# Write the find_trending_materials() function, which takes a list of brands (each with a list of materials or practices) and returns a list of materials or practices that are trending (i.e., those that appear more than once across all brands).

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_trending_materials(brands):
    counter = {}

    for brand in brands:
        for material in brand['materials']:
            if material not in counter:
                counter[material] = 0
            counter[material] += 1
    
    trending = []
    for count in counter:
        if counter[count] >= 2:
            trending.append(count)
    
    return trending

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))
