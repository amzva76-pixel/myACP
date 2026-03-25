import math

def circle_properties(radius):
    """
    Calculate the circumference and area of a circle.
    Returns a tuple: (circumference, area)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Oops! Radius must be a number 🧐")
    if radius < 0:
        raise ValueError("Radius can't be negative 🙅‍♀️")
    
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

def draw_circle():
    """Draw a cute ASCII circle with stickers!"""
    print("\n🎀 Here's your cute circle 🎀\n")
    print("      🌸🌸🌸🌸🌸")
    print("   🌸           🌸")
    print("  🌸   💖💎💖   🌸")
    print("   🌸           🌸")
    print("      🌸🌸🌸🌸🌸\n")
          
if __name__ == "__main__":
    print("🌈💖 Welcome to the Magical Circle Calculator 💖🌈")
    print("   (｡♥‿♥｡) ✨ Let's discover your circle's secrets ✨\n")
    
    try:
        r = float(input("💌 Please enter the radius of your circle: "))
        circumference, area = circle_properties(r)
        
        draw_circle()
        
        print("💫✨ Your Circle's Magical Stats ✨💫")
        print(f"🔵 Circumference: {circumference:.2f} units 🌟")
        print(f"💠 Area: {area:.2f} square units 🌟")
        print("\n🌸 Thank you for using the Magical Circle Calculator 🌸")
        print("💖 Stay round and fabulous! 💖\n")
    
    except ValueError as ve:
        print(f"🚫 Error: {ve}")
    except TypeError as te:
        print(f"🚫 Error: {te}")
    except Exception as e:
        print(f"😵 Unexpected error: {e}")