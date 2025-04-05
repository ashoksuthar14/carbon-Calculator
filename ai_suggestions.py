import google.generativeai as genai

# Configure Google Generative AI with your API key
genai.configure(api_key='AIzaSyDtj4fVBSHa4s6WdVupOoegQBCAzQ-XQwY')

# Set up the model
model = genai.GenerativeModel('gemini-pro')

def get_personalized_suggestions(user_data, emissions):
    """
    Get personalized suggestions for reducing carbon footprint using Gemini AI
    
    Args:
        user_data (dict): User's input data from the form
        emissions (dict): Calculated emissions for different categories
    
    Returns:
        list: List of personalized suggestions
    """
    # Create a detailed prompt for the AI
    prompt = f"""
    As a carbon footprint expert, provide 3 specific, actionable suggestions to reduce carbon emissions based on this user's data:

    Current Emissions (metric tons CO2/year):
    - Transportation: {emissions['transportation']:.2f}
    - Household: {emissions['household']:.2f}
    - Food: {emissions['food']:.2f}
    - Waste: {emissions['waste']:.2f}
    - Lifestyle: {emissions['lifestyle']:.2f}
    Total: {emissions['total']:.2f}

    User Profile:
    - Transport Mode: {user_data.get('transport_mode', 'Not specified')}
    - Diet Type: {user_data.get('diet_type', 'Not specified')}
    - Home Type: {user_data.get('home_type', 'Not specified')}
    - AC Usage: {user_data.get('ac_usage', 'Not specified')}
    - Recycling Habits: {user_data.get('recycling', 'Not specified')}

    Provide 3 personalized suggestions that are:
    1. Specific and actionable
    2. Include potential CO2 savings
    3. Consider the user's current lifestyle
    4. Focus on the areas with highest emissions
    Format each suggestion as: "Suggestion: [action] - Can save [X] metric tons CO2/year"
    """

    try:
        # Generate response from Gemini
        response = model.generate_content(prompt)
        
        # Extract suggestions from response
        suggestions = []
        for line in response.text.split('\n'):
            if line.startswith('Suggestion:') or line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
                # Clean up the suggestion text
                suggestion = line.replace('Suggestion:', '').strip()
                if suggestion:
                    suggestions.append(suggestion)
        
        # Ensure we have at least 3 suggestions
        while len(suggestions) < 3:
            suggestions.append(get_default_suggestion(len(suggestions)))
        
        return suggestions[:3]  # Return top 3 suggestions
        
    except Exception as e:
        print(f"Error generating AI suggestions: {e}")
        return get_default_suggestions()

def get_default_suggestions():
    """Return default suggestions if AI generation fails"""
    return [
        "Switch to LED bulbs and smart power strips - Can save 0.15 metric tons CO2/year",
        "Reduce meat consumption by having 2 vegetarian days per week - Can save 0.3 metric tons CO2/year",
        "Use public transport or carpool twice a week - Can save 0.5 metric tons CO2/year"
    ]

def get_default_suggestion(index):
    """Get a default suggestion based on index"""
    defaults = get_default_suggestions()
    return defaults[min(index, len(defaults) - 1)]
