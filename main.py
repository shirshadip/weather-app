def main():
    print("=" * 50)
    print("Welcome to Weather App!")
    print("=" * 50)
    
    while True:
        print("\n--- Main Menu ---")
        choose = input(
            "What would you like to check?\n"
            "1. Today's weather\n"
            "2. 5-day forecast\n"
            "3. Exit\n"
            "Enter your choice (1-3): "
        ).strip()
        
        if choose in ["1", "todays weather", "today's weather", "today"]:
            city = input("\nEnter city name (e.g., kolkata,IN): ").strip()
            
            if not city:
                print("⚠️  City name cannot be empty. Please try again.")
                continue
            
            print("\nWould you like to see the 5-day forecast as well?")
            forecast_choice = input("Enter (y/n): ").strip().lower()
            
            if forecast_choice in ["y", "yes"]:
                try:
                    import one
                    import five
                    print("\n📍 Current Weather:")
                    one.get_weather(city=city)
                    print("\n📅 5-Day Forecast:")
                    five.get_forecast(city=city)
                except ImportError as e:
                    print(f"❌ Error importing module: {e}")
                except Exception as e:
                    print(f"❌ Error fetching weather: {e}")
            else:
                try:
                    import one
                    print("\n📍 Current Weather:")
                    one.get_weather(city=city)
                except ImportError as e:
                    print(f"❌ Error importing module: {e}")
                except Exception as e:
                    print(f"❌ Error fetching weather: {e}")
        
        elif choose in ["2", "forecast"]:
            city = input("\nEnter city name (e.g., kolkata,IN): ").strip()
            
            if not city:
                print("⚠️  City name cannot be empty. Please try again.")
                continue
            
            try:
                import five
                print("\n📅 5-Day Forecast:")
                five.get_forecast(city=city)
            except ImportError as e:
                print(f"❌ Error importing module: {e}")
            except Exception as e:
                print(f"❌ Error fetching weather: {e}")
        
        elif choose in ["3", "exit", "quit"]:
            print("\n👋 Thank you for using Weather App! Goodbye!")
            break
        
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, or 3.")
        
        # Ask if user wants to continue
        print("\n" + "-" * 50)
        continue_choice = input("Would you like to check another location? (y/n): ").strip().lower()
        
        if continue_choice not in ["y", "yes"]:
            print("\n👋 Thank you for using Weather App!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")