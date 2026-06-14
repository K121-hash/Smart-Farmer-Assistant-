"""
Smart Farmer Assistant - Agricultural Advisory System

A Python-based application that helps farmers make informed farming decisions
through crop recommendations, fertilizer advice, pest control guidance,
planting season information, weather-based farming advice, and livestock management tips.
"""

__version__ = "1.0.0"
__author__ = "K121-hash"
__description__ = "Intelligent Agricultural Advisory System"

# Import main components here for easier access
try:
    from smart_farmer_assistant.main import FarmerAdvisor
    __all__ = ['FarmerAdvisor']
except ImportError:
    __all__ = []
