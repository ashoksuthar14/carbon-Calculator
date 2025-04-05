import json
import plotly.graph_objects as go
import plotly.utils
from datetime import datetime

from ai_suggestions import get_personalized_suggestions as get_ai_suggestions

def get_personalized_suggestions(user_data):
    """Generate personalized suggestions based on user data and emissions"""
    # First, calculate emissions for this user (importing locally to avoid circular imports)
    from app import calculate_emissions
    emissions = calculate_emissions(user_data)
    
    # Get AI-powered suggestions
    return get_ai_suggestions(user_data, emissions)

def calculate_tree_equivalent(total_emissions):
    """Calculate environmental equivalents for the emissions"""
    # Average tree absorbs about 22 kg of CO2 per year
    trees_needed = (total_emissions * 1000) / 22
    
    # Calculate other environmental equivalents
    equivalents = {
        'trees': round(trees_needed),
        'car_miles': round(total_emissions * 2500),  # 1 ton CO2 = ~2,500 miles driven
        'led_bulbs': round(total_emissions * 120),   # 1 ton CO2 = ~120 LED bulbs for a year
        'homes': round(total_emissions * 0.12, 1),   # 1 ton CO2 = ~0.12 average homes powered for a year
        'smartphone_charges': round(total_emissions * 121000),  # 1 ton CO2 = ~121,000 smartphone charges
        'beef_burgers': round(total_emissions * 220),  # 1 ton CO2 = ~220 beef burgers
        'plastic_bags': round(total_emissions * 10000)  # 1 ton CO2 = ~10,000 plastic bags produced
    }
    
    return equivalents

def get_badge_details(total_emissions, improvements=None):
    """Get badge and level based on emissions and improvements"""
    badges = {
        5: {
            'title': '🌍 Planet Guardian',
            'level': 'Master',
            'description': 'Your carbon footprint is impressively low!'
        },
        10: {
            'title': '🍃 Conscious Consumer',
            'level': 'Advanced',
            'description': 'You\'re making great progress in reducing emissions!'
        },
        15: {
            'title': '🌱 Eco Starter',
            'level': 'Beginner',
            'description': 'You\'re taking the first steps toward sustainability!'
        }
    }
    
    for threshold, badge in sorted(badges.items()):
        if total_emissions <= threshold:
            return badge
    
    return badges[15]  # Default badge

def create_emissions_chart(emissions):
    """Create interactive Plotly chart for emissions breakdown"""
    categories = ['Household', 'Transportation', 'Food', 'Waste', 'Lifestyle']
    values = [
        emissions['household'],
        emissions['transportation'],
        emissions['food'],
        emissions['waste'],
        emissions['lifestyle']
    ]
    
    colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c', '#9b59b6']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=.4,
        marker=dict(colors=colors),
        textinfo='label+percent',
        hovertemplate="<b>%{label}</b><br>" +
                      "CO₂: %{value:.1f} metric tons<br>" +
                      "<extra></extra>"
    )])
    
    fig.update_layout(
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return plotly.utils.PlotlyJSONEncoder().encode(fig)

def create_comparison_chart(user_emissions, avg_emissions):
    """Create comparison chart between user and average emissions"""
    categories = ['Your Emissions', 'Average in Your Area']
    values = [user_emissions, avg_emissions]
    
    fig = go.Figure(data=[go.Bar(
        x=categories,
        y=values,
        marker_color=['#2ecc71', '#95a5a6'],
        text=[f'{v:.1f}' for v in values],
        textposition='auto',
    )])
    
    fig.update_layout(
        title=dict(
            text='How You Compare',
            y=0.9,
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        yaxis_title="Metric Tons CO₂/Year",
        showlegend=False,
        margin=dict(t=50, b=0, l=0, r=0),
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return plotly.utils.PlotlyJSONEncoder().encode(fig)

def get_achievement_stats(emissions):
    """Calculate achievement statistics"""
    stats = {
        'total_score': 100 - (emissions['total'] * 5),  # Higher score for lower emissions
        'achievements': []
    }
    
    # Add achievements based on different metrics
    if emissions['transportation'] < 2:
        stats['achievements'].append({
            'icon': '🚲',
            'title': 'Low-Carbon Commuter',
            'description': 'Your transportation emissions are admirably low!'
        })
    
    if emissions['household'] < 3:
        stats['achievements'].append({
            'icon': '💡',
            'title': 'Energy Saver Pro',
            'description': 'You\'re a master at managing household energy!'
        })
    
    if emissions['food'] < 1.5:
        stats['achievements'].append({
            'icon': '🥗',
            'title': 'Eco Diet Champion',
            'description': 'Your food choices are planet-friendly!'
        })
    
    return stats
