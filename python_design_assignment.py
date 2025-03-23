class Smartphone:
    """Represents a smartphone with various attributes and functionalities."""

    def __init__(self, brand, model, storage_gb, camera_mp, battery_mah):
        """Initializes a Smartphone object with brand, model, storage, camera, and battery."""
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.camera_mp = camera_mp
        self.battery_mah = battery_mah
        self.is_on = False
        self.current_app = None

    def power_on(self):
        """Turns the smartphone on."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Turns the smartphone off."""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def install_app(self, app_name):
        """Installs an app on the smartphone."""
        print(f"Installing {app_name} on {self.brand} {self.model}...")
        # Simulate installation process
        print(f"{app_name} installed successfully.")

    def open_app(self, app_name):
        """Opens a specified app."""
        if self.is_on:
            self.current_app = app_name
            print(f"Opening {app_name} on {self.brand} {self.model}.")
        else:
            print(f"Cannot open {app_name}. {self.brand} {self.model} is off.")

    def close_app(self):
        """Closes the currently opened app."""
        if self.is_on and self.current_app:
            print(f"Closing {self.current_app} on {self.brand} {self.model}.")
            self.current_app = None
        elif self.is_on:
            print("No app is currently open.")
        else:
            print(f"Cannot close app. {self.brand} {self.model} is off.")

    def display_specs(self):
         """Displays the smartphone specifications."""
         print(f"Brand: {self.brand}")
         print(f"Model: {self.model}")
         print(f"Storage: {self.storage_gb} GB")
         print(f"Camera: {self.camera_mp} MP")
         print(f"Battery: {self.battery_mah} mAh")

# Inheritance Example: A GamingSmartphone which inherits from Smartphone.
class GamingSmartphone(Smartphone):
    """Represents a gaming smartphone with enhanced features."""

    def __init__(self, brand, model, storage_gb, camera_mp, battery_mah, refresh_rate_hz, cooling_system):
        """Initializes a GamingSmartphone with additional gaming-specific attributes."""
        super().__init__(brand, model, storage_gb, camera_mp, battery_mah)
        self.refresh_rate_hz = refresh_rate_hz
        self.cooling_system = cooling_system

    def display_specs(self):
        """Overrides the display_specs method to include gaming features."""
        super().display_specs()
        print(f"Refresh Rate: {self.refresh_rate_hz} Hz")
        print(f"Cooling System: {self.cooling_system}")

    def boost_performance(self):
        """Boosts the smartphone's performance for gaming."""
        if self.is_on:
            print(f"Boosting performance of {self.brand} {self.model} for optimal gaming.")
        else:
            print(f"Cannot boost performance. {self.brand} {self.model} is off.")


# Example Usage:
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 50, 4500)
phone2 = GamingSmartphone("ROG", "Phone 7", 512, 64, 6000, 165, "Vapor Chamber")

phone1.power_on()
phone1.install_app("SocialMediaApp")
phone1.open_app("SocialMediaApp")
phone1.close_app()
phone1.power_off()

print("\nGaming Phone Specs:")
phone2.display_specs()
phone2.power_on()
phone2.boost_performance()
phone2.power_off()