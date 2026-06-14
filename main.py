"""
Smart Farmer Assistant - Agricultural Advisory System
Code in Place Final Project
Author: Kyauta Ayuba Dabu

A Python-based agricultural advisory application that helps farmers make informed 
farming decisions through interactive guidance on crops, fertilizers, pest control, 
planting seasons, weather advice, and livestock management.
"""

__version__ = "1.0.0"
__author__ = "Kyauta Ayuba Dabu"
__description__ = "Interactive Agricultural Advisory System"

farmer_score = 0


def crop_recommendation():
    """Provide crop recommendations based on region (north/south)"""
    global farmer_score

    print("\n🌱 Crop Recommendation")
    farmer_score += 10

    region = input("Enter your region (north/south): ").lower()

    if region == "north":
        print("\nRecommended crops:")
        print("- Maize")
        print("- Millet")
        print("- Sorghum")
        print("- Groundnut")
        print("- Wheat")
        print("- Cotton")

    elif region == "south":
        print("\nRecommended crops:")
        print("- Cassava")
        print("- Yam")
        print("- Rice")
        print("- Plantain")
        print("- Sugarcane")
        print("- Potato")
        print("- Onion")

    else:
        print("Region not recognized.")


def fertilizer_advice():
    """Provide fertilizer recommendations for specific crops"""
    global farmer_score

    print("\n🌾 Fertilizer Advice")
    farmer_score += 10

    fertilizers = {
        "maize": "Apply NPK 15-15-15 during early growth.",
        "rice": "Use NPK and Urea for better yield.",
        "cassava": "Apply NPK 12-12-17 fertilizer.",
        "tomato": "Use compost and NPK fertilizer.",
        "wheat": "Apply NPK fertilizer and nitrogen top dressing.",
        "cotton": "Use NPK fertilizer rich in phosphorus.",
        "sugarcane": "Apply organic manure and NPK fertilizer.",
        "potato": "Apply compost and balanced NPK fertilizer.",
        "onion": "Apply nitrogen-rich fertilizer in stages."
    }

    crop = input("Enter crop name: ").lower()

    if crop in fertilizers:
        print(f"\nRecommendation: {fertilizers[crop]}")
    else:
        print("Sorry, no fertilizer information available.")


def pest_control():
    """Provide pest control guidance for specific crops"""
    global farmer_score

    print("\n🐛 Pest Control Tips")
    farmer_score += 10

    pests = {
        "maize": "Watch for armyworms. Use approved pesticides.",
        "rice": "Monitor for stem borers and weeds.",
        "tomato": "Control aphids and whiteflies regularly.",
        "cassava": "Check for cassava mosaic disease.",
        "wheat": "Monitor for rust disease and aphids.",
        "cotton": "Watch for bollworms and whiteflies.",
        "sugarcane": "Monitor for stem borers and termites.",
        "potato": "Check for late blight and aphids.",
        "onion": "Watch for thrips and onion maggots."
    }

    crop = input("Enter crop name: ").lower()

    if crop in pests:
        print(f"\nAdvice: {pests[crop]}")
    else:
        print("No pest information available.")


def planting_guide():
    """Provide planting season information for specific crops"""
    global farmer_score

    print("\n📅 Planting Season Guide")
    farmer_score += 10

    seasons = {
        "maize": "Best planted between April and June.",
        "rice": "Best planted between May and July.",
        "cassava": "Can be planted at the start of the rainy season.",
        "tomato": "Best planted during cooler periods with irrigation.",
        "wheat": "Best planted between November and December.",
        "cotton": "Best planted at the beginning of the rainy season.",
        "sugarcane": "Best planted during the rainy season.",
        "potato": "Best planted during cool weather conditions.",
        "onion": "Best planted between October and December."
    }

    crop = input("Enter crop name: ").lower()

    if crop in seasons:
        print(f"\nPlanting Guide: {seasons[crop]}")
    else:
        print("No planting information available.")


def weather_advice():
    """Provide farming advice based on current weather conditions"""
    global farmer_score

    print("\n☁️ Weather-Based Farming Advice")
    farmer_score += 10

    weather = input("Enter current weather (rainy/sunny/dry): ").lower()

    if weather == "rainy":
        print("\n✅ Good time for planting maize, rice, vegetables, and sugarcane.")

    elif weather == "sunny":
        print("\n✅ Irrigate crops regularly and monitor soil moisture.")

    elif weather == "dry":
        print("\n✅ Focus on drought-resistant crops and irrigation.")

    else:
        print("Weather condition not recognized.")


def livestock_management():
    """Provide livestock management tips for different animals"""
    global farmer_score

    print("\n🐄 Livestock Management Tips")
    farmer_score += 10

    animal = input("Enter livestock (cattle/goat/sheep/poultry): ").lower()

    tips = {
        "cattle": "Provide adequate water, vaccination, and quality feed.",
        "goat": "Maintain clean housing and deworm regularly.",
        "sheep": "Ensure proper grazing and disease monitoring.",
        "poultry": "Provide balanced feed and keep housing clean."
    }

    if animal in tips:
        print(f"\nTip: {tips[animal]}")
    else:
        print("No information available.")


def show_achievement():
    """Display farmer's achievement level based on score"""
    global farmer_score

    print("\n🏆 Farmer Achievement Status")
    print(f"Your Score: {farmer_score}")

    if farmer_score >= 50:
        print("🌟 Master Farmer")
    elif farmer_score >= 30:
        print("🌱 Skilled Farmer")
    elif farmer_score >= 10:
        print("🚜 Beginner Farmer")
    else:
        print("👨‍🌾 New Farmer")


def main():
    """Main interactive menu for the Smart Farmer Assistant"""
    while True:

        print("\n" + "=" * 45)
        print("🌿 SMART FARMER ASSISTANT 🌿")
        print("=" * 45)

        print("1. Crop Recommendation")
        print("2. Fertilizer Advice")
        print("3. Pest Control Tips")
        print("4. Planting Season Guide")
        print("5. Weather Advice")
        print("6. Livestock Management")
        print("7. Farmer Achievement")
        print("8. Exit")

        choice = input("\nChoose an option (1-8): ")

        if choice == "1":
            crop_recommendation()

        elif choice == "2":
            fertilizer_advice()

        elif choice == "3":
            pest_control()

        elif choice == "4":
            planting_guide()

        elif choice == "5":
            weather_advice()

        elif choice == "6":
            livestock_management()

        elif choice == "7":
            show_achievement()

        elif choice == "8":
            print("\nThank you for using Smart Farmer Assistant!")
            print("Happy Farming! 🌱🚜")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
